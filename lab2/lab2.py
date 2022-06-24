from paddleocr import PaddleOCR

test = PaddleOCR(use_angle_cls=True, use_gpu=False)
result = test.ocr('source/lab2/4.jpg')
print(result)
