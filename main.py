from tkinter import *
from inCalc import calcular
import math

op = []
clearonwrite = False
ans = 0

def addOP(val):
    global op, clearonwrite
    global s1

    if clearonwrite:
        clearOP()
    
    if not op or not (isinstance(op[-1], (int, float)) and isinstance(val, (int, float))):
        op.append(val)
    else:
        op[-1] = (op[-1]*10)+val

    s1.config(text=(s1["text"] + str(val)))

def clearOP():
    global op, clearonwrite
    global s1, s2
    
    op = []
    s1.config(text=" ")
    s2.config(text=" ")
    clearonwrite = False

def fullcalc():
    global op, clearonwrite, ans
    global s1, s2

    if not op:
        clearOP()
        return

    r = 0
    while len(op) > 1:
        r = calcular(op)
        if r != 0:
            print("error ", r)
            break

    if r == 0:
        s2.config(text="= " + str(op[0]))
        ans = op[0]
    elif r == -1:
        clearOP()
        s1.config(text="Syntax Error")
    elif r == -2:
        clearOP()
        s1.config(text="Math Error")

    clearonwrite = True
                    
def delOP():
    global op
    global s1, s2
    if len(op) == 0 or len(s1["text"]) == 0:
        return
    if not isinstance(op[-1], (int, float)) or len(str(math.trunc(op[-1]))) == 1:
        op.pop()
    else:
        op[-1] = math.trunc(op[-1]/10)

    s2.config(text=" ")
    s1.config(text=s1["text"][:-1])
    clearonwrite = False

    


window = Tk()
window.title("Tkalculadora")
window.geometry("400x250")
window.configure(bg="#555b67")

screens = Frame(window, bd=2, relief="groove")
screens.pack(fill="x", padx=10, pady=10, expand=True)
screens.columnconfigure(0, weight=1)

Label(screens, fg="black", text="Casio Cannabis fx-777 pro").grid(row=0, column=0, sticky="w", padx=5)
s1 = Label(screens, font=("Arial", 16), bg="#a8ac93", fg="black", justify="left")
s1.grid(row=1, column=0, sticky="nsew", padx=5)
s2 = Label(screens, font=("Arial", 16), bg="#a8ac93", fg="black", justify="right", state="disabled")
s2.grid(row=2, column=0, sticky="nsew", padx=5)

root = Frame(window, bd=2, relief="groove")
root.pack(fill="x", padx=10, pady=10, expand=True)
root.columnconfigure([0, 1, 2, 3, 4], weight=1)

Button(root, text="0", command=lambda:addOP(0), bg="#8888a8", fg="white").grid(row=0, column=0, sticky="nsew")
Button(root, text="1", command=lambda:addOP(1), bg="#8888a8", fg="white").grid(row=0, column=1, sticky="nsew")
Button(root, text="2", command=lambda:addOP(2), bg="#8888a8", fg="white").grid(row=0, column=2, sticky="nsew")
Button(root, text="3", command=lambda:addOP(3), bg="#8888a8", fg="white").grid(row=0, column=3, sticky="nsew")
Button(root, text="4", command=lambda:addOP(4), bg="#8888a8", fg="white").grid(row=0, column=4, sticky="nsew")

Button(root, text="5", command=lambda:addOP(5), bg="#8888a8", fg="white").grid(row=1, column=0, sticky="nsew")
Button(root, text="6", command=lambda:addOP(6), bg="#8888a8", fg="white").grid(row=1, column=1, sticky="nsew")
Button(root, text="7", command=lambda:addOP(7), bg="#8888a8", fg="white").grid(row=1, column=2, sticky="nsew")
Button(root, text="8", command=lambda:addOP(8), bg="#8888a8", fg="white").grid(row=1, column=3, sticky="nsew")
Button(root, text="9", command=lambda:addOP(9), bg="#8888a8", fg="white").grid(row=1, column=4, sticky="nsew")

Button(root, text="+", command=lambda:addOP("+"), bg="#8888a8", fg="white").grid(row=2, column=0, sticky="nsew")
Button(root, text="-", command=lambda:addOP("-"), bg="#8888a8", fg="white").grid(row=2, column=1, sticky="nsew")
Button(root, text="*", command=lambda:addOP("*"), bg="#8888a8", fg="white").grid(row=2, column=2, sticky="nsew")
Button(root, text="/", command=lambda:addOP("/"), bg="#8888a8", fg="white").grid(row=2, column=3, sticky="nsew")
Button(root, text="=", command=fullcalc, bg="#bc6578", fg="white").grid(row=2, column=4, sticky="nsew")

Button(root, text="ANS", command=lambda:addOP(ans), bg="#bc6578", fg="white").grid(row=3, column=2, sticky="nsew")
Button(root, text="DEL", command=delOP, bg="#bc6578", fg="white").grid(row=3, column=3, sticky="nsew")
Button(root, text="AC", command=clearOP, bg="#bc6578", fg="white").grid(row=3, column=4, sticky="nsew")


root.mainloop()
