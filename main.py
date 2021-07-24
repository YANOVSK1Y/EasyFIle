import tkinter
from tkinter import StringVar, Frame
from tkinter import filedialog as fd
import os


class Easyfile(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.my_string_var = StringVar()
        self.base_file_text = ''
        self._init_window()


    def _init_window(self):
        self.window.title = "Easyfile"
        # discribed labels
        tkinter.Label(text="Old name", width=23, background='blue').place(x=100, y=50)
        tkinter.Label(text='Enter new name', width=23, background='green').place(x=400, y=50)
        # labels and input fields
        tkinter.Label(text='', width=23, bg='grey').place(x=100, y=75)
        tkinter.Entry(text='', width=13).place(x=400, y=75)
        tkinter.Entry(text='', width=10).place(x=503, y=75)
        # buttons
        tkinter.Button(text="Brows file", width="20", command=self.openFiles).place(x=100, y=100)
        tkinter.Button(text="Raname", width="20", command=self.rename).place(x=400, y=100)
        #label for file content
        # tkinter.Label(self.window ,text='', bg='lightblue', textvariable=self.my_string_var, justify='left').place(x=100, y=150)
        self.text = tkinter.Text(bg='lightblue', height=10, width=20)
        self.text.place(x=100, y=150)

    def readl_data_from_file(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
            self.base_file_text = text
        self.text.insert('1.0', text)
        return text

    def openFiles(self):
        f_types = [("All Files","*.*"),("PDF File" , "*.pdf"), ('Python files', '*.py'), ("Text files", '*.txt')]
        dlg = fd.Open(self, filetypes = f_types)
        fl = dlg.show()

        if fl != '':
            self.my_string_var.set(self.readl_data_from_file(fl))


    def writedata(self), filename, text):
        with open(filename, 'w') as f:
            f.write(text)






    def rename(self):
        pass

if __name__ == '__main__':

    window = tkinter.Tk(className='easyfile')
    window.geometry("700x400")
    e = Easyfile(window)
    window.mainloop()
