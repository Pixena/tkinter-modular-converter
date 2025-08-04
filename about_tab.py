import tkinter as tk
from tkinter import ttk

BG_COLOR = "#181818"
FG_COLOR = "#fff"
ACCENT_COLOR = "#ff8800"

class AboutTab:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        title = ttk.Label(self.frame, text="О программе", font=('Arial', 14, 'bold'), foreground=ACCENT_COLOR)
        title.pack(pady=(20, 5))
        text = (
            "Модульный конвертер величин\n"
            "Автор: Pixena\n"
            "Версия: 1.0\n\n"
            "Программа позволяет быстро и удобно переводить длину, массу и температуру\n"
            "между различными единицами измерения.\n\n"
            "Просто выберите вкладку, введите значение и получите результат!"
        )
        label = ttk.Label(self.frame, text=text, font=('Arial', 11), foreground=FG_COLOR, justify="center")
        label.pack(pady=10)