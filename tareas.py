import psycopg2
import conexion_db as con

def registrar(tarea):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='tolist_db'
        )

        cursor = connection.cursor()

        # Consulta SQL parametrizada (PREVENCIÓN DE INYECCIÓN SQL)
        sql = "INSERT INTO list_tasks (tasks,IsCompleted) VALUES (%s,0)"

        # Solicitud de datos al usuario
        #lista = input("Ingrese la tarea: ")

        # Los datos se pasan como una tupla (o lista)
        datos = (tarea,)  # La coma es crucial para crear una tupla de un solo elemento

        cursor.execute(sql, datos)
        connection.commit()

        registros = cursor.rowcount
        

    except psycopg2.Error as error:  # Especificar el tipo de excepción es mejor
        print(f"Error al insertar el registro: {error}")
        connection.rollback() #Revertir la transacción en caso de error

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#Ejemplo de uso
if __name__ == "__main__":
    registrar()