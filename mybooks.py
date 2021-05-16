from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

root = Tk() # Create app window

root.title("My Books Database App") # app window title
root.configure(background="light blue") #background color on app window
root.geometry("850x500") #size for app window
root.resizable(width=False,height=False) #disables resizing

#create label
title_label= ttk.Label(root, text="Title", background="light blue", font=("TkDefaultFont",16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24,textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

author_label= ttk.Label(root, text="Author", background="light blue", font=("TkDefaultFont",16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24,textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

ISBN_label= ttk.Label(root, text="ISBN", background="light blue", font=("TkDefaultFont",16))
ISBN_label.grid(row=0, column=4, sticky=W)
ISBN_text = StringVar()
ISBN_entry = ttk.Entry(root, width=24,textvariable=ISBN_text)
ISBN_entry.grid(row=0, column=5, sticky=W)

add_btn = Button(root, text="Add Book", bg="blue", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="white")
list_bx.grid(row=3,column=1, columnspan=14, sticky=W + E, pady=40,padx=15)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

modify_btn = Button(root, text="Modify Row", bg="purple", fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=3)

delete_btn = Button(root, text="Delete Row", bg="red", fg="white", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=4)

view_btn = Button(root, text="View all", bg="black", fg="white", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)

clear_btn = Button(root, text="Clear", bg="maroon", fg="white", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)

exit_btn = Button(root, text="Exit", bg="blue", fg="white", font="helvetica 10 bold", command="exit")
exit_btn.grid(row=15, column=5)

root.mainloop()