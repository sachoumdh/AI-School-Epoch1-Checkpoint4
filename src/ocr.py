import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_dataset = {
    "image.png": "03. Encoding Categorical Variables: Why?"
    "Open Minds Club"
    "Machine learning algorithms work with numbers, they cannot process raw text labels.:"
    "Rule of thumb"
    "2 categories -> Binary Encoding"
    "Many categories, no order -> One-Hot Encoding"
    "Ordered categories -> Ordinal Encoding"
    "IT"
    "School",
    "image1.png": "La typaguephie"
    "un atout"
    "pour votre image de marque",
    "image2.png": "FOREVERBLUR"
}

# Creating a list to store the accuracies of each image, initially the list is empty
Accuracies_List = []

# Loop through the dataset and compare the converted text to the text in the dictionary
for i, (file, reference) in enumerate(image_dataset.items()):

    # The model analyzes the image and returns the text it thinks it sees
    text = pytesseract.image_to_string(Image.open("data/" + file))

    # Calculate the accuracy of each image
    accuracy = sum(1 for a, b in zip(reference, text) if a == b)

    accuracy = accuracy / len(reference) * 100

    # Add the accuracy to the list
    Accuracies_List.append(accuracy)

    # Print the accuracy of each image in percentage
    print(f"Image {i}: {accuracy:.2f}%")
    