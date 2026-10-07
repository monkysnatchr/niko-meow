import tkinter as tk
from tkinter import *
import subprocess
import platform
from pathlib import Path

BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

window = tk.Tk()
window.title("Niko")
window.geometry("200x200")
window.resizable(False, False)
icon_image = tk.PhotoImage(file='pancakes.png')
window.iconphoto(True, icon_image)


normal_image = tk.PhotoImage(
    file=str(ASSETS / "niko_normal.png")
)

meow_image = tk.PhotoImage(
    file=str(ASSETS / "niko_meow.png")
)

niko = tk.Label(
    window,
    image=normal_image,
    borderwidth=0
)

niko.pack(pady=30)


def play_sound():
    sound = str(ASSETS / "meow.wav")
    system = platform.system()

    if system == "Linux":
        subprocess.Popen(
            ["paplay", sound],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    elif system == "Windows":
        import winsound
        winsound.PlaySound(
            sound,
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    elif system == "Darwin":
        subprocess.Popen(
            ["afplay", sound],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


def meow():
    niko.config(image=meow_image)
    play_sound()
    window.after(700, normal)


def normal():
    niko.config(image=normal_image)


button = tk.Button(
    window,
    text="мяу",
    font=("Arial", 18),
    command=meow
)

button.pack()

window.mainloop()
