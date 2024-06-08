from tkinter import Tk,Label,Entry,Text,Scrollbar,RIGHT,Y,Button,END
# import main
from SETTINGS import *
from sys import exit

class Fun:
    def Exit():
        exit()
        # return 
    def Search(link,text):
        # main.Command(comm="get").Run(topic=Init().enter.get())
        # link,text = main.Command(comm="show").Run(topic=Init().enter.get())
        # Init().dialog.delete(0.0,END)
        # Init().dialog.insert('1.0',text)
        return Init().enter.get()
    def Clear():
        Init().dialog.delete(0.0,END)
    def Save():
        pass
    def Settings():
        pass


class Init:
    def __init__(self):
        self.window = Tk()
        self.window.title("Wiki")
        self.window.minsize(532,768)
        self.window.maxsize(532,768)
        Label(self.window,text="Is A WikiPedia?  ---Create By Foracy").place(x=WIDTH*0.40,y=10)
    def LOOP(self):
        self.enter = Entry(self.window)
        self.enter.place(x=WIDTH*0.4,y=40)
        self.dialog = Text(self.window)
        self.dialog.place(x=10,y=120,width=WIDTH-20,height=HEIGH-200)
        scroll = Scrollbar()
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.dialog.yview)
        self.dialog.config(yscrollcommand=scroll.set)
        self.button_search = Button(self.window,bg="red",text="Search",command=Fun().Search)
        self.button_search.place(x=WIDTH*0.5,y=70)
        self.button_exit = Button(self.window,bg="yellow",text="Exit",command=Fun().Exit)
        self.button_exit.place(x=10,y=HEIGH-50)
        self.button_clear = Button(self.window,bg="#00ff00",text="Clear",command=Fun().Clear)
        self.button_clear.place(x=WIDTH*0.3,y=HEIGH-50)
        self.button_settings = Button(self.window,bg="#f0ffff",text="Settings",command=Fun().Settings)
        self.button_settings.place(x=WIDTH*0.60,y=HEIGH-50)
        self.button_save = Button(self.window,bg="green",text="Save",command=Fun().Save)
        self.button_save.place(x=WIDTH-50,y=HEIGH-50)
        self.window.mainloop()

