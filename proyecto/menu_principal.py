import tkinter as tk
from tkinter import font

from config import WINDOW_TITLE, WINDOW_SIZE, BG_COLOR
from ui.widget.button import crear_boton

def main():

    def iniciar_simulacion():
        root.destroy()
        import ui.Pestañas.simulacion


    def cargar_guardado():
        root.destroy()
        import ui.Pestañas.cargar_datos

    def editar_tren():
        root.destroy()
        import ui.Pestañas.editar_tren

    def salir():
        root.destroy()

    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=BG_COLOR)


    titulo_font = font.Font(family="Arial", size=28, weight="bold")

    titulo = tk.Label(root, text="MENÚ\nPRINCIPAL", bg="white", fg="black", font=titulo_font, justify="center")
    titulo.pack(pady=30)

    btn_iniciar = crear_boton("INICIAR SIMULACIÓN", iniciar_simulacion)
    btn_cargar   = crear_boton("CARGAR GUARDADO", cargar_guardado)
    btn_config   = crear_boton("EDITAR TREN", editar_tren)
    btn_salir    = crear_boton("SALIR", salir)


    root.mainloop()

if __name__ == "__main__":
    print("Ejecutando desde Main.")
    main()

