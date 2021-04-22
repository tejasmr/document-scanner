# DocumentScanner: Open Source solution for document scanning

## Scan Function

### Input

`Image as np.array`

### Output

`Scanned Image as np.array`

## Requirements

`1. matplotlib==3.2.2`

`2. numpy==1.18.5`

`3. ocrd-fork-pylsd==0.0.3`

`4. opencv-python==4.2.0.34`

`5. scipy==1.5.0`

## For Python 2/3

```js
pip install matplotlib==3.2.2
pip install numpy==1.18.5
pip install ocrd-fork-pylsd==0.0.3
pip install opencv-python==4.2.0.34
pip install scipy==1.5.0
```

(or)

```js
pip install matplotlib==3.2.2 numpy==1.18.5 ocrd-fork-pylsd==0.0.3 opencv-python==4.2.0.34 scipy==1.5.0
```

## For Python 3

```js
pip3 install matplotlib==3.2.2
pip3 install numpy==1.18.5
pip3 install ocrd-fork-pylsd==0.0.3
pip3 install opencv-python==4.2.0.34
pip3 install scipy==1.5.0
```

(or)

```js
pip3 install matplotlib==3.2.2 numpy==1.18.5 ocrd-fork-pylsd==0.0.3 opencv-python==4.2.0.34 scipy==1.5.0
```

## Usage

```py
import cv2
from scanner import DocScanner

image = cv2.imread('cell_pic.jpg')
scanned_image = DocScanner().scan(image)
cv2.imshow('Output Image', scanned_image)
cv2.waitKey(0)
```

## Pytesseract

### Main

```py
import cv2
import pytesseract as pt
# need to install pillow
from PIL import Image

img = cv2.imread('image.jpg')
output_string = pt.image_to_string(Image.fromarray(img))
print(output_string)
```

### Boundary Box
```py
import cv2
import pytesseract

img = cv2.imread('image.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
```

### To Dictionary
```py
import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('invoice-sample.jpg')

d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d.keys())
# Output: dict_keys(['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'])
# d['text'] gives the string
```
