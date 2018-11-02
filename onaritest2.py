is_quit = False

KeyComb_Quit = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='q')},
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='q')},
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='q')}

]

def on_press(key):
    global is_quit
        if any([key in comb for comb in KeyComb_Quit]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in KeyComb_Quit):
            is_quit = True

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


# The currently active modifiers
current = set()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

if is_quit:
    break
