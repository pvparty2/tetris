import time, os

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
    def __init__(self, x=0, y=0, descending=False, on=False):
        '''Initialize a Pixel with (x, y) coordinates, a 'decreasing' and 'is_on' Boolean variables.'''
        self.x = x
        self.y = y
        self.descending = descending
        self.on = on
        self.coordinates = (x, y)
    

    def __repr__(self):
        '''
            Function that returns the value of a pixel.
            We need this to populate the gaming board.'''
        if self.on:
            return '#'
        return '_'

    
    def move(self):
        '''
            This function moves a pixel down the gaming board.
            The y coordinate of a pixel decreases by 1.
            This function returns None.'''
        self.y -= 1
        return None

    
    def __add__(self, other):
        '''
            Add 2 Pixels.
            The add operator will override the self Pixel with the other Pixel
            if the self Pixel is not on.'''
        if self.on:
            return self
        self.on = True
        return other


class Frame:
    '''
        This class holds the current frame. 
        This frame will be printed to the screen.
        This frame must be updated every second.
    '''
    def __init__(self, width=15, height=20):
        '''Initialize a Frame with set width and height.'''
        self._width = width
        self._height = height
        self._center = self._width // 2

        # Create an empty width by height frame.
        # We want to do this only once upon initialization.
        self.frame = []
        for i in range(self._height):
            self.frame.append([])
            for j in range(self._width):
                self.frame[i].append(Pixel(x=j, y=i))

    
    def __repr__(self):
        '''
            Make the frame print prettily to the screen.'''
        s = ''
        for i in range(self._height):
            for j in range(self._width):
                s += str(self.frame[i][j])
            s += '\n'
        return s


    def __add__(self, other):
        '''
            Add the pixels of 2 frames, with equal width and height.
            If both pixels not on, then not on pixel.
            If self has a not on pixel, but other has a on pixel, then override the self pixel.
            If both not on pixels, then self remains not on.'''
        for i in range(self._height):
            for j in range(self._width):
                # if the pixel in the other object is on, then assign to self.
                thepixel = other.frame[i][j]
                if thepixel.on:
                    self.frame[i][j] = thepixel
        return self

    
    def descending(self):
        '''
            If at least one pixel in a frame is descending, then descending() returns True.
            Otherwise, returns False to say that none of them are descending.'''
        for i in range(self._height):
            for j in range(self._width):
                thepixel = self.frame[i][j]
                if thepixel.descending:
                    return True
        return False


class Iblock(Frame):
    '''This class represent the i-block.'''
    def __init__(self):
        Frame.__init__(self)
        # Construct the I-block
        self.coordinates = ((0, self._center),
                            (1, self._center),
                            (2, self._center),
                            (3, self._center))
        for i, j in self.coordinates:
            self.frame[i][j] = Pixel(x=j, y=i, on=True)


game = Frame()
game + Iblock()
for c in range(30):
    os.system('cls')
    print(game)
    time.sleep(0.25)
    # What do we want to do?
    # The Iblock should descend down the frame.
    # It will descend if each pixel within the Iblock is descending.
    # A pixel is not descending on two ocassions:
    # 1. If it is not all the way at the bottom of a frame.
    # 2. If there is another pixel directly below it that meets 2 conditions:
    #   a. It is on, and
    #   b. It is not descending.
    for i in range(game._height-1, -1, -1): # work from the bottom to the top
        for j in range(game._width-1, -1, -1): # work from right to left
            thepixel = game.frame[i][j]
            if not thepixel.on:
                # skip pixels that are not on
                continue
            if thepixel.y == game._height-1:
                # if the pixel is all the way at the bottom of the screen, it should not be descending.
                thepixel.descending = False
            elif (game.frame[i+1][j].on and not game.frame[i+1][j].descending):
                # if there is another pixel directly below: that is on and not descending, thepixel should not be descending
                thepixel.descending = False
            else:
                game.frame[i][j].on = False
                game.frame[i+1][j].on = True
