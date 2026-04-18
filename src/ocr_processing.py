import cv2 as cv
import pytesseract


# Function to convert an image to grayscale and extract text from both the original and grayscale images
def grayscale_image(image_path):

    # Load the original image 
    img = cv.imread(image_path)

    # Convert the original image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # Use pytesseract to extract text from the original image
    text_original = pytesseract.image_to_string(img, lang='eng').replace('\n',' ')

    # Use pytesseract to extract text from the grayscale image
    text_gray = pytesseract.image_to_string(gray, lang='eng').replace('\n',' ')

    # Return Results
    return img, gray, text_original, text_gray

# main function to excute the processing function
if __name__ == "__main__":
    img3, gray, text1, text2 = grayscale_image("data/image3.png")

    # Display the original image in a window
    cv.imshow('Original Image', img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Print the dimensions of the original image
    print(f"Original Image Dimensions : {img3.shape}")

    # Use pytesseract to extract text from the original image
    text1 = pytesseract.image_to_string(img3, lang='eng').replace('\n',' ')

    # Print the texte detected in the original image
    print("Text detected in the original image is:")
    print(text1)



    # Display the grayscale image in a window
    cv.imshow('Grayscale Image', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # Print the dimensions of the grayscale image
    print(f"Grayscale Image Dimensions : {gray.shape}")

    # Use pytesseract to extract text from the grayscale image
    text2 = pytesseract.image_to_string(gray, lang='eng').replace('\n',' ')

    # Print the texte detected in the grayscale image
    print("Text detected in the grayscale image is:")
    print(text2)


