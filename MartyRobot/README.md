#Marty the Robot - Sample Text
## Oveview
Sample code for marty the robot, both in Python and Scratch
##Technical Overview
###Scratch
A Scratch .sb3 is included in the repository

###Python
A more advanced implamention of the marty robot can be achived by Python.

##Network Setup
### Wireless Network
The Wireless Network **MartyTheRobot** is broadcast with the password **M@rtyR0bot**
The Network range of the access point is **192.168.0.1/24** 
The Admin IP address of the router is **192.168.0.1** 
The Admin account for the router is **admin** with password **admin**
The DHCP Range of the Network is **192.168.0.100 - 192.168.0.200** The first 10 addresses are reserved for Marty Robots. 
### Marty Robots
The marty robots function best as wireless clients, rather than hosts. In my testing, I've found the connection between a laptop and a marty robot is very inconsistant, although the robot is very close. 
| Marty | Mac Address | IP Address |
| ----- | ----------- | ---------- |
| 285 | B4:E6:2D:08:D2:ED | 192.168.0.101 |
| 078 | B4:E6:2D:08:CA:4E | 192.168.0.102 |
| 982 | A0:20:A6:15:F5:06 | 192.168.0.103 | 

### Raspberry Pi
The Raspberry Pi running the sense hat is connected to the same Marty network on IP **192.168.0.50**. SSH access is enabled for user **greigmitchell**

##References
- https://userguides.robotical.io/martyv2/documentation/python_function_reference
- https://www.w3schools.com/python/python_functions.asp
- https://userguides.robotical.io/martyv1/support_faqs/getting_started/calibrating_with_the_app
- https://userguides.robotical.io/martyv2/documentation/python_function_reference (NB The marty versions we use are V1 - take note that not all commands are valid for V1 Robots)
- 