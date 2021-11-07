from tkinter import *
def value(n):
    if n == "1":
        print("10")
    else:
        print("0")
window = Tk()
button1 = Button(window, text = "Button1", command=lambda: value("1")).pack()
button2 = Button(window, text = "Button2", command=lambda: value("2")).pack()
button3 = Button(window, text = "Button3", command=lambda: value("3")).pack()
window.mainloop()