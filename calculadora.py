from tkinter import *


# ------FUNCTIONS------
def fsuma(num1, num2):
    result = num1 + num2
    return result


def fresta(num1, num2):
    result = num1 - num2
    return result


def fmultiply(num1, num2):
    result = num1 * num2
    return result


def fdivide(num1, num2):
    result = num1 / num2
    return result


def calc(num1, operator, num2):
    if operator == "+":
        fresult = fsuma(num1, num2)
        return fresult
    elif operator == "-":
        fresult = fresta(num1, num2)
        return fresult
    elif operator == "*":
        fresult = fmultiply(num1, num2)
        return fresult
    elif operator == "/":
        fresult = fdivide(num1, num2)
        return fresult
    else:
        print("Fatal error")



def resetequal():
    global equalpress
    equalpress = 0


def pressed0():
    num = numinput.get() + "0"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed1():
    num = numinput.get() + "1"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed2():
    num = numinput.get() + "2"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed3():
    num = numinput.get() + "3"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed4():
    num = numinput.get() + "4"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed5():
    num = numinput.get() + "5"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed6():
    num = numinput.get() + "6"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed7():
    num = numinput.get() + "7"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed8():
    num = numinput.get() + "8"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def pressed9():
    num = numinput.get() + "9"
    numinput.delete(0, END)
    numinput.insert(0, num)
    resetequal()


def suma():
    global num1
    num1 = numinput.get()
    numinput.delete(0, END)
    global operator
    operator = "+"
    resetequal()


def resta():
    global num1
    num1 = numinput.get()
    numinput.delete(0, END)
    global operator
    operator = "-"
    resetequal()


def multiply():
    global num1
    num1 = numinput.get()
    numinput.delete(0, END)
    global operator
    operator = "*"
    resetequal()


def divide():
    global num1
    num1 = numinput.get()
    numinput.delete(0, END)
    global operator
    operator = "/"
    resetequal()


def equal():
    global equalpress
    global num
    global num1
    global operator
    equalpress += 1
    if equalpress >= 2:
        numinput.delete(0, END)
        num = ""
        num1 = ""
    else:
        num2 = numinput.get()
        fresultado = calc(float(num1), str(operator), float(num2))
        if (fresultado - int(fresultado)) == 0.0:
            numinput.delete(0, END)
            fresultado0 = int(fresultado)
            numinput.insert(0, fresultado0)
        numinput.delete(0, END)
        numinput.insert(0, fresultado)


# -------TK BASES---------
root = Tk()
root.geometry("251x400")
root.title("Calculadora")
root.iconbitmap("icon.ico")

# -------ENTRY-------
numinput = Entry(font=("Symbol", 20), width=16, borderwidth=13, justify=RIGHT, state="normal")

# ----VALUES----
numfont = 20
xpad = 23
ypad = 15

numfont2 = 15
xpad2 = 8
ypad2 = 1

# -------BUTTONS---------
button0 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="0", command=pressed0)
button1 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="1", command=pressed1)
button2 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="2", command=pressed2)
button3 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="3", command=pressed3)
button4 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="4", command=pressed4)
button5 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="5", command=pressed5)
button6 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="6", command=pressed6)
button7 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="7", command=pressed7)
button8 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="8", command=pressed8)
button9 = Button(font=("Arial", numfont), padx=xpad, pady=ypad, text="9", command=pressed9)

sumabutton = Button(font=("Symbol", numfont2), text="+", padx=xpad2, pady=ypad2, command=suma, bg="#b0b0b0")
restabutton = Button(font=("Symbol", numfont2), text="-", padx=xpad2, pady=ypad2, command=resta, bg="#b0b0b0")
multiplybutton = Button(font=("Symbol", numfont2), text="´", padx=xpad2, pady=ypad2, command=multiply, bg="#b0b0b0")
dividebutton = Button(font=("Symbol", numfont2), text="/", padx=10, pady=ypad2, command=divide, bg="#b0b0b0")

equalbutton = Button(font=("Symbol", numfont), padx=23, pady=15, text="=", command=equal, bg="#ffb366")

# --------BUTTONS POSITIONS---------
numinput.grid(row=0, column=0, columnspan=3, sticky=W + N)
button7.grid(row=1, column=0, sticky=W)
button8.grid(row=1, column=1, sticky=W)
button9.grid(row=1, column=2, sticky=W)
button4.grid(row=2, column=0, sticky=W)
button5.grid(row=2, column=1, sticky=W)
button6.grid(row=2, column=2, sticky=W)
button1.grid(row=3, column=0, sticky=W)
button2.grid(row=3, column=1, columnspan=2, sticky=W)
button3.grid(row=3, column=2, sticky=W)
button0.grid(row=4, column=0, rowspan=2, sticky=W)

sumabutton.place(x=83, y=315)
restabutton.place(x=126, y=315)
multiplybutton.place(x=83, y=358)
dividebutton.place(x=126, y=358)

equalbutton.grid(row=4, column=2, rowspan=2, sticky=W)

mainloop()
