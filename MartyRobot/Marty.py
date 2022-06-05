from martypy import Marty
import os 
import time
import subprocess
import keyboard

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
  marty.get_battery_voltage()

#Clear marty calibration details, and save new - DO NOT USE YET!
def martycalibrate():
  print("Calibrating Marty")
  marty.clear_calibration()
  marty.save_calibration()

#Make marty walk by # of steps, -ive values possible
def martywalk(steps):
  marty.walk(num_steps=steps, blocking=None)

#Make marty kick with foot defined. Possible values of 'left' or 'right' 
def martykick (foot):
  marty.kick(side=foot)

#Marty dance routine in time specified. Side is defined as start foot.
def martydance ():
  marty.dance(side="right", move_time=5000)

#Wave marty arms back and forth. acceptable values between -100 and 100 in time specified.
def martyarms ():
  marty.arms(-100, 100, 2000)
  marty.arms(100, -100, 2000)
  marty.arms(-100, 100, 2000)
  marty.arms(100, -100, 2000)   
  marty.arms(0, 0, 2000) 

#Move Martys eyes to one of 4 poses [angry | excited | normal | wide] Can also accept a integer in angle number. -ive accepted.  
def martyeyes (): 
  marty.eyes("angry")
  marty.eyes("excited")
  marty.eyes("normal")
  marty.eyes("wide")

#Turn Marty on the spot. Pass left or right to the method and will be translated into 90 (Left) or -90 (Right) ~approx 10 - 12 steps needed to turn 90 degrees.
def martyturn (direction): 
  turndir=0
  if direction == "left":
    turndir = 90
  elif direction == "right":
    turndir = -90
  marty.walk(num_steps=12, start_foot='auto',turn=turndir)

#Play a sound from the internal marty speaker. Acceptable sound values of 20 - 20,000Hz. Maximum duration of 5000ms (5 Seconds)
def martysound (): 
  marty.play_sound(name_or_freq_start=200,freq_end=1000,duration=5000)

#Make marty lean in a specified direction. Choice of [left | right | forward | backward]
def martylean (direction): 
  marty.lean(direction=direction)

#Open Marty Communication Socket on Defined IP address
#TODO Dont think this is correct, only holding open for one job - is this a network comms issue?
#marty=Marty('socket://'+ MartyIP, blocking=True)

#martycalibrate() ##TODO This does not work - breaks calibration!!
martyalive()
martysound()
martywalk(5)
martyturn("right")
martykick("left")
martykick("right")
martydance()
martylean("forward")
martylean("back")
martyarms()
martyeyes()