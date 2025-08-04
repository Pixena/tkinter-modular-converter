import tkinter as tk
from tkinter import ttk
import temp_logic
import config

BG_COLOR = "#181818"
FG_COLOR = "#fff"
ACCENT_COLOR = "#ff8800"
ENTRY_BG = "#222"
ENTRY_FG = "#fff"

class TempTab:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
        title = ttk.Label(self.frame, text="Конвертер температуры", font=('Arial', 14, 'bold'), foreground=ACCENT_COLOR)
        title.pack(pady=(10, 2))

        desc = ttk.Label(self.frame, text="Введите значение, выберите шкалы и нажмите 'Перевести'.", font=('Arial', 10), foreground="#bbb")
        desc.pack(pady=(0, 10))

        entry_frame = ttk.Frame(self.frame)
        entry_frame.pack(pady=5)
        ttk.Label(entry_frame, text="Значение:").pack(side=tk.LEFT, padx=(0, 5))
        self.entry = tk.Entry(entry_frame, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=FG_COLOR, width=12, font=('Arial', 11))
        self.entry.pack(side=tk.LEFT)
        self.entry.insert(0, "0")

        units_frame = ttk.Frame(self.frame)
        units_frame.pack(pady=5)
        ttk.Label(units_frame, text="Из:").pack(side=tk.LEFT)
        self.from_var = tk.StringVar(value=config.TEMP_UNITS[0])
        self.from_menu = ttk.Combobox(units_frame, textvariable=self.from_var, values=config.TEMP_UNITS, width=12, state="readonly")
        self.from_menu.pack(side=tk.LEFT, padx=5)
        ttk.Label(units_frame, text="в:").pack(side=tk.LEFT)
        self.to_var = tk.StringVar(value=config.TEMP_UNITS[1])
        self.to_menu = ttk.Combobox(units_frame, textvariable=self.to_var, values=config.TEMP_UNITS, width=12, state="readonly")
        self.to_menu.pack(side=tk.LEFT, padx=5)

        self.button = ttk.Button(self.frame, text="Перевести", command=self.convert)
        self.button.pack(pady=10)

        self.result_label = ttk.Label(self.frame, text="", font=('Arial', 12, 'bold'), foreground=ACCENT_COLOR)
        self.result_label.pack(pady=5)

        ttk.Label(self.frame, text="История:").pack(pady=(10, 0))
        self.history = tk.Listbox(self.frame, height=4, bg=ENTRY_BG, fg=ENTRY_FG, font=('Arial', 10))
        self.history.pack(fill='x', padx=30, pady=(0, 10))

    def convert(self):
        value = self.entry.get()
        try:
            num = float(value)
        except:
            self.result_label.config(text="Ошибка: введите число")
            return
        from_unit = self.from_var.get()
        to_unit = self.to_var.get()
        result = temp_logic.convert_temp(num, from_unit, to_unit)
        self.result_label.config(text=f"{num} {from_unit} = {result} {to_unit}")
        self.history.insert(0, f"{num} {from_unit} → {result} {to_unit}")