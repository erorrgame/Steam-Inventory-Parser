import tkinter as tk
from tkinter import *
from parcer_inventory import get_items


def show_result():
    result_text = get_items(steam_id.get(), game_id.get())
    console_text.config(state=tk.NORMAL)
    console_text.delete("1.0", tk.END)
    for item in result_text:
        console_text.insert(tk.END, item)
    console_text.config(state=tk.DISABLED)


# Создание окна
window = tk.Tk()
window.title("Консоль")
window.geometry('700x500')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.config(width=200, height=200)
frame.pack()

steam_lb = Label(
    frame,
    text="Введите Steam ID пользователя   "
)
steam_lb.config(font=("Arial", 12))
steam_lb.grid(row=3, column=1)

game_lb = Label(
    frame,
    text="Введите ID игры   ",
)
game_lb.config(font=("Arial", 12))
game_lb.grid(row=4, column=1)

steam_id = Entry(
    frame,
)
steam_id.config(font=("Arial", 12))
steam_id.grid(row=3, column=2, pady=5)

game_id = Entry(
    frame,
)
game_id.config(font=("Arial", 12))
game_id.grid(row=4, column=2, pady=5)

# Создание виджета текстовой области
console_text = tk.Text(window, height=20, width=65)
console_text.config(bg="#C1CDCD", font=("Arial", 10), relief="groove", state=tk.DISABLED)
console_text.pack()

# Создание кнопки для вызова функции
loadimage = PhotoImage(file="knopka.png")
button = tk.Button(window, text="Показать результат", command=show_result, image=loadimage)
button["border"] = "0"
button.pack()


# Запуск основного цикла окна
window.mainloop()
