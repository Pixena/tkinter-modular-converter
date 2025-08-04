import tkinter as tk
from tkinter import ttk
import length_tab
import mass_tab
import temp_tab
import about_tab

BG_COLOR = "#181818"
FG_COLOR = "#fff"
ACCENT_COLOR = "#ff8800"
TAB_BG = "#222"
TAB_ACTIVE = "#333"

class MainWindow:
    def __init__(self, master):
        master.title("Конвертер величин")
        master.geometry("540x340")
        master.configure(bg=BG_COLOR)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=BG_COLOR, borderwidth=0)
        style.configure('TNotebook.Tab', background=TAB_BG, foreground=FG_COLOR, font=('Arial', 11, 'bold'), padding=10)
        style.map('TNotebook.Tab', background=[('selected', ACCENT_COLOR)], foreground=[('selected', BG_COLOR)])
        style.configure('TFrame', background=BG_COLOR)
        style.configure('TLabel', background=BG_COLOR, foreground=FG_COLOR, font=('Arial', 11))
        style.configure('TButton', background=ACCENT_COLOR, foreground=BG_COLOR, font=('Arial', 11, 'bold'))
        style.map('TButton', background=[('active', '#ffb366')])

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.tabs = {}

        self.length_tab = length_tab.LengthTab(self.notebook)
        self.notebook.add(self.length_tab.frame, text="Длина")
        self.tabs['Length'] = self.length_tab

        self.mass_tab = mass_tab.MassTab(self.notebook)
        self.notebook.add(self.mass_tab.frame, text="Масса")
        self.tabs['Mass'] = self.mass_tab

        self.temp_tab = temp_tab.TempTab(self.notebook)
        self.notebook.add(self.temp_tab.frame, text="Температура")
        self.tabs['Temperature'] = self.temp_tab

        self.about_tab = about_tab.AboutTab(self.notebook)
        self.notebook.add(self.about_tab.frame, text="О программе")
        self.tabs['About'] = self.about_tab