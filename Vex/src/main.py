# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Riley                                                        #
# 	Created:      11/4/2026, 4:08:02 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

brain = Brain()
controller = Controller(PRIMARY)
LeftMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
RightMotor = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
LeftMotor2 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
RightMotor2 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
ToggleMotor = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)

c_x = 0
c_y = 0
c_angle = 0
constant = 0
error = 2

def distance(x, y, c_x, c_y):
    x2 = x - c_x
    y2 = y - c_y
    x3 = x**2
    y3 = y**2
    distance = (x3 + y3)**0.5
    c_x = x
    c_y = y
    return distance

def angle(c_angle, x, y, c_x, c_y):
    x2 = x - c_x
    y2 = y - c_y
    arc_angle = math.atan2(y2, x2)
    t_angle = arc_angle - c_angle
    return t_angle

def pid(x, y, c_x, c_y, c_angle, p_angle, constant, error):
    t_angle = angle(c_angle, x, y, c_x, c_y)
    cp = c_angle - t_angle
    cd = c_angle - p_angle
    velocity = constant * (cp - cd)
    return velocity

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    LeftMotor.spin_for(FORWARD, 2, TURNS, 100, PERCENT, False)
    RightMotor.spin_for(FORWARD, 2, TURNS, 100, PERCENT, False)
    LeftMotor2.spin_for(FORWARD, 2, TURNS, 100, PERCENT, False)
    RightMotor2.spin_for(FORWARD, 2, TURNS, 100, PERCENT, False)
    ToggleMotor.spin_for(FORWARD, 2, TURNS, 100, PERCENT, False)

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    i = 0
    while i < 1:
        APressing = controller.axis1.position()
        APressing3 = controller.axis3.position()
        LeftMotor.spin(FORWARD,(APressing3 + APressing))
        RightMotor.spin(FORWARD,(APressing3 - APressing))
        LeftMotor2.spin(FORWARD,(APressing3 + APressing))
        RightMotor2.spin(FORWARD,(APressing3 - APressing))
        if controller.buttonL2.pressing():
            ToggleMotor.spin(FORWARD, 100)
        else:
            ToggleMotor.spin(FORWARD, 0)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
