import cv2
import pytesseract


# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
# with open('test.pdf', 'w+b') as f:
# f.write(pdf) # pdf type is bytes by default


def img_to_string(image):
    # cv2 images are BGR, tesseract needs RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # create a timeout if tesseract would stop working
    try:
        print(pytesseract.image_to_string(img_rgb, timeout=10))
    except RuntimeError as timeout_error:
        print(timeout_error)
