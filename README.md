import tkinter as tk

def click():
    global score
    score += 1
    # Обновляем текст на метке
    label_score.config(text=f"Счёт: {score}")

window = tk.Tk()
window.title("Мой первый кликер")
window.geometry("300x200")

score = 0

label_score = tk.Label(window, text=f"Счёт: {score}", font=("Arial", 24))
label_score.pack(pady=20)

btn_click = tk.Button(window, text="Кликни меня!", command=click, 
                      width=15, height=2, bg="lightblue")
btn_click.pack(pady=10)

window.mainloop()
