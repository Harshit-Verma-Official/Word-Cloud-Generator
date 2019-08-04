from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from cloud import ImageGenerator as ig
import re


class user_interface(Frame):
    """docstring for user_interface"""

    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.wordlist = []

        self.heading = Label(self.root, text="WordCloud ImageGen", bg="#333945", fg="white", font="Courier 20 bold")
        self.heading.place(x=0, y=10, width=600, height=50)

        self.img = ImageTk.PhotoImage(Image.open("assets\\img.png"))
        self.panel = Label(root, image=self.img)
        self.panel.place(x=45, y=65)

        self.word_enter = Label(self.root, text="Enter Words : ", fg="black", font="Times 13 bold")
        self.word_enter.place(x=45, y=245)

        self.word_enter1 = Label(self.root, text="Resolution : ", fg="black", font="Times 13 bold")
        self.word_enter1.place(x=45, y=300)

        self.entry = Entry(self.root)
        self.entry.place(x=180, y=248, height=25, width=150)

        self.imgwidth = Entry(self.root)
        self.imgwidth.place(x=180, y=300, height=25, width=60)

        self.cross = Label(self.root, text="X", fg="black")
        self.cross.place(x=249, y=300)

        self.imgheight = Entry(self.root)
        self.imgheight.place(x=270, y=300, height=25, width=60)

        self.next_btn = Button(self.root, text="Next", bg="#535C68", fg="white", command=lambda: self.next_click(),
                               font="Courier 13 bold")

        self.next_btn.place(x=400, y=245, width=180, height=40)

        self.gen_btn = Button(self.root, text="Generate Image!", bg="#535C68", fg="white",
                              command=lambda: self.gen_img(), font="Courier 13 bold")
        self.gen_btn.place(x=400, y=315, width=180, height=40)

        self.author = Label(root, text="Designed & Developed by - HARSHIT RAJPUT @ 2019", font="Times 10")
        self.author.place(x=160, y=380)

    def next_click(self):

        word = self.entry.get()
        self.entry.delete(0, 'end')

        if re.match(r'^[a-zA-Z]+$', word):
            self.wordlist.append(word)
        else:
            messagebox.showerror("Error Msg", "Invalid Format!")

    def gen_img(self):
        height = int(self.imgheight.get())
        width = int(self.imgwidth.get())
        if ig().generate(" ".join(self.wordlist), height, width):
            messagebox.showinfo("Success", "Image Generated Successfully!")
            self.clear_words()
        else:
            self.clear_words()
            messagebox.showerror("Error Msg", "Error in generating image!")

    def clear_words(self):

        self.wordlist.clear()
