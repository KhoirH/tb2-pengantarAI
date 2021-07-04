# from app.main.service.employee_service import get_all_employee
from imutils.video import VideoStream
import imutils
import time
import cv2
import face_recognition
import numpy as np

def getlist_file(data):
    employees = data
    known_face_encodings = []
    known_face_names = []
    id_list = []
    for employee in employees: 
        known_face_names.append(employee.NAME)
        id_list.append(employee.ID_EMPLOYEE)
        image = face_recognition.load_image_file(employee.PHOTO_EMPLOYEE)
        image_face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_face_encoding)

    return known_face_encodings, known_face_names, id_list

def generate_frames(data):
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
    (known_face_encodings, known_face_names, id_list) = getlist_file(data)

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
