# coding=utf-8

import funcDroid.sim as sim
import time

PRETO = 0
VERMELHO = 1
AMARELO = 2
VERDE = 3
AZUL = 5
BRANCO = 6
frente = 1
tras = -1
horario = -1
antihorario = 1

## Setters
def init(_clientID, robotname):
	global robot, robo, robotFrontLeftMotor, robotFrontRightMotor, robotBackRightMotor, robotBackLeftMotor, garraRobotRight, garraRobotLeft
	global clientID
	global paEsquerda, paDireita
	global elevador, irRight, irLeft, us_front, us_left, us_left_front, us_right_front
	global color_sensor_Left, color_sensor_Right, color_sensor_Middle, color_sensor_Right2, color_sensor_Left2, color_sensor_Side
	global positionrobot, angLeft, angRight, orientationrobot

	clientID = _clientID

	sim.simxStartSimulation(clientID, sim.simx_opmode_oneshot_wait)
	print ('Connected to remote API server')
	sim.simxAddStatusbarMessage(clientID,'Funcionando...',sim.simx_opmode_oneshot_wait)
	time.sleep(0.02)

	# Coletar handles
	#Robô
	erro, robot = sim.simxGetObjectHandle(clientID, robotname, sim.simx_opmode_blocking) 
	erro, robo = sim.simxGetObjectHandle(clientID, 'robo', sim.simx_opmode_blocking)
	#Motores
	[erro, robotFrontLeftMotor] = sim.simxGetObjectHandle(clientID, 'OmniWheel45_typeA', sim.simx_opmode_blocking)
	[erro, robotBackLeftMotor] = sim.simxGetObjectHandle(clientID, 'OmniWheel45_typeB', sim.simx_opmode_blocking)
	[erro, robotFrontRightMotor] = sim.simxGetObjectHandle(clientID, 'OmniWheel45_typeD', sim.simx_opmode_blocking)
	[erro, robotBackRightMotor] = sim.simxGetObjectHandle(clientID, 'OmniWheel45_typeC', sim.simx_opmode_blocking)
	#Garra
	[erro, paDireita] = sim.simxGetObjectHandle(clientID, 'Junta_direita', sim.simx_opmode_blocking)
	[erro, paEsquerda] = sim.simxGetObjectHandle(clientID, 'Junta_esquerda', sim.simx_opmode_blocking)
	#Sensores
	erro, irRight = sim.simxGetObjectHandle(clientID, 'Sensor_IR_direito', sim.simx_opmode_blocking)
	erro, irLeft = sim.simxGetObjectHandle(clientID, 'Sensor_IR_esquerdo', sim.simx_opmode_blocking)
	erro, us_front = sim.simxGetObjectHandle(clientID, 'SensorFrente', sim.simx_opmode_blocking)
	erro, us_left = sim.simxGetObjectHandle(clientID, 'SensorLado', sim.simx_opmode_blocking)
	erro, us_left_front = sim.simxGetObjectHandle(clientID, 'SensorLado0', sim.simx_opmode_blocking)
	erro, us_right_front = sim.simxGetObjectHandle(clientID, 'SensorLado1', sim.simx_opmode_blocking)

	erro , color_sensor_Left = sim.simxGetObjectHandle(clientID, 'SensorCorDireita', sim.simx_opmode_blocking)
	erro , color_sensor_Right = sim.simxGetObjectHandle(clientID, 'SensorCorEsquerda', sim.simx_opmode_blocking)
	erro , color_sensor_Middle = sim.simxGetObjectHandle(clientID, 'SensorCorMeio', sim.simx_opmode_blocking)
	erro, color_sensor_Left2 = sim.simxGetObjectHandle(clientID, 'SensorCorDireita2', sim.simx_opmode_blocking)
	erro, color_sensor_Right2 = sim.simxGetObjectHandle(clientID, 'SensorCorEsquerda2', sim.simx_opmode_blocking)
	erro, color_sensor_Side = sim.simxGetObjectHandle(clientID, 'CorLado', sim.simx_opmode_blocking)
	

	# Criar stream de dados
	[erro, positionrobot] = sim.simxGetObjectPosition(clientID, robot, -1, sim.simx_opmode_streaming)

	erro, angLeft = sim.simxGetJointPosition(clientID, robotFrontLeftMotor, sim.simx_opmode_streaming)
	erro, angRight = sim.simxGetJointPosition(clientID, robotFrontRightMotor, sim.simx_opmode_streaming)
	[erro, orientationrobot] = sim.simxGetObjectOrientation(clientID,robot,-1,sim.simx_opmode_streaming)

	sim.simxReadProximitySensor(clientID, irRight, sim.simx_opmode_streaming)
	sim.simxReadProximitySensor(clientID, irLeft, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Left, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Right, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Middle, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Left2, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Right2, 0, sim.simx_opmode_streaming)
	sim.simxGetVisionSensorImage(clientID, color_sensor_Side, 0, sim.simx_opmode_streaming)