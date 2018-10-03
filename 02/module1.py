try:
    import Image
except ImportError:
    from PIL import Image
import numpy as np
import pytesseract
import cv2
import sys

src_path="C:/Users/Aayush/Desktop/major 1/"

def get_the_string(imPath):
    #if len(sys.argv) < 2:
     #   print('Usage: python ocr_simple.py image.jpg')
     
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')
 
  # Read image from disk
    img = cv2.imread(imPath, cv2.IMREAD_COLOR)

    #Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.jpg", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.jpg", img)
  # Run tesseract OCR on image
    text = pytesseract.image_to_string(Image.open(src_path+"thres.jpg"), config=config)

    #os.remove(temp)
    return text


if __name__ == '__main__':
    print("Recognizing text from image")
    result= get_the_string(src_path+"upes.jpg")
    print(result)
