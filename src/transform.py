import numpy as np
import cv2


# sorts the coordinates so that the same point always has the same index
# important as four_point_transform() assumes which coordinate is which point
# otherwise the image could end up upside-down or twisted
def sort_coordinates(pts):
    # 2d array for the coordinates
    rect = np.zeros((4, 2), dtype="float32")

    # top-left point will have the smallest sum
    # bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # top-right point will have the smallest difference
    # bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, points):
    # sort coordinates
    rect = sort_coordinates(points)

    # tl=top-left, tr=top-right, br=bottom-right, bottom-left
    (tl, tr, br, bl) = rect

    # calc width of the new image, which will be max distance between
    #                                           br and bl x-coordinates or
    #                                           tr and tl x-coordinates
    width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    width = max(int(width_a), int(width_b))

    # calc height of the new image, which will be max distance between
    #                                           tr and br y-coordinates or
    #                                           tl and bl y-coordinates
    height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    height = max(int(height_a), int(height_b))

    # create top-down view of the document
    dst = np.array([
        [0, 0],
        [width - 1, 0],
        [width - 1, height - 1],
        [0, height - 1]], dtype="float32")

    # calc perspective transform matrix and apply
    matrix = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, matrix, (width, height))

    return warped
