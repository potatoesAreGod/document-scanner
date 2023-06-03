from src.scan import scan_document
from src.save import save_document
from src.ocr import img_to_string
from os import path

debug = 1  # enables debugging output
demo = 0  # auto-loads a demo image
demo_img = "./images/demo.png"  # image to be used in the demo
filetype = ".png"  # format to save as. leave empty to not save
save_path = path.join(path.expanduser("~"), "Downloads")  # where to save scanned docs. defaults to user's downloads

# TODO: Make use to the DEBUG var
# TODO: OCR -> Editable document
# TODO: Create a UI for dropping images (Web/Desktop/React(or is it electron?) -> convert to web+desktop)

if __name__ == "__main__":
    if demo:
        doc = scan_document(demo_img, 0)
    else:
        doc = scan_document("./images/demo.png", debug)

    save_document("document", filetype, save_path, doc)
    img_to_string(doc)
