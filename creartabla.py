import sqlite3
conexion=sqlite3.connect("basededatos1.db")
cursor=conexion.cursor()
lista_personas=[('pedro','rodrigez','Perez',26),('maria','lopez','Gomez',45),('luis','gonzales','Perez',46)]
#cursor.execute("CREATE TABlE PERSONAS (nombre TEXT,apellido1 TEXT,apellido2 TEXT,edad INTEGER)")
#cursor.execute("INSERT INTO PERSONAS VALUES('Antonio','Perez','Gomez',35)")
#cursor.executemany("INSERT	 INTO	PERSONAS	 VALUES	(?,?,?,?)",lista_personas)
cursor.execute("SELECT * FROM PERSONAS WHERE  edad>20 ORDER BY nombre ")
#cursor.execute("SELECT * FROM PERSONAS WHERE  nombre='maria' ")
#cursor.execute("UPDATE PERSONAS SET edad=30 WHERE nombre='maria' ")
#cursor.execute	("DELETE FROM PERSONAS WHERE nombre	='pedro'")
personas=cursor.fetchall()
for 	persona	 in personas:	 
		print(persona)
conexion.commit()
conexion.close()