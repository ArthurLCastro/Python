# Script para leitura continua da Serial /dev/ttyACM0
# Arthur Castro
# fev de 2018

import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1:
	valor = ser.readline()
	print(valor)
