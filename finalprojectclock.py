'''Author Kiley Gilbert
Date Begun 11/19/14
Final Project Clock'''

#Importing the necessary modules 
from asyncio import sleep
import ensurepip
from logging import root
from threading import Thread
from tkinter import *
import datetime
import time
from tkinter.font import Font
from typing import Self
import winsound
import tkinter as tk
import tkinter
import pip
import _strptime
ensurepip

#Function to set the alarm 
def Alarm(set_alarm_timer):
    '''This function takes the alarms time as input and
    waits until the alarm set time to trigger the alarm'''
    while True:
        time.sleep(1) #waits for 1 second
        actual_time = datetime.datetime.now() #Gets the current time
        cur_time = actual_time.strftime("%H:%M:%S") #Formats the current time
        cur_date = actual_time.strftime("%d/%m/%Y") #Formats the current date

        if cur_time == set_alarm_timer: # Checks if the current time matches the alarm time
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)# Plays the alarm sound

            break #exits the loop

        def validate_time(hour, minute, second):
            if not hour.isdigit() or not minute.isdigit() or not second.isdigit():
                return False, "Time must be numeric."
            if not (0 <= int(hour) < 24):
                return False, "Hour must be between 0 and 23."
            if not (0 <= int(minute) < 60):
                return False, "Minute must be between 0 and 59."
            if not (0 <= int(second) < 60):
                return False, "Second must be between 0 and 59."
                return True, ""
#function to get time
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}" #formats the time
    Alarm(alarm_set_time) #set the alarm

#function displays a message when the alarm is set
def alarm_set_message():
    print("Alarm has been set!")

#function displays a message when the alarm is stopped
def alarm_stopped_message():
    print("Alarm has been stopped!")

#function displays a message when settings are opened
def settings_opened_message():
    print("Settings window opened!")

#Creating the First Window
window = Tk()
window.title("Final Project Alarm Clock") #sets the window title
window.geometry("500x290") #sets the window size
window.config(bg="#FF81C0") #imports the background image
window.resizable(width=False,height=False) #disables windows resize

#adding labels and input fields for the alarm time
time_format=Label(window, text= "Stop the Alarm at Anytime", 
                  fg="white",bg="#FFC0CB",font=("Arial",15)).place(x=120,y=160)
setYourAlarm = Label(window,text = "Set Your Alarm",
                     fg="white",bg="#FFC0CB",relief = "solid",font=("Helevetica",17,"bold")).place(x=180, y=10)
#variables to store alarm time
hour = StringVar()
min = StringVar()
sec = StringVar()
 #inputs fields for alarm times
hourTime= Entry(window,textvariable = hour,bg = "#F0FFFF",width = 7,font=(40)).place(x=200,y=50)
minTime= Entry(window,textvariable = min,bg = "#F0FFFF",width = 8,font=(40)).place(x=220,y=50)
secTime = Entry(window,textvariable = sec,bg = "#F0FFFF",width = 10,font=(40)).place(x=240,y=50)
 
 #buttons to set and stop alarms and open settings window
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#C875C4",
                width = 15,command = get_alarm_time,font=(20)).place(x =100,y=100)
stop = Button(window, text="Stop Alarm", fg="Black", bg="#C875C4", width=15, 
              command=("stop_alarm"), font=(20)).place(x=250, y=100)
submit = Button(window, text ="Settings", 
command=("open"), font=(20)).place(x=10, y=240)
submit = Button(window, text ="Exit", 
command=("window.destroy"), font=(20)).place(x=450, y=240)


#creating the second window
window = Tk()
window.title("Settings") #setting window title
window.geometry("200x360") #setting window size
window.config(bg="#FF81C0") #importing background image
window.resizable(width=False,height=False) #disables window resizing

#buttons and lables for alarm settings
submit = Button(window, text ="Choose your alarm sound", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=80)

choseyouralarm=Label(window, text="Click to choose your alarm" 
                     ,fg="Black",bg="#FFC0CB",
                width = 20,font=(7)).place(x =5  ,y=50)

submit = Button(window, text ="Volume Control", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=160)

volumecontrol=Label(window, text="Choose the volume level" 
                     ,fg="Black",bg="#FFC0CB",
                width = 20,font=(7)).place(x =5  ,y=120)
submit = Button(window, text ="Exit", 
command=("window.destroy"), font=(20)).place(x=160, y=310)
# Function to choose alarm sound
def choose_alarm_sound():
    print("Alarm sound chosen")

# Function to adjust volume
def adjust_volume():
    print("Volume adjusted")

# Function to exit the application
def exit_application():
    window.destroy()


#creating the third window
window = Tk()
window.title("Choosing Alarm Sound")
window.geometry("300x360")
window.config(bg="#FF81C0")
window.resizable(width=False,height=False)

#dictionary to store ringtones paths
ringtones_path = { "Classic Bell": "D:/Library/to/classic_bell.wav",
    "Siren": "D:/Library/to/siren.wav",
    "Ocean Waves": "D:/Library/to/ocean_waves.wav",
    "Music": "D:/Library/to/music.wav",
    "Science Alarm": "D:/Library/to/science_alarm.wav"}

#buttons and lables for alarm sounds
choseyouralarm=Label(window, text="There are five options" 
                     ,fg="Black",bg="#FFC0CB",
                width = 20,font=(7)).place(x =5  ,y=50)

submit = Button(window, text ="Classic Bell", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=80)

submit = Button(window, text ="Siren", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=120)

submit = Button(window, text ="Ocean Waves", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=160)

submit = Button(window, text ="Music", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=200)

submit = Button(window, text ="Science Alarm", 
command=("choose_alarm_sound"), font=(20)).place(x=5, y=240)

submit = Button(window, text ="Exit", 
command=("window.destroy"), font=(20)).place(x=260, y=310)

#runs the main loop
window.mainloop()