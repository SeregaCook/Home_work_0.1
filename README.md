import tkinter as tk

# Функция, которая срабатывает при нажатии на кнопку
def click():
    global score
    score += 1
    # Обновляем текст на метке
    label_score.config(text=f"Счёт: {score}")

# Создаем главное окно
window = tk.Tk()
window.title("Мой первый кликер")
window.geometry("300x200")

# Переменная для хранения очков
score = 0

# Создаем метку для отображения счета
label_score = tk.Label(window, text=f"Счёт: {score}", font=("Arial", 24))
label_score.pack(pady=20)

# Создаем кнопку кликера
btn_click = tk.Button(window, text="Кликни меня!", command=click, 
                      width=15, height=2, bg="lightblue")
btn_click.pack(pady=10)

# Запуск цикла обработки событий
window.mainloop()
