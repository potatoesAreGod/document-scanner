import cv2
from os import remove, path
from PIL import Image


def save_document(filename, filetype, save_path, image):
    if filetype in [".jpeg", ".png", ".pxm", ".exr", ".tiff", ".jpeg2000", ".pam"]:
        image_name = path.join(save_path, filename + filetype)
        # save the image
        cv2.imwrite(image_name, image)

    elif filetype == "pdf":
        image_name = path.join(save_path, filename + ".png")
        # save the image
        cv2.imwrite(image_name, image)
        # set filename
        pdf_name = filename + ".pdf"
        image_path = path.join(save_path, image_name)
        pdf_path = path.join(save_path, pdf_name)
        # open the previously saved image
        image = Image.open(image_path)
        # convert
        im = image.convert("RGB")
        # save as pdf
        im.save(pdf_path)
        # remove unwanted image; we only want the pdf
        remove(image_path)

    else:
        print("Not saving document!")
        return
