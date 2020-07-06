#!C:\Program Files (x86)\Python37-32\python.exe
print("Content-type: text/html\n\n");

# ========== Obtendo dados da Página Web ==========
import cgi

form = cgi.FieldStorage()

palavra =  form.getvalue('palavra')

# ========== Chamadas de funções ==========
from saida_de_dados import *
from processamento_de_dados import *

resultado = processaDados(palavra)

imprime(palavra, resultado)