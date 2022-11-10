import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="1234",
                                  port= 3307, 
                                  database="criptomonedas")
cursor1=conexion1.cursor()
sql="insert into criptomonedas(nombre_criptomoneda) values (%s)"
datos=["Binance"]
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()  

  