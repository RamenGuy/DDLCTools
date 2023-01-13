import PhoneConversation
import PoemWordHelper
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font

main = tk.Tk()
main.title("DDLC Tools")
main.resizable(False, False)
buttonFont = font.Font(family="segoe", size=12)
style1 = ttk.Style(main)
style1.configure('TFrame')
style1.configure('mainFrame.TFrame', background="#191a36")
buttonsColor = "#0d0e28"

ico = Image.open('mm.png')
photo = ImageTk.PhotoImage(ico)
main.wm_iconphoto(True, photo)
frame = ttk.Frame(main, relief='sunken', style='mainFrame.TFrame', borderwidth=2)
frame.grid(column=0, row=0)
buttonPoem = tk.Button(frame, text="Poem Word Helper", command=PoemWordHelper.main, background=buttonsColor,
                       font=buttonFont, foreground="#ffffff", activebackground="#0a0a1a", activeforeground="#a8a8a8")
buttonPoem.grid(column=0, row=0)
buttonPhone = tk.Button(frame, text="Phone Conversation Helper", command=PhoneConversation.main,
                        background=buttonsColor, font=buttonFont, foreground="#ffffff", activebackground="#0a0a1a",
                        activeforeground="#a8a8a8")
buttonPhone.grid(column=1, row=0)

main.mainloop()