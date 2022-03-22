from pynput import keyboard


def move_right(game):
    '''
        Responds to a keypress 'd' by moving each pixel 1 unit along the width.
        Moves a pixel 1 unit to the right by calling the game function move_right()'''
    while True:
        event = keyboard.read_event()
        if event.even_type == keyboard.KEY_DOWN:
            key = event.name
            if key == 'd':
                game.move_right()

