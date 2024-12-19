
from tkinter import Tk, Label
import tkinter as tk
import conexion_db as consultar
import tareas as insertar
import borrar as Borrar
import completar_tarea as actualizar

#insertar.registrar()
#consultar.conectar()
#consulta = Databases()
#consulta.conexion()
#consulta.Consultar()

#consultar.conectar()
#insertar.registrar()
#Borrar.Borrar_tarea()





# Crear la ventana principal
root = tk.Tk()

#medida del canvas
ventana = tk.Label(root, text="TO DO LIST", width=10, height=3)
ventana.pack()

# Crear un widget de entrada
entry = tk.Entry(root)
entry.pack()
etiqueta = tk.Label(root, text="")
etiqueta.pack()


# Función para obtener el texto ingresado
def obtener_texto():
    insertar.registrar(entry.get())
    Obtener_tareas_pendientes()

def borrar_tarea():
    Borrar.Borrar_tarea(int(entry.get()))
    Obtener_tareas_pendientes()

def Obtener_tareas_pendientes():
    consulta_tareas = consultar.conectar()
    string_tareas = "TAREAS PENDIENTES: \n"
    for row in consulta_tareas: 
        string_tareas = string_tareas  + " \n" + str(row[0])+ " "+row[1]+ (" - [Completada] " if row[2] == 1 else "")

    etiqueta.config(text=string_tareas)

def completar_tarea():
    actualizar.completar_tarea(int(entry.get()))
    Obtener_tareas_pendientes()
        
    
Obtener_tareas_pendientes()
 
# Crear un botón para obtener el texto
boton = tk.Button(root, text="Agregar Tarea", command=obtener_texto)
boton.pack()

boton_eliminar = tk.Button(root, text="Eliminar tarea por ID", command=borrar_tarea)
boton_eliminar.pack()

boton_completar_tarea = tk.Button(root, text="Completar Tarea por ID", command=completar_tarea)
boton_completar_tarea.pack()
       
       




# Iniciar el bucle principal de la aplicación
root.mainloop()

