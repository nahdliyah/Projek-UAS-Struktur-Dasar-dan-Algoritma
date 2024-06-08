from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import tkinter as tk


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("New Arrivals")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 832, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0, 0.0, 264.0, 832.0, fill="#F1EBC9", outline="")

        entry_image_1 = PhotoImage(file=("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(731.5,40.5, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.entry_1.place(
        x=523.0,
        y=17.0,
        width=417.0,
        height=45.0)

        button_image_1 = PhotoImage(file=("button_1.png"))
        self.button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(x=952.0, y=17.0, width=47.0, height=47.0)

        self.canvas.create_text(87.0, 102.0, anchor="nw", text="XIAOMI", fill="#000000", font=("Lato Black", 24 * -1, "bold"))

        button_image_2 = PhotoImage(file=("button_2.png"))
        self.button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
        self.button_2.place(x=0.0, y=148.0, width=264.0, height=44.0)

        button_image_3 = PhotoImage(file=("button_3.png"))
        self.button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"),relief="flat")
        self.button_3.place(x=0.0, y=202.0, width=264.0, height=44.0)

        button_image_4 = PhotoImage(
            file=("button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=256.0,
            width=264.0,
            height=44.0
        )

        button_image_5 = PhotoImage(
            file=("button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=310.0,
            width=264.0,
            height=44.0
        )

        self.canvas.create_text(
            582.0,
            97.0,
            anchor="nw",
            text="NEW ARRIVALS",
            fill="#000000",
            font=("Lato Bold", 48 * -1,"bold")
        )

        image_image_1 = PhotoImage(
            file=("image_1.png"))
        self.image_1 = self.canvas.create_image(
            757.0,
            306.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("image_2.png"))
        self.image_2 = self.canvas.create_image(
            757.0,
            608.0,
            image=image_image_2
        )
        self.window.resizable(True, True)
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
