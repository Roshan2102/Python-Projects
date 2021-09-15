# Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is: ", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()

clock.title("WAKING ALARM CLOCK")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hours", fg="red",
                    bg="black", relief="solid", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="Hour Min Sec", font=60).place(x=110)
SetYourAlarm = Label(clock, text="When to wake you up", fg="blue",
                     relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="pink",
                 width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=min, bg="pink",
                width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink",
                width=15).place(x=200, y=30)

submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=70)
clock.mainloop()
