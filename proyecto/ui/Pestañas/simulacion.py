import tkinter as tk
from tkinter import font

from config.settings import WINDOW_SIZE, TITULO3
import os

root = tk.Tk()
root.title(TITULO3)
root.geometry(WINDOW_SIZE)
root.configure(bg="#ffffff")

titulo_font = font.Font(family="Arial", size=18, weight="bold")

titulo = tk.Label(root, text="Simulación", bg="white", font=titulo_font)
titulo.pack(pady=10)


frame_hora = tk.Frame(root, bg="white", bd=2, relief="groove")
frame_hora.pack(pady=20)

lbl_hora_titulo = tk.Label(frame_hora, text="Hora de simulación:", bg="white", font=("Arial", 11, "bold"))
lbl_hora_titulo.pack(pady=(5,0))

lbl_hora = tk.Label(frame_hora, text="9:30", bg="white", font=("Arial", 25, "bold"))
lbl_hora.pack(pady=(0,5))



frame_est = tk.Frame(root, bg="white")
frame_est.pack(pady=30)


tren1 = tk.Label(frame_est, text="🚆", bg="white", font=("Arial",30))
tren1.grid(row=0, column=0, padx=50)

tren2 = tk.Label(frame_est, text="🚆", bg="white", font=("Arial",30))
tren2.grid(row=0, column=2, padx=50)


est1 = tk.Label(frame_est, text="Puerto\nMontt", bg="white", relief="groove", width=12)
est1.grid(row=1, column=0, pady=10)

est2 = tk.Label(frame_est, text="Osorno", bg="white", relief="groove", width=12)
est2.grid(row=1, column=1, pady=10)

est3 = tk.Label(frame_est, text="Valdivia", bg="white", relief="groove", width=12)
est3.grid(row=1, column=2, pady=10)



frame_btns = tk.Frame(root, bg="white")
frame_btns.pack(pady=30)

btn_avanzar = tk.Button(frame_btns, text="Avanzar turno", width=15, relief="groove")
btn_pausar  = tk.Button(frame_btns, text="Pausar", width=15, relief="groove")

btn_avanzar.grid(row=0, column=0, padx=10, pady=5)
btn_pausar.grid(row=0, column=1, padx=10, pady=5)


btn_reiniciar = tk.Button(root, text="Reiniciar", width=40, relief="groove")
btn_reiniciar.pack(pady=10)

def volver_menu():
    root.destroy()
    import menu_principal
    menu_principal.main()


btn_volver = tk.Button(root, text="Volver al menú", width=40, relief="groove", command=volver_menu)
btn_volver.pack(pady=10)


root.mainloop()
