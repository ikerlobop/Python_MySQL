# Python_MySQL

Como conectar y crear bases de datos en MySQL phpMyAdmin usando Python.

Primero, es necesario instalar el paquete conector de MySQL para Python. Para hacerlo, se debe ir al directorio "Scripts" de la instalación de Python.

  Por ejemplo, en mi caso: 
  
  C:\Language\Python\Python36-32\Scripts

y abrir la ventana de comandos desde allí. Luego, se debe escribir el siguiente comando:

  C:\Language\Python\Python36-32\Scripts> pip install pymysql

Esto instalará el paquete "pymysql" para poder conectarse a una base de datos MySQL desde Python.

Yo estoy utilizando XAMPP para la base de datos. Este es un paso opcional, si ya tienes instalado MySQL, puedes saltar este paso.
Antes de comenzar a programar, ejecuta el panel de control de XAMPP y inicia Apache y MySQL.

Vas al navegador e introduces: 
http://localhost/phpmyadmin/ 
Ya te puedes conectar a la base de datos,

Vamos a construir la conexión con la tabla en Python:

#importamos librería instalada anteriormente
import pymysql

#Conexión a base de datos
connection = pymysql.connect(host="localhost",user="root",passwd="",database="databaseName" )
cursor = connection.cursor()

connection.close()

Por ejemplo si mi base de datos es "trabajo" y tiene usuario root y password(1234), quedaría así.

#importamos librería instalada anteriormente
import pymysql

#Conexión a base de datos
connection = pymysql.connect(host="localhost",user="root",passwd="1234",database="trabajo" )
cursor = connection.cursor()

connection.close()

De momento os dejo la conexión, más adelante incorporaré el CRUD completo.


