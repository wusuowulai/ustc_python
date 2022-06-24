import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# Trump特征图片
trump_image = face_recognition.load_image_file("source/5.jpg")
trump_face_encoding = face_recognition.face_encodings(trump_image)[0]

# Trump's wife图片
wife_image = face_recognition.load_image_file("source/1.jpg")
wife_face_encoding = face_recognition.face_encodings(wife_image)[0]


known_face_encodings = [
    trump_face_encoding,
    wife_face_encoding
]
known_face_names = [
    "trump",
    "wife"
]

# 所需要识别的图片
unknown_image = face_recognition.load_image_file("source/2.jpg")
# 确定人脸数量
face_locations = face_recognition.face_locations(unknown_image)

print("Found {} face(s) in this photograph.".format(len(face_locations)))


# 确定人脸编码
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)


for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)

    name = "Unknown"

    face_distances = face_recognition.face_distance(
        known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),
                   (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5),
              name, fill=(255, 255, 255, 255))

del draw

pil_image.show()
