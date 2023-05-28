from src import four_point_transform
import numpy as np
import argparse
import cv2

# args parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
ap.add_argument("-c", "--coords",
                help="comma separated list of source points")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])

# load coordinates
pts = np.array(eval(args["coords"]), dtype="float32")

# transform the image
warped = four_point_transform(image, pts)

# compare input to transformed
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
