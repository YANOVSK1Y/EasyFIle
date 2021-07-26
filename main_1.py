import tkinter
from tkinter import StringVar, Frame
from tkinter import filedialog as fd
import os


class EasyFile(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window

    def _init_window(self):
        pass

    def _open_file(self):
        f_types = [("All Files","*.*"),("PDF File" , "*.pdf"), ('Python files', '*.py'), ("Text files", '*.txt')]
        dlg = fd.Open(self, filetypes = f_types)
        fl = dlg.show()
        if fl != '':
            self.my_string_var.set(self.readl_data_from_file(fl))

    def _read_text(self):
        pass

    def _write_text(self):
        pass




if __name__ == '__main__':
    window = tkinter.Tk(className='easyfile')
    window.geometry("700x500")
    e = EasyFile(window)
    window.mainloop()
