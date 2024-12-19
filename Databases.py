

import psycopg2
class Databases():

    def __init__(self):
        self.connection = None
   
    @property
    def connection (self):
        return self.connection        

    def conexion(self):
        self.connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='tolist_db'
        )



    def Consultar(self):
        elcursor= self.connection.cursor()
        elcursor.execute('SELECT * FROM list_tasks')
        
        




       
    