# Leitura da Porta Serial com Python

Para a execução destes scripts, deve-se:
  1. Instalar a bilbioteca [pySerial](http://pyserial.readthedocs.io/en/latest/pyserial.html)
  2. Modificar a linha 6 para a Porta Serial que se queira ler:
  
    `ser = serial.Serial('/dev/ttyACM0', 9600)`

O script [leitura_da_porta_serial.py](https://github.com/ArthurLCastro/Python/blob/master/Leitura%20da%20Porta%20Serial%20com%20Python/leitura_da_porta_serial.py) faz apenas uma leitura por vez, enquanto o script [leitura_continua_da_porta_serial.py](https://github.com/ArthurLCastro/Python/blob/master/Leitura%20da%20Porta%20Serial%20com%20Python/leitura_continua_da_porta_serial.py) lê continuamente os dados enviados através da porta serial.
