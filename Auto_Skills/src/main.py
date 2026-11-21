# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ethan                                                        #
# 	Created:      11/20/2026, 6:51:24 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
LeftMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
RightMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
LeftMotor2 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
RightMotor2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
ToggleMotor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)

def DRIVETRAIN(DIRECTION, VELOCITY, UNITS, WAIT):
    LeftMotor.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    LeftMotor2.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    RightMotor.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    RightMotor2.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)

def autonomous():
    brain.timer.clear()
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    Inertial.set_heading(0, DEGREES)
    DRIVETRAIN(FORWARD, 20, TURNS, True)

# create competition instance
comp = Competition(autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
