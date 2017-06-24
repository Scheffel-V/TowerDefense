from ctypes import *
# https://stackoverflow.com/questions/35988/c-like-structures-in-python
# https://docs.python.org/3/library/ctypes.html

class POSITION(Structure):
	{"x","y"}

class RECTANGLE(Structure):
	{"position","width","height","image", "imageString"}

def newRECTANGLE(position, width, height, image):
	return RECTANGLE(position, width, height, pygame.image.load(image), image)

def collide(rect1, rect2):
	#let
	position1 = (rect2.position.x + 1, rect2.position.y + 1 )
	position2 = (rect2.position.x  + rect2.width - 1, rect2.position.y + 1)
	position3 = (rect2.position.x  + rect2.width - 1, rect2.position.y + rect2.height - 1)
	position4 = (rect2.position.x  + 1, rect2.position.y + rect2.height  - 1)
	#in
	if isInside(rect1.position, position1, rect1.width, rect1.height) or isInside(rect1.position, position2, rect1.width, rect1.height) or isInside(rect1.position, position3,rect1.width, rect1.height) or isInside(rect1.position, position4, rect1.width, rect1.height):
		return True
	else: 
		return False

def isInside(position1, position2, width, height):
	if position1.x <= position2.x < position1.x + width:
		if position1.y <= position2.y < position1.y + height:
			return True
	else:
		return False

def calcCenter(rect):
	return ( int(rect.position.x + .5 * rect.width), int(rect.position.y + .5 * rect.height) )

def getDims(rect):
	return (rect.width, rect.height)