import cv2 as cv
import cv2
import pytesseract

img3 = cv.imread('data/image3.png')
cv.imshow('Original Image', img3)
cv.waitKey(0)
cv.destroyAllWindows()

print(f"Original Image Dimensions : {img3.shape}")

text1 = pytesseract.image_to_string(img3, lang='eng').replace('\n',' ')
print(text1)

gray = cv.cvtColor(img3, cv.COLOR_RGB2GRAY)
cv.imshow('Grayscale Image', gray)
cv.waitKey(0)
cv.destroyAllWindows()

print(f"Grayscale Image Dimensions : {gray.shape}")

text2 = pytesseract.image_to_string(gray, lang='eng').replace('\n',' ')
print(text2)