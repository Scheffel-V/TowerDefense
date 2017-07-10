#OK
import rectangle
import config
from func import *

class Enemie(rectangle.Rectangle):
    def __init__(self, position, width, height, image, health, speed, earnCash, lifesWillTook, firstDir, multiplier):
        super(Enemie, self).__init__(position, width, height, image)
        self._health = health
        self._speed = speed
        self._originalSpeed = speed
        self._earnCash = earnCash
        self._lifesWillTook = lifesWillTook
        self._specialEffects = []
        self._upFlag = False
        self._downFlag = False
        self._rightFlag = False
        self._leftFlag = False
        self._setInitialFlags(firstDir)

    def getHealth(self):
        return self._health

    def setHealth(self, health):
        self._health = health

    def getSpeed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed = speed

    def refreshSpeed(self):
        self._speed = self._originalSpeed

    def getEarnCash(self):
        return self._earnCash

    def setEarnCash(self, earnCash):
        self._earnCash = earnCash

    def getLifesWillTook(self):
        return self._lifesWillTook

    def setLifesWillTook(self, lifesWillTook):
        self._lifesWillTook = lifesWillTook

    def hit(self, damage, towerDefense):
        if damage >= self._health:
            towerDefense.getPlayer().addCash(self._earnCash)
            self.despawn(towerDefense)
            self._health = self._health - damage
        else:
            self._health = self._health - damage

    def slow(self, slow):
        if self._speed != 0:
            self._speed -= slow

    def stun(self):
        self._speed = 0

    def setBurn(self, burnEffect):
        if not self.isBurned():
            self._specialEffects.append(burnEffect)


    def setIce(self, iceEffect):
        if not self.isIced():
            self._specialEffects.append(iceEffect)
            self.slow(iceEffect.getSlow())


    def setPoison(self, poisonEffect):
        if not self.isPoisoned():
            self._specialEffects.append(poisonEffect)


    def setThunder(self, thunderEffect):
        if not self.isStunned():
            self._specialEffects.append(thunderEffect)
            self.stun()

    def isIced(self):
        frozzen = self.activator("Ice")
        list_of_elements = list(self._specialEffects)
        return self.isSomething(list_of_elements,frozzen)

    def isBurned(self):
        burned = self.activator("Burn")
        list_of_elements = list(self._specialEffects)
        return self.isSomething(list_of_elements,burned)

    def isPoisoned(self):
        poisoned = self.activator("Poison")
        list_of_elements = list(self._specialEffects)
        return self.isSomething(list_of_elements,poisoned)

    def isStunned(self):
        stunned = self.activator("Thunder")
        list_of_elements = list(self._specialEffects)
        return self.isSomething(list_of_elements,stunned)
    
    def activator(self, name):
        def stringComp(element): 
            return element.getName() == name
        return stringComp

    def isSomething(self,list,func_activator):
        if is_empty(list):
            return False
        if func_activator(first(list)):
            return True
        else:
            return self.isSomething(rest(list), func_activator)

    def setEffect(self, effect):
        if self.activator("Ice")(effect):
            self.setIce(effect)
        elif self.activator("Burn")(effect):
            self.setBurn(effect)
        elif self.activator("Poison")(effect):
            self.setPoison(effect)
        elif self.activator("Thunder")(effect):
            self.setThunder(effect)

    def delEffect(self, effect):
        if self.activator("Ice")(effect):
            self.refreshSpeed()
        elif self.activator("Thunder")(effect):
            self.refreshSpeed()
        if self._specialEffects.__contains__(effect):
            self._specialEffects.remove(effect)

    def executeEffects(self, towerDefense):
        list_of_effects = list(self._specialEffects)
        self.executeEffects2(list_of_effects,towerDefense)
    
    def executeEffects2(self,list,towerDefense):
        if not(is_empty(list)):
            if self.activator("Burn")(first(list)) :
                self.hit(first(list).getDamagePerSecond(), towerDefense)
            elif self.activator("Poison")(first(list)):
                self.hit(first(list).getDamagePerSecond(), towerDefense)
            first(list).decDuration()
            self.executeEffects2( rest(list),towerDefense)

    def despawn(self, towerDefense):
        towerDefense.delEnemie(self)

    def insideRectPosition(self, rectMap):
        actualMap = rectMap.getMap()
        
        index = self.insideRectPositionPerLine(actualMap,0)
        return first(index),second(index)
    
    def insideRectPositionPerLine(self,actualMap,x):
        if not(is_empty(actualMap)):
            column = first(actualMap)
            index = self.insideRectPositionPerColumn(column,x,0)
            aux_index = self.insideRectPositionPerLine(rest(actualMap), x+1)
            
            return [first(index)*first(aux_index), second(index)*second(aux_index)]
        else:
            return [1,1]
    
    def insideRectPositionPerColumn(self,column,x,y):
        if is_empty(column):
            return [1,1]
        elif second(first(column)).isInside(self.getCenter()):
            return [x,y]
        else:
            return self.insideRectPositionPerColumn(rest(column),x,y+1)

    def _setInitialFlags(self, firstDir):
        if first(firstDir) == "U":
            self._upFlag = True
        elif first(firstDir) == "D":
            self._downFlag = True
        elif first(firstDir) == "R":
            self._rightFlag = True
        elif first(firstDir) == "L":
            self._leftFlag = True

    def _setFlags(self, up, down, left, right):
        self._upFlag = up
        self._downFlag = down
        self._leftFlag = left
        self._rightFlag = right

    # Logica pros bichinhos andarem em qualquer mapa criado desde que ele
    # nao volte pra esquerda nenhuma vez. Ainda vou acabar a ultima parte
    # pro mapa poder voltar ( mapas em espiral )
    def move(self, mapMatrix, rectMap, towerDefense):

        rectPosition = self.insideRectPosition(rectMap)
        rectPositionI = first(rectPosition)
        rectPositionJ = second(rectPosition)
        mapMatrixNextColumn = mapMatrix[rectPositionI][rectPositionJ + 1]
        mapMatrixPrevColumn = mapMatrix[rectPositionI][rectPositionJ - 1]
        mapMatrixNextRow = mapMatrix[rectPositionI + 1][rectPositionJ]
        mapMatrixPrevRow = mapMatrix[rectPositionI - 1][rectPositionJ]
        mapMatrixPosition = mapMatrix[rectPositionI][rectPositionJ]

        if mapMatrixPosition == config.Config.MAP_NUMBMATRIX_DESPAWN:
            towerDefense.getPlayer().decLife()
            self.despawn(towerDefense)
        else:
            if self._rightFlag:
                self.executeRightFlag(mapMatrixNextColumn, mapMatrixPosition, mapMatrixPrevRow, mapMatrixNextRow)

            elif self._leftFlag:
                self.executeLeftFlag(mapMatrixPrevColumn, mapMatrixPosition, mapMatrixPrevRow, mapMatrixNextRow)

            elif self._downFlag:
                self.executeDownFlag(mapMatrixPrevColumn, mapMatrixPosition, mapMatrixNextColumn, mapMatrixNextRow)

            elif self._upFlag:
                self.executeUpFlag(mapMatrixPrevColumn, mapMatrixPosition, mapMatrixNextColumn, mapMatrixPrevRow)

    def executeRightFlag(self, mapMatrixNextColumn, mapMatrixPosition, mapMatrixPrevRow, mapMatrixNextRow):
        if self.isContinueMoving(mapMatrixNextColumn, mapMatrixNextColumn, mapMatrixNextColumn):
            self.moveRight()
        elif mapMatrixPosition == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
            if mapMatrixPrevRow == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(True, False, False, False)
            elif mapMatrixNextRow == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, True, False, False)

    def executeLeftFlag(self, mapMatrixPrevColumn, mapMatrixPosition, mapMatrixPrevRow, mapMatrixNextRow):
        if self.isContinueMoving(mapMatrixPrevColumn, mapMatrixPrevColumn, mapMatrixPrevColumn):
            self.moveLeft()
        elif mapMatrixPosition == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
            if mapMatrixPrevRow == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(True, False, False, False)
            elif mapMatrixNextRow == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, True, False, False)

    def executeDownFlag(self, mapMatrixPrevColumn, mapMatrixPosition, mapMatrixNextColumn, mapMatrixNextRow):
        if self.isContinueMoving(mapMatrixNextRow, mapMatrixNextRow, mapMatrixNextRow):
            self.moveDown()
        elif mapMatrixPosition == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
            if mapMatrixNextColumn == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, False, False, True)
            elif mapMatrixPrevColumn == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, False, True, False)

    def executeUpFlag(self, mapMatrixPrevColumn, mapMatrixPosition, mapMatrixNextColumn, mapMatrixPrevRow):
        if self.isContinueMoving(mapMatrixPrevRow, mapMatrixPrevRow, mapMatrixPrevColumn):
            self.moveUp()
        elif mapMatrixPosition == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
            if mapMatrixNextColumn == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, False, False, True)
            elif mapMatrixPrevColumn == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
                self._setFlags(False, False, True, False)

    def isContinueMoving(self, firstCondition, secondCondition, thirdCondition):
        return firstCondition == config.Config.MAP_NUMBMATRIX_CENTRALPATH \
               or secondCondition == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION \
               or thirdCondition == config.Config.MAP_NUMBMATRIX_DESPAWN

    def moveRight(self):
        positionX = first(self._position)
        positionY = second(self._position)
        positionX += self._speed
        self.setPosition((positionX, positionY))

    def moveLeft(self):
        positionX = first(self._position)
        positionY = second(self._position)
        positionX -= self._speed
        self.setPosition((positionX, positionY))

    def moveDown(self):
        positionX = first(self._position)
        positionY = second(self._position)
        positionY += self._speed
        self.setPosition((positionX, positionY))

    def moveUp(self):
        positionX = first(self._position)
        positionY = second(self._position)
        positionY -= self._speed
        self.setPosition((positionX, positionY))
