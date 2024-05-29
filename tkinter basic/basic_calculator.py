import tkinter as tkr
from tkinter import *


'''
m is the rood
m = tkr.Tk(className='Calc')

# w = Label(m, text='----Basic Calculator----', width = 36,bg="lightgray")
# w.pack()

widgets are added here

 m.mainloop()  #use to run app
'''


expression = ""


#fnc to update exp in the txt box
def press(num):
    global expression
    cursor_pos = exp_field.index(INSERT)
    expression += str(num)
    equation.set(expression)
    exp_field.icursor(cursor_pos + len(str(num)))

# fnc to eval final exp
def equalpress():
    #use try and except stmt to handle zero error\
    try:

        global expression
        #eval fnc evals the sxp n str converts it
        total = (eval(expression))

        #determine no of decimal places
        if isinstance(total,float):
            total_str = f"{total:.10g}"  #formats total to hav upto 10 significant digits n chose most approp rep to display it
            if '.' in total_str:
                int_part, dec_part = total_str.split('.')
                if len(dec_part) >5:
                    total_str = f"{total:.5e}"  #convert to exp if more than 5 decimal places
        else:
            total_str = str(total)

        equation.set(total_str)
        #intialize exp with empty
        expression = ""

    except (ZeroDivisionError,SyntaxError,NameError):
        equation.set("--Error--")
        expression = ""



#fnc to clr content
def clear():
    global expression
    expression = ""
    equation.set("0")
    exp_field.icursor(0)

def key_press(event):
    key = event.char
    if key.isdigit() :
        press(key)
    elif key in "+-*/%":
        press(key)
    elif key == "\r":
        equalpress()
    elif key == "\x08":  # Backspace
        clear()

#driver code
if __name__ == "__main__":
    #create gui window
    gui = tkr.Tk(className="Calc")
    gui.title("----Basic Calculator----")
    gui.geometry("224x430")
    gui.minsize(width=224, height=430)
    gui.configure(bg="#f4e2e4")



    #stringvar is the var class -> create an instance of this class
    equation = StringVar()
    equation.set("0")

    #text entry box for exp
    exp_field = Entry(gui, textvariable=equation,font=('Arial', 18),insertwidth=2,width=14,borderwidth=4,bd=5, bg="#f0ccd3")

    #grid method to place widget
    exp_field.grid(columnspan=3, padx=10,pady=10,sticky="nsew")


    #config col n row weights to make them resize with window
    for i in range(3):
        gui.grid_columnconfigure(i, weight=1)
    for i in range(6):
        gui.grid_rowconfigure(i, weight=1)

    #creat buttons -> user press -> fn or command is executed

    buttons =[
        '*','/','Clear',
        '%','-','+',
        '7','8','9',
        '4', '5', '6',
        '1', '2', '3',
        '.', '0', '='
    ]

    #create n place dynamically
    row_val =1
    col_val =0

    for button_text in buttons:
        if button_text == '=':
            btn = Button(gui,text=button_text,font=('Arial', 12),fg='black',bg='light pink', command=equalpress,height=2,width=6)
        elif button_text=='Clear':
            btn = Button(gui, text=button_text,font=('Arial', 12), fg='black', bg='#d38894', command=clear, height=2, width=6)
        elif button_text in ('+','-','*','/','%'):
            btn = Button(gui, text=button_text, font=('Arial', 12), fg='black', bg='#f0aaa2',
                         command=lambda b=button_text: press(b) if b not in ('+','-','*','/','%')else press(f" {b} "), height=2,width=6)
        else:
            btn = Button(gui, text=button_text, font=('Arial', 12), fg='black', bg='#e5bacd',
                         command=lambda b=button_text: press(b), height=2, width=6)

        btn.grid(row=row_val,column=col_val, padx=5,pady=5,sticky="nsew")

        col_val +=1
        if col_val >2:
            col_val =0
            row_val +=1



    gui.bind('<Key>', key_press)
    exp_field.focus_set()
    #set focus to entry widget
    gui.mainloop()
