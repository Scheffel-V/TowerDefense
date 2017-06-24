# coding=utf-8
import rectangle
import config
from func import *
# Classe Map:
# Define o mapa do jogo (os quadradinhos verdes).
# Varia em função do número de quadradinhos na altura e largura,
# e da altura e da larguda dos quadradinhos em pixels.
class Map2:
    def __init__(self, mapDimension, rectDimensionPx, matrix, mode=None):
        self._dimension = mapDimension
        self._rectWidth = rectDimensionPx[0]
        self._rectHeight = rectDimensionPx[1]
        self._map2 = []
        self.inicializeMap(matrix, mode)

    def getDimension(self):
        return self._dimension

    def setDimension(self, dimension):
        self._dimension = dimension

    def getRectWidth(self):
        return self._rectWidth

    def getRectHeight(self):
        return self._rectHeight

    def getMap(self):
        return self._map2

    def inicializeMap(self, matrix, mode=None):
        if mode == 'creation':
            grassImg = config.Config.GRASS_IMAGE
            regPathImg = config.Config.REGULAR_PATH_IMAGE
            spawnImg = config.Config.SPAWN_IMAGE
            desPawnImg = config.Config.DESPAWN_IMAGE
            centralPathImg = config.Config.CENTRAL_PATH_IMAGE
            changeDirImg = config.Config.CHANGEDIR_IMAGE
        else:
            grassImg = config.Config.GRASS_IMAGE
            regPathImg = config.Config.REGULAR_PATH_IMAGE
            spawnImg = config.Config.REGULAR_PATH_IMAGE
            desPawnImg = config.Config.REGULAR_PATH_IMAGE
            centralPathImg = config.Config.REGULAR_PATH_IMAGE
            changeDirImg = config.Config.REGULAR_PATH_IMAGE

            imageList =[grassImg,regPathImg,spawnImg,desPawnImg,centralPathImg,changeDirImg] # Cause the subfunctions couldn't see these atributes
                                                                                             # it was needed pass them to the subfuncionts
        self._map2 = createMap(matrix,self.getRectWidth(),self.getRectHeight(),imageList)
       


def transformLineInMap(line_matrix, x, y,widht,height,imageList):
    if(is_empty (line_matrix)):
        return empty
    if first(line_matrix) == config.Config.MAP_NUMBMATRIX_GRASS:
        return cons((0, rectangle.Rectangle((x, y), widht, height, imageList[0])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))
    elif first(line_matrix) == config.Config.MAP_NUMBMATRIX_PATH:
         return cons((1, rectangle.Rectangle((x, y), widht, height, imageList[1])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))

    elif first(line_matrix) == config.Config.MAP_NUMBMATRIX_SPAWN:
         return cons((2, rectangle.Rectangle((x, y), widht, height, imageList[2])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))

    elif first(line_matrix) == config.Config.MAP_NUMBMATRIX_DESPAWN:
         return cons((3, rectangle.Rectangle((x, y), widht, height, imageList[3])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))

    elif first(line_matrix) == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
         return cons((4, rectangle.Rectangle((x, y), widht, height, imageList[4])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))

    elif first(line_matrix) == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
         return cons((5, rectangle.Rectangle((x, y), widht, height, imageList[5])), transformLineInMap(rest(line_matrix), x + widht, y,widht,height,imageList))


def createMap(matrix,widht,height,imageList):
    return transformMatrixInMap(matrix,0,widht,height,imageList)

def transformMatrixInMap(matrix ,y , widht, height, imageList):
    if is_empty(matrix):
        return empty
    else:
        return cons( transformLineInMap(first(matrix), 0, y,widht,height,imageList), transformMatrixInMap(rest(matrix),y + height ,widht,height,imageList)) 

