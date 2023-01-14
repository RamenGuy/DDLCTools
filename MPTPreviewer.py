import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import os

# PLANS:
# Make a function that loads eyes/nose/eyebrows/mouth whenever poses are selected and updated, and load poses when characters are selected and updated.
# Also, clothes. Maybe, uh, just rework this whole file.
# Draw order: Bodybase, headbase, mouth, nose, eyes, eyebrows.

def main():
    global myimg
    master = tk.Tk()
    master.title("MPT Previewer")
    style1 = ttk.Style(master)
    style1.configure('TFrame')
    style1.configure('mainFrame.TFrame', background="#191a36")
    ico = Image.open('icon.png')
    photo = ImageTk.PhotoImage(ico)
    if __name__ == '__main__':
        master.wm_iconphoto(False, photo)

    image = Image.open('zilch.png')
    myimg = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(master,image=myimg)
    imageLabel.grid(column=1, row=0)

    files = []
    for filename in os.listdir(os.getcwd() + "/sayori"):
        with open(os.path.join(os.getcwd() + "/sayori", filename), 'r') as f:  # open in readonly mode
            files.append(filename)
    fileNames = tk.StringVar(value=files)
    fileBox = tk.Listbox(master, listvariable=fileNames, height=60, width=50)
    fileBox.grid(column=0, row=0, padx=10, pady=10)

    with open("characters.txt", "r") as file:
        characters = eval(file.read())
        characterFullNames = list(characters.keys())

    characterString = tk.StringVar(master, value=characterFullNames)
    characterListBox = tk.Listbox(master, listvariable=characterString, height=len(characterFullNames))
    characterListBox.grid(column=2, row=0)

    poses = []
    posesString = tk.StringVar(master, value=poses)
    posesListBox = tk.Listbox(master, listvariable=posesString, height=len(poses))
    posesListBox.grid(column=2, row=1)


    eyes = []
    if len(characterListBox.curselection()):
        for filename in os.listdir(os.getcwd() + f"/{characterFullNames[characterListBox.curselection()[0]]}/"):
            with open(os.path.join(os.getcwd() + f"/{characterFullNames[characterListBox.curselection()[0]]}/",
                          filename), 'r') as f:  # open in readonly mode
                if filename.startswith(f"{characterFullNames[characterListBox.curselection()[0]]}_{poseBox.selection_get()}_eyes"):
                    eyes.append(filename)
    eyesString = tk.StringVar(master, value=eyes)
    eyesListBox = tk.Listbox(master, listvariable=eyesString, height=len(eyes))
    eyesListBox.grid(column=2, row=2)

    def addImage():
        global myimg
        fg = Image.open(os.getcwd() + "/sayori/" + fileBox.selection_get())
        imager = ImageTk.getimage(myimg)
        imager.paste(im=fg, box=(0, 0), mask=fg)
        myimg = ImageTk.PhotoImage(imager)
        imageLabel.config(image=myimg)
    addImageButton = tk.Button(master, text="Add", command=addImage)
    addImageButton.grid(column=0, row=1)
    
    def compileImage():
        global myimg
        try:
            fg = Image.open(os.getcwd() + f"/{characterFullNames[characterListBox.curselection()[0]]}/" + fileBox.selection_get())
        except IndexError:
            ...
        imager = ImageTk.getimage(myimg)
        imager.paste(im=fg, box=(0, 0), mask=fg)
        myimg = ImageTk.PhotoImage(imager)
        imageLabel.config(image=myimg)
    compileButton = tk.Button(master, text="Compile", command=compileImage)
    compileButton.grid(column=1, row=1)

    charSelect = tk.Button(master, text="Select Character", command=selchar)
    charSelect.grid(column=2, row=1)

    master.mainloop()


if __name__ == '__main__':
    main()
