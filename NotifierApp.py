from tkinter import *
from tkinter import messagebox
import time
from plyer import notification

gui = Tk()
gui.geometry('500x300')
gui.title('Notifier App')
gui.configure(bg='#9ECFC2')

def createNotification():
    if titleEntry.get() == '' or messageEntry.get() == '' or whenToDisplayEntry.get() == '':
        messagebox.showerror('Error', 'Must fill all fields.')

    else:
        get_title = titleEntry.get()
        get_message = messageEntry.get()
        get_time = float(whenToDisplayEntry.get())
        messagebox.showinfo('Notification', 'Successfully created a notification!')
        time.sleep(get_time * 60)
        notification.notify(title=get_title, message=get_message, app_icon='D:\Downloads\icon.ico', timeout=10)


pic = PhotoImage(file='D:\Downloads\image1.png')
picLabel = Label(gui,image=pic,height=100,width=100).place(x=1,y=1)
bigTitle = Label(gui, text = 'Make a notification', font = ('Arial', 30),bg='#9ECFC2').place(x = 100,y = 1)
title = Label(gui,text='Title of notification:',font=('Arial', 15),bg='#9ECFC2').place(x=1,y=100)
titleEntry = Entry(gui, width='20',font=('Arial', 15))
titleEntry.place(x=170,y=100)
message = Label(gui,text='Message:',font=('Arial', 15),bg='#9ECFC2').place(x=1,y=150)
messageEntry = Entry(gui, width='27',font=('Arial', 15))
messageEntry.place(x=95,y=150)
whenToDisplay = Label(gui,text='When to display(in minutes):', font=('Arial', 15),bg='#9ECFC2').place(x=1,y=200)
whenToDisplayEntry = Entry(gui, width='12',font=('Arial', 15))
whenToDisplayEntry.place(x=260,y=200)
createButton = Button(gui,text='Create a notification!',command=createNotification,font = ('Arial', 13)).place(x=165,y=255)

gui.mainloop()