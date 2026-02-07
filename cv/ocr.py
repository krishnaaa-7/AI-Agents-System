import pytesseract
import cv2
import numpy as np

def extract_text(image):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text
