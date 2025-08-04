# Конвертер величин
# Автор: Pixena
# Версия: 1.0
# Точка входа для конвертера

import tkinter as tk
import interface

def main():
    root = tk.Tk()
    app = interface.MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()