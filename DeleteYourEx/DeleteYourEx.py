import face_recognition
from os import listdir
from os.path import isfile, join
import os


# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
unknown_image = face_recognition.load_image_file("obama2.jpg")
known_faces = []
# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    known_faces = [
        biden_face_encoding,
        obama_face_encoding
    ]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()


# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


def get_the_person_face(image):
    the_person = face_recognition.load_image_file(image)
    the_face = face_recognition.face_encodings(the_person)[0]
    return the_face


def get_photos(user_input):
    if os.path.isfile(user_input):
        pass
    elif os.path.isdir(user_input):
        pass
