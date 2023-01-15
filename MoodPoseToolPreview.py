import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import os
import mpt_s
import ImageConverters
# PLANS:
# Make a function that loads eyes/nose/eyebrows/mouth whenever poses are selected and updated, and load poses when characters are selected and updated.
# Also, clothes. Maybe, uh, just rework this whole file.
# Draw order: Bodybase, headbase, mouth, nose, eyes, eyebrows.
# Strings order for IC: r, l, head, mouth, nose, eyes, eyebrows

def main():
    global myimg
    global lAssets
    global rAssets
    global headAssets
    global mouthAssets
    global noseAssets
    global eyesAssets
    global eyebrowsAssets
    master = tk.Tk()
    master.title("MPT Previewer")
    style1 = ttk.Style(master)
    style1.configure('TFrame')
    style1.configure('mainFrame.TFrame', background="#191a36")
    ico = Image.open('icon.png')
    photo = ImageTk.PhotoImage(ico)
    #master.resizable(False, False)
    if __name__ == '__main__':
        master.wm_iconphoto(False, photo)

    imageFrame = tk.Frame(master, relief='sunken', borderwidth=5)
    imageFrame.grid(column=3, row=0, padx=10)
    image = Image.open('zilch.png')
    image = image.resize((480, 480))
    myimg = ImageTk.PhotoImage(image)
    imageLabel = tk.Label(imageFrame, image=myimg)
    imageLabel.grid(column=0, row=0)

    with open("characters.txt", "r") as file:
        characters = eval(file.read())
        characterFullNames = list(characters.keys())

    characterString = tk.StringVar(master, value="")
    characterListBox = ttk.Combobox(master, textvariable=characterString, height=len(characterFullNames), values=characterFullNames[0:4])
    characterListBox.grid(column=0, row=0)
    assetFrame = tk.Frame(master, relief='sunken', borderwidth=2)
    assetFrame.grid(column=0, row=1)
    lAssets = []
    rAssets = []
    headAssets = []
    mouthAssets = []
    noseAssets = []
    eyesAssets = []
    eyebrowsAssets = []
    lString = tk.StringVar(assetFrame, value="")
    lBox = ttk.Combobox(assetFrame, textvariable=lString, height=len(lAssets), values=lAssets)
    lBox.grid(column=0, row=0)
    rString = tk.StringVar(assetFrame, value="")
    rBox = ttk.Combobox(assetFrame, textvariable=rString, height=len(lAssets), values=rAssets)
    rBox.grid(column=0, row=1)
    headString = tk.StringVar(assetFrame, value="")
    headBox = ttk.Combobox(assetFrame, textvariable=headString, height=len(headAssets), values=headAssets)
    headBox.grid(column=0, row=2)
    mouthString = tk.StringVar(assetFrame, value="")
    mouthBox = ttk.Combobox(assetFrame, textvariable=mouthString, height=len(mouthAssets), values=mouthAssets)
    mouthBox.grid(column=0, row=3)
    noseString = tk.StringVar(assetFrame, value="")
    noseBox = ttk.Combobox(assetFrame, textvariable=noseString, height=len(noseAssets), values=noseAssets)
    noseBox.grid(column=0, row=4)
    eyesString = tk.StringVar(assetFrame, value="")
    eyesBox = ttk.Combobox(assetFrame, textvariable=eyesString, height=len(eyesAssets), values=eyesAssets)
    eyesBox.grid(column=0, row=5)
    eyebrowsString = tk.StringVar(assetFrame, value="")
    eyebrowsBox = ttk.Combobox(assetFrame, textvariable=eyebrowsString, height=len(eyebrowsAssets), values=eyebrowsAssets)
    eyebrowsBox.grid(column=0, row=6)
    def compileImage():
        global myimg
        myimg = ImageTk.PhotoImage(Image.open("zilch.png").resize((480, 480)))
        out = ImageConverters.ICSayoriTurned(myimg, [rString, lString, headString, mouthString, noseString, eyesString,
                                                     eyebrowsString, characterString])
        myimg = ImageTk.PhotoImage(out)
        imageLabel.config(image=myimg)
    def updateChar():
        global rAssets
        global lAssets
        global headAssets
        global mouthAssets
        global noseAssets
        global eyesAssets
        global eyebrowsAssets
        if characterString.get().lower() == "sayori":
            lAssets = mpt_s.assets['l']
            rAssets = mpt_s.assets['r']
            headAssets = mpt_s.assets['head']
            mouthAssets = mpt_s.assets['mouth']
            noseAssets = mpt_s.assets['nose']
            eyesAssets = mpt_s.assets['eyes']
            eyebrowsAssets = mpt_s.assets['eyebrows']
            lBox.config(values=lAssets)
            rBox.config(values=rAssets)
            headBox.config(values=headAssets)
            mouthBox.config(values=mouthAssets)
            noseBox.config(values=noseAssets)
            eyesBox.config(values=eyesAssets)
            eyebrowsBox.config(values=eyebrowsAssets)
    compileButton = tk.Button(master, command=compileImage, text="Compile")
    compileButton.grid(column=0, row=2)
    updateButton = tk.Button(master, command=updateChar, text="Select Character")
    updateButton.grid(column=0, row=3)
    master.mainloop()

if __name__ == '__main__':
    main()
