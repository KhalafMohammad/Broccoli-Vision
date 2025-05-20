# calc_angle = m.atan2 ( y2 - y1 , x2 - x1 )
import math as m
calc_angle = m.atan2 ( 2 - 1 , 5 - 0 )
if ( calc_angle < 0 ): 
        calc_angle += m.pi * 2

    # angle = m.degrees ( calc_angle )
    # if(angle <= 90 and angle >= 0):
    #     angle = 90 + angle
    # elif(angle >= 90 and angle <= 180):
    #     angle = 90 + angle
    # elif(angle >= 180 and angle <= 270):
    #     angle = 90 + angle
    # elif(angle >= 270 and angle <= 360):
    #     angle = 90 + angle
angle = 90 - (calc_angle * (180 / m.pi))
# angle = m.degrees ( angle )
    # if angle < 0:
    #     angle = angle + 360
    # else:
        
    # angle = (angle + 90) % 360
print( "angle found" , angle )