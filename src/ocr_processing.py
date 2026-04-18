import cv2 as cv
import cv2
import pytesseract
from google.colab.patches import cv2_imshow

img2 = cv.imread('/content/AI-School-Epoch1-Checkpoint4/data/image2.png')
cv2_imshow(img2)

img2.shape

text1 = pytesseract.image_to_string(img2, lang='eng').replace('\n',' ')
print(text1)

gray = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)
cv2_imshow(gray)

gray.shape

text2 = pytesseract.image_to_string(gray, lang='eng').replace('\n',' ')
print(text2)