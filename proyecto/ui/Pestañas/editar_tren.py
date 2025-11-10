import tkinter as tk
from tkinter import font, ttk
import os
import ast
from config.settings import WINDOW_TITLE, WINDOW_SIZE , ARCHIVO , TITULO2

def cargar_diccionario():
   
    if not os.path.exists(ARCHIVO):
        return {}
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
        if contenido == "":
            return {}
        try:
            return ast.literal_eval(contenido)
        except:
            return {}

def guardar_diccionario(dic):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(str(dic))
    print("Archivo trenes.txt actualizado correctamente.")

def guardar_tren():
    dic = cargar_diccionario()
    datos = {k: v.get() for k, v in entries.items()}
    ID = datos["ID"].strip()

    if ID == "":
        print("⚠️ Debe ingresar un ID para el tren.")
        return

    dic[ID] = datos
    guardar_diccionario(dic)
    print(f"✅ Tren con ID {ID} guardado o actualizado correctamente.")

def modificar_tren():
    dic = cargar_diccionario()
    ID = entries["ID"].get().strip()

    if ID not in dic:
        print(f"⚠️ No existe el tren con ID {ID}.")
        return

    nuevos_datos = {k: v.get() for k, v in entries.items()}
    dic[ID] = nuevos_datos
    guardar_diccionario(dic)
    print(f"✏️ Tren con ID {ID} modificado correctamente.")

def eliminar_tren():
    dic = cargar_diccionario()
    ID = entries["ID"].get().strip()

    if ID in dic:
        del dic[ID]
        guardar_diccionario(dic)
        print(f"🗑️ Tren con ID {ID} eliminado correctamente.")
    else:
        print(f"⚠️ No existe el tren con ID {ID} para eliminar.")

def volver_menu():
    root.destroy()
    import menu_principal
    menu_principal.main()


root = tk.Tk()
root.title(TITULO2)
root.geometry(WINDOW_SIZE)
root.configure(bg="white")

titulo_font = font.Font(family="Arial", size=18, weight="bold")
titulo = tk.Label(root, text="Editar tren", bg="white", font=titulo_font)
titulo.pack(pady=10)

frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

labels = ["TREN", "ESTACION FINAL", "ID", "NOMBRE", "VELOCIDAD", "CAPACIDAD"]
entries = {}

for i, label in enumerate(labels):
    lbl = tk.Label(frame, text=label, bg="white", font=("Arial", 11, "bold"))
    lbl.grid(row=i*2, column=0, sticky="w", pady=(10,0))

    if label == "TREN":
        tren_lista = ["X'trapolis 100", "SFB-500", "Locomotora V-607"]
        cmb_tren = ttk.Combobox(frame, values=tren_lista, width=37, state="readonly")
        cmb_tren.grid(row=i*2+1, column=0, pady=(0,10))
        entries[label] = cmb_tren

    elif label == "ESTACION FINAL":
        estaciones = ["Puerto Montt", "Osorno", "Valdivia"]
        cmb_est = ttk.Combobox(frame, values=estaciones, width=37, state="readonly")
        cmb_est.grid(row=i*2+1, column=0, pady=(0,10))
        entries[label] = cmb_est

    else:
        entry = tk.Entry(frame, width=40, relief="groove")
        entry.grid(row=i*2+1, column=0, pady=(0,10))
        entries[label] = entry

btn_guardar_ahora = tk.Button(root, text="Guardar cambios", width=40, relief="groove", command=guardar_tren)
btn_guardar_ahora.pack(pady=10)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Modificar tren", width=15, relief="groove", command=modificar_tren).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Cancelar", width=15, relief="groove", command=volver_menu).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Eliminar", width=15, relief="groove", command=eliminar_tren).grid(row=0, column=2, padx=10)

root.mainloop()
