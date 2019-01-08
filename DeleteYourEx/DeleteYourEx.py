import face_recognition
import os
import multiprocessing

def remove_images_without_target_face(unknown_images_path, target_face_path):
    """
    The function removes images that do not contain the target person's face.
    :param unknown_images_path: a list of unknown image's path
    :param target_face_path: the target image path.
    :return: a list of images that has the target face.
    """
    manager = multiprocessing.Manager()
    p_return_values = manager.list()
    jobs = []
    # gets the target face encoding.
    target_face_encoding = get_target_face_encodings(target_face_path)
    image_path_and_numpy_array = {}
    for i in unknown_images_path:
        image_path_and_numpy_array[i] = face_recognition.load_image_file(i)
    for i in image_path_and_numpy_array:
        p = multiprocessing.Process(target=recognize, args=(i, image_path_and_numpy_array, target_face_encoding,
                                                            p_return_values))
        jobs.append(p)
        p.start()
        # try:
        #     face_encodings = face_recognition.face_encodings(image_path_and_numpy_array[i])
        #     if len(face_encodings) > 1:
        #         results = face_recognition.compare_faces(face_encodings, target_face_encoding)
        #         counter = 0
        #         for r in results:
        #             if r:
        #                 counter += 1
        #         if counter == 0:
        #             image_path_and_numpy_array[i] = None
        #     else:
        #         results = face_recognition.compare_faces(face_encodings, target_face_encoding)
        #         if not results[0]:
        #             image_path_and_numpy_array[i] = None
        # except IndexError:
        #     image_path_and_numpy_array[i] = None
    processed_images_list = []
    for i in jobs:
        i.join()

    for i in p_return_values:
        image_path_and_numpy_array.pop(i)

    for i in image_path_and_numpy_array:
        processed_images_list.append(i)
    return processed_images_list


def get_target_face_encodings(image_path):
    target_image = face_recognition.load_image_file(image_path)
    return face_recognition.face_encodings(target_image)[0]


def delete_images(images):
    for i in images:
        if os.path.exists(i):
            os.remove(i)
        else:
            print("The file does not exist")


def recognize(i, image_path_and_numpy_array, target_face_encoding, p_return_values):
    try:
        face_encodings = face_recognition.face_encodings(image_path_and_numpy_array[i])
        if len(face_encodings) > 1:
            results = face_recognition.compare_faces(face_encodings, target_face_encoding)
            counter = 0
            for r in results:
                if r:
                    counter += 1
            if counter == 0:
                p_return_values.append(i)
        else:
            results = face_recognition.compare_faces(face_encodings, target_face_encoding)
            if not results[0]:
                p_return_values.append(i)
    except IndexError:
        p_return_values.append(i)
