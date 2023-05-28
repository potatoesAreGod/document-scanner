from skimage.filters import threshold_local
from src.transform import four_point_transform
import cv2
import imutils


# TODO: optimize imports

def find_edges(img):
    # convert image to grayscale, blur it, and find edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    print("STEP 1: Edge Detection")
    cv2.imshow("Image", img)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return edged


def find_corners(edged_img, image):
    # find the contours in the edged image
    # and keep only the largest outline
    cornered = cv2.findContours(edged_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cornered = imutils.grab_contours(cornered)
    cornered = sorted(cornered, key=cv2.contourArea, reverse=True)[:5]
    # loop over all the found outlines
    for c in cornered:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if the approximated contour has four points, then assume that a valid screen is found
        if len(approx) == 4:
            outline = approx
            break

    print("STEP 2: Find contours of paper")
    cv2.drawContours(image, [outline], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return outline


def warp_image(orig, outline, ratio):
    # apply the four point transform to obtain a top-down view of the original image
    warped = four_point_transform(orig, outline.reshape(4, 2) * ratio)

    # effects to make it look like paper and easier to read
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    transformed = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > transformed).astype("uint8") * 255

    return warped


def scan_document(img, debug):
    # TODO: Create proper file validation
    # Such as ensure only images can be loaded, path validation
    image = cv2.imread(img)

    # TODO: move these vars to the functions where they're used
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

    # analyze and transform the image
    edged = find_edges(image)
    outline = find_corners(edged, image)
    warped = warp_image(orig, outline, ratio)
    final = imutils.resize(warped, height=650)

    cv2.imshow("Original", orig)
    cv2.imshow("Scanned", final)
    cv2.waitKey(0)

    return final
