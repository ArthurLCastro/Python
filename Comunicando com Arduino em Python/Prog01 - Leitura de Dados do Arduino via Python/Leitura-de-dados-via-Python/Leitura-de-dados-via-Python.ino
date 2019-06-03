// Leitura de dados do Arduino via Python
// Arthur L Castro
// Junho de 2019

/*
 Este programa demonstra a execução de uma função qualquer, retornando um dado pela Serial
 quando o caracter 'g' é recebido. Um programa em Python fará parte desta comunicação
*/

void setup(){
   Serial.begin(9600);
}

void loop(){
  if(Serial.available()>0){
    if(Serial.read() == 'g'){

      // A linha abaixo pode ser substituída pela leitura do valor de um pino do Arduino, por exemplo
      long var = random();        // Gera um valor aleatório para demonstração da comunicação
      
      Serial.println(var);
    }
  }
}
