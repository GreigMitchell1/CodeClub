from martypy import Marty
import os 
import time
import subprocess
#import keyboard

Marty1 = "192.168.8.243" #example
Marty2 = "192.168.0.101"
Marty3 = "192.168.0.107"
Marty4 = "192.168.0.108"

#Test IP address of Marty is active and return response
def martyalive():
  print("Testing Current Network Environment")
  #subprocess_result = subprocess.Popen('iwgetid',shell=True,stdout=subprocess.PIPE)
  #subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
  #network_name = subprocess_output[0].decode('utf-8')
  #print(network_name)
  print("Testing Marty IP address")
  response = os.system("ping -qc 1 " + Marty1)
  #and then check the response...
  if response == 0:
   print (Marty1, 'is up!')
  else:
   print (Marty1, 'is down!')
  return response
  marty.get_battery_voltage()

def martyhello():
  marty1.hello()
  marty2.hello()
  marty3.hello()
  #marty4.hello()
  
#Clear marty calibration details, and save new - DO NOT USE YET!
def martycalibrate():
  print("Calibrating Marty")
  marty.clear_calibration()
  marty.save_calibration()

#Make marty walk by # of steps, -ive values possible
def martywalk(steps):
  marty1.walk(num_steps=steps)
  marty2.walk(num_steps=steps)
  marty3.walk(num_steps=steps)
  marty4.walk(num_steps=steps)

#Make marty kick with foot defined. Possible values of 'left' or 'right' 
def martykick (foot):
  marty1.kick(side=foot)

#Marty dance routine in time specified. Side is defined as start foot.
def martydance ():
  marty1.dance(side="right", move_time=5000)
  #marty2.dance(side="left", move_time=5000)
  #marty3.dance(side="right", move_time=5000)
  #marty4.dance(side="left", move_time=5000)

#Wave marty arms back and forth. acceptable values between -100 and 100 in time specified.
def martyarms ():
  marty1.arms(-100, 100, 2000)
  marty1.arms(100, -100, 2000)
  marty1.arms(-100, 100, 2000)
  marty1.arms(100, -100, 2000)   
  marty1.arms(0, 0, 2000) 

#Move Martys eyes to one of 4 poses [angry | excited | normal | wide] Can also accept a integer in angle number. -ive accepted.  
def martyeyes (): 
  marty1.eyes("angry")
  marty1.eyes("excited")
  marty1.eyes("normal")
  marty1.eyes("wide")

#Turn Marty on the spot. Pass left or right to the method and will be translated into 90 (Left) or -90 (Right) ~approx 10 - 12 steps needed to turn 90 degrees.
def martyturn (direction): 
  turndir=0
  if direction == "left":
    turndir = 90
  elif direction == "right":
    turndir = -90
  marty1.walk(num_steps=12, start_foot='auto',turn=turndir)

#Play a sound from the internal marty speaker. Acceptable sound values of 20 - 20,000Hz. Maximum duration of 5000ms (5 Seconds)
def martysound (): 
  marty1.play_sound(name_or_freq_start=200,freq_end=400,duration=5000)
  #marty2.play_sound(name_or_freq_start=400,freq_end=600,duration=5000)
  #marty3.play_sound(name_or_freq_start=600,freq_end=800,duration=5000)

#Make marty lean in a specified direction. Choice of [left | right | forward | backward]
def martylean (direction): 
  marty1.lean(direction=direction)

#Open Marty Communication Socket on Defined IP address
#TODO Dont think this is correct, only holding open for one job - is this a network comms issue?

marty1=Marty('socket://192.168.8.192', blocking=True)
marty2=Marty('socket://192.168.0.101', blocking=True)
#marty3=Marty('socket://192.168.0.107', blocking=True)
#marty4=Marty('socket://192.168.0.108', blocking=True)

#martycalibrate() ##TODO This does not work - breaks calibration!!
#martyalive()
martyhello()
#martyarms()
#martysound()
#martywalk(5)
#martyturn("right")
#martykick("left")
#martykick("right")
while 1==1:
  martydance()
#martylean("forward")
#martylean("back")martyarms()
#martyeyes()
