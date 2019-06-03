import serial
import time

ser = serial.Serial('COM4', 9600)

print("Inicializando...")
time.sleep(3)

def getValues():
	ser.write(b'g')
	arduinoData = ser.readline().decode('ascii')
	return arduinoData

while(1):

	userInput = input('\n(Em caso afirmativo digite "sim")\n Deseja ler dados da porta Serial? ')

	if (userInput == 'sim'):
		print(getValues())