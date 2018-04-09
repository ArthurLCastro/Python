# Adicionar linha em Tabela MySQL com Python
# Arthur Castro
# 09 de abril de 2018

import mysql.connector

print("---------- Cadastro de Clientes ----------")
nome = raw_input("Nome: ")
email = raw_input("e-mail: ")
fone = raw_input("Telefone: ")
print("------------------------------------------")

conn = mysql.connector.connect(
			user='root',
			password='root',
			host='localhost',
			database='Cadastro')

cur = conn.cursor()
query = ("INSERT INTO CLIENTES (NOME, EMAIL, FONE) VALUES ('" + nome + "','" + email + "','" + fone + "')")
cur.execute(query)
conn.commit()

print("Novo cliente adicionado!")

cur.close()
conn.close()
