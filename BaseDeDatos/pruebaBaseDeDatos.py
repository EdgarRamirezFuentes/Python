import psycopg2

conn = psycopg2.connect(
    user="edgar-dev",
    password="2014131046",
    host="localhost",
    port="5432",
    database="test_db"
)

## * Traer todos los registros de una tabla
cursor = conn.cursor() ## * Objeto que permite ejecutar sentencias sobre la base de datos.
query = "SELECT * from persona ORDER BY id_persona"
cursor.execute(query) ## * Ejecuta queries en la base de datos.
registros = cursor.fetchall()
print(registros)

'''
## * Traer un registro en específico de una tabla.
idPersona = input("Ingresa el ID a buscar: ")
query2 = "SELECT * FROM persona WHERE id_persona = %s"
cursor.execute(query2,(idPersona))
registros2 = cursor.fetchone()
if registros2 != None:
    print(registros2)
else:
    print("No existe registro con el ID: " + idPersona)


## * Seleccionar varios registros de una tabla
letrasNombres = input("Ingresa los ID a buscar separados por una coma: ")
tuplaLetras = tuple(letrasNombres.split(","))
query3 = "SELECT * FROM persona WHERE id_persona IN %s"
cursor.execute(query3,(tuplaLetras,))
registros3 = cursor.fetchall()
if registros3 != None:
    for registro in registros3:
        print(registro)
else:
    print("No existe registro que contengan las letras propocionadas: ")


## * Insertar un registro a una tabla
nombrePersona = input("Ingresa el nombre de la persona: ")
correoPersona = input("Ingresa el correo de la persona: ")
query4 = "INSERT into persona(nombre_persona, email_persona) values(%s, %s)"
cursor.execute(query4, (nombrePersona, correoPersona))
conn.commit() ## * Guarda la información de las sentencias SQL realizadas, se utiliza en INSERT, UPDATE o DELETE.
print("Registros insertados: " + str(cursor.rowcount)) ## * Retorna el número de registros modificados


## * Insertar varios registros en una sentencia
personas = (
    ("Yael Medina", "yael@gmail.com"),
    ("Tony Arce", "tony@gmail.com"),
    ("Arnulfo Alfaro", "arnulfo@gmail.com")    
)
query5 = "INSERT into persona(nombre_persona, email_persona) values(%s, %s)"
cursor.executemany(query5, personas)
conn.commit() ## * Guarda la información de las sentencias SQL realizadas, se utiliza en INSERT, UPDATE o DELETE.
print("Registros insertados: " + str(cursor.rowcount)) ## * Retorna el número de registros modificados



## * Actualizar datos de un registro en la base de datos

idPersona = input("Ingresa el ID de la persona a modificar: ")
nuevoNombre = input("Ingresa el nuevo nombre de la persona: ")
query6 = "UPDATE persona SET email_persona = %s where id_persona = %s"
cursor.execute(query6, (nuevoNombre, idPersona))
conn.commit()
print("Se ha modificado " + str(cursor.rowcount) + " registro.")



## * Actualizar varios registros de una tabla
personas = (
    ("Edgar", 1),
    ("Yael Akimichi", 2),
    ("Arnulfo García", 4)
)
query7 = "UPDATE persona SET nombre_persona = %s WHERE id_persona = %s"
cursor.executemany(query7, personas)
conn.commit()
print(f'Se han modificado {cursor.rowcount} registros')


## * Eliminar un registro de una tabla
idAEliminar = input("Ingresa el ID del registro a eliminar: ")
query8 = 'DELETE FROM persona WHERE id_persona = %s'
cursor.execute(query8, (idAEliminar,))
conn.commit()
print(f'Se eliminó {cursor.rowcount} con éxito')


## * Eliminar varios registros de una tabla

IDs = input("Ingresa los ID a eliminar separados por una coma: ")
tuplaIDs = tuple(IDs.split(','))
query9 = "DELETE FROM persona WHERE id_persona = %s"
cursor.executemany(query9, (tuplaIDs))
conn.commit()
print(f'Se eliminaron {cursor.rowcount} registros con éxito')

'''

cursor.close()
conn.close()

