from martypy import Marty
import os 
import time

marty=Marty('socket://192.168.4.1', blocking=False)
#marty.__init__("wifi", "192.168.4.1")
print("Movement 1")
marty.arms(left_angle=100, right_angle=-100, move_time=2000,blocking=None)
time.sleep(5)
print("Movement 2")
marty.arms(left_angle=-100, right_angle=100, move_time=2000,blocking=None)
#marty.kick(side='left',)
#marty.lean(direction='left',move_time=1000)

#marty.play_sound(name_or_freq_start=200,freq_end=1000,duration=5000)

#marty.eyes(pose_or_angle='angry',move_time=1000)


