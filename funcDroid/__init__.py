# coding=utf-8
# Insert in a script in Coppelia

try:
	import funcDroid.sim
except:
	print ('--------------------------------------------------------------')
	print ('"sim.py" could not be imported. This means very probably that')
	print ('either "sim.py" or the remoteApi library could not be found.')
	print ('Make sure both are in the same folder as this file,')
	print ('or appropriately adjust the file "sim.py"')
	print ('--------------------------------------------------------------')
	print ('')

from .globalDefs import *
import funcDroid.globalDefs as glob
import sys


sim.simxFinish(-1) # just in case, close all opened connections
_clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5)
_robotname = 'robo'

if _clientID != -1:
	glob.init(_clientID, _robotname)
	clientID = glob.clientID
	time.sleep(2)

	
else:
	print ('Failed connecting to remote API server')
	sys.exit()

