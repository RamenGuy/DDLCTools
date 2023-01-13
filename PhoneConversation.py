import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font

def main():
    master = tk.Tk()
    master.title("Phone Call Helper")
    master.resizable(False, False)
    buttonFont = font.Font(family="segoe", size=12)
    style1 = ttk.Style(master)
    style1.configure('TFrame')
    style1.configure('mainFrame.TFrame', background="#191a36")
    buttonsColor = "#0d0e28"
    ico = Image.open('mm.png')
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
    caller = tk.StringVar(master, name="CallerVariable")
    currentCaller = tk.Label(master, text="Currently calling: " + caller.get())
    currentCaller.grid(column=0, row=2)
    currentCaller.config(text="Currently calling: " + caller.get())

    def addLine():
        with open("conversation.txt", "a") as convo:
            if characterListBox.selection_get() != "Narrator":
                convo.write(f"phone_{characters[characterListBox.selection_get()]} \"{line.get()}\"")
            else:
                convo.write(f"\"{line.get()}\"")
            convo.write("\n")
            line.set("")

    def startCall():
        if caller.get() == "":
            with open("conversation.txt", "a") as convo:
                convo.write(f"$ phone.call(\"{characters[characterListBox.selection_get()]}\")\n")
                caller.set(characterListBox.selection_get())
                print(f"Calling {characterListBox.selection_get()}")
                currentCaller.config(text="Currently calling: " + caller.get())
        else:
            print("Couldn't start another call - one is already in progress!")

    def endCall():
        if caller.get() != "":
            with open("conversation.txt", "a") as convo:
                convo.write(f"$ phone.end_call()\n")
                caller.set("")
                print("Call ended.")
                currentCaller.config(text="Currently calling: " + caller.get())
        else:
            print("Couldn't end the call - none are in progress!")

    addButton = tk.Button(master, text="Add", command=addLine)
    addButton.grid(column=1, row=1)
    callButton = tk.Button(master, text="Call", command=startCall)
    callButton.grid(column=1, row=2)
    endCallButton = tk.Button(master, text="End Call", command=endCall)
    endCallButton.grid(column=2, row=2)
    master.mainloop()


if __name__ == '__main__':
    main()
