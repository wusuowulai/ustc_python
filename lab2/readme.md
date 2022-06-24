```python
from paddleocr import PaddleOCR

test = PaddleOCR(use_angle_cls=True, use_gpu=False)
result = test.ocr('source/4.jpg')
print(result)
```

当前目录下执行 `python lab2.py`即可运行

如果需要识别不同的图片需要更改`result = test.ocr('source/1.jpg')`中的图片链接。

