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
