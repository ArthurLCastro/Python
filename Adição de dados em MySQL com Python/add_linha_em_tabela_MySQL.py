# Adicionar linha em Tabela MySQL com Python
# Arthur Castro
# 07 de abril de 2018

import mysql.connector

conn = mysql.connector.connect(
			user='root',
			password='root',
			host='127.0.0.1',
			database='Cadastro')

cur = conn.cursor()
query = ("INSERT INTO Clientes (NOME, EMAIL, FONE) VALUES ('Arthur Castro','arthur.castro07@gmail.com','912345678')")
cur.execute(query)
conn.commit()

cur.close()
conn.close()