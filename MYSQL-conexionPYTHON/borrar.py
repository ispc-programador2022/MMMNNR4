import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  port= 3307,
                                  password="1234", 
                                  database="criptomonedas")
cursor1=conexion1.cursor()
cursor1.execute("delete from criptomonedas where id=3")
for fila in cursor1:
    print(fila)
conexion1.close()   