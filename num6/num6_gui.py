# num6_gui.py

from tkinter import *
from tkinter.messagebox import *
import num6


__version__ = '0.3.2'


def exit_f():
    retv = askquestion('Confirmation', 'Are you sure you want to exit ? ')
    if retv == 'yes':
        root.destroy()
    elif retv == 'no':
        return 'Exit permission denied ! '
    else:
        return 'Exit permission denied ! '


def num6_encrypt():
    return num6.encrypt(string=normal_value.get('1.0'))


def num6_decrypt():
    return num6.decrypt(string=encrypted_value.get())


def Clear():
    print('Clearing this')


def Copy():
    print('Coping this')


root = Tk()
root.title(f'Num6 - {__version__}')
winsize_height = root.winfo_screenheight
winsize_width = root.winfo_screenwidth
# root.geometry(f'{winsize_height}x{winsize_width}')
root.geometry('750x550')
# root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", exit_f)


def about():
    showinfo('About', f'Num6 - version {__version__}')


def author():
    showinfo('Author', 'Developer:\nMd. Almas Ali')


def open():
    showinfo('Result', 'Openning file.')


mainmenu = Menu(root)

Filemenu = Menu(mainmenu, tearoff=0)
Filemenu.add_command(label='Open', command=open)
Filemenu.add_separator()
Filemenu.add_command(label='Exit', command=exit_f)
mainmenu.add_cascade(label='File', menu=Filemenu)

aboutmenu = Menu(mainmenu, tearoff=0)
aboutmenu.add_command(label='About', command=about)
mainmenu.add_cascade(label='About', menu=aboutmenu)

authormenu = Menu(mainmenu, tearoff=0)
authormenu.add_command(label='Author', command=author)
mainmenu.add_cascade(label='Author', menu=authormenu)
root.config(menu=mainmenu)

f1 = Frame(root, bg="lightblue", borderwidth=6, relief=SUNKEN)
f1.pack(side='top', fill='x')

f2 = Frame(root, bg='aqua')
f2.pack(side='bottom', fill="x")

f3 = Frame(root, bg="lightblue", borderwidth=6, relief=SUNKEN)
f3.pack()

f4 = Frame(root, bg="lightblue", borderwidth=6, relief=SUNKEN)
f4.pack()

Label(f1, text='Num6', fg='green', bg="lightblue",
      font="Times 26 bold").pack(padx=8, pady=5)

Label(f2, text="© Copyright by Md. Almas Ali.",
      fg='green', bg='aqua', font="Times 8 bold").pack()

encryption_value = StringVar()
decryption_value = StringVar()

scrollbar = Scrollbar(f3)
scrollbar.pack(side='right', fill='y')

scrollbar2 = Scrollbar(f3, orient='horizontal')
scrollbar2.pack(side='bottom', fill='x')

Label(f3, text='Normal value :', bg='lightblue').pack()

normal_value = Text(f3, bg='white', fg='black',
                  yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set, height=10, width=700)

normal_value.pack(expand=True, fill='both')
scrollbar.config(command=normal_value.yview)
scrollbar2.config(command=normal_value.xview)


scrollbar = Scrollbar(f4)
scrollbar.pack(side='right', fill='y')

scrollbar2 = Scrollbar(f4, orient='horizontal')
scrollbar2.pack(side='bottom', fill='x')

Label(f4, text='Encryped value :', bg='lightblue').pack()

encrypted_value = Text(f4, bg='white', fg='black',
                  yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set, height=10, width=700)

encrypted_value.pack(expand=True, fill='both')
scrollbar.config(command=encrypted_value.yview)
scrollbar2.config(command=encrypted_value.xview)

Button(f4, text='Clear', bg='darkgreen', fg='white', command=Clear).pack()
Button(f4, text='Copy', bg='darkgreen', fg='white', command=Copy).pack()
Button(f4, text='Encrypt', bg='darkgreen',
       fg='white', command=num6_encrypt).pack()

#Text(f2, textvariable=encryption_value, bg='lightblue', fg='black', font='Times 8 bold').pack(pady=30)

#Button(f1, text='Encrypt', bg='darkgreen', fg='white', command=num6_encrypt).pack(pady=30)


#Label(f1, text='Encrypted value :', bg='lightblue').pack()

#Text(f2, textvariable=decryption_value, bg='lightblue', fg='black', font='Times 8 bold').pack(pady=30)

#Button(f1, text='Decrypt', bg='darkgreen', fg='white', command=num6_decrypt).pack(pady=30)

root.mainloop()
