import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk


def main():
    master = tk.Tk()
    master.title("GC Registration Helper")
    master.resizable(False, False)
    style1 = ttk.Style(master)
    style1.configure('TFrame')
    style1.configure('mainFrame.TFrame', background="#191a36")
    ico = Image.open('icon.png')
    photo = ImageTk.PhotoImage(ico)
    if __name__ == '__main__':
        master.wm_iconphoto(False, photo)
    with open("characters.txt", "r") as file:
        characters = eval(file.read())
        characterFullNames = list(characters.keys())

    characterString = tk.StringVar(master, value=characterFullNames)
    characterListBox = tk.Listbox(master, listvariable=characterString, height=len(characterFullNames))
    characterListBox.grid(column=0, row=0)
    line = tk.StringVar(master, value="")
    lineBox = tk.Entry(master, textvariable=line)
    lineBox.grid(column=1, row=0)

    newGCFrame = tk.Frame(master, relief='sunken', borderwidth=2)
    newGCFrame.grid(column=2, row=0)
    newGCName = tk.StringVar(master, value="")
    newGCVisName = tk.StringVar(master, value="")
    newGCIcon = tk.StringVar(master, value="")
    gcNameEntry = tk.Entry(newGCFrame, textvariable=newGCName)
    gcNameEntry.grid(column=1, row=0)
    gcVisNameEntry = tk.Entry(newGCFrame, textvariable=newGCVisName)
    gcVisNameEntry.grid(column=1, row=1)
    gcIconEntry = tk.Entry(newGCFrame, textvariable=newGCIcon)
    gcIconEntry.grid(column=1, row=2)
    gcNameLabel = tk.Label(newGCFrame, text="Internal Name")
    gcNameLabel.grid(column=0, row=0)
    gcVisNameLabel = tk.Label(newGCFrame, text="Display Name")
    gcVisNameLabel.grid(column=0, row=1)
    gcIconLabel = tk.Label(newGCFrame, text="Icon File Name")
    gcIconLabel.grid(column=0, row=2)

    inGC = []
    currentGC = tk.StringVar(master)

    def newGC():
        with open("gc_register.txt", "a") as convo:
            convo.write(f"""@register
def __register_{newGCName.get()}_messages():
    register_group_chat(GroupChat(
                \"{newGCVisName.get()}\", \"mod_assets/phone/{newGCIcon.get()}\", \"{newGCName.get()}\"),
        {inGC.__str__().removesuffix("]").removeprefix("[")})
        """)
            convo.write("\n")
        currentGC.set(newGCName.get())
        newGCName.set("")
        newGCVisName.set("")
        newGCIcon.set("")

    def addLine():
        with open("gc_register.txt", "a") as convo:
            convo.write(f"    register_message(\"{currentGC.get()}\","
                        f" \"{characters[characterListBox.selection_get()]}\", _(\"{line.get()}\"))")
            convo.write("\n")
            line.set("")

    def addMember():
        inGC.append(characters[characterListBox.selection_get()])

    addButton = tk.Button(master, text="Add Message", command=addLine)
    addButton.grid(column=1, row=1)
    addToGCButton = tk.Button(master, text="Add to GC", command=addMember)
    addToGCButton.grid(column=0, row=1)
    newGCButton = tk.Button(newGCFrame, text="Create GC", command=newGC)
    newGCButton.grid(column=0, row=3)
    master.mainloop()


if __name__ == '__main__':
    main()
