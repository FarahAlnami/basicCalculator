from tkinter import *


# The function to display numbers on the screen
def click(num):
    global operation
    operation = operation + str(num)
    theInput.set(operation)


# The function to Clear the calculation
def clear():
    global operation
    operation = ""
    theInput.set("")


# The function to preform the calculation

def equal():
    global operation
    theSum = str(eval(operation))
    theInput.set(theSum)
    operation = ""


# Making the root (Window), naming it, and set the background.
root = Tk()
root.title("Calculator")
root.configure(bg='#203C4A')
root.resizable(False, False)
# initializing the operation which we will use in our calculations and the variable which will contain our user's input.
operation = ''
theInput = StringVar()

# Setting the calculation screen.
screen = Entry(root, font=('courier', 25), fg='white', textvariable=theInput, justify='right',
               bg='#203C4A').grid(columnspan=4, ipady=10)

# Setting the buttons in the first row (7,8,9, '+')
button_7 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="7", bg='#203C4A', relief='flat',
                  command=lambda: click(7)).grid(row=1, column=0)
button_8 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="8", bg='#203C4A', relief='flat',
                  command=lambda: click(8)).grid(row=1, column=1)
button_9 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="9", bg='#203C4A', relief='flat',
                  command=lambda: click(9)).grid(row=1, column=2)
button_add = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="+", bg='#203C4A', relief='flat',
                    command=lambda: click('+')).grid(row=1, column=3)
# Buttons in the second row (4,5,6, '-')
button_4 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="4", bg='#203C4A', relief='flat',
                  command=lambda: click(4)).grid(row=2, column=0)
button_5 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="5", bg='#203C4A', relief='flat',
                  command=lambda: click(5)).grid(row=2, column=1)
button_6 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="6", bg='#203C4A', relief='flat',
                  command=lambda: click(6)).grid(row=2, column=2)
button_subtract = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="-", bg='#203C4A', relief='flat',
                         command=lambda: click('-')).grid(row=2, column=3)
# Buttons in the third row (1,2,3, '×')
button_1 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="1", bg='#203C4A', relief='flat',
                  command=lambda: click(1)).grid(row=3, column=0)
button_2 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="2", bg='#203C4A', relief='flat',
                  command=lambda: click(2)).grid(row=3, column=1)
button_3 = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="3", bg='#203C4A', relief='flat',
                  command=lambda: click(3)).grid(row=3, column=2)
button_times = Button(root, padx=16, bd=8, fg='white', font=('courier', 20), text="×", bg='#203C4A', relief='flat',
                      command=lambda: click('*')).grid(row=3, column=3)
# Buttons in the fourth row (0,Clear,'=', '÷')
button_0 = Button(root, padx=16, pady=16, bd=8, fg='white', font=('courier', 20), text="0", bg='#203C4A', relief='flat',
                  command=lambda: click(0)).grid(row=4, column=0)
button_clear = Button(root, padx=16, pady=16, bd=8, fg='white', font=('courier', 20), text="C", bg='#203C4A',
                      relief='flat', command=clear).grid(row=4, column=1)
button_equal = Button(root, padx=16, pady=16, bd=8, fg='white', font=('courier', 20), text="=", bg='#203C4A',
                      relief='flat', command=equal).grid(row=4, column=2)
button_divide = Button(root, padx=16, pady=16, bd=8, fg='white', font=('courier', 20), text="÷", bg='#203C4A',
                       relief='flat', command=lambda: click('/'), ).grid(row=4, column=3)
root.mainloop()
