#importamos librería previamente instalada
import pymysql

#Conectamos a la base de datos
connection = pymysql.connect(host="localhost",user="root",passwd="",database="databaseName" )

#Establece un cursor(indicador)
cursor = connection.cursor()

#Cerramos la conexión
connection.close()
