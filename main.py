# import os
import time

import funcDroid.globalDefs as glob
import funcDroid.sim as sim
from funcDroid.garraAlgo import abrir_garra, fechar_garra
from funcDroid.motor import andar_livre, giro_livre, Stop, andar_em_metros, giro_aberto, andar_livre_lado, andar_diagonal
from funcDroid.sensor import getColor as le_cor, getDistanceIR as le_distancia

CorEsquerda = glob.color_sensor_Left
CorDireita = glob.color_sensor_Right
CorMeio = glob.color_sensor_Middle
CorDireita2 = glob.color_sensor_Right2
CorEsquerda2 = glob.color_sensor_Left2
CorLado = glob.color_sensor_Side

SensorUsEsquerdoFront = glob.us_left_front
SensorUsDireitoFront = glob.us_right_front
SensorUsFrente = glob.us_front
SensorUsEsquerda = glob.us_left

frente = glob.frente
tras = glob.tras
horario = glob.horario
antihorario = glob.antihorario

#################################################################################

# Nomes dos Sensores:
# Ultrassom:
# 	SensorUsFrente
#	SensorUsEsquerda
# Cor:
#	CorEsquerda
#	CorDireita

# PRETO = 0
# VERMELHO = 1
# AMARELO = 2
# VERDE = 3
# AZUL = 5
# BRANCO = 6

# Funções movimento:
#	andar_em_metros(direção, velocidade, metros)
#	andar_livre(direção, velocidade)
#	giro_livre(orientação, velocidade)
#	parar()
#
# Funções sensores:
#	le_cor(sensor)
#	le_distancia(sensor)

# ESCREVER SEU CÓDIGO AQUI:
#################################################################################
li = []
a = True


class odiocoopelia:

    def main(self, a):
        while a == True:
            # andar_diagonal(2)
            andar_livre_lado(1,2)
            # giro_livre(-1,2)
            # andar_livre(1,2)

init = odiocoopelia()
init.main(a)

#################################################################################

# Pause simulation
clientID = glob.clientID
# sim.simxPauseSimulation(clientID,sim.simx_opmode_oneshot_wait)

# Now close the connection to V-REP:
# sim.simxAddStatusbarMessage(clientID, 'Programa pausado', sim.simx_opmode_blocking )
sim.simxFinish(clientID)
print('Program ended')
