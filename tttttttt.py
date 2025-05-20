# import cv2 as cv
# from math import atan2, cos, sin, sqrt, pi
# import numpy as np
 
# def drawAxis(img, p_, q_, color, scale):
#   p = list(p_)
#   q = list(q_)
 
#   ## [visualization1]
#   angle = atan2(p[1] - q[1], p[0] - q[0]) # angle in radians
#   hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
 
#   # Here we lengthen the arrow by a factor of scale
#   q[0] = p[0] - scale * hypotenuse * cos(angle)
#   q[1] = p[1] - scale * hypotenuse * sin(angle)
#   cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
 
#   # create the arrow hooks
#   p[0] = q[0] + 9 * cos(angle + pi / 4)
#   p[1] = q[1] + 9 * sin(angle + pi / 4)
#   cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
 
#   p[0] = q[0] + 9 * cos(angle - pi / 4)
#   p[1] = q[1] + 9 * sin(angle - pi / 4)
#   cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), color, 3, cv.LINE_AA)
#   ## [visualization1]
 
# def getOrientation(pts, img):
#   ## [pca]
#   # Construct a buffer used by the pca analysis
#   sz = len(pts)
#   data_pts = np.empty((sz, 2), dtype=np.float64)
#   for i in range(data_pts.shape[0]):
#     data_pts[i,0] = pts[i,0,0]
#     data_pts[i,1] = pts[i,0,1]
 
#   # Perform PCA analysis
#   mean = np.empty((0))
#   mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)
 
#   # Store the center of the object
#   cntr = (int(mean[0,0]), int(mean[0,1]))
#   ## [pca]
 
#   ## [visualization]
#   # Draw the principal components
#   cv.circle(img, cntr, 3, (255, 0, 255), 2)
#   p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
#   p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])
#   drawAxis(img, cntr, p1, (255, 255, 0), 1)
#   drawAxis(img, cntr, p2, (0, 0, 255), 5)
 
#   angle = atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians
#   ## [visualization]
 
#   # Label with the rotation angle
#   label = "  Rotation Angle: " + str(-int(np.rad2deg(angle)) - 90) + " degrees"
#   textbox = cv.rectangle(img, (cntr[0], cntr[1]-25), (cntr[0] + 250, cntr[1] + 10), (255,255,255), -1)
#   cv.putText(img, label, (cntr[0], cntr[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv.LINE_AA)
 
#   return angle
 
# # Load the image
# img = cv.imread("frame_4.png")
# img1 = cv.imread("frame_1.png")
# img2 = cv.imread("frame_2.png")
# img3 = cv.imread("frame_3.png")

 
# # Was the image there?
# if img is None:
#   print("Error: File not found")
#   exit(0)
 
# cv.imshow('Input Image', img)
 
# # Convert image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# gray3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
 
# # Convert image to binary
# _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# _, bw1 = cv.threshold(gray1, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# _, bw2 = cv.threshold(gray2, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# _, bw3 = cv.threshold(gray3, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

 
# # Find all the contours in the thresholded image
# contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours1, _ = cv.findContours(bw1, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours2, _ = cv.findContours(bw2, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours3, _ = cv.findContours(bw3, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

 
# for i, c in enumerate(contours):
 
#   # Calculate the area of each contour
#   area = cv.contourArea(c)
 
#   # Ignore contours that are too small or too large
#   if area < 3700 or 100000 < area:
#     continue
 
#   # Draw each contour only for visualisation purposes
#   cv.drawContours(img, contours, i, (0, 0, 255), 2)
 
#   # Find the orientation of each shape
#   getOrientation(c, img)

# for i, c in enumerate(contours1):
 
#   # Calculate the area of each contour
#   area = cv.contourArea(c)
 
#   # Ignore contours that are too small or too large
#   if area < 3700 or 100000 < area:
#     continue
 
#   # Draw each contour only for visualisation purposes
#   cv.drawContours(img1, contours1, i, (0, 0, 255), 2)
 
#   # Find the orientation of each shape
#   getOrientation(c, img1)

# for i, c in enumerate(contours2):
#     # Calculate the area of each contour
#     area = cv.contourArea(c)
     
#     # Ignore contours that are too small or too large
#     if area < 3700 or 100000 < area:
#         continue
     
#     # Draw each contour only for visualisation purposes
#     cv.drawContours(img2, contours2, i, (0, 0, 255), 2)
     
#     # Find the orientation of each shape
#     getOrientation(c, img2)

# for i, c in enumerate(contours3):
#     # Calculate the area of each contour
#     area = cv.contourArea(c)
     
#     # Ignore contours that are too small or too large
#     if area < 3700 or 100000 < area:
#         continue
     
#     # Draw each contour only for visualisation purposes
#     cv.drawContours(img3, contours3, i, (0, 0, 255), 2)
     
#     # Find the orientation of each shape
#     getOrientation(c, img3)

    
# cv.imshow('Output Image', img)
# cv.imshow('Output Image1', img1)
# cv.imshow('Output Image2', img2)
# cv.imshow('Output Image3', img3)
# cv.waitKey(0)
# cv.destroyAllWindows()
  
# # Save the output image to the current directory
# cv.imwrite("output_img.jpg", img)






# This programs calculates the orientation of an object.
# The input is an image, and the output is an annotated image
# with the angle of otientation for each object (0 to 180 degrees)
 
import cv2 as cv
from math import atan2, cos, sin, sqrt, pi
import numpy as np
 
# Load the image
img = cv.imread("frame_0pro.png")
 
# Was the image there?
if img is None:
  print("Error: File not found")
  exit(0)
  
# Convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
 
# Convert image to binary
_, bw = cv.threshold(gray, 10, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

cv.imshow('Input Image', bw)
 
# Find all the contours in the thresholded image
contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
 
for i, c in enumerate(contours):
 
  # Calculate the area of each contour
  area = cv.contourArea(c)
 
  # Ignore contours that are too small or too large
  if area < 3700 or 100000 < area:
    continue
 
  # cv.minAreaRect returns:
  # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
  rect = cv.minAreaRect(c)
  box = cv.boxPoints(rect)
  box = np.intp(box)
 
  # Retrieve the key parameters of the rotated bounding box
  center = (int(rect[0][0]),int(rect[0][1])) 
  width = int(rect[1][0])
  height = int(rect[1][1])
  angle = int(rect[2])
 
  x,y = center
  print(x,y)

  if width < height:
    angle = angle
  else:
    angle = 90 - angle
         
  label = "  Rotation Angle: " + str(angle) + " degrees"
  textbox = cv.rectangle(img, (center[0]-35, center[1]-25), 
    (center[0] + 295, center[1] + 10), (255,255,255), -1)
  cv.putText(img, label, (center[0]-50, center[1]), 
    cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 1, cv.LINE_AA)
  cv.drawContours(img,[box],0,(0,0,255),2)
 
cv.imshow('Output Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
  
# Save the output image to the current directory
cv.imwrite("min_area_rec_output.jpg", img)