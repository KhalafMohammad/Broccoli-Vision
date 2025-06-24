# # calc_angle = m.atan2 ( y2 - y1 , x2 - x1 )
# import math as m
# calc_angle = m.atan2 ( 2 - 1 , 5 - 0 )
# if ( calc_angle < 0 ): 
#         calc_angle += m.pi * 2

#     # angle = m.degrees ( calc_angle )
#     # if(angle <= 90 and angle >= 0):
#     #     angle = 90 + angle
#     # elif(angle >= 90 and angle <= 180):
#     #     angle = 90 + angle
#     # elif(angle >= 180 and angle <= 270):
#     #     angle = 90 + angle
#     # elif(angle >= 270 and angle <= 360):
#     #     angle = 90 + angle
# angle = 90 - (calc_angle * (180 / m.pi))
# # angle = m.degrees ( angle )
#     # if angle < 0:
#     #     angle = angle + 360
#     # else:
        
#     # angle = (angle + 90) % 360
# print( "angle found" , angle )
import cv2
import numpy as np

# Example points (e.g., contour of an object)
points = np.array([[100, 200], [150, 100], [200, 200], [150, 300]])

# Get the rotated rectangle from points
rect = cv2.minAreaRect(points)
box = cv2.boxPoints(rect)
box = np.int0(box)

# Extract center, size, and angle
(center_x, center_y), (width, height), angle = rect
center = (int(center_x), int(center_y))

# Convert angle to radians
angle_rad = np.deg2rad(angle)

# Compute direction vector of the rectangle's orientation
dx = np.cos(angle_rad)
dy = np.sin(angle_rad)

# Define line endpoints from center outward
length = 100  # Length of orientation line to draw
pt1 = (int(center_x - dx * length), int(center_y - dy * length))
pt2 = (int(center_x + dx * length), int(center_y + dy * length))

# Compute a point 25% down the orientation line from the center
quarter_length = 0.25 * length
quarter_point = (
    int(center_x + dx * quarter_length),
    int(center_y + dy * quarter_length)
)

# Draw everything
img = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.drawContours(img, [box], 0, (0, 255, 0), 2)        # Rectangle (green)
cv2.circle(img, center, 5, (0, 0, 255), -1)            # Center point (red)
cv2.line(img, pt1, pt2, (255, 0, 0), 2)                # Orientation line (blue)
cv2.circle(img, quarter_point, 5, (0, 255, 255), -1)   # 1/4 down point (yellow)

# Show result
cv2.imshow("Min Area Rect with Line and Quarter Point", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
