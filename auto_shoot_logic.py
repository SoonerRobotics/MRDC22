# logicial layout for the autoshoot process
#calculate angle
#wait for correct color
# launch ball

#assumes that the launch mechinism is pointed directly at the center of the goal system (left to right)
#assumes no drag
#assumes that launch and landing point are on the same horizontal plane
import math 
import time
distance_to_goal = 0.0 #given in meters, variable
ball_mass = 0.0 #set to estimated ball mass
coeff_drag = 0.0 #invariable, coeffecient drag for ball
volume_ball = 0.0 #invariable, set to estimated ball volume
velocity = 0.0 #velocity of ball, m/s
g = 9.81 #gravity m/s^2
receieved_color = 0 #color from target, 1-4
target_color = 4 #target color 1-4

def calculate_angle():
    theta = 0
    r = distance_to_goal
    v = velocity
    inter = (r*g)/(v**2)
    print("Inter =")
    print(inter)
    inter2 = math.asin(inter)
    print("Inter2 = ")
    print(inter2)
    theta = inter2/2
    print ("Theta = ")
    print (theta)
    return theta
#launch_angle = calculate_angle()
def align_angle():
    #set tube angle to launch_angle in radians
    pass
def check_color():
    color_match = 0
    receieved_color= int(input()) #eventually change this to get color from camera
    if receieved_color  == target_color:
        color_match = 1
    else:
        color_match = 0
    return color_match

def shoot_ball():
    color1 = check_color()
    while color1 != 1:
        time.sleep(.1)
        print("Checking color")
        color1 = check_color()
    print("Launching ball")
    #launch ball bc color matches goal
shoot_ball()