import tkinter as tk
from PIL import ImageTk, Image
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def main():
    master = tk.Tk()
    master.title("Poem Word List Helper")
    master.resizable(False, False)
    ico = Image.open('mm.png')
    photo = ImageTk.PhotoImage(ico)
    if __name__ == '__main__':
        master.wm_iconphoto(False, photo)
    sPoints = tk.IntVar(master, 0)
    nPoints = tk.IntVar(master, 0)
    yPoints = tk.IntVar(master, 0)
    mPoints = tk.IntVar(master, 0)
    word = tk.StringVar(master, "")
    wordFrame = tk.Frame(master, relief='sunken', borderwidth=2)
    wordFrame.grid(column=0, row=0)
    wordBox = tk.Entry(master=wordFrame, textvariable=word)
    wordBox.grid(column=0, row=0)
    frameEntry = tk.Frame(master, relief='sunken', borderwidth=2)
    frameEntry.grid(column=1, row=0)
    sLabel = tk.Label(master=frameEntry, text="S")
    sLabel.grid(column=0, row=0)
    nLabel = tk.Label(master=frameEntry, text="N")
    nLabel.grid(column=1, row=0)
    yLabel = tk.Label(master=frameEntry, text="Y")
    yLabel.grid(column=2, row=0)
    mLabel = tk.Label(master=frameEntry, text="M")
    mLabel.grid(column=3, row=0)
    sBox = tk.Entry(master=frameEntry, textvariable=sPoints, width=5)
    sBox.grid(column=0, row=1)
    nBox = tk.Entry(master=frameEntry, textvariable=nPoints, width=5)
    nBox.grid(column=1, row=1)
    yBox = tk.Entry(master=frameEntry, textvariable=yPoints, width=5)
    yBox.grid(column=2, row=1)
    mBox = tk.Entry(master=frameEntry, textvariable=mPoints, width=5)
    mBox.grid(column=3, row=1)

    # noinspection PyUnusedLocal
    def addWord():
        wordToAdd = f"{word.get()},"
        s = sPoints.get()
        n = nPoints.get()
        y = yPoints.get()
        m = mPoints.get()
        toAdd = eval(config['DEFAULT']['PointsOrder'])
        '''
        if sPoints.get() != 0:
            wordToAdd += f"{sPoints.get()},"
        if nPoints.get() != 0:
            wordToAdd += f"{nPoints.get()},"
        if yPoints.get() != 0:
            wordToAdd += f"{yPoints.get()},"
        if mPoints.get() != 0:
            wordToAdd += f"{mPoints.get()},"
            '''
        for i in toAdd:
            wordToAdd += f"{i},"
        wordToAdd = wordToAdd.strip(",")
        with open("poemwords.txt", "a") as f:
            print(wordToAdd)
            f.write(wordToAdd)
            f.write("\n")
        # sPoints.set(0)
        # nPoints.set(0)
        # yPoints.set(0)
        # mPoints.set(0)
        word.set("")

    addButton = tk.Button(wordFrame, text="Add", command=addWord)
    addButton.grid(column=0, row=1)
    master.mainloop()


if __name__ == '__main__':
    main()
