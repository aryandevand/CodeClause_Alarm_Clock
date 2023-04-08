from tkinter import *
import datetime
import time
from tkinter import messagebox

root = Tk()
root.title("Advanced Alarm Clock")

label1 = Label(root, text="Enter the time in 24 hour format (HH:MM:SS)")
label1.pack(pady=10)

time_entry = Entry(root, font=("Helvetica", 20))
time_entry.pack(pady=10)

status_label = Label(root, text="")
status_label.pack(pady=10)

def alarm():
    status_label.config(text="Alarm is going off!")
    root.update()
    time.sleep(5)
    status_label.config(text="")
    root.update()
    messagebox.showinfo("Alarm", "Alarm Triggerer")

def set_alarm():
    alarm_time = time_entry.get()
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            alarm()
            break
        else:
            status_label.config(text=f"Waiting for {alarm_time}")
            root.update()
            time.sleep(1)

Button(root, text="Set Alarm", command=set_alarm).pack(pady=5)
Button(root, text="Exit", command=exit).pack(pady=10)

root.mainloop()



