import tkinter as tk
from tkinter import ttk
import mass_logic
import config

class MassTab:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg=config.BG_COLOR)
        title = tk.Label(self.frame, text="Конвертер массы", font=(config.FONT_FAMILY, 18, 'bold'), fg=config.OP_COLOR, bg=config.BG_COLOR)
        title.pack(pady=(20, 5))

        self.entry = tk.Entry(self.frame, font=(config.FONT_FAMILY, 24), bg=config.BG_COLOR, fg='white', bd=0, justify='right', insertbackground='white')
        self.entry.insert(0, '1')
        self.entry.pack(pady=10, padx=20, fill='x')

        units_frame = tk.Frame(self.frame, bg=config.BG_COLOR)
        units_frame.pack(pady=5)
        tk.Label(units_frame, text="Из:", font=(config.FONT_FAMILY, 14), fg='white', bg=config.BG_COLOR).pack(side=tk.LEFT)
        self.from_var = tk.StringVar(value=config.MASS_UNITS[0])
        self.from_menu = ttk.Combobox(units_frame, textvariable=self.from_var, values=config.MASS_UNITS, width=12, state="readonly", font=(config.FONT_FAMILY, 12))
        self.from_menu.pack(side=tk.LEFT, padx=5)
        tk.Label(units_frame, text="в:", font=(config.FONT_FAMILY, 14), fg='white', bg=config.BG_COLOR).pack(side=tk.LEFT)
        self.to_var = tk.StringVar(value=config.MASS_UNITS[1])
        self.to_menu = ttk.Combobox(units_frame, textvariable=self.to_var, values=config.MASS_UNITS, width=12, state="readonly", font=(config.FONT_FAMILY, 12))
        self.to_menu.pack(side=tk.LEFT, padx=5)

        self.button = tk.Button(self.frame, text="Перевести", font=(config.FONT_FAMILY, 16, 'bold'), bg=config.OP_COLOR, fg='white', bd=0, command=self.convert, activebackground='#ffb366')
        self.button.pack(pady=15, ipadx=10, ipady=5)

        self.result_label = tk.Label(self.frame, text="", font=(config.FONT_FAMILY, 16, 'bold'), fg=config.OP_COLOR, bg=config.BG_COLOR)
        self.result_label.pack(pady=10)

    def convert(self):
        value = self.entry.get()
        try:
            num = float(value)
        except:
            self.result_label.config(text="Ошибка: введите число")
            return
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()
        result = mass_logic.convert_mass(num, from_unit, to_unit)
        self.result_label.config(text=f"{num} {from_unit} = {result} {to_unit}")