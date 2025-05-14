import math as m

y2 = 0
y1 = 0
x2 = 3
x1 = 0

calc_angle = m.atan2 ( y2 - y1 , x2 - x1 )

if ( calc_angle < 0 ): 
    calc_angle += m.pi * 2

angle = m.degrees ( calc_angle )
if(angle <= 90 and angle >= 0):
    angle = 90 - angle
elif(angle >= 90 and angle <= 180):
    angle = 90 - angle
elif(angle >= 180 and angle <= 270):
    angle = 90 - angle
elif(angle >= 270 and angle <= 360):
    angle = 90 - angle

if angle < 0:
    angle = angle + 360
print( "angle found" , angle )