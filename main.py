from src.scan import scan_document
from src.save import save_document
from src.ocr import img_to_string
from os import getcwd

demo = 1  # auto-loads a demo image
demo_img = "./images/demo.png"  # image to be used in the demo
filetype = ".png"  # format to save as. leave empty to not save
language = "en-US"  # what language to assume the doc is in
try_to_guess_words = 1
directory = getcwd()  # where to save files

if __name__ == "__main__":
    if demo:
        doc = scan_document(demo_img)
    else:
        img = input("Enter image to be scanned: ")
        doc = scan_document(img)

    content = img_to_string(doc, try_to_guess_words, language)
    save_document("document", filetype, directory, content, doc)
