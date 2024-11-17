import tkinter as tk
import time

# Напишем функцию
def print_line():
    # Список строк, которые будут выводиться в окно
    lines = [
        "Запуск программы...",
        "Выполняется операция 1...",
        "Выполняется операция 2...",
        "Выполняется операция 3...",
        "Процесс завершен."
    ]

    for line in lines:
        # Добавляем строку в текстовое поле
        text_box.insert(tk.END, line + '\n')
        # Прокручиваем текст вниз
        text_box.see(tk.END)
        # Обновляем окно, чтобы изменения сразу отобразились
        window.update()
        # Пауза перед следующей строкой
        time.sleep(1)

# Создаем главное окно
window = tk.Tk()
window.title("Программа")

# Создаем текстовое поле для вывода строк
text_box = tk.Text(window, height=10, width=40)
text_box.pack(pady=20)

# Кнопка для запуска вывода текста
start_button = tk.Button(window, text="Запуск", command=print_line)
start_button.pack()

# Запуск основного цикла обработки событий
window.mainloop()



