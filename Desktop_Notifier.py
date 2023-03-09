
from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from plyer import notification
import time


root=Tk()

root.title("DESKTOP NOTIFIER")

root.geometry("350x300")

root.resizable(False,False)

root.configure(bg="pink")

def get_details() :
    get_msg = msg.get()
    get_time = time1.get()

    if get_msg=="" or get_time=="":
        messagebox.showerror("Alert", "All The Fields Are Required!")
    else:
        rem_time = float(get_time)
        min_to_sec = rem_time*60
        messagebox.showinfo("Notifier Set", "Set Notification?")

        time.sleep(min_to_sec)

        notification.notify(message=get_msg,
                            app_name='notifier',
                            timeout=10)


Label(root,text="Desktop Notifier", font="calibri 30 bold", bg="pink").pack()

Label(root,text="Display Msg : ", font="aerial 10 bold", bg="pink").place(x=40,y=90)

Label(root,text="Set Time : ", font="aerial 10 bold", bg="pink").place(x=40,y=130)

msg=Entry(root, bd=4)
msg.place(x=140,y=90)

time1=Entry(root, bd=4)
time1.place(x=140,y=130)

Button(root, text="Set Remainder", bg="black", fg="pink", bd=4, command=get_details).place(x=130,y=190)


mainloop()
