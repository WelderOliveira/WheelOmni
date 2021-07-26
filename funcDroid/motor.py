# coding=utf-8
# Insert in a script in Coppelia

import funcDroid.sim as sim
import funcDroid.globalDefs as glob
from funcDroid.globalDefs import *

import numpy as np
import funcDroid.sensor as sense

## FUNÇÕES DE LOCOMOÇAO ######################################

def Stop():
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackRightMotor, 0, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackLeftMotor, 0, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)
	time.sleep(0.1)

def MoveForward(v):
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor, v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def MoveBack(v):
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, -v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor, -v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def MoveDirectionPosition(direcao, dist):   #Andar reto para frente ou para trás
	andar_em_metros(direcao, 5, dist)

def andar_livre(d,v):

	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v*(-1), sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def andar_livre_lado(d,v):

	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def andar_diagonal(v):

	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,-1*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,1*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,1*v*(-1), sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,-1*v*(-1), sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def giro_livre(d,v):

	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade

	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)

def giro_aberto(d,v):
	sim.simxPauseCommunication(glob.clientID, True)
	if d ==-1:
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
		#sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackRightMotor,(-1)*d*v, sim.simx_opmode_oneshot)
	else:
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotFrontLeftMotor, d*v, sim.simx_opmode_oneshot)
		#sim.simxSetJointTargetVelocity(glob.clientID,glob.robotBackLeftMotor, d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)


def TurnDirectionAng(direcao, ang):   #Girar para a direita ou para a esquerda pelo angulo que você escolher
	if (ang == 180):
		Girar_180_graus_v2(glob.clientID, glob.robotFrontRightMotor, glob.robotFrontLeftMotor, glob.robo)
	else:
		Girar_90_graus_v2(glob.clientID, glob.robotFrontRightMotor, glob.robotFrontLeftMotor, glob.robotBackRightMotor, glob.robotBackLeftMotor, glob.robo, direcao)


def andar_em_metros(d,v,m):
	# d = 1 , andar para frente
	# d =-1 , andar para trás
	# v = velocidade
	# m = valor em metros
	d = d*-1


	erro,a_inicial=sim.simxGetObjectPosition(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
	x_inicial=a_inicial[0]
	y_inicial=a_inicial[1]
	sim.simxPauseCommunication(glob.clientID, True)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotFrontLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackRightMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(glob.clientID, glob.robotBackLeftMotor,d*v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(glob.clientID, False)
	while(True):
		erro,a=sim.simxGetObjectPosition(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
		x=a[0]
		y=a[1]
		# print(x,y,erro)
		if(abs(x-x_inicial)>=m or abs(y-y_inicial)>=m):
			break
	Stop()
	time.sleep(0.2)


def MoveForwardPosition(dist):
	MoveDirectionPosition(frente, dist)



def gira_livre_uma_roda(roda, d, v):

			# roda: escolher com qual roda girar
			# d = 1 , anti horario
			# d = -1 , horario
			# v = velocidade
	if (roda == direita):
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotLeftMotor, d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor, 0, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)
	elif(roda == esquerda):
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotLeftMotor, 0, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID, glob.robotRightMotor, -d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

def MoveSquareForward():
	andar_em_metros(frente, 8, 0.18)
	align.Align()


def TurnInSquare(angle): #gira no centro do quadrado e vai para ponta
	print(angle)
	if(sense.getColor(glob.color_sensor_Left) == PRETO or sense.getColor(glob.color_sensor_Right) == PRETO):
	#align.Align()
		MoveDirectionPosition(tras, 0.065)
	if(angle > 0):
		TurnDirectionAng(esquerda, abs(angle))
	if(angle < 0):
		TurnDirectionAng(direita, abs(angle))
	#MoveDirectionPosition(frente, 0.025)
	align.Align()

def inicio_virar_SUL(): # para a função COM VISÃO

	d=0

	while(True):

		erro,b=sim.simxGetObjectOrientation(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
		gamma=(b[2]*180)/(np.pi)

		if(gamma>=-3 and gamma<=3):
			Stop()
			break

		if(d==0):
			if(gamma>0 and gamma<179.99):
				d = 1
			else:
				d = -1

		v=4
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor,d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

	align.Align()
	andar_em_metros(tras, 5, 0.065)
	return

def inicio_virar_NORTE(): # para a função SEM VISÃO; lembrar de adicionar no if(nao viu prataleira) virar 180.

	d=0

	while(True):

		erro,b=sim.simxGetObjectOrientation(glob.clientID,glob.robo,-1,sim.simx_opmode_blocking)
		gamma=(b[2]*180)/(np.pi)

		if(gamma>=177 or gamma<=-177):
			Stop()
			break

		if(d==0):
			if(gamma>0 and gamma<179.99):
				d = 1
			else:
				d =-1

		v=4
		sim.simxPauseCommunication(glob.clientID, True)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotRightMotor,d*v, sim.simx_opmode_oneshot)
		sim.simxSetJointTargetVelocity(glob.clientID,glob.robotLeftMotor,(-1)*d*v, sim.simx_opmode_oneshot)
		sim.simxPauseCommunication(glob.clientID, False)

	align.Align()
	return


def Girar_X_graus(clientID, _robotRightMotor, _robotLeftMotor, _robo, d, graus):
	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade

	v = 5
	g = graus
	erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)
	while (erro != 0):
		erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)

	gamma_inicial = b_inicial[2] * 180 / (np.pi)
	gamma_target = gamma_inicial - g * d
	if (abs(gamma_target) > 190):
		gamma_target = d * g

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, _robotRightMotor, d * v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotLeftMotor, (-1) * d * v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	while (True):
		erro, b = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
		gamma = b[2] * 180 / (np.pi)

		# print(gamma)
		if (abs(abs(gamma) - abs(gamma_inicial)) >= 0.85 * g):
			break

	# print(gamma_inicial,gamma)
	Stop(clientID, _robotRightMotor, _robotLeftMotor)
	erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
	# gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, _robotRightMotor, d * 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotLeftMotor, (-1) * d * 0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	# print(gamma_inicial,gamma_target,gamma)
	while (True):
		sign = np.sign(gamma)
		erro, b = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
		gamma = b[2]
		gamma = gamma * 180 / (np.pi)

		# print(gamma)
		if (d * (gamma - gamma_target) < 0 or np.sign(gamma) != sign):
			break

	# print(gamma_inicial,gamma)
	Stop(clientID, _robotRightMotor, _robotLeftMotor)


