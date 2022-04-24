#8
"""
Графические фишки
"""
import tkinter as tk

app = tk.Tk()
app.geometry('600x400')# размер окна

def click():
    print('Clicked')

B = tk.Button(app,text = 'search',command = click,height = 5,width=15,bg = '#FF00FF') # кнопка с текстом seach размер кнопки в пикселях bg is color
B.place(x=10, y=10) # где кнопка
B.pack() # разместить кнопку
app.mainloop()# запуск
