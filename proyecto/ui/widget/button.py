import tkinter as tk
from tkinter import font


def crear_boton(texto, command):
        return tk.Button( text=texto,
                        font=("Arial", 12, "bold"),
                        width = 25, height=2,
                        relief="groove",
                        command=command).pack(pady=6)

