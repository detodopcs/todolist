import psycopg2


def conectar():
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='tolist_db'
        )

        print("Conexion exitosa")
        cursor=connection.cursor()
        cursor.execute('SELECT version()')
        row=cursor.fetchone()
        #print(row)
        cursor.execute('SELECT * FROM list_tasks ORDER BY id')
        rows=cursor.fetchall()        
        #for row in rows:
            #return rows
            #print(row)
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print("conexion finalizada")

    return rows




