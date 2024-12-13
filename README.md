User Manual 
                                                  Alarm Clock 
      Kiley Gilbert 
        12/11/24
                                                             Table of Contents
Imports
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




The purpose of this clock is to be used as an alarm clock for day to day tasks, setting the time, using alarms and making timely reminders. This begins with gathering of all imports then configuring all the necessary time adjustments for your time zone.

Getting Started With Alarm Clock

There are a few basic downloads from the python library that should not be difficult to get from any computer. Installation is also very simple as many of the imports can be pulled directly from python, if not there are other optional sites the imports, like time and datetime can be pulled from. 

System Requirements

Operating System: Windows 7 or later
Python 3.6 or later
Required Libraries: tkinter, datetime, winsound

When first opening the clock you’ll be greeted with 3 separate windows, the clock itself that will allow you to set the time, the settings menu, allowing changes to made within the alarms functions and sounds.

 User Interface Overview
 
Main Window: This is where you can set and stop the alarm.

Settings Window: Allows you to choose the alarm sound and control the volume.

Alarm Sound Selection Window: Provides options to select different alarm sounds.

Setting the Alarm

Open the main window of the application.

Enter the desired alarm time in the format HH:MM:SS.

Click the "Set Your Alarm" button to activate the alarm.

Stopping the Alarm

To stop the alarm, click the "Stop Alarm" button in the main window, this will reset the alarm and allow the user to redo their alarm.

Settings and Customization

Open the settings window by clicking the "Settings" button in the main window. Choose your preferred alarm sound from the available options, there are currently five.

Adjust the volume level as needed for the alarm to sound.

Troubleshooting or Issues

Alarm not sounding: Ensure the sound files are in the correct directories

Incorrect time format: Make sure to enter the time in HH:MM:SS format.

Application not starting: Verify that all required libraries are installed.

Contact Information:
KileyGilbert@gmail.com 


