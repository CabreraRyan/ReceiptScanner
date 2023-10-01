# import the necessary packages
import pytesseract
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/Tesseract.exe'

# construct the argument parser and parse the arguments}
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="C/Users/cabre/Documents/ReceiptScanner")
args = vars(ap.parse_args())

# load the input image and convert it from BGR to RGB channel
# ordering}
image = cv2.imread(args["image"])
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(image)
print(text)

