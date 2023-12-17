import customtkinter as CTk
#import keyboard as keyb

app = CTk.CTk()
app.title("Calculator")
app.geometry("370x410")
app.resizable(width=False, height=False)

resh = "0"

Font = CTk.CTkFont(size=55)

Frame = CTk.CTkFrame(app, width=300, height=330, fg_color="#373737")
Frame.place(x=0, y=80)
FramePer = CTk.CTkFrame(app, width=200, height=330, fg_color="#000000")
FramePer.place(x=220, y=80)
TextCalc = CTk.CTkLabel(app, text_color="white", text=resh)
TextCalc.configure(font=Font)
TextCalc.place(x=25, y=10)

#Функции - инструменты

def c():
    global resh
    resh = "0"
    TextCalc.configure(text=resh, text_color="white")

def del_():
    global resh
    resh = resh + "/"
    TextCalc.configure(text=resh, text_color="white")

def um():
    global resh
    resh = resh + "*"
    TextCalc.configure(text=resh, text_color="white")

def min():
    global resh
    resh = resh + "-"
    TextCalc.configure(text=resh, text_color="white")

def pl():
    global resh
    resh = resh + "+"
    TextCalc.configure(text=resh, text_color="white")

def skob_left():
    global resh
    if resh == "0":
        resh = "("
        TextCalc.configure(text=resh, text_color="white")
    else:
        resh = resh + "("
        TextCalc.configure(text=resh, text_color="white")

def skob_right():
    global resh
    if resh == "0":
        resh = ")"
        TextCalc.configure(text=resh, text_color="white")
    else:
        resh = resh + ")"
        TextCalc.configure(text=resh, text_color="white")

def ubrat():
    global resh
    resh = resh[:-1]
    TextCalc.configure(text=resh, text_color="white")

def ravn():
    global resh
    if resh in "":
        resh = "0"
        TextCalc.configure(text=resh, text_color="white")
    else:
        try:
            resh = str((eval(resh)))
            TextCalc.configure(text=resh, text_color="white")
        except:
            TextCalc.configure(text="ERROR", text_color="red")
            resh = "0"

#Функции - цифры

def one():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "1"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "1"
            TextCalc.configure(text=resh, text_color="white")

def two():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "2"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "2"
            TextCalc.configure(text=resh, text_color="white")

def three():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "3"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "3"
            TextCalc.configure(text=resh, text_color="white")

def four():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "4"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "4"
            TextCalc.configure(text=resh, text_color="white")

def five():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "5"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "5"
            TextCalc.configure(text=resh, text_color="white")

def six():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "6"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "6"
            TextCalc.configure(text=resh, text_color="white")

def seven():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "7"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "7"
            TextCalc.configure(text=resh, text_color="white")

def eight():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "8"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "8"
            TextCalc.configure(text=resh, text_color="white")

def nine():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "9"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "9"
            TextCalc.configure(text=resh, text_color="white")

def zero():
    global resh
    size = 0
    for i in resh:
        size = size + 1
    if size >= 11:
        TextCalc.configure(text="MAX", text_color="red")
    else:
        if resh == "0":
            resh = "0"
            TextCalc.configure(text=resh, text_color="white")
        else:
            resh = resh + "0"
            TextCalc.configure(text=resh, text_color="white")

def toch():
    global resh
    resh = resh + "."
    TextCalc.configure(text=resh, text_color="white")

#Кнопки
Btn1 = CTk.CTkButton(app, text_color="white", text=1, width=60, command=lambda: one())
Btn1.configure(font=Font)
Btn1.place(x=10, y=90)

Btn2 = CTk.CTkButton(app, text_color="white", text=2, width=60, command=lambda: two())
Btn2.configure(font=Font)
Btn2.place(x=80, y=90)

Btn3 = CTk.CTkButton(app, text_color="white", text=3, width=60, command=lambda: three())
Btn3.configure(font=Font)
Btn3.place(x=150, y=90)

