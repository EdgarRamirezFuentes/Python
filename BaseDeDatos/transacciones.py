import psycopg2

conn = psycopg2.connect(
    user="edgar-dev",
    password="2014131046",
    host="localhost",
    port="5432",
    database="test_db"
)

## * Solo se utiliza en pruebas
## ! conn.autocommit = True
cursor = conn.cursor()
try:
    
    query = "INSERT INTO persona(nombre_persona, email_persona) VALUES (%s, %s)"
    cursor.execute(query, ("Barry Allen", "barry@gmail.com"))
    
    query = "UPDATE persona SET nombre_persona = %s WHERE id_persona = %s"
    
    ## ! Si no existe el ID no lanza error
    cursor.execute(query, ("Yael Medina", 30000)) 
    
    conn.commit()
except Exception as ex:
    ## * Deshace los cambios previamente realizados
    conn.rollback()
    print(f"Ocurrió un error en las transacciones: {e}")

cursor.close()
conn.close()
