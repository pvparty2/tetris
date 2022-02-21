'''
    Re-create the Tetris game using print statements.
    The game will need all the shapes.
    The game will need a space to hold the current board, i.e. frame.
    The shapes will need to appear on screen.
    The shapes will need to move down every second.
    The shapes will need to stop once touching another shape on the current board.
    The game will need to take in player inputs: right and left and down.
'''

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
        self.frame = [list(' ' * self._width)] * self._height # Create an empty frame

    
    def __str__(self):
        '''Make the frame print prettily to the screen.'''
        s = ''
        for line in self.frame:
            s = s + ''.join(line) + '\n'
        return s




