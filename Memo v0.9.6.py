import Tkinter as tk
#from Tkinter import Tk, Toplevel, Button, Frame, Scrollbar, Label
import random
action = 'GAME STARTED' 

btnmass = []
btnmass2 = []
Btnall1 = [x+1 for x in range(25)]
Btnall2 = [x+1 for x in range(25)]
random.shuffle(Btnall1)
random.shuffle(Btnall2)


def show_message():
   if len(btnmass) == 0:
      print 'ooy'

"""
       btnmass = Btnall1
       for k in range(25):
          Btnmass[k] = tk.Button(gameFrame, text = Btnall1[k], width = 26, height = 12,bg = 'grey', fg = 'black')
          k+1
"""
						     
def func(event): 
   global action 
   btn['state'] = 'disabled' 
   print action 
   if btn['state'] == 'disabled': 
      action = ' '
   else:
      action = 'press button Start Game'

root = tk.Tk() 
root.title("memo v1")  
root.state('zoomed')

panelFrame = tk.Frame(root, height = 20, bg = 'grey') 
panelFrame.pack(side = 'top', fill = 'x') 

gameFrame = tk.Frame(root, height = 230, bg = 'black') 
gameFrame.pack(side = 'bottom', fill = 'both') 


btn1 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black',command = show_message) 
btn1.grid(row = 1, column = 1,padx = 2,pady = 1) 
btnmass.append(btn1)

btn2 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black',command = show_message) 
btn2.grid(row = 1, column = 2,padx = 2,pady = 1)
btnmass.append(btn2)

btn3 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn3.grid(row = 1, column = 3,padx = 2,pady = 1) 
btnmass.append(btn3)

btn4 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn4.grid(row = 1, column = 4,padx = 2,pady = 1) 
btnmass.append(btn4)

btn5 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn5.grid(row = 1, column = 5,padx = 2,pady = 1) 
btnmass.append(btn5)

btn6 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn6.grid(row = 1, column = 6,padx = 2,pady = 1)  
btnmass.append(btn6)

btn7 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn7.grid(row = 1, column = 7,padx = 2,pady = 1) 
btnmass.append(btn7)

btn8 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn8.grid(row = 1, column = 8,padx = 2,pady = 1) 
btnmass.append(btn8)

btn9 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn9.grid(row = 1, column = 9,padx = 2,pady = 1) 
btnmass.append(btn9)

btn10 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn10.grid(row = 1, column = 10,padx = 2,pady = 1)
btnmass.append(btn10)

btn11 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn11.grid(row = 2, column = 1,padx = 2,pady = 1) 
btnmass.append(btn11)

btn12 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn12.grid(row = 2, column = 2,padx = 2,pady = 1) 
btnmass.append(btn12)

btn13 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn13.grid(row = 2, column = 3,padx = 2,pady = 1) 
btnmass.append(btn13)

btn14 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn14.grid(row = 2, column = 4,padx = 2,pady = 1)  
btnmass.append(btn14)

btn15 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn15.grid(row = 2, column = 5,padx = 2,pady = 1) 
btnmass.append(btn15)

btn16 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn16.grid(row = 2, column = 6,padx = 2,pady = 1) 
btnmass.append(btn16)

btn17 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn17.grid(row = 2, column = 7,padx = 2,pady = 1) 
btnmass.append(btn17)

btn18 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn18.grid(row = 2, column = 8,padx = 2,pady = 1) 
btnmass.append(btn18)

btn19 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn19.grid(row = 2, column = 9,padx = 2,pady = 1)
btnmass.append(btn19)

btn20 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn20.grid(row = 2, column = 10,padx = 2,pady = 1) 
btnmass.append(btn20)

btn21 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn21.grid(row = 3, column = 1,padx = 2,pady = 1)  
btnmass.append(btn21)

btn22 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn22.grid(row = 3, column = 2,padx = 2,pady = 1) 
btnmass.append(btn22)

btn23 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn23.grid(row = 3, column = 3,padx = 2,pady = 1) 
btnmass.append(btn23)

btn24 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn24.grid(row = 3, column = 4,padx = 2,pady = 1) 
btnmass.append(btn24)

btn25 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn25.grid(row = 3, column = 5,padx = 2,pady = 1) 
btnmass.append(btn25)

btn26 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn26.grid(row = 3, column = 6,padx = 2,pady = 1) 
btnmass2.append(btn26)

btn27 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn27.grid(row = 3, column = 7,padx = 2,pady = 1) 
btnmass2.append(btn27)

btn28 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn28.grid(row = 3, column = 8,padx = 2,pady = 1) 
btnmass2.append(btn28)

btn29 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn29.grid(row = 3, column = 9,padx = 2,pady = 1)  
btnmass2.append(btn29)

btn30 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn30.grid(row = 3, column = 10,padx = 2,pady = 1) 
btnmass2.append(btn30)

btn31 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn31.grid(row = 4, column = 1,padx = 2,pady = 1) 
btnmass2.append(btn31)

btn32 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn32.grid(row = 4, column = 2,padx = 2,pady = 1) 
btnmass2.append(btn32)

btn33 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn33.grid(row = 4, column = 3,padx = 2,pady = 1) 
btnmass2.append(btn33)

btn34 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn34.grid(row = 4, column = 4,padx = 2,pady = 1) 
btnmass2.append(btn34)

btn35 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn35.grid(row = 4, column = 5,padx = 2,pady = 1) 
btnmass2.append(btn35)

btn36 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn36.grid(row = 4, column = 6,padx = 2,pady = 1) 
btnmass2.append(btn36)

btn37 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn37.grid(row = 4, column = 7,padx = 2,pady = 1) 
btnmass2.append(btn37)

btn38 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn38.grid(row = 4, column = 8,padx = 2,pady = 1) 
btnmass2.append(btn38)

btn39 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn39.grid(row = 4, column = 9,padx = 2,pady = 1) 
btnmass2.append(btn39)

btn40 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn40.grid(row = 4, column = 10,padx = 2,pady = 1) 
btnmass2.append(btn40)

btn41 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn41.grid(row = 5, column = 1,padx = 2,pady = 1) 
btnmass2.append(btn41)

btn42 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn42.grid(row = 5, column = 2,padx = 2,pady = 1) 
btnmass2.append(btn42)

btn43 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn43.grid(row = 5, column = 3,padx = 2,pady = 1) 
btnmass2.append(btn43)

btn44 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn44.grid(row = 5, column = 4,padx = 2,pady = 1) 
btnmass2.append(btn44)

btn45 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn45.grid(row = 5, column = 5,padx = 2,pady = 1) 
btnmass2.append(btn45)

btn46 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn46.grid(row = 5, column = 6,padx = 2,pady = 1) 
btnmass2.append(btn46)

btn47 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn47.grid(row = 5, column = 7,padx = 2,pady = 1) 
btnmass2.append(btn47)

btn48 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn48.grid(row = 5, column = 8,padx = 2,pady = 1) 
btnmass2.append(btn48)

btn49 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn49.grid(row = 5, column = 9,padx = 2,pady = 1) 
btnmass2.append(btn49)

btn50 = tk.Button(gameFrame, text = '', width = 26, height = 12,bg = 'grey', fg = 'black') 
btn50.grid(row = 5, column = 10,padx = 2,pady = 1) 
btnmass2.append(btn50)

btn = tk.Button(panelFrame, text= "Start New Game", width=12,height=2, bg="white") 
btn.bind("<Button-1>", func) 
btn.pack(side = 'top')

root.mainloop()
