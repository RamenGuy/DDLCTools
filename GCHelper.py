import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk


def main():
    master = tk.Tk()
    master.title("GC Helper")
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
    gcActive = tk.BooleanVar(master, name="CallerVariable")
    inGC = tk.StringVar(master, name="GCMemberVar")
    GCInfo = tk.Label(master, text=f"Currently messaging: {gcActive.get()}\nIn GC: {inGC.get()}")
    GCInfo.grid(column=0, row=2)
    GCInfo.config(text=f"Currently messaging: {gcActive.get()}\nIn GC: {inGC.get()}")

    newGCFrame = tk.Frame(master, relief='sunken', borderwidth=2)
    # newGCFrame.grid(column=2, row=0)
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

    discussionIDCurrent = tk.StringVar(master, value="")

    def newGC():
        with open("gc.txt", "a") as convo:
            convo.write(f"default {newGCName.get()} = phone.GroupChat(\"Sayori\","
                        f" \"mod_assets/phone/{newGCIcon.get()}\", \"{newGCName.get()}\")")
            convo.write("\n")
        newGCName.set("")
        newGCVisName.set("")
        newGCIcon.set("")

    def addLine():
        with open("gc.txt", "a") as convo:
            if characterListBox.selection_get() != "Narrator":
                convo.write(f"$ phone.message(\"{characters[characterListBox.selection_get()]}\", _(\"{line.get()}\"))")
            else:
                convo.write(f"\"{line.get()}\"")
            convo.write("\n")
            line.set("")

    def addMember():
        with open("gc.txt", "a") as convo:
            convo.write(f"$ phone.label(\"'{characterListBox.selection_get()}' was added to the group chat\")\n")
            inGC.set(f"{inGC.get()}, {characterListBox.selection_get()}")
            GCInfo.config(text=f"Currently messaging: {gcActive.get()}\nIn GC: {inGC.get()}")

    def startDiscussion():
        if not gcActive.get():
            with open("gc.txt", "a") as convo:
                convo.write(f"$ phone.discussion({discussionIDCurrent.get()})\n")
                discussionIDCurrent.set("")
                gcActive.set(True)
                GCInfo.config(text=f"Currently messaging: {gcActive.get()}\nIn GC: {inGC.get()}")
        else:
            print("Couldn't start another discussion - one is already in progress!")

    def endDiscussion():
        if gcActive.get():
            with open("gc.txt", "a") as convo:
                convo.write(f"$ phone.end_discussion()\n")
                gcActive.set(False)
                inGC.set("")
                GCInfo.config(text=f"Currently messaging: {gcActive.get()}\nIn GC: {inGC.get()}")
        else:
            print("Couldn't end the discussion - none are in progress!")

    addButton = tk.Button(master, text="Add Message", command=addLine)
    addButton.grid(column=1, row=1)
    addToGCButton = tk.Button(master, text="Add to GC", command=addMember)
    addToGCButton.grid(column=0, row=1)
    discussionCtrlFrame = tk.Frame(master, relief='sunken', borderwidth=2)
    discussionCtrlFrame.grid(column=2, row=0)
    startDiscussionButton = tk.Button(discussionCtrlFrame, text="Start Discussion", command=startDiscussion)
    startDiscussionButton.grid(column=0, row=1)
    endDiscussionButton = tk.Button(discussionCtrlFrame, text="End Discussion", command=endDiscussion)
    endDiscussionButton.grid(column=0, row=2)
    discussionToOpen = tk.Entry(discussionCtrlFrame, textvariable=discussionIDCurrent)
    discussionToOpen.grid(column=0, row=3)
    newGCButton = tk.Button(newGCFrame, text="Make New GC", command=newGC)
    newGCButton.grid(column=2, row=1)

    master.mainloop()


if __name__ == '__main__':
    main()
