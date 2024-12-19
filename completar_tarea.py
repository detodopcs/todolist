import psycopg2


def completar_tarea(tarea_id):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='tolist_db'
        )

        cursor = connection.cursor()
        # Consulta SQL parametrizada (PREVENCIÓN DE INYECCIÓN SQL)
        sql = f"UPDATE list_tasks SET Iscompleted=1 WHERE id={tarea_id}"
        cursor.execute(sql)
        connection.commit()       

    except psycopg2.Error as error:  # Especificar el tipo de excepción es mejor
        print(f"Error al intentar actualizar un registro: {error}")
        connection.rollback() #Revertir la transacción en caso de error

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

