import tkinter as tk
from tkinter import filedialog


def pick_folder():

    root = tk.Tk()

    root.withdraw()

    root.attributes(
        "-topmost",
        True
    )

    folder = filedialog.askdirectory()

    root.destroy()

    return folder