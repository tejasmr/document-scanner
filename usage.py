"""
Requirements

matplotlib==3.2.2
numpy==1.18.5
ocrd-fork-pylsd==0.0.3
opencv-python==4.2.0.34
scipy==1.5.0

-> For Python 2/3

pip install matplotlib==3.2.2
pip install numpy==1.18.5
pip install ocrd-fork-pylsd==0.0.3
pip install opencv-python==4.2.0.34
pip install scipy==1.5.0

(or)

pip install matplotlib==3.2.2 numpy==1.18.5 ocrd-fork-pylsd==0.0.3 opencv-python==4.2.0.34 scipy==1.5.0

-> For Python 3

pip3 install matplotlib==3.2.2
pip3 install numpy==1.18.5
pip3 install ocrd-fork-pylsd==0.0.3
pip3 install opencv-python==4.2.0.34
pip3 install scipy==1.5.0

(or)

pip3 install matplotlib==3.2.2 numpy==1.18.5 ocrd-fork-pylsd==0.0.3 opencv-python==4.2.0.34 scipy==1.5.0

"""

import cv2
from scanner import DocScanner

image = cv2.imread('cell_pic.jpg')
scanned_image = DocScanner().scan(image)
cv2.imshow('Output Image', scanned_image)
cv2.waitKey(0) 

