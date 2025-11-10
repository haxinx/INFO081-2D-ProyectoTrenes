import tkinter as tk
from tkinter import font
import time
from reloj.py import SimulationClock
from config import WINDOW_TITLE, WINDOW_SIZE, BG_COLOR
from ui.widget.button import crear_boton




def main():

    mi_reloj = SimulationClock(hora_inicio=6)
    running = True
    pasos_simulacion = 0

    print("iniciando simulación de trenes")

    while running:
        mi_reloj.avanzar_tiempo(minutos=1)
        hora_actual_str = mi_reloj.get_hora_str()
        print(f"Hora: {hora_actual_str}")
        pasos_simulacion += 1
    
        if pasos_simulacion > (60 * 24):
        running = False
        print("Simulación de un dia completada.")
    
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


