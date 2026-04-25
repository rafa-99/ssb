import os

import tkinter as tk
import tkinter.filedialog

SIZE = 512

def startUI():
    root = rootView()
    root.mainloop()

def rootView():
    root = tk.Tk()

    root.title("Firewall Tool")
    root.minsize(SIZE, SIZE)
    root.geometry(f"{SIZE}x{SIZE}")

    placeFrames(root)

    return root

def placeFrames(view):
    executablePath = tk.StringVar(value="None")
    executableFrame(view, executablePath)

# Executable file logic
def getExecutablePath(pathVariable, displayLabel):
    path = tk.filedialog.askopenfilename()
    if path:
        pathVariable.set(path)
        displayLabel.set(os.path.basename(path))

def executableFrame(view, path):
    frame = tk.Frame(master=view)

    displayLabel = tk.StringVar(value="None")
    label = tk.Label(master=frame, textvariable=displayLabel)

    button = tk.Button(master=frame, text="Select Executable", command=lambda: getExecutablePath(path, displayLabel))

    label.pack(side="left", padx=5)
    button.pack(side="left", padx=5)
    
    frame.pack(pady=10)