Btn4 = CTk.CTkButton(app, text_color="white", text=4, width=60, command=lambda: four())
Btn4.configure(font=Font)
Btn4.place(x=10, y=170)

Btn5 = CTk.CTkButton(app, text_color="white", text=5, width=60, command=lambda: five())
Btn5.configure(font=Font)
Btn5.place(x=80, y=170)

Btn6 = CTk.CTkButton(app, text_color="white", text=6, width=60, command=lambda: six())
Btn6.configure(font=Font)
Btn6.place(x=150, y=170)

Btn7 = CTk.CTkButton(app, text_color="white", text=7, width=60, command=lambda: seven())
Btn7.configure(font=Font)
Btn7.place(x=10, y=250)

Btn8 = CTk.CTkButton(app, text_color="white", text=8, width=60, command=lambda: eight())
Btn8.configure(font=Font)
Btn8.place(x=80, y=250)

Btn9 = CTk.CTkButton(app, text_color="white", text=9, width=60, command=lambda: nine())
Btn9.configure(font=Font)
Btn9.place(x=150, y=250)

Btn0 = CTk.CTkButton(app, text_color="white", text=0, width=60, command=lambda: zero())
Btn0.configure(font=Font)
Btn0.place(x=10, y=330)

BtnToch = CTk.CTkButton(app, text_color="white", text=".", width=60, command=lambda: toch())
BtnToch.configure(font=Font)
BtnToch.place(x=80, y=330)

BtnC = CTk.CTkButton(app, text_color="white", text="C", width=60, command=lambda: c())
BtnC.configure(font=Font)
BtnC.place(x=150, y=330)

BtnSkobLeft = CTk.CTkButton(app, text_color="white", text="(", width=60, command=lambda: skob_left())
BtnSkobLeft.configure(font=Font)
BtnSkobLeft.place(x=300, y=170)

BtnSkobRight = CTk.CTkButton(app, text_color="white", text=")", width=60, command=lambda: skob_right())
BtnSkobRight.configure(font=Font)
BtnSkobRight.place(x=300, y=250)

BtnUbrat = CTk.CTkButton(app, text_color="white", text="<-", width=60, command=lambda: ubrat())
BtnUbrat.configure(font=Font)
BtnUbrat.place(x=300, y=90)

BtnRavn = CTk.CTkButton(app, text_color="white", text="=", width=60, command=lambda: ravn())
BtnRavn.configure(font=Font)
BtnRavn.place(x=300, y=330)

#Кнопки - инструменты
BtnDel = CTk.CTkButton(app, text_color="white", text="/", width=60, command=lambda: del_())
BtnDel.configure(font=Font)
BtnDel.place(x=230, y=90)

BtnUm = CTk.CTkButton(app, text_color="white", text="*", width=60, command=lambda: um())
BtnUm.configure(font=Font)
BtnUm.place(x=230, y=170)

BtnMin = CTk.CTkButton(app, text_color="white", text="-", width=60, command=lambda: min())
BtnMin.configure(font=Font)
BtnMin.place(x=230, y=250)

BtnPl = CTk.CTkButton(app, text_color="white", text="+", width=60, command=lambda: pl())
BtnPl.configure(font=Font)
BtnPl.place(x=230, y=330)

#Кнопки с клавиатуры

#keyb.add_hotkey("c" or "C", lambda: c())
#keyb.add_hotkey("/", lambda: del_())
#keyb.add_hotkey("*", lambda: um())
#keyb.add_hotkey("-", lambda: min())
#keyb.add_hotkey("+", lambda: pl())

#keyb.add_hotkey("1", lambda: one())
#keyb.add_hotkey("2", lambda: two())
#keyb.add_hotkey("3", lambda: three())
#keyb.add_hotkey("4", lambda: four())
#keyb.add_hotkey("5", lambda: five())
#keyb.add_hotkey("6", lambda: six())
#keyb.add_hotkey("7", lambda: seven())
#keyb.add_hotkey("8", lambda: eight())
#keyb.add_hotkey("9", lambda: nine())
#keyb.add_hotkey("0", lambda: one())

app.mainloop()