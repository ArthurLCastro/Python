# Adicionar linha em Tabela MySQL com Python
# Arthur Castro
# 07 de abril de 2018

import mysql.connector

conn = mysql.connector.connect(
			user='root',
			password='root',
			host='localhost',
			database='Cadastro')

cur = conn.cursor()
query = ("INSERT INTO CLIENTES (NOME, EMAIL, FONE) VALUES ('Arthur Castro','arthur.castro07@gmail.com','912345678')")
cur.execute(query)
conn.commit()

cur.close()
conn.close()
