from tetris import Frame
# Create 1 class for each block object.
class Block:
    '''
        This class represents the current block.
        The current block can be one of seven blocks: 
            I, O, S, Z, J, L, T.
    '''
blocks = {
    'iblock': [['#']] * 4,
    'oblock': [['#', '#']] * 2,
    'sblock': [[' ', '#', '#'], ['#', '#', ' ']],
    'zblock': [['#', '#', ' '], [' ', '#', '#']],
    'jblock': [[' ', '#']] * 3 + [['#', '#']],
    'lblock': [['#', ' ']] * 3 + [['#', '#']],
    'tblock': [['#', '#', '#'], [' ', '#', ' ']]
}

class Iblock(Frame):
    '''This class represent the i-block.'''
    def __init__(self):
        Frame.__init__(self)
        # Construct the I-block
        for i in range(4):
            self.frame[i][self._center] = '#'

class Oblock(Frame):
    '''This class represent the i-block.'''
    def __init__(self):
        Frame.__init__(self)
        # Construct the I-block
        for i in range(2):
            self.frame[i][self._center] = '#'
            self.frame[i][self._center+1] = '#'
        


# The i-block needs to appear on the current frame.
# The i-block needs to appear in the center of the current frame.


# GOAL: Display block on the frame.
# Add the block to the current frame.
