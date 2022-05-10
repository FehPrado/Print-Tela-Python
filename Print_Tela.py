import pyautogui
import time     
from tkinter import *



menu_inicial = Tk()
menu_inicial.title("Print Tela")
menu_inicial['bg'] = '#46685b'
menu_inicial.geometry('300x200')

def executar(): 

   for i in range (1,10+1):
    foto=pyautogui.screenshot()
    time.sleep(10)
    foto.save('foto1%d.png'%(i))
    print('Working %d'%(i))
print('working')

#botão

btn1 = Button(menu_inicial, text = 'Executar', command = executar)
btn1.pack()
btn1.place(x=100, y=100)

menu_inicial.mainloop()