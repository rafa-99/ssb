import tkinter as tk

def start_UI():
    root = root_view()

    root.mainloop()

def root_view():
    root = tk.Tk()

    root.title("Firewall Tool")
    root.minsize(512, 512)
    root.geometry("512x512")

    return root