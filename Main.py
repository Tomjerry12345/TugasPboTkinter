from tkinter import *
from PIL import Image , ImageTk

class Window(Frame) :


    def __init__(self ,master=None):

        Frame.__init__(self , None)
        self.master = master
        self.init_window()


    def init_window(self):

        self.master.title("Tomjerry")
        self.pack(fill=BOTH, expand='yes')
        self.configure(bg ="orange")

        self.showImg()
        self.showText()

    def showImg(self):

        width = 200
        height = 200
        imageX = 150
        imageY = 20
        load = Image.open("tom.JPG")
        load = load.resize((width,height), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=imageX, y=imageY)

    def showText(self):
        textX = 180
        textY = 210
        text = Label(self, text="Andri Alfiandi" , bg ="orange" , font=("Helvetica", 18))
        text.place(x = textX, y = textY)

root = Tk()

root.geometry("500x500")
root.configure(bg = "black")

app = Window(root)

root.mainloop()