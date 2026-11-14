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
Inertial = Inertial()

def pid_calculate(KP, KD, KI, last_error, last_time, target_heading):
    heading = Inertial.heading()
    time = brain.timer.time(MSEC)
    error = heading - target_heading
    P = KP * error
    I = KI
    D = KD * ((error-last_error)/(time-last_time))
    last_error = error
    last_time = time
    result = P + I + D
    return result

class PID:
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

generic_pid = PID(0.2, 0.2, 0)

def autonomous():
    brain.timer.clear()
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    Inertial.set_heading(0, DEGREES)
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
