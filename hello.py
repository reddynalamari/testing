from tkinter import *
from PIL import Image
import customtkinter as tk
root = tk.CTk()
tk.set_appearance_mode("light")
root.config(height=750,width=1500,background="#FADFF5")
root.resizable(False,False)
class ping_pong:
    count = 0
    texts = ["Baaga Alochinchukoni Select chey!","Oppuko kada","Malli Okkasari Alochinchu"]
    def __init__(self) -> None:
        self.l1 = tk.CTkLabel(master=root,font=("arial",35,"bold"),bg_color="#FAD7F4")
        self.l1.place(x=450,y=200)
        self.label("Do You Love Me?")
        self.please("Resources\\tenor.gif",400,300)
    def label(self,data):
        self.l1.configure(text=data)
    def please(self,gif_location,a,b):
        og = Image.open(gif_location)
        f = og.n_frames
        image_object = [PhotoImage(file=gif_location, format = f"gif -index {i}") for i in range(f)]
        count = 0
        show_animation = None
        def animation(count):
            global show_animation
            new_image_object = image_object[count]
            self.gif_label.configure(image=new_image_object)
            count = count+1
            if count == f:
                count = 0
            show_animation = root.after(50, lambda:animation(count))
        self.gif_label = tk.CTkLabel(master=root,text="",image="")
        self.gif_label.place(x=a,y=b)
        animation(count)
    def yes(self):
        try:
            self.gif_label.destroy()
            print("xfg")
        except:
            pass
        # self.please("Resources\\Line Stickers & Themes.gif",400,300)
        gif_location = "Resources\\Line Stickers & Themes.gif"
        og = Image.open(gif_location)
        f = og.n_frames
        image_object = [PhotoImage(file=gif_location, format = f"gif -index {i}") for i in range(f)]
        count = 0
        show_animation = None
        def animation(count):
            global show_animation
            new_image_object = image_object[count]
            self.gif_label.configure(image=new_image_object)
            count = count+1
            if count == f:
                count = 0
            show_animation = root.after(50, lambda:animation(count))
        self.gif_label = tk.CTkLabel(master=root,text="",image="")
        self.gif_label.place(x=400,y=300)
        animation(count)

shashi = ping_pong()

b1 = tk.CTkButton(master=root,text="Yes",bg_color="#FAD7F4",fg_color="white",font=("arial",20,"bold"),\
                  text_color="red",width=2,command=shashi.yes)
b1.place(x=500,y=250)
b2 = tk.CTkButton(master=root,text=" No ",bg_color="#FAD7F4",fg_color="white",font=("arial",20,"bold"),\
                  text_color="red",width=2)
b2.place(x=650,y=250)
root.mainloop()
