import tkinter
from tkinter import *
from tkinter import messagebox
val = ""
a = 0
operator = ""
def btn_1_onclick():
    global val
    val = val + "1"
    data.set(val)
def btn_2_onclick():
    global val
    val = val + "2"
    data.set(val)
def btn_3_onclick():
    global val
    val = val + "3"
    data.set(val)
def btn_4_onclick():
    global val
    val = val + "4"
    data.set(val)
def btn_5_onclick():
    global val
    val = val + "5"
    data.set(val)
def btn_6_onclick():
    global val
    val = val + "6"
    data.set(val)
def btn_7_onclick():
    global val
    val = val + "7"
    data.set(val)
def btn_8_onclick():
    global val
    val = val + "8"
    data.set(val)
def btn_9_onclick():
    global val
    val = val + "9"
    data.set(val)


def btn_0_onclick():
    global val
    val = val + "0"
    data.set(val)
def btn_plus_clicked():
    global a
    global operator
    global val
    a=int(val)
    operator="+"
    val=val+"+"
    data.set(val)
def btn_minus_clicked():
    global a
    global operator
    global val
    a=int(val)
    operator="-"
    val=val+"-"
    data.set(val)
def btn_mul_clicked():
    global a
    global operator
    global val
    a=int(val)
    operator="*"
    val=val+"*"
    data.set(val)
def btn_div_clicked():
    global a
    global operator
    global val
    a=int(val)
    operator="/"
    val=val+"/"
    data.set(val)
def c_pressed():
    global a
    global operator
    global val
    val=""
    a=0
    operator=""
    data.set(val)
def result():
    global a
    global operator
    global val
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        c = a+x
        data.set(c)
        val=str(c)
    if operator=="-":
        x=int((val2.split("-")[1]))
        c = a-x
        data.set(c)
        val=str(c)
    if operator=="*":
        x=int((val2.split("*")[1]))
        c = a*x
        data.set(c)
        val=str(c)
    if operator=="/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.throwerror("error","division by zero")
            a=""
            val=""
            data.set(val)
        else:
            c=int(a/x)
            data.set(c)
            val=str(c)
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("calculator")
data = StringVar()
lbl=Label(
    root,
    anchor=SE,
    text="Label",
    font = ("verdana",20),
    textvariable=data,

)
lbl.pack(expand=True,fill="both",)
textvaribale=data
background="#534e52"
fg="#965d62"
btnrow1=Frame(root,bg="#965d62")
btnrow1.pack(expand=True,fill="both")
btnrow2=Frame(root,bg="#965d62")
btnrow2.pack(expand=True,fill="both")
btnrow3=Frame(root,bg="#965d62")
btnrow3.pack(expand=True,fill="both")
btnrow4=Frame(root,bg="#965d62")
btnrow4.pack(expand=True,fill="both")
btnrow5=Frame(root,bg="#965d62")
btnrow5.pack(expand=True,fill="both")
btnrow6=Frame(root,bg="#965d62")
btnrow6.pack(expand=True,fill="both")
btnrow7=Frame(root,bg="#965d62")
btnrow7.pack(expand=True,fill="both")
btnrow8=Frame(root,bg="#965d62")
btnrow8.pack(expand=True,fill="both")
btnrow9=Frame(root,bg="#965d62")
btnrow9.pack(expand=True,fill="both")
btnrow10=Frame(root,bg="#965d62")
btnrow10.pack(expand=True,fill="both")
btnrow11=Frame(root,bg="#965d62")
btnrow11.pack(expand=True,fill="both")
btnrow12=Frame(root,bg="#965d62")
btnrow12.pack(expand=True,fill="both")
btnrow13=Frame(root,bg="#965d62")
btnrow13.pack(expand=True,fill="both")
btnrow14=Frame(root,bg="#965d62")
btnrow14.pack(expand=True,fill="both")
btnrow15=Frame(root,bg="#965d62")
btnrow15.pack(expand=True,fill="both")
btnrow16=Frame(root,bg="#965d62")
btnrow16.pack(expand=True,fill="both")

btn1=Button(
    btnrow1,
    text="1",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_1_onclick
)
btn1.pack(side=LEFT,expand=True,fill="both"),
btn2 = Button(
    btnrow1,
    text="2",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command = btn_2_onclick,
)
btn2.pack(side=LEFT,expand=True,fill="both",)
btn3=Button(
    btnrow1,
    text="3",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_3_onclick,
)
btn3.pack(side=LEFT,expand=True,fill="both",)
btn4=Button(
    btnrow2,
    text="4",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_4_onclick,)
btn4.pack(side=LEFT,expand=True,fill="both"),
btn5=Button(
    btnrow2,
    text="5",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_5_onclick,
)
btn5.pack(side=LEFT,expand=True,fill="both"),
btn6=Button(
    btnrow2,
    text="6",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_6_onclick,)
btn6.pack(side=LEFT,expand=True,fill="both"),
btn7=Button(
    btnrow3,
    text="7",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_7_onclick
)
btn7.pack(side=LEFT,expand=True,fill="both"),
btn8=Button(
    btnrow3,
    text="8",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_8_onclick
)
btn8.pack(side=LEFT,expand=True,fill="both"),
btn9=Button(
    btnrow3,
    text="9",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command = btn_9_onclick
)
btn9.pack(side=LEFT,expand=True,fill="both"),

btnc=Button(
    btnrow4,
    text="c",
    font=("verdana", 22),
    relief=GROOVE,
    border=0,
    command = c_pressed
)
btnc.pack(side=LEFT,expand=True,fill="both",)

btn0=Button(
    btnrow4,
    text="0",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_0_onclick
)
btn0.pack(side=LEFT,expand=True,fill="both"),
btnminus=Button(
    btnrow2,
    text="-",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_minus_clicked
)
btnminus.pack(side=LEFT,expand=True,fill="both"),
btnmul=Button(
    btnrow3,
    text="*",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command = btn_mul_clicked
)
btnmul.pack(side=LEFT,expand=True,fill="both"),
btnequal=Button(
    btnrow4,
    text="=",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command =result
)
btnequal.pack(side=LEFT, expand=True, fill="both"),
btndiv=Button(
    btnrow4,
    text="/",
    font=("verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked
)
btndiv.pack(side=LEFT, expand=True, fill="both"),
btnplus=Button(
    btnrow1,
    text="+",
    font=("verdana",22),

    relief=GROOVE,
    border=0,
    command =btn_plus_clicked,
)
btnplus.pack(side=LEFT,expand=True,fill="both"),
root.mainloop()





























