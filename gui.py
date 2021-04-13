from tkinter import *
from tkinter.tix import *
import pyperclip

class Gui:

    def __init__(self, toTranslate, translation):
        self.root = self.rt()
        self.translation = translation
        frame = Frame(width="500", height="700")
        frame.grid(row=0, column=0)

        Label(frame, text='ORIGINAL TEXT', font=('Microsoft Sans Serif', 15, 'bold'), pady=15, padx=4, justify=CENTER, bg='#EFEFEF', fg='#2C82C9').grid(row=0, column=0)
        originalTextField = ScrolledWindow(frame, width=500, height=200)
        originalTextField.grid(row=1, column=0)
        win = originalTextField.window
        Label(win, text=toTranslate, font=('Microsoft Sans Serif', 12), pady=20, padx=30, bg='#EFEFEF',justify=LEFT, wraplength=400, fg='#181303').pack()

        Label(frame, text='TRANSLATED TEXT', font=('Microsoft Sans Serif', 15, 'bold'), pady=15, padx=4, bg='#EFEFEF', fg='#2C82C9').grid(row=2, column=0)

        Button(frame, command=self.copy, text="COPY TO CLIPBOARD", font=('Microsoft Sans Serif', 12), bg='#2C82C9', fg='#181303').grid(row=4, column=0, pady=15)

        translatedTextField = ScrolledWindow(frame, width=500, height=200)
        translatedTextField.grid(row=3, column=0)
        win2 = translatedTextField.window
        Label(win2, text=translation, font=('Microsoft Sans Serif', 12), pady=20, padx=30, bg='#EFEFEF', justify=LEFT, wraplength=400, fg='#181303').pack()



    def copy(self):
        pyperclip.copy(self.translation)


    def rt(self):
        root = Tk()
        root.title('Translate')
        root.resizable(False, False)
        root.bind('<Escape>', lambda event: self.root.destroy())
        root.configure(background='#EFEFEF')
        positionRight = int(root.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(root.winfo_screenheight() / 2 - 600 / 2)
        root.geometry("500x600+{}+{}".format(positionRight, positionDown))
        return root
