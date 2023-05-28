from src.scan import scan_document
from src.save import save_document

debug = 1  # enables debugging output
demo = 0  # auto-loads a demo image
demo_img = "./images/demo.png"  # image to be used in the demo
filetype = "pdf"  # format to save as; pdf, png. leave empty to not save

# TODO: Make use to the DEBUG var
# TODO: OCR -> Editable document
# TODO: Save to PDF
# TODO: Save to PNG
# TODO: Create a UI for dropping images (Web/Desktop/React(or is it electron?) -> convert to web+desktop)

if __name__ == "__main__":
    if demo:
        doc = scan_document(demo_img, 0)
    else:
        doc = scan_document("./images/demo.png", debug)

    save_document(doc, filetype)
