import tkinter

window = tkinter.Tk(className='easyfile')
window.geometry("700x200")
# label_file_name = tkinter.Label(text='File name')
# label_new_file_name = tkinter.Label(text='New file name')


tkinter.Label(text="Old name", width=23, background='blue').place(x=100, y=50)
tkinter.Label(text='Enter new name', width=23, background='green').place(x=400, y=50)

tkinter.Label(text='', width=23, bg='grey').place(x=100, y=75)
tkinter.Entry(text='', width=13).place(x=400, y=75)
tkinter.Entry(text='', width=10).place(x=503, y=75)


tkinter.Button(text="Brows file", width="20").place(x=100, y=100)
tkinter.Button(text="Raname", width="20").place(x=400, y=100)



#
# label_file_name.pack()
# label_new_file_name.pack()
#
# label_filename = tkinter.Label(text="", width=10)
# label_rename_file_input = tkinter.Label(text='enter new name', width=20)
#
# label_filename.pack()
# label_rename_file_input.pack()

window.mainloop()
