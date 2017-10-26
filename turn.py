#!/usr/bin/python

import os
import weather as W
import time

#a = raw_input()
cmd = 'sudo ./rpi-oled '
#os.system(cmd + str(a))
print("weather info")
count = 0
while count < 10:
	weather = (W.getWeather())
	if weather is not None:
		args = (" ".join(weather))
	else:
		args = "not weather info"	
	print("weather reload")	
	print(args)
	os.system(cmd + args)
	time.sleep(3)
	count = count + 1 
