# from app.main.service.employee_service import get_all_employee
from imutils.video import VideoStream
import imutils
import time
import cv2
import face_recognition
import numpy as np
from app.main.service.activity_service import insert_activity

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
    
    (known_face_encodings, known_face_names, id_list) = getlist_file(data)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    is_stoped = False
    while True:
        frame = videostream.read()
        frame = imutils.resize(frame, width=600)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    # if name != "Unknown":
                    #     emit('message', {'hello': "Hello"})
   


   
        process_this_frame = not process_this_frame

   
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')