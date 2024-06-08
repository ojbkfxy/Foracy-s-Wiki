from tkinter import *
import main
import sys
window = Tk()
window.title("Wiki")
WIDTH,HEIGH = 512,768
window.minsize(532,768)
window.maxsize(532,768)
def Exit():
    sys.exit()
def Search():
    main.Command(comm="get").Run(topic=enter.get())
    link,text = main.Command(comm="show").Run(topic=enter.get())
    dialog.delete(0.0,END)
    dialog.insert('1.0',text)
def Clear():
    dialog.delete(0.0,END)
def Save():
    pass
Label(window,text="Is A WikiPedia?  ---Create By Foracy").place(x=WIDTH*0.40,y=10)
enter = Entry(window)
enter.place(x=WIDTH*0.4,y=40)
dialog = Text(window)
dialog.place(x=10,y=120,width=WIDTH-20,height=HEIGH-200)
scroll = Scrollbar()
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=dialog.yview)
dialog.config(yscrollcommand=scroll.set)
button_search = Button(window,bg="red",text="Search",command=Search).place(x=WIDTH*0.5,y=70)
button_exit = Button(window,bg="yellow",text="Exit",command=Exit).place(x=10,y=HEIGH-50)
button_clear = Button(window,bg="#00ff00",text="Clear",command=Clear).place(x=WIDTH*0.3,y=HEIGH-50)
button_Settings = Button(window,bg="#f0ffff",text="Settings").place(x=WIDTH*0.60,y=HEIGH-50)
button_save = Button(window,bg="green",text="Save").place(x=WIDTH-50,y=HEIGH-50)
window.mainloop()