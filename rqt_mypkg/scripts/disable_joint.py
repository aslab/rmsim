#!/usr/bin/env python3

import os

os.system('rosrun dynamic_reconfigure dynparam set /robominer/Rev8_r_1_position_controller/pid p 0')
os.system('rosrun dynamic_reconfigure dynparam set /robominer/Rev8_r_1_position_controller/pid i 0')
os.system('rosrun dynamic_reconfigure dynparam set /robominer/Rev8_r_1_position_controller/pid d 0')

