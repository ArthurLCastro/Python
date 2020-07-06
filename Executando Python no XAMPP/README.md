# Executando Python no XAMPP

Este é um simples teste do uso do CGI (Common Gateway Interface) em Python e uma forma de processar dados recebidos por um formulário web

## **Configuração do XAMPP:**
Adicione ".py" ao "AddHandler" do arquivo de configuração [httpd.conf](httpd.conf) do apache que se encontra em .../xampp/apache/conf

Abaixo está a linha 435 modificada:

    AddHandler cgi-script .cgi .pl .asp .py

## **Informando caminho do Python Interpreter:**
Na primeira linha do arquivo [web-to-python.py](web-to-python.py) informe o diretório em que se encontra o python instalado em seu computador:

    #!C:\Program Files (x86)\Python37-32\python.exe

## **Executando Teste:**
Abra o arquivo [entrada_de_dados.html](entrada_de_dados.html) no navegador e envie uma palavra qualquer. O servidor irá utilizar o Python para processar e exibir a página com a contagem das letras.