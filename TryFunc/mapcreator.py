import config
import pygame
import sys
import map
import rectangle
from sys import argv
import os
from func import *


class MapCreator:
	def __init__(self, filemap=None):		
		self._conf = config.Config()
		self._screen = pygame.display.set_mode(self._conf.DISPLAY_SIZE)
		self._matrix = [[0 for aux in range(self._conf.MAP_DIMX)] for aux2 in range(self._conf.MAP_DIMY)]
		self._rectMap = map.Map2(self._conf.MAP_DIMS, self._conf.RECT_DIMS_px, self._matrix, 'creation')
		self._currentValue = 1
		self._filemap = filemap
		#self._matrix = self.createMatrixWithZeros(self._conf.MAP_DIMX, self._conf.MAP_DIMY)

	def createMatrixWithZeros(self, x, y):
		return self.createMatrixColumn(self.createMatrixLane(x), y)

	def createMatrixLane(self, x):
		if x == 0:
			return []
		else:
			return cons(0, self.createMatrixLane(x-1))

	def createMatrixColumn(self, lane, y):
		if y == 0:
			return []
		else:
			return cons(lane, self.createMatrixColumn(lane,y-1))

	def getCurrentValue(self):
		return self._currentValue

	def getConf(self):
		return self._conf

	def getRectMap(self):
		return self._rectMap

	def getMatrix(self):
		return self._matrix

	def getScreen(self):
		return self._screen

	def setCurrentValue(self, value):
		if value in self.getConf().MAP_NUMBMATRIX_VALUES:
			self._currentValue = value

	def setMatrix(self, matrix):
		self._matrix = matrix

	def setRectMap(self, rectMap):
		self._rectMap = rectMap

	def setMatrixElement(self,coords,value=0):
		try:
			if self._isValidValue(value):
				self._matrix[second(coords)][first(coords)] = value
			else:
				raise ValueError("Invalid value !")
		except IndexError:
			print("Not valid X or Y coords !")
			raise
		except TypeError:
			pass

	def getMatrixElement(self,x,y):
		try:
			element = self.getMatrix()[x][y]
		except IndexError:
			printf("Por favor insira um x e y valido")
			raise

		return element

	def setWindowCaption(self, string):
		pygame.display.set_caption(string)

	def getClickedSquare(self, pxPosition):
		xPos = int(first(pxPosition)/self.getConf().RECT_DIMX_px)
		yPos = int(second(pxPosition)/self.getConf().RECT_DIMX_px)
		if xPos < self.getConf().MAP_DIMX and yPos < self.getConf().MAP_DIMY:	
			return (xPos, yPos)
		pass

	def getNewFileName(self):
		if self._filemap != None:
			return self._filemap

		maps = os.listdir("maps")

		if is_empty(maps):
			return 'maps/map1.map'

		all_index = []
		for mapa in maps:
			name = mapa.split('/')[-1]
			index = int(name.split('.')[0][3:])
			all_index.append(index)
		#maps = list(map(lambda x: x.split('/')[-1], maps))
		#maps =list(map(lambda x: int(x.split('.')[0][3:]), maps))
		#all_index = list(map(lambda x: cons(x, all_index), maps))
		return 'maps/map' + str(max(all_index)+1) + '.map'


	def saveMatrix(self):

		try:
			filename = 'maps/' + argv[1]
		except IndexError:
			filename = self.getNewFileName()
			pass
		print("Saving map as " + filename)
		file = open(filename, 'w') 

		for line in self.getMatrix():
			file.write(str(line)+'\n')

		file.close()

	def loadMap(self, player_map):

		if player_map.split('.')[-1] != 'map':
			print("Por favor insira um arquivo do tipo .map")
			raise

		f = open(player_map)
		self._matrix = []
		for line in f.readlines():
			self._matrix.append([int(x) for x in line.strip('[]\n').split(',')])


	#TODO: @Otavio -> Tirar as coisas hardcoded
	def _handleMenuClick(self, pos):
		if self.getClickedSquare(pos) == None: #ou seja, se nenhum dos quadrados na tela foi apertado...
			if second(pos) < 372 and second(pos) > 328:
				if first(pos) < 537 and first(pos) > 508:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_PATH)
				elif first(pos) < 617 and first(pos) > 583:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_CENTRALPATH)
				elif first(pos) < 692 and first(pos) > 655:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_SPAWN)
				elif first(pos) < 767 and first(pos) > 727:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_CHANGEDIRECTION)
			elif second(pos) < 458 and second(pos) > 409:
				if first(pos) < 537 and first(pos) > 508:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_DESPAWN)

	def _isValidValue(self,value):
		if value in self.getConf().MAP_NUMBMATRIX_VALUES:
			return True
		return False

	def _updateRectMap(self):
		self.setRectMap(map.Map2(self.getConf().MAP_DIMS, self.getConf().RECT_DIMS_px, self._matrix, 'creation'))
		for i in range(0, self.getRectMap().getDimension()[0]):
			for j in range(0, self.getRectMap().getDimension()[1]):
				self.getRectMap().getMap()[i][j][1].paint(self.getScreen())

	def _updateScreenBuffer(self):
		self._updateRectMap()
		#TODO: More things in here

	def _show(self):
		pygame.display.update()

	def _drawTowerMenu(self):

		towerMenuBackground = pygame.image.load(self.getConf().CREATIONMODE_IMAGE)
		normalPath          = pygame.image.load(self.getConf().REGULAR_PATH_IMAGE)
		centralPath         = pygame.image.load(self.getConf().CENTRAL_PATH_IMAGE)
		spawn               = pygame.image.load(self.getConf().SPAWN_IMAGE)
		changedir           = pygame.image.load(self.getConf().CHANGEDIR_IMAGE)
		despawn             = pygame.image.load(self.getConf().DESPAWN_IMAGE)

		self.getScreen().blit(towerMenuBackground, (480,        0  ))
		self.getScreen().blit(normalPath,          (480 + 35 , 340 ))
		self.getScreen().blit(centralPath,         (480 + 112, 340 ))
		self.getScreen().blit(spawn,               (480 + 187, 340 ))
		self.getScreen().blit(changedir,           (480 + 262, 340 ))
		self.getScreen().blit(despawn,             (480 + 35 , 422 ))

	def start(self):
		pygame.init()
		self._drawTowerMenu()

		isLeftClicked = False
		isRightClicked = False

		while True:
			mousePos = pygame.mouse.get_pos()
			if isLeftClicked:
				self.setMatrixElement(self.getClickedSquare(mousePos),value=self.getCurrentValue())

			elif isRightClicked:
				self.setMatrixElement(self.getClickedSquare(mousePos),value=0)

			event = pygame.event.poll() # same as 'for event in pygame.event.get():' but more elegant

			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				self.saveMatrix()
				sys.exit("Exiting Map Creation !")

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.getConf().LEFT_BUTTON:
				isLeftClicked = True
				self._handleMenuClick(mousePos)

			if event.type == pygame.MOUSEBUTTONUP and event.button == self.getConf().LEFT_BUTTON:
				isLeftClicked = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.getConf().RIGHT_BUTTON:
				isRightClicked = True

			if event.type == pygame.MOUSEBUTTONUP and event.button == self.getConf().RIGHT_BUTTON:
				isRightClicked = False

			self._updateScreenBuffer()
			self._show()


# if __name__ == '__main__':
# 	mapcreator = MapCreator()
# 	mapcreator.setWindowCaption("Map Creation Window !")
# 	mapcreator.start()
	