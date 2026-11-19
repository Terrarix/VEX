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

#######################################################################################################
""" -----------------------------------ASSIGNING DEVICES--------------------------------------------"""
#######################################################################################################

brain = Brain()
controller = Controller(PRIMARY)
LeftMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
RightMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, True)
LeftMotor2 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)
RightMotor2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
ToggleMotor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
ArmMotor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
ArmMotor2 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
ClawMotor = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)

######################################################################################################
""" -----------------------------------CLASSES & FUNCTIONS-----------------------------------------"""
######################################################################################################

"""
class PID_TURN:
    def __init__(self, KP, KD, KI):
        self.KP=KP
        self.KD=KD
        self.KI=KI
        self.last_error = 0
        self.last_time = 0

    def calculate(self, target_angle, current_angle):
        time = brain.timer.time(MSEC)
        error = current_angle - target_angle
        P = self.KP * error
        I = self.KI
        if time == self.last_time:
            D= 0
        else:
            D = self.KD * ((error-self.last_error)/(time-self.last_time))
        self.last_error = error
        self.last_time = time
        result = P + I + D
        return result

DTT_PID = PID_TURN(0.2, 0.2, 0)
"""

def DT_PID(target_angle):
    current_angle = Inertial.heading(DEGREES)
    velocity = DTT_PID.calculate(target_angle, current_angle)
    LeftMotor.spin(FORWARD,(velocity * 1))
    LeftMotor2.spin(FORWARD,(velocity * 1))
    RightMotor.spin(FORWARD,(velocity * 1))
    RightMotor2.spin(FORWARD,(velocity * 1))

def DRIVETRAIN(DIRECTION, VELOCITY, UNITS, WAIT):
    LeftMotor.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    LeftMotor2.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    RightMotor.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    RightMotor2.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)

def ArmControl(DIRECTION, VELOCITY, UNITS, WAIT):
    ArmMotor.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)
    ArmMotor2.spin(DIRECTION, VELOCITY, UNITS, wait=WAIT)

def ClawControl(DIRECTION, WAIT):
    ClawMotor.spin(DIRECTION, 100, 1, wait=WAIT)

######################################################################################################
""" -----------------------------------COMPETITION CODE--------------------------------------------"""
######################################################################################################

##################
"""----AUTO----"""
##################

def autonomous():
    brain.timer.clear()
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    Inertial.set_heading(0, DEGREES)
    """
    ToggleMotor.spin(FORWARD, 2, TURNS, False)
    DRIVETRAIN(REVERSE, 1, TURNS, True)
    ArmControl(FORWARD, 2, TURNS, False)
    ClawControl(FORWARD, False)
    DRIVETRAIN(FORWARD, 2, TURNS, True)
    DTT_PID(90)
    DRIVETRAIN(FORWARD, 2, TURNS, True)
    ArmControl(REVERSE, 1.5, TURNS, True)
    ClawControl(REVERSE, False)
    """

##################
"""---DRIVER---"""
##################

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    i = 0
    while i < 1:
        APressing = controller.axis1.position()
        APressing3 = controller.axis3.position()
        LeftMotor.spin(FORWARD,(APressing3 + APressing) * 4)
        RightMotor.spin(FORWARD,(APressing3 - APressing) * 4)
        LeftMotor2.spin(FORWARD,(APressing3 + APressing) * 4)
        RightMotor2.spin(FORWARD,(APressing3 - APressing) * 4)
        if controller.buttonL2.pressing():
            ToggleMotor.spin(FORWARD, 80)
        else:
            ToggleMotor.spin(FORWARD, 0)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
