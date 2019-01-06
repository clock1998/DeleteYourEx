import face_recognition
import os

#
# # Load the jpg files into numpy arrays
# biden_image = face_recognition.load_image_file("biden.jpg")
# obama_image = face_recognition.load_image_file("obama.jpg")
# unknown_image = face_recognition.load_image_file("obama2.jpg")
# known_faces = []
# # Get the face encodings for each face in each image file
# # Since there could be more than one face in each image, it returns a list of encodings.
# # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
# try:
#     biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
#     obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#     known_faces = [
#         biden_face_encoding,
#         obama_face_encoding
#     ]
# except IndexError:
#     print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
#     quit()
#
#
# # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
# results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
#
# print("Is the unknown face a picture of Biden? {}".format(results[0]))
# print("Is the unknown face a picture of Obama? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


def remove_images_without_target_face(unknown_images_path, target_face_path):
    """
    The function removes images that do not contain the target person's face.
    :param unknown_images_path: a list of unknown image's path
    :param target_face_path: the target image path.
    :return: a list of images that has the target face.
    """
    # gets the target face encoding.
    target_face_encoding = get_target_face_encodings(target_face_path)
    image_path_and_numpy_array = {}
    for i in unknown_images_path:
        image_path_and_numpy_array[i] = face_recognition.load_image_file(i)
    for i in image_path_and_numpy_array:
        try:
            face_encodings = face_recognition.face_encodings(image_path_and_numpy_array[i])
            if len(face_encodings) > 1:
                results = face_recognition.compare_faces(face_encodings, target_face_encoding)
                counter = 0
                for r in results:
                    if r:
                        counter += 1
                if counter == 0:
                    image_path_and_numpy_array[i] = None
            else:
                results = face_recognition.compare_faces(face_encodings, target_face_encoding)
                if not results[0]:
                    image_path_and_numpy_array[i] = None
        except IndexError:
            image_path_and_numpy_array[i] = None
    processed_images_list = []
    for i in image_path_and_numpy_array:
        if image_path_and_numpy_array[i] is not None:
            processed_images_list.append(i)
    return processed_images_list


def get_target_face_encodings(image_path):
    target_image = face_recognition.load_image_file(image_path)
    return face_recognition.face_encodings(target_image)[0]
