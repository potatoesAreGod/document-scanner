import cv2
from pytesseract import image_to_string
import language_tool_python as ltp


def img_to_string(image, autocorr: int, lang: str):
    # cv2 images are BGR color format, tesseract uses RGB
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print("Scanning for text...")

    # create a timeout if tesseract would stop working
    content = image_to_string(img_rgb, timeout=10)

    if autocorr == 1:
        content = guess_words(content, lang)

    print(f"Text content found {content}")

    return content


def guess_words(text: str, lang: str):
    tool = ltp.LanguageTool(lang)

    # Only correct spelling errors
    matches = tool.check(text)
    matches = [rule for rule in matches if ruleset(rule)]

    # Correct text
    text = ltp.utils.correct(text, matches)
    tool.close()

    return text


def ruleset(rule):
    return rule.message == "Possible spelling mistake found." and len(rule.replacements)
