import serial
import time

ser = serial.Serial('COM4', 9600)

print("Inicializando...")
arquivo = open('dados.txt', 'w')
time.sleep(3)

def getValues():
	ser.write(b'g')
	arduinoData = ser.readline().decode('ascii')
	return arduinoData

while(1):

	userInput = input('\n(Em caso afirmativo digite "sim")\n Deseja ler dados da porta Serial? ')

	if (userInput == 'sim'):
		leitura = getValues()
		print(leitura)

		arquivo.write(leitura)
		arquivo.close()
		break