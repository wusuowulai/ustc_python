import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("picture/1.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)
for face_landmarks in face_landmarks_list:
    #face_landmarks_list中每个元素都包含以下key的字典
    #打印此图像中每个面部特征的位置
    facial_features = [
        'chin',
        'left_eyebrow',
        'right_eyebrow',
        'nose_bridge',
        'nose_tip',
        'left_eye',
        'right_eye',
        'top_lip',
        'bottom_lip'
    ]
    for facial_feature in facial_features:
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
    #在图像中画出每个人脸特征！
    for facial_feature in facial_features:
        d.line(face_landmarks[facial_feature], width=5)
pil_image.show()
