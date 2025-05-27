import math as m

def get_angle(x1,y1,x2,y2):
    global angle
    calc_angle = m.atan2 ( y2 - y1 , x2 - x1 )
    
    calc_angle
    if ( calc_angle < 0 ): 
        calc_angle += m.pi * 2

    angle = 90 - (calc_angle * (180 / m.pi))
    
    if angle > 0:
        angle = 360 - angle
    
    angle = abs(angle)
    return angle