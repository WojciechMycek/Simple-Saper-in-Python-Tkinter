from tkinter import *
from PIL import ImageTk,Image
from random import randrange
from tkinter import messagebox

class Board(Frame):
    def __init__(self, master, bombs,flags,empty,number_of_buttons, i ,var,points,score):
        super().__init__(master)
        self.master = master
        self.bombs=bombs
        self.flags=flags
        self.empty=empty
        self.var=var
        self.number_of_buttons=number_of_buttons
        self.number_of_bombs = 4
        self.i = i
        self.var = var
        self.points = points
        self.score = score
        self.texty = StringVar()
        self.list_buttons = []
        self.list_bomb = []


        #root setting window
        self.master.geometry("400x400")
        self.master.title("Saper in Python by Mycek")
        self.master.iconbitmap('D:\Pulpit\Python/bomb.ico')
    
    def open_game(self):
        top = Toplevel()
        lbl = Label(top)
        self.__init__(self.master,6,3,3,6,1,0,0,0)
        self.generate_buttons(top)

    def options(self):
        top = Toplevel()
        lbl = Label(top,text="Our options").pack()
        

    def generate_buttons(self,top):
        #generate bombs
        self.list_bomb = []
        for x in range(self.number_of_bombs):
            self.list_bomb.append(randrange(20))
            print(self.list_bomb[x])
        
        #Photos on buttons
        self.photo = PhotoImage(file = r"D:\Pulpit\Python\images/circle1.png")
        self.photo_smile = PhotoImage(file = r"D:\Pulpit\Python\images/smile.png")
        self.photo_bomba = PhotoImage(file = r"D:\Pulpit\Python\images/bomba.png")

        #button quit
        button_quit = Button(top,text="Exit", command=top.destroy)
        button_quit.grid(row=14, column=4,pady=10)

        #Label_score
        Label_score = Label(top,text="Your score: " + str(self.score))
        Label_score.grid(row=14, column=0,columnspan=2)


        while self.i < self.number_of_buttons:
            for j in range(self.number_of_buttons):
                buttons = Button(top, text="*",image=self.photo,padx=10,pady=10,command=lambda var=self.var, lan=j:self.change_text_buttons(lan,var,top))
                buttons.grid(row=self.i,column=j,padx=10,pady=10)
                self.list_buttons.append(buttons)
                self.var+=1
                if(j==self.number_of_buttons-1):
                    self.i+=1

    def change_text_buttons(self,tekst,var,top):
        self.texty.set(tekst)

        for i in range(len(self.list_buttons)):
         if i==var:
            self.list_buttons[i].config(image=self.photo_smile)
            self.score+=1
            Label_score = Label(top,text="Your score: " + str(self.score))
            Label_score.grid(row=14, column=0,columnspan=2)
            for j in range(len(self.list_bomb)):
                if i==self.list_bomb[j]:
                    self.list_buttons[i].config(image=self.photo_bomba)
                    Label_score = Label(top,text="Lost, Sry little one")
                    messagebox.showinfo("Loser. Sry litlle one!", "Lost!")
                    Label_score.grid(row=14, column=0,columnspan=2)
                    button_reset = Button(top,text="Exit", command=top.destroy)
                    button_reset.grid(row=14, column=4,pady=10)

    def menu(self):
        #img
        global my_img1
        my_img1 = ImageTk.PhotoImage(Image.open("D:\Pulpit\Python\images/bomba.png"))

        #label
        label = Label(self.master,text="Saper by Mycek!",height=2,bd=20,font=50,fg='blue',bg='green')
        image_label = Label(image=my_img1)

        #btn
        btn_click = Button(self.master,text="Start!",width=6,command=self.open_game)
        btn_option = Button(self.master,text="Options",width=6,command=self.options)
        btn_exit = Button(self.master,text="Exit",width=6, command=self.master.destroy)

        #grid

        #label grid
        label.grid(row=0,column=0)
        image_label.grid(row=0,column=1)

        #label place
        label.place(x=200,y=25,anchor="center")
        image_label.place(x=200,y=110,anchor="center")

        #btn grid
        btn_click.grid(row=1,column=0)
        btn_click.place(x=200,y=200,anchor="center")

        btn_option.grid(row=2,column=0)
        btn_option.place(x=200,y=230,anchor="center")


        btn_exit.grid(row=3,column=0)
        btn_exit.place(x=200,y=260,anchor="center")


root = Tk()
app = Board(root,6,3,3,6,1,0,0,0)
app.menu()
app.mainloop()
