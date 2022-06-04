from martypy import Marty
import os 
import time
import subprocess

MartyIP = "192.168.4.1" #example

#Test IP address of Marty is active and return response
def martyalive():
  print("Testing Current Network Environment")
  #subprocess_result = subprocess.Popen('iwgetid',shell=True,stdout=subprocess.PIPE)
  #subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
  #network_name = subprocess_output[0].decode('utf-8')
  #print(network_name)
  print("Testing Marty IP address")
  response = os.system("ping -qc 1 " + MartyIP)
  #and then check the response...
  if response == 0:
   print (MartyIP, 'is up!')
  else:
   print (MartyIP, 'is down!')
  return response

#Clear marty calibration details, and save new - DO NOT USE YET!
def martycalibrate():
  print("Calibrating Marty")
  marty.clear_calibration()
  marty.save_calibration()

#Make marty walk by # of steps, -ive values possible
def martywalk(steps):
  marty.walk(num_steps=steps)

#Make marty kick with foot defined. Possible values of 'left' or 'right' 
def martykick (foot):
  marty.kick(side=foot)

#Open Marty Communication Socket on Defined IP address
#TODO Dont think this is correct, only holding open for one job - is this a network comms issue?
marty=Marty('socket://'+ MartyIP, blocking=False)

#martycalibrate() ##TODO This does not work - breaks calibration!!
#martyalive()
marty.get_battery_voltage()
martywalk(5)
marty.kick(side='left', blocking=None)

#martykick("left")
#martykick("right")


# marty.kick(side='left')
#marty.arms(left_angle=100, right_angle=-100, move_time=2000,blocking=None)
#time.sleep(5)
#marty.kick(side='left', blocking=None)
#marty.arms(left_angle=-100, right_angle=100, move_time=2000,blocking=None,)

#marty.kick(side='left',)
#marty.lean(direction='left',move_time=1000)

#marty.play_sound(name_or_freq_start=200,freq_end=1000,duration=5000)

#marty.eyes(pose_or_angle='angry',move_time=1000)


