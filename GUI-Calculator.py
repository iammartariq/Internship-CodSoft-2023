
from tkinter import *
root = Tk()

#GUI 
root.title("CALCULATOR BY AMMAR TARIQ")

def click(event):
    global screenvalue
    text = event.widget.cget("text")
    print(text)
    if text =="=":
        if screenvalue.get().isdigit():
            value = int(screenvalue.get())
        else:
            value = eval(screen.get())
            screenvalue.set(value)
            screen.update()
    elif text =="C":
        screenvalue.set("")
        screen.update()
        pass

    else:
        screenvalue.set(screenvalue.get() + text)
        screen.update()

#width x height
root.geometry("600x500")
root.minsize(300,300)
root.maxsize(800,800)

#screen
screenvalue = StringVar()
screenvalue.set(" ")
screen = Entry(root, textvariable=screenvalue, font="Arial 30", bg="light grey")
screen.pack(padx=30, pady=11, ipadx=30)

#frames

frame1 = Frame(root)

button7 = Button(frame1, text="7", font="arial 25", bg="black", fg="white")
button7.pack(side=LEFT, padx=5, pady=5)
button7.bind("<Button-1>", click)

button8 = Button(frame1, text="8", font="arial 25", bg="black", fg="white")
button8.pack(side=LEFT, padx=5, pady=5)
button8.bind("<Button-1>", click)

button9 = Button(frame1, text="9", font="arial 25", bg="black", fg="white")
button9.pack(side=LEFT, padx=5, pady=5)
button9.bind("<Button-1>", click)

button0 = Button(frame1, text="0", font="arial 25", bg="black", fg="white")
button0.pack(side=LEFT, padx=5, pady=5)
button0.bind("<Button-1>", click)

buttonC = Button(frame1, text="C", font="arial 25", bg="black", fg="white")
buttonC.pack(side=LEFT, padx=5, pady=5)
buttonC.bind("<Button-1>", click)

frame1.pack()

frame2 = Frame(root)

button4 = Button(frame2, text="4", font="arial 25", bg="black", fg="white")
button4.pack(side=LEFT, padx=5, pady=5)
button4.bind("<Button-1>", click)

button5 = Button(frame2, text="5", font="arial 25", bg="black", fg="white")
button5.pack(side=LEFT, padx=5, pady=5)
button5.bind("<Button-1>", click)

button6 = Button(frame2, text="6", font="arial 25", bg="black", fg="white")
button6.pack(side=LEFT, padx=5, pady=5)
button6.bind("<Button-1>", click)

buttonx= Button(frame2, text="*", font="arial 25", bg="black", fg="white")
buttonx.pack(side=LEFT, padx=5, pady=5, ipadx=3)
buttonx.bind("<Button-1>", click)

button= Button(frame2, text="/", font="arial 25", bg="black", fg="white")
button.pack(side=LEFT, padx=5, pady=5, ipadx=8)
button.bind("<Button-1>", click)

frame2.pack()

frame3 = Frame(root)

button3 = Button(frame3, text="3", font="arial 25", bg="black", fg="white")
button3.pack(side=LEFT, padx=5, pady=5)
button3.bind("<Button-1>", click)

button2 = Button(frame3, text="2", font="arial 25", bg="black", fg="white")
button2.pack(side=LEFT, padx=5, pady=5)
button2.bind("<Button-1>", click)

button1 = Button(frame3, text="1", font="arial 25", bg="black", fg="white")
button1.pack(side=LEFT, padx=5, pady=5)
button1.bind("<Button-1>", click)

button = Button(frame3, text="+", font="arial 25", bg="black", fg="white")
button.pack(side=LEFT, padx=5, pady=5, ipadx=0.75)
button.bind("<Button-1>", click)

button = Button(frame3, text="-", font="arial 25", bg="black", fg="white")
button.pack(side=LEFT, padx=5, pady=5, ipadx=7)
button.bind("<Button-1>", click)

frame3.pack()

frame4 = Frame(root)

button = Button(frame4, text="=", font="arial 25", bg="black", fg="white")
button.pack(padx=5, pady=5)
button.bind("<Button-1>", click)

frame4.pack()

root.mainloop()
