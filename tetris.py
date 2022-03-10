import time

'''
    Re-create the Tetris game using print statements.
    The game will need all the shapes.
    The game will need a space to hold the current board, i.e. frame. DONE
    The shapes will need to appear on screen.
    The shapes will need to move down every second.
    The shapes will need to stop once touching another shape on the current board.
    The game will need to take in player inputs: right and left and down.
'''


class Pixel:
    '''
        This class is supposed to model exactly 1 Pixel on the Tetris board. 
        It is either on or off.
        The pixel is either decreasing or stationary.
        The pixel has x and y coordinates for a given frame.
    '''
    def __init__(self, x=0, y=0, decreasing=False, on=False):
        '''Initialize a Pixel with (x, y) coordinates, a 'decreasing' and 'on' Boolean variables.'''
        self.x = x
        self.y = y
        self.decreasing = decreasing
        self.on = on


class Frame:
    '''
        This class holds the current frame. 
        This frame will be printed to the screen.
        This frame must be updated every second.
    '''
    def __init__(self):
        '''Initialize a Frame with set width and height.'''
        self._width = 15
        self._height = 20
        self._center = self._width // 2
        
        # Create an empty width x height frame
        self.frame = []
        self.empty_pixel = '_'
        for i in range(self._height):
            self.frame.append(list(self.empty_pixel * self._width)) 

    
    def __str__(self):
        '''Make the frame print prettily to the screen.'''
        s = ''
        for i in range(len(self.frame)):
            if i == (len(self.frame) - 1):
                s = s + ''.join(self.frame[i])
            else:
                s = '\r' + s + ''.join(self.frame[i]) + '\n'
        return s


    def __add__(self, other):
        '''Add the pixels of the frame to the pixels of the block.
           If both empty pixels, then empty pixel.
           If one empty and one non-empty pixel, then non-empty pixel.
           If both non-empty pixels, then non-empty pixel from self.
        '''
        new_frame = []
        for i in range(self._height):
            new_row = []
            for j in range(self._width):
                if not self.frame[i][j] == self.empty_pixel:
                    new_row.append(self.frame[i][j])
                else:
                    new_row.append(other.frame[i][j]) 
            new_frame.append(new_row)
        return new_frame


import os
class Iblock(Frame):
    '''This class represent the i-block.'''
    def __init__(self):
        Frame.__init__(self)
        # Construct the I-block
        for i in range(4):
            self.frame[i][self._center] = '#'
game = Frame()
game.frame = game + Iblock()
for i in range(30):
    os.system('cls')
    print(game)
    time.sleep(1)
    for i in range(game._height):
        i = game._height - 1 - i # start on last row
        if i == (game._height - 1):
            continue
        for j in range(game._width):
            if not game.frame[i][j] == '_':
                game.frame[i+1][j] = game.frame[i][j]
                game.frame[i][j] = '_'

