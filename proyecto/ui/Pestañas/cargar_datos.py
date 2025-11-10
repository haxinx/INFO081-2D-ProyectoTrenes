import tkinter as tk
from tkinter import font, messagebox
import os, ast
from config.settings import WINDOW_SIZE, TITULO4, ARCHIVO



def cargar_trenes():

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if data == "":
                return {}
            return ast.literal_eval(data)
    except:
        return {}

def guardar_trenes(data):
 
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write(str(data))


root = tk.Tk()
root.title(TITULO4)
root.geometry(WINDOW_SIZE)
root.configure(bg="white")

titulo_font = font.Font(family="Arial", size=20, weight="bold")

titulo = tk.Label(root, text="Trenes Guardados", bg="white", fg="black", font=titulo_font)
titulo.pack(pady=25)

trenes = cargar_trenes()

lista = tk.Listbox(root, width=100, height=12)
lista.pack(pady=15)


for tid, datos in trenes.items():
    nombre = datos.get("NOMBRE", "?")
    destino = datos.get("ESTACION FINAL", "?")
    capacidad = datos.get("CAPACIDAD", "?")
    lista.insert(
        tk.END, 
        f"ID: {tid}  -  Nombre: {nombre}  -  Destino final: {destino}  -  Pasajeros: {capacidad}"
    )

def eliminar():
    sel = lista.curselection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecciona un tren primero")
        return

    item = lista.get(sel[0])
    tid = item.split()[1] 

    if tid in trenes:
        confirm = messagebox.askyesno("Confirmar", f"¿Eliminar el tren con ID {tid}?")
        if confirm:
            del trenes[tid]
            guardar_trenes(trenes)
            lista.delete(sel[0])
            messagebox.showinfo("OK", "Tren eliminado correctamente")

def volver_menu():
    root.destroy()
    import menu_principal
    menu_principal.main()


frame_btns = tk.Frame(root, bg="white")
frame_btns.pack(pady=25)

btn_eliminar = tk.Button(frame_btns, text="Eliminar tren", width=20, relief="groove", command=eliminar)
btn_eliminar.grid(row=0, column=0, padx=10)

btn_volver = tk.Button(frame_btns, text="Volver al menú", width=20, relief="groove", command=volver_menu)
btn_volver.grid(row=0, column=1, padx=10)

root.mainloop()
