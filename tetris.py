import time, os
from threading import Thread

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
        '''Initialize a Pixel with (x, y) coordinates, a 'decreasing' and 'on' Boolean variables.'''
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


    def get_pixel(self, x, y):
        '''
            Function returns a pixel at coordinates (x, y).
            x is the value along the width of the frame.
            y is the value along the height of the frame.'''
        try:
            return self.frame[y][x]
        except IndexError:
            return None# f'Pixel({x}, {y}) is not inside the domain of the frame.'

    
    def descending(self):
        '''
            Returns True if at least one pixel in the frame is descending.'''
        for i in range(self._height-1, -1, -1):
            for j in range(self._width-1, -1, -1):
                thepixel = self.get_pixel(j, i)
                if thepixel.descending:
                    return True
        return False


    def descend(self):
        '''
            Descends pixels down the length of the frame.
            A pixel is not descending on two occasions:
            1. If it is not all the way at the bottom of a frame.
            2. If there is another pixel directly below it that meets 2 conditions:
              a. It is on, and
              b. It is not descending.'''
        # look at each pixel from bottom right corner
        for i in range(self._height-1, -1, -1):
            for j in range(self._width-1, -1, -1):
                thepixel = self.get_pixel(j, i)
                if not thepixel.on:
                    # skip pixels that are not on
                    continue

                otherpixel = self.get_pixel(j, i+1)
                if not otherpixel:
                    # if otherpixel does not exist, then thepixel is all the way at the bottom of the screen
                    # therefore, thepixel should not be descending
                    thepixel.descending = False
                    continue

                if (otherpixel.on and not otherpixel.descending):
                    # if there is another pixel directly below: that is on and not descending, thepixel should not be descending
                    thepixel.descending = False
                else:
                    # else descend the pixel
                    thepixel.on = False
                    thepixel.descending = False
                    otherpixel.on = True
                    otherpixel.descending = True


    def move_right(self):
        for i in range(self._height-1, -1, -1):
            for j in range(self._width-1, -1, -1):
                thepixel = self.get_pixel(j, i)
                if thepixel.descending and thepixel.x < (self._width-1):
                    otherpixel = self.get_pixel(j+1, i)
                    thepixel.on = False
                    thepixel.descending = False
                    otherpixel.on = True
                    otherpixel.descending = True


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
            self.frame[i][j] = Pixel(x=j, y=i, on=True, descending=True)


game = Frame()
game + Iblock()
def movement():
    while True:
        x = input()
        if x.lower() == 'd':
            game.move_right()


Thread(target=movement).start()

for c in range(35):
    os.system('cls')
    print(game)
    time.sleep(0.5)
    if game.descending():
        game.descend()
    else:
        game + Iblock()
