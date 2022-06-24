import face_recognition

trump_image = face_recognition.load_image_file("picture/1.jpg")

unknown_image_1 = face_recognition.load_image_file("picture/3.jpg")
unknown_image_2 = face_recognition.load_image_file("picture/4.jpg")

trump_face_encoding = face_recognition.face_encodings(trump_image)[0]
unknown_image_1_encoding = face_recognition.face_encodings(unknown_image_1)[0]
unknown_image_2_encoding = face_recognition.face_encodings(unknown_image_2)[0]

result = face_recognition.compare_faces([trump_face_encoding], unknown_image_1_encoding)
print("Is the first unkown face a picture of trump?")
print(result)
result = face_recognition.compare_faces([trump_face_encoding], unknown_image_2_encoding)
print("Is the first unkown face a picture of trump?")
print(result)

quit()
