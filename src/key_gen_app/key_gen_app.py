import random
import string
from threading import *
from tkinter import *


def key_gen():
    options = (
        (string.ascii_letters + string.digits + string.punctuation)
        .replace("o", "")
        .replace("O", "")
        .replace("|", "")
    )
    try:
        key = "".join(random.sample(options, 50))
        text_box.insert("end", key, "center")
    except Exception as e:
        text_box.insert("end", e)


def btn_click():
    try:
        text_box.config(state="normal")
        text_box.delete(1.0, "end")
        thread = Thread(target=key_gen)
        thread.start()

    except Exception as e:
        text_box.insert("end", e)


root = Tk()
root.title("Django Secret Key Generator")
root.geometry("700x250")

text_box = Text(root, font=("arial", 18), height=1)
text_box.pack(side=TOP, padx=20, pady=20)
text_box.tag_configure("center", justify="center")

key_btn = Button(
    root,
    text="Generate Secret Key",
    font=("courier", 18),
    relief="ridge",
    command=lambda: btn_click(),
)
key_btn.pack(side=TOP, pady=20)

root.mainloop()
