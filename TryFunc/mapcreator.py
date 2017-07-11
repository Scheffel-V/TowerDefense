import config
import pygame
import sys
import map as map2
import rectangle
from sys import argv
import os
from func import *

class MapCreator:
	def __init__(self, filemap=None):
		self._conf = config.Config()
		self._screen = pygame.display.set_mode(self._conf.DISPLAY_SIZE)
		self._matrix = []
		self.inicializeMatrix2PerLines(self._conf.MAP_DIMX, 0, self._conf.MAP_DIMY)
		self._rectMap = map2.Map2(self._conf.MAP_DIMS, self._conf.RECT_DIMS_px, self._matrix, 'creation')
		self._currentValue = 1
		self._filemap = filemap
	
	def inicializeMatrix2PerLines(self,max_X,x,max_Y):
		if not (x == max_X):
			self._matrix.append(self.inicializeMatrix2PerColumns(0,max_Y))
			self.inicializeMatrix2PerLines(max_X,x+1,max_Y)
	
	def inicializeMatrix2PerColumns(self,y,max_Y):
		if not (y == max_Y):
			return cons(0, self.inicializeMatrix2PerColumns(y+1,max_Y))
		else:
			return empty

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
				x = coords[1]
				y = coords[0]
				self._matrix[x][y] = value
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
		xPos = int(pxPosition[0]/self.getConf().RECT_DIMX_px)
		yPos = int(pxPosition[1]/self.getConf().RECT_DIMX_px)
		if xPos < self.getConf().MAP_DIMX and yPos < self.getConf().MAP_DIMY:	
			return (xPos, yPos)
		pass

	def getNewFileName(self):

		if self._filemap != None:
			return self._filemap

		maps = os.listdir("maps")

		if maps == []:
			return 'maps/map1.map'

		all_index = self.getNewFileName2(maps)

		return 'maps/map' + str(max(all_index)+1) + '.map'

	def getNewFileName2(self,maps):
		if(not(is_empty(maps))):
			mapa = first(maps)
			name = mapa.split('/')[-1]
			index = int(name.split('.')[0][3:])
			return cons(index,self.getNewFileName2(rest(maps)))
		else:
			return empty
	def saveMatrix(self):

		try:
			filename = 'maps/' + argv[1]
		except IndexError:
			filename = self.getNewFileName()
			pass
		print("Saving map as " + filename)
		file = open(filename, 'w') 

		list(map(lambda line: file.write(str(line)+'\n'),list(self.getMatrix())))
		file.close()

	def loadMap(self, player_map):

		if player_map.split('.')[-1] != 'map':
			print("Por favor insira um arquivo do tipo .map")
			raise

		f = open(player_map)
		self._matrix = []
		file_lines = f.readlines()
		self.inicializeMatrixPerLines(file_lines)	
	def inicializeMatrixPerLines(self,matrix):
		if not (is_empty(matrix)):
			self._matrix.append(self.inicializeMatrixPerColumns(first(matrix).strip('[]\n').split(',')))
			self.inicializeMatrixPerLines(rest(matrix))
	def inicializeMatrixPerColumns(self,line):
		if not (is_empty(line)):
			return cons(int(first(line)), self.inicializeMatrixPerColumns(rest(line)))
		else:
			return empty
        

	#TODO: @Otavio -> Tirar as coisas hardcoded
	def _handleMenuClick(self, pos):
		if self.getClickedSquare(pos) == None: #ou seja, se nenhum dos quadrados na tela foi apertado...
			if pos[1] < 372 and pos[1] > 328:
				if pos[0] < 537 and pos[0] > 508:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_PATH)
				elif pos[0] < 617 and pos[0] > 583:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_CENTRALPATH)
				elif pos[0] < 692 and pos[0] > 655:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_SPAWN)
				elif pos[0] < 767 and pos[0] > 727:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_CHANGEDIRECTION)
			elif pos[1] < 458 and pos[1] > 409:
				if pos[0] < 537 and pos[0] > 508:
					self.setCurrentValue(self.getConf().MAP_NUMBMATRIX_DESPAWN)

	def _isValidValue(self,value):
		if value in self.getConf().MAP_NUMBMATRIX_VALUES:
			return True
		return False

	def _updateRectMap(self):
		self.setRectMap(map2.Map2(self.getConf().MAP_DIMS, self.getConf().RECT_DIMS_px, self._matrix, 'creation'))
		self.paintRectMap(self.getScreen())

	def paintRectMap(self, gameDisplay):
		matrix = self.getRectMap().getMap()
		self.paintRectMapPerLine(matrix,gameDisplay)


	def paintRectMapPerLine(self,matrix,gameDisplay):
		if not (is_empty(matrix)):
			line = list(first(matrix))
			self.paintRectMapPerColumn(line,gameDisplay)
			self.paintRectMapPerLine(rest(matrix),gameDisplay)
		else:
			pass

	def paintRectMapPerColumn(self,line,gameDisplay):
		if not (is_empty(line)):
			second(first(line)).paint(gameDisplay)
			self.paintRectMapPerColumn(rest(line),gameDisplay)
	





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

		self.goFunctional()
	def goFunctional(self):
		
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
		self.goFunctional()


# if __name__ == '__main__':
# 	mapcreator = MapCreator()
# 	mapcreator.setWindowCaption("Map Creation Window !")
# 	mapcreator.start()
	
