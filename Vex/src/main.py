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

brain = Brain()
controller = Controller(PRIMARY)
LeftMotor = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
RightMotor = Motor(Ports.PORT11, GearSetting.RATIO_6_1, True)
LeftMotor2 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
RightMotor2 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, True)
ToggleMotor = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True)
ArmMotor = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
ClawMotor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)

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
        APressing = controller.axis1()
        APressing3 = controller.axis3()
        L2Pressing = controller.buttonL2()
        R2Pressing = controller.buttonR2()
        LeftMotor.spin(FORWARD,(APressing3 + APressing))
        RightMotor.spin(FORWARD,(APressing3 - APressing))
        LeftMotor2.spin(FORWARD,(APressing3 + APressing))
        RightMotor2.spin(FORWARD,(APressing3 - APressing))
        if L2Pressing == "True":
            ToggleMotor.spin(FORWARD, 100)
        if L2Pressing == "False":
                    ToggleMotor.spin(FORWARD, 0)
        if R2Pressing == "True":
                    ClawMotor.spin(FORWARD, 100)
        if R2Pressing == "False":
                    ClawMotor.spin(FORWARD, 0)

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
