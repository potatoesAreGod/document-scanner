import cv2
from os import path
from pytesseract import image_to_pdf_or_hocr
from docx import Document


def save_document(filename: str, filetype: str, directory: str, content: str, image):
    if filetype in [".jpeg", ".png", ".pxm", ".exr", ".tiff", ".jpeg2000", ".pam"]:
        image_name = path.join(directory, filename + filetype)
        # save the image
        cv2.imwrite(image_name, image)

    elif filetype == ".pdf":
        img_rgb = cv2.cvtColor(content, cv2.COLOR_BGR2RGB)
        pdf = image_to_pdf_or_hocr(img_rgb, extension="pdf")
        with open(filename + filetype, "w+b") as f:
            f.write(pdf)
            f.close()

    elif filetype == ".hocr":
        img_rgb = cv2.cvtColor(content, cv2.COLOR_BGR2RGB)
        hocr = image_to_pdf_or_hocr(img_rgb, extension="hocr")
        with open(filename + filetype, "w+b") as f:
            f.write(hocr)
            f.close()

    elif filetype == ".txt":
        with open(filename + filetype, "w") as f:
            f.write(content)
            f.close()

    elif filetype == ".docx":
        d = Document()
        d.add_paragraph(content, style=None)
        d.save(filename + filetype)

    else:
        print("Not saving document!")
