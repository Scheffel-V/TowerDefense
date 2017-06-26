#OK
import pygame
from func import *

# Classe Rectangle:
# Unidade da tela do jogo, de onde todas as outras derivam.F
class Rectangle(object):
    def __init__(self, position, width, height, image):
        self._position = position # top left
        self._width = width
        self._height = height
        self._image = pygame.image.load(image)
        self._imageString = image

    def collide(self, rectTwo):
        rectTwoPos = rectTwo.getPosition()
        rectTwoDims = rectTwo.getDims()
        position1 = (first(rectTwoPos) + 1, second(rectTwoPos) +1)
        position2 = (first(rectTwoPos) + first(rectTwoDims) - 1, second(rectTwoPos)  + 1)
        position3 = (first(rectTwoPos) + first(rectTwoDims) - 1, second(rectTwoPos)  + second(rectTwoDims) - 1)
        position4 = (first(rectTwoPos) + 1, second(rectTwoPos)  + second(rectTwoDims) - 1)
        if self.isInside(position1) or self.isInside(position2) or self.isInside(position3) or self.isInside(position4):
            return True
        else:
            return False

    def calcCenter(self):
        return int(first(self._position) + .5 * self._width), int(second(self._position) + .5 * self._height)

    def getImage(self):
        return self._image

    def getImageString(self):
        return self._imageString

    def setImage(self, image):
        self._image = pygame.image.load(image)

    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position
        self.calcCenter()

    def getCenter(self):
        return self.calcCenter()

    def getWidth(self):
        return self._width

    def setWidth(self, width):
        self._width = width
        self.calcCenter()

    def getheight(self):
        return self._height

    def setheight(self, height):
        self._height = height
        self.calcCenter()

    def getDims(self):
        return [self.getWidth(), self.getheight()]

    def paint(self, surface):
        surface.blit(self._image, self._position)

    def isInside(self, position):
        if (first(self._position) <= first(position) < first(self._position) + self._width) and (second(self._position)  <= second(position) < second(self._position) + self._height):
                return True
        else:
            return False
