#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, Response, redirect
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os
from imutils.video import VideoStream
import face_recognition
import numpy as np
import imutils
import cv2
import time
from werkzeug.utils import secure_filename
from PIL import Image
import glob
from model.anggota import checkLastId, createAnggota
from model.history import checkHistoryNow, createHistory

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#



@app.route('/')
def home():
    return render_template('videostream.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload-dataset', methods=['GET', 'POST'])
def uploadDataset():
    if request.method == 'POST':
        # check if the post request has the file part
        name=request.form['nama']
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ext = filename.rsplit('.', 1)[1].lower()
            createAnggota(name, app.config['UPLOAD_FOLDER'] + "/" + name + '.' + ext)
            last_data = checkLastId()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],  str(last_data[0]) + '_' + name + '.' + ext))
            return redirect(request.url)
    return render_template('inputData.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def getlist_file(path):
    known_face_encodings = []
    known_face_names = []
    id_list = []
    for filename in glob.glob(path + '/*'): 
        im=filename.replace('\\', '/')
        namefile=im.rsplit('/', 1)[1].rsplit('.', 1)[0]
        name = namefile.rsplit('_', 1)[1]
        id = namefile.rsplit('_', 1)[0]
        known_face_names.append(name)
        id_list.append(id)
        image = face_recognition.load_image_file(im)
        image_face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_face_encoding)

    return known_face_encodings, known_face_names, id_list

def generate_frames():
    videostream = VideoStream(src=0).start()
    time.sleep(2.0)
    
    # # Load a sample picture and learn how to recognize it.
    # obama_image = face_recognition.load_image_file("dataset/obama.jpg")
    # obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    # print(getlist_file(app.config['UPLOAD_FOLDER']))
    # # Load a second sample picture and learn how to recognize it.
    # biden_image = face_recognition.load_image_file("dataset/biden.jpg")
    # biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    # Create arrays of known face encodings and their names
    # known_face_encodings = [
    #     obama_face_encoding,
    #     biden_face_encoding
    # ]
    # known_face_names = [
    #     "Barack Obama",
    #     "Joe Biden"
    # ]
    (known_face_encodings, known_face_names, id_list) = getlist_file(app.config['UPLOAD_FOLDER'])

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        frame = videostream.read()
        frame = imutils.resize(frame, width=600)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    # if name != "Unknown":
                    #     id_anggota = id_list[best_match_index]
                    #     checkAvaliable = checkHistoryNow(id_anggota)
                    #     if len(checkAvaliable) == 0:
                    #         createHistory(id_anggota)
                    #         break



                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')



#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