def Girar_90_graus_v2(clientID, robotFrontRightMotor, robotFrontLeftMotor, robotBackRightMotor, robotBackLeftMotor,
					  robo, d):
	# d = 1 , anti horario, esquerda
	# d =-1 , horario, direita
	# v = velocidade

	v = 3
	g = 90
	erro, b_inicial = sim.simxGetObjectOrientation(clientID, robo, -1, sim.simx_opmode_streaming)
	while (erro != 0):
		erro, b_inicial = sim.simxGetObjectOrientation(clientID, robo, -1, sim.simx_opmode_streaming)

	gamma_inicial = b_inicial[1] * 180 / (np.pi)
	gamma_target = gamma_inicial - g * d
	maxgamma = 0
	if (abs(gamma_target) > 90):
		gamma_target = d * g

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, robotFrontRightMotor, (-1) * d * v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotFrontLeftMotor, d * v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotBackRightMotor, (-1) * d * v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotBackLeftMotor, d * v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	while (True):
		erro, b = sim.simxGetObjectOrientation(clientID, robo, -1, sim.simx_opmode_buffer)
		gamma = b[1] * 180 / (np.pi)

		# print(gamma_inicial, gamma, gamma_target)
		if (abs(abs(gamma) - abs(gamma_inicial)) >= 0.80 * g):
			break

	# time.sleep(0.01)

	# print(gamma_inicial,gamma)
	Stop(clientID, robotFrontRightMotor, robotFrontLeftMotor, robotBackRightMotor, robotBackLeftMotor)
	erro, b_inicial = sim.simxGetObjectOrientation(clientID, robo, -1, sim.simx_opmode_buffer)
	# gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, robotFrontRightMotor, (-1) * d * 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotFrontLeftMotor, d * 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotBackRightMotor, (-1) * d * 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, robotBackLeftMotor, d * 0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	# print(gamma_inicial,gamma_target,gamma)
	while (True):
		sign = np.sign(gamma)
		erro, b = sim.simxGetObjectOrientation(clientID, robo, -1, sim.simx_opmode_buffer)
		gamma = b[1]
		gamma = gamma * 180 / (np.pi)

		# print(gamma, gamma_target)
		# print(abs(abs(gamma)-abs(gamma_target)))
		if (abs(abs(abs(gamma) - abs(gamma_target))) < 2 or np.sign(gamma) != sign):
			break

	# print(gamma_inicial,gamma)
	Stop(clientID, robotFrontRightMotor, robotFrontLeftMotor, robotBackRightMotor, robotBackLeftMotor)


def Girar_180_graus_v2(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor,
					   _robo):
	v = 3
	g = 90
	d = 0
	offset = 10

	erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)
	while (erro != 0):
		erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_streaming)

	gamma_inicial = b_inicial[1] * 180 / (np.pi)
	gamma_target = -gamma_inicial
	sign = np.sign(gamma_inicial)
	# if(np.sign(gamma_target+offset*sign) == sign):
	#	d = 1

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, _robotFrontRightMotor, v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotFrontLeftMotor, (-1) * v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotBackRightMotor, v, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotBackLeftMotor, (-1) * v, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	time.sleep(1.1)

	while (True):
		erro, b = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
		gamma = b[1] * 180 / (np.pi)
		print(gamma_inicial, gamma)

		if (np.sign(gamma) != sign and abs(gamma_inicial) < 12):
			sign = -sign
		print(gamma_target + offset * sign, offset, sign)
		# print(gamma >= gamma_target+offset, not sign)

		if (gamma <= gamma_target + offset * sign and sign > 0):
			break
		elif (gamma >= gamma_target + offset * sign and sign < 0):
			break

		time.sleep(0.01)

	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)
	erro, b_inicial = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
	# gamma_inicial=b_inicial[2]*180/(np.pi)

	sim.simxPauseCommunication(clientID, True)
	sim.simxSetJointTargetVelocity(clientID, _robotFrontRightMotor, 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotFrontLeftMotor, (-1) * 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotBackRightMotor, 0.5, sim.simx_opmode_oneshot)
	sim.simxSetJointTargetVelocity(clientID, _robotBackLeftMotor, (-1) * 0.5, sim.simx_opmode_oneshot)
	sim.simxPauseCommunication(clientID, False)

	# print(gamma_inicial,gamma_target,gamma)
	while (True):
		sign = np.sign(gamma)
		erro, b = sim.simxGetObjectOrientation(clientID, _robo, -1, sim.simx_opmode_buffer)
		gamma = b[1]
		gamma = gamma * 180 / (np.pi)

		# print(gamma)
		if (abs(gamma - gamma_target) < 2 or np.sign(gamma) != sign):
			break

	# print(gamma_inicial,gamma)
	Stop(clientID, _robotFrontRightMotor, _robotFrontLeftMotor, _robotBackRightMotor, _robotBackLeftMotor)