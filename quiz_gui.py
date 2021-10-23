# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:59:45 2021

@author: Dennis Waswa
"""

import art, re
import quiz as q_module 
from datetime import datetime 
from tkinter import *

root = Tk()
root.title('QUIZ CHALLENGE')
root.geometry("600x400")

def start():
    print('start')
    
def questions():
    print('question 1')
    # questions_x = q_module.select_questions(q_module.get_available_data_files(), num)  
    # for que in questions_x:
        
    #     que += questions_x
    #     return questions_x
    
def answers():
    print('testing answers')
    
def points():
    print('testing points')
def next_button():
    print('onclick')
    
    
part_text = StringVar()
part_label = Label(root, text='Question', font=('bold', 14), pady=20)
part_label.grid(row=0, column= 0, sticky=W)
part_label = Label(root, text='Subject', font=('bold', 14))
part_label.grid(row=0, column= 3, sticky=W)


part_label = Label(root, text= '', font=('bold', 14), pady=20, command= questions())
part_label.grid(row=1, column= 1)

#buttons

b1 = Button(root, text = 'shuffle_x', width=12, command= lambda: answers())
b1.grid(row = 4, column = 0, pady =20)
b2 = Button(root, text = 'shuffle_x', width=12, command= lambda: answers())
b2.grid(row = 4, column = 1, padx=20)
b3 = Button(root, text = 'shuffle_x', width=12, command= lambda: answers())
b3.grid(row = 4, column = 2, padx=20)
b4 = Button(root, text = 'shuffle_x', width=12, command= lambda: answers())
b4.grid(row = 4, column = 3)
b4 = Button(root, text = 'Next', width=12, command= next_button())
b4.grid(row = 5, column = 3, pady = 20)


  
mainloop()