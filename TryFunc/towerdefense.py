#OK
# coding=utf-8
import pygame

import config
import map as map2
import towers
import traps
import enemies
import rectangle
import waves
from func import *
import menu as MENU
# Classe TowerDefense:
# A classe principal. É aqui que todas as interações do jogador com
# a partida são realizadas. Por exemplo eventos de estar comprando uma torre,
# estar dando upgrade, estar parado, controle de inimigos, controle das torres,
# printar na tela esses devidos objetos, etc...
class TowerDefense:
    I, J = 0, 0
    selectedObject = 0

    def __init__(self, player, player_map):
        self._towerList = []
        self._enemiesList = []
        self._trapList = []
        self._purchasingTower = False
        self._purchasingTrap = False
        self._clickedInTower = False
        self._clickedInTrap = False
        self._loseGame = False
        self._matrix = 0
        self._player_map = None
        self.setPlayerMap(player_map)
        self.inicializeMatrix()
        self._rectMap = map2.Map2(config.Config.MAP_DIMS, config.Config.RECT_DIMS_px, self._matrix)
        self._towerMenuBackground = pygame.image.load(config.Config.MENUTOWERS_IMAGE)
        self._buyingTowers = [towers.ClassicTowerBuyer(config.Config.CLASSICTOWER_BUYER_POS),
                              towers.BlueTowerBuyer(config.Config.BLUETOWER_BUYER_POS),
                              towers.PoisonTowerBuyer(config.Config.POISONTOWER_BUYER_POS),
                              towers.ThunderTowerBuyer(config.Config.THUNDERTOWER_BUYER_POS)]
        self._buyingTraps = [traps.FireTrapBuyer(config.Config.FIRETRAP_BUYER_POS),
                             traps.IceTrapBuyer(config.Config.ICETRAP_BUYER_POS),
                             traps.ThunderTrapBuyer(config.Config.THUNDERTRAP_BUYER_POS),
                             traps.PoisonTrapBuyer(config.Config.POISONTRAP_BUYER_POS)]
        self._damageButton = rectangle.Rectangle(config.Config.UPGRADEBUTTON_DAMAGE_POSITION,
                                                  config.Config.UPGRADEBUTTON_DAMAGE_WIDTH,
                                                  config.Config.UPGRADEBUTTON_DAMAGE_HEIGHT,
                                                  config.Config.UPGRADEBUTTON_DAMAGE_IMAGE)
        self._rangeButton = rectangle.Rectangle(config.Config.UPGRADEBUTTON_RANGE_POSITION,
                                                 config.Config.UPGRADEBUTTON_RANGE_WIDTH,
                                                 config.Config.UPGRADEBUTTON_RANGE_HEIGHT,
                                                 config.Config.UPGRADEBUTTON_RANGE_IMAGE)
        self._effectButton = rectangle.Rectangle(config.Config.UPGRADEBUTTON_EFFECT_POSITION,
                                                 config.Config.UPGRADEBUTTON_EFFECT_WIDTH,
                                                 config.Config.UPGRADEBUTTON_EFFECT_HEIGHT,
                                                 config.Config.UPGRADEBUTTON_EFFECT_IMAGE)
        self._trapButton = rectangle.Rectangle(config.Config.UPGRADEBUTTON_TRAP_POSITION,
                                                 config.Config.UPGRADEBUTTON_TRAP_WIDTH,
                                                 config.Config.UPGRADEBUTTON_TRAP_HEIGHT,
                                                 config.Config.UPGRADEBUTTON_TRAP_IMAGE)
        self._FPS = False
        self._shift = False
        self._insideDamageButton = False
        self._insideRangeButton = False
        self._insideEffectButton = False
        self._insideTrapButton = False
        self._waveOn = False
        self._cash = config.Config.PLAYER_CASH
        self._player = player
        self._timer = 0
        self._endTimer = 5
        self._enemieTimer = 1
        self._beginWaveTimer = 10
        self._enemieFirstDirection = self.getFirstDir()
        self._wave = waves.Waves(self._enemieFirstDirection, self.getEnemySpawnPosition())
        self._spawnEnemieCount = 10

    def getPlayerMap(self):
        return self._player_map

    def setPlayerMap(self, player_map):
        if player_map.split('.')[-1] != 'map':
            print("Por favor insira um arquivo do tipo .map")
            raise
 
        self._player_map = player_map


    def getPlayer(self):
        return self._player

    def addTower(self, newTower):
        self._towerList.append(newTower)

    def getTowers(self):
        return self._towerList
    
    def addTrap(self, newTrap):
        self._trapList.append(newTrap)
        
    def getTraps(self):
        return self._trapList

    def addEnemie(self, newEnemie):
        self._enemiesList.append(newEnemie)

    def squarePosToPixel(self, pos):
        return (config.Config.RECT_DIMX_px * pos[1], config.Config.RECT_DIMY_px * pos[0]) #TODO: @Vinicius, Can you understand why reversed 0 and 1 ?
                                                                                          #TODO: @Otávio, yes. And you could make this way:
                                                                                          #return self._rectMap.getMap()[pos[0]][pos[1]][1].getPosition()
                                                                                          #                                              ^- thats to get the rectangle
                                                                                          #                                                 on the (pos[0], pos[1]) of
                                                                                          #                                                 the map.

    def getEnemySpawnPosition(self):
        try:
            i,j = self.getSpawnPosition()
            return (self.squarePosToPixel([i,j]))
        except IndexError:
            print("Failed to acess matrix line")
            raise

    def getSpawnPosition(self):
        matrix = self._matrix
        return self.getSpawnPositionPerLine(matrix,0)
    def getSpawnPositionPerLine(self,matrix,x):
        if not (is_empty(matrix)):
            line = list(first(matrix))
            
            i,j = self.getSpawnPositionPerColumn(line,x,0)
            i_aux,j_aux = self.getSpawnPositionPerLine(rest(matrix),x+1)
            
            return i*i_aux, j * j_aux
        else:
            return 1,1
    def getSpawnPositionPerColumn(self,column,x,y):
        if is_empty(column):
            return 1,1
        elif first(column) == config.Config.MAP_NUMBMATRIX_SPAWN:
            return x,y
        else:
            return self.getSpawnPositionPerColumn(rest(column),x,y+1)


    def getFirstDir(self):
        spawnPosI, spawnPosJ = self.getSpawnPosition()
        if self._matrix[spawnPosI + 1][spawnPosJ] == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
            return 'D'
        elif self._matrix[spawnPosI - 1][spawnPosJ] == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
            return 'U'
        elif self._matrix[spawnPosI][spawnPosJ + 1] == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
            return 'R'
        elif self._matrix[spawnPosI][spawnPosJ - 1] == config.Config.MAP_NUMBMATRIX_CENTRALPATH:
            return 'L'

    def spawnEnemie(self):
        self._spawnEnemieCount += 1
        enemie = self._wave.getEnemieToSpawn()
        if enemie.getLifesWillTook() == 15:
            self._spawnEnemieCount = 10
        self.addEnemie(enemie)
        self._enemieTimer = 1
        if self._spawnEnemieCount == 10:
            self._beginWaveTimer = 10
            self._waveOn = False

    def delEnemie(self, enemie):
        if self._enemiesList.__contains__(enemie):
            self._enemiesList.remove(enemie)

    def getEnemies(self):
        return self._enemiesList

    def turnOnPurchasingTower(self):
        self._purchasingTower = True

    def turnOffPurchasingTower(self):
        self._purchasingTower = False

    def isPurchasingTower(self):
        return self._purchasingTower

    def turnOnPurchasingTrap(self):
        self._purchasingTrap = True

    def turnOffPurchasingTrap(self):
        self._purchasingTrap = False

    def isPurchasingTrap(self):
        return self._purchasingTrap

    def turnOnClickedInTower(self):
        self._clickedInTower = True

    def turnOffClickedInTower(self):
        self._clickedInTower = False

    def isClickedInTower(self):
        return self._clickedInTower

    def turnOnClickedInTrap(self):
        self._clickedInTrap = True

    def turnOffClickedInTrap(self):
        self._clickedInTrap = False

    def isClickedInTrap(self):
        return self._clickedInTrap

    def towerInsideButton(self, mousePosition):
        if self._insideDamageButton:
            if not self._damageButton.isInside(mousePosition):
                self._damageButton.setImage(config.Config.UPGRADEBUTTON_DAMAGE_IMAGE)
                self._insideDamageButton = False
        elif self._damageButton.isInside(mousePosition):
            self._damageButton.setImage(config.Config.UPGRADEBUTTON_DAMAGE_MOUSEINSIDE_IMAGE)
            self._insideDamageButton = True

        if self._insideRangeButton:
            if not self._rangeButton.isInside(mousePosition):
                self._rangeButton.setImage(config.Config.UPGRADEBUTTON_RANGE_IMAGE)
                self._insideRangeButton = False
        elif self._rangeButton.isInside(mousePosition):
            self._rangeButton.setImage(config.Config.UPGRADEBUTTON_RANGE_MOUSEINSIDE_IMAGE)
            self._insideRangeButton = True

        if self._insideEffectButton:
            if not self._effectButton.isInside(mousePosition):
                self._effectButton.setImage(config.Config.UPGRADEBUTTON_EFFECT_IMAGE)
                self._insideEffectButton = False
        elif self._effectButton.isInside(mousePosition):
            self._effectButton.setImage(config.Config.UPGRADEBUTTON_EFFECT_MOUSEINSIDE_IMAGE)
            self._insideEffectButton = True

    def trapInsideButton(self, mousePosition):
        if self._insideTrapButton:
            if not self._trapButton.isInside(mousePosition):
                self._trapButton.setImage(config.Config.UPGRADEBUTTON_TRAP_IMAGE)
                self._insideTrapButton = False
        elif self._trapButton.isInside(mousePosition):
            self._trapButton.setImage(config.Config.UPGRADEBUTTON_TRAP_MOUSEINSIDE_IMAGE)
            self._insideTrapButton = True

    def executePurchasingTower(self, gameDisplay, mousePosition):
        matrix = self.getRectMap().getMap()
        self.executePurchasingStructPerLine(matrix,gameDisplay,mousePosition,0,self.isInsidePath(self.selectedObject),self.getTowers())
        
    def executePurchasingStructPerLine(self,matrix, gameDisplay,mousePosition,x,activateFunction,listOfStructs):
        if not (is_empty(matrix)):
            line = list(first(matrix))
            self.executePurchasingStructPerColumn(line,gameDisplay,mousePosition,x,0,activateFunction,listOfStructs)
            self.executePurchasingStructPerLine(rest(matrix),gameDisplay,mousePosition,x+1,activateFunction,listOfStructs)
        else:
            pass
    def executePurchasingStructPerColumn(self,line,gameDisplay,mousePosition,x,y,activateFunction,listOfStructs):
        if not (is_empty(line)):
            currentMapRect = self.getRectMap().getMap()[x][y][1]
            if currentMapRect.isInside(mousePosition):
                self.selectedObject.setPosition(currentMapRect.getPosition())
                self.selectedObject.paint(gameDisplay)
                collide = False
                collide = self.collideSomething(listOfStructs,self.selectedObject)
                if not collide:
                    if activateFunction:
                        collide = True
                if collide:
                    self.selectedObject.paintRange(gameDisplay, config.Config.COLLIDE_COLOR)
                else:
                    self.selectedObject.paintRange(gameDisplay, config.Config.NOT_COLLIDE_COLOR)

            self.executePurchasingStructPerColumn(rest(line),gameDisplay,mousePosition,x,y+1,activateFunction,listOfStructs)


    def collideSomething(self,list,something):
        if is_empty(list):
            return False
        if(first(list).collide(something)):
            return True
        else:
            return self.collideSomething(rest(list),something)

    def executePurchasingTrap(self, gameDisplay, mousePosition):
        matrix = self.getRectMap().getMap()
        self.executePurchasingStructPerLine(matrix,gameDisplay,mousePosition,0,not(self.isInsideCentralPath(self.selectedObject)),self.getTraps())
        

    def executeClickedInTower(self, gameDisplay, mousePosition):
        self.selectedObject.paintRange(gameDisplay, config.Config.GREEN)
        self.selectedObject.paintAtributes(gameDisplay)
        self._damageButton.paint(gameDisplay)
        self._rangeButton.paint(gameDisplay)
        self._effectButton.paint(gameDisplay)
        if self._insideDamageButton:
            self.paintMessage(gameDisplay, mousePosition, "Price:%.1f" % self.selectedObject.getUpgradeDamagePrice())
        elif self._insideRangeButton:
            self.paintMessage(gameDisplay, mousePosition, "Price:%.1f" % self.selectedObject.getUpgradeRangePrice())
        elif self._insideEffectButton:
            self.paintMessage(gameDisplay, mousePosition, "Price:%.1f" % self.selectedObject.getUpgradeEffectPrice())
        elif self._insideTrapButton:
            self.paintMessage(gameDisplay, mousePosition, "Price:%.1f" % self.selectedObject.getPriceToUpgrade())

    def executeClickedInTrap(self, gameDisplay, mousePosition):
        self.selectedObject.paintRange(gameDisplay, config.Config.GREEN)
        self.selectedObject.paintAtributes(gameDisplay)
        self._trapButton.paint(gameDisplay)
        if self._insideTrapButton:
            self.paintMessage(gameDisplay, mousePosition, "Price:%.1f" % self.selectedObject.getPriceToUpgrade())

    def getRectMap(self):
        return self._rectMap

    def mousePress(self, mousePosition, gameDisplay):

        if self.isPurchasingTower():
            if self.isInsideRect(mousePosition): #EFEITO COLATERAL - arrumar
                newTower = self.selectedObject
                newTower.setPosition(self.getRectMap().getMap()[self.I][self.J][1].getPosition())
                newTowerColliding = False
                newTowerColliding = self.collideSomething(list(self.getTowers()),newTower)
                if not newTowerColliding:
                    newTowerColliding = self.isInsidePath(newTower)
                if not newTowerColliding:
                    if self._player.haveCashToBuy(newTower.getPrice()):
                        self.addTower(newTower)
                        self._player.purchaseObject(newTower.getPrice())
                        if self.isShiftOn():
                            self.selectedObject = self.selectedObject.newCopy()
                        else:
                            self.turnOffPurchasingTower()
                    else:
                        self.turnOffPurchasingTower()
                        self.paintHaveNoCashMess(gameDisplay, mousePosition)
                        self._timer = 3
        elif self.isPurchasingTrap():
            if self.isInsideRect(mousePosition):
                newTrap = self.selectedObject
                newTrap.setPosition(self.getRectMap().getMap()[self.I][self.J][1].getPosition())
                newTrapColliding = False
                newTrapColliding = self.collideSomething(list(self.getTraps()),newTrap)
                if not newTrapColliding:
                    if self.isInsideCentralPath(newTrap):
                        newTrapColliding = False
                    else:
                        newTrapColliding = True
                if not newTrapColliding:
                    if self._player.haveCashToBuy(newTrap.getPrice()):
                        self.addTrap(newTrap)
                        self._player.purchaseObject(newTrap.getPrice())
                        if self.isShiftOn():
                            self.selectedObject = self.selectedObject.newCopy()
                        else:
                            self.turnOffPurchasingTrap()
                    else:
                        self.turnOffPurchasingTrap()
                        self.paintHaveNoCashMess(gameDisplay, mousePosition)
                        self._timer = 3
        elif self.isInsideTower(mousePosition):
            self.turnOnClickedInTower()
        elif self.isInsideTrap(mousePosition):
            self.turnOnClickedInTrap()
        elif self.isClickedInTower():
            if self._damageButton.isInside(mousePosition):
                if self._player.haveCashToBuy(self.selectedObject.getUpgradeDamagePrice()):
                    self._player.purchaseObject(self.selectedObject.getUpgradeDamagePrice())
                    self.selectedObject.upgradeDamage()
            elif self._rangeButton.isInside(mousePosition):
                if self._player.haveCashToBuy(self.selectedObject.getUpgradeRangePrice()):
                    self._player.purchaseObject(self.selectedObject.getUpgradeRangePrice())
                    self.selectedObject.upgradeRange()
            elif self._effectButton.isInside(mousePosition):
                if self._player.haveCashToBuy(self.selectedObject.getUpgradeEffectPrice()):
                    self._player.purchaseObject(self.selectedObject.getUpgradeEffectPrice())
                    self.selectedObject.upgradeEffect()
            else:
                self.turnOffClickedInTower()
        elif self.isClickedInTrap():
            if self._trapButton.isInside(mousePosition):
                if self._player.haveCashToBuy(self.selectedObject.getPriceToUpgrade()):
                    self._player.purchaseObject(self.selectedObject.getPriceToUpgrade())
                    self.selectedObject.upgrade()
            else:
                self.turnOffClickedInTrap()
        elif self.isInsideBuying(mousePosition): #EFEITO COLATERAL - arrumar
            if self.selectedObject.getFirstClass() == "Tower":
                self.turnOnPurchasingTower()
            elif self.selectedObject.getFirstClass() == "Trap":
                self.turnOnPurchasingTrap()

    def isInsideRect(self, mousePosition):
        matrix = self.getRectMap().getMap()
        return self.isInsideRectPerLine(matrix,mousePosition,0)

    def isInsideRectPerLine(self,matrix,mousePosition,x):
        if not (is_empty(matrix)):
            line = list(first(matrix))
            ans1 = self.isInsideRectPerColumn(line,mousePosition,x,0)
            ans2 = self.isInsideRectPerLine(rest(matrix),mousePosition,x+1)
            return ans2 or ans1
        else:
            return False

    def isInsideRectPerColumn(self,line,mousePosition,x,y):
        if not (is_empty(line)):
            if self.getRectMap().getMap()[x][y][1].isInside(mousePosition):
                self.I = x
                self.J = y
                return True
            return self.isInsideRectPerColumn(rest(line),mousePosition,x,y+1)
        else:
            return False

    def isInsideTowerOrTrap(self, mousePosition):
        return self.isInsideTower(mousePosition) or self.isInsideTrap(mousePosition)

    def isInsideSomething(self,list,something):
        if is_empty(list):
            return False
        if(first(list).isInside(something)):
            self.selectedObject = first(list)
            return True
        else:
            return self.isInsideSomething(rest(list),something)

    def isInsideTower(self, mousePosition):
        if mousePosition[0] > 480:
            return False
        else:
            return self.isInsideSomething(list(self.getTowers()),mousePosition)
            
    def isInsideTrap(self, mousePosition):
        if mousePosition[0] > 480:
            return False
        else:
            return self.isInsideSomething(list(self.getTraps()),mousePosition)

    def isInsideBuying(self,mousePosition):
        return self.isInsideBuyingAux(mousePosition,0)
    def isInsideBuyingAux(self, mousePosition,i):
        if mousePosition[0] < 480:
            return False
        else:
            if (i < 4):
                if self._buyingTowers[i].isInside(mousePosition):
                    towerClass = self._buyingTowers[i].getClass()
                    if towerClass == "ClassicTowerBuyer":
                        self.selectedObject = towers.ClassicTower((0, 0))
                    elif towerClass == "BlueTowerBuyer":
                        self.selectedObject = towers.BlueTower((0, 0))
                    elif towerClass == "PoisonTowerBuyer":
                        self.selectedObject = towers.PoisonTower((0, 0))
                    elif towerClass == "ThunderTowerBuyer":
                        self.selectedObject = towers.ThunderTower((0, 0))
                    return True

                if self._buyingTraps[i].isInside(mousePosition):
                    trapClass = self._buyingTraps[i].getClass()
                    #print(trapClass)
                    if trapClass == "FireTrapBuyer":
                        self.selectedObject = traps.FireTrap((0, 0))
                    elif trapClass == "IceTrapBuyer":
                        self.selectedObject = traps.IceTrap((0, 0))
                    elif trapClass == "ThunderTrapBuyer":
                        #print("ENTREI")
                        self.selectedObject = traps.ThunderTrap((0, 0))
                    elif trapClass == "PoisonTrapBuyer":
                        self.selectedObject = traps.PoisonTrap((0, 0))
                    return True
                return self.isInsideBuyingAux(mousePosition,i+1)
            else:
                return False
        return False

    def isInsidePath(self, object):
        rectMap = self.getRectMap().getMap()
        return self.isInsidePathPerLine(rectMap,object,0)
    
    def isInsidePathPerLine(self,matrix,object,x):
        if not (is_empty(matrix)):
            line = list(first(matrix))
            ans1 = self.isInsidePathPerColumn(line,object,x,0)
            ans2 = self.isInsidePathPerLine(rest(matrix),object,x+1)
            return ans2 or ans1
        else:
            return False

    def isInsidePathPerColumn(self,line,object,x,y):
        if not (is_empty(line)):
            if first(first(line)) != 0:
                if first(line)[1].collide(object):
                    return True
            return self.isInsidePathPerColumn(rest(line),object,x,y+1)
        else:
            return False
    
    def isInsideCentralPath(self, object):
        rectMap = self.getRectMap().getMap()
        return self.isInsideCentralPathPerLine(rectMap,object,0)

    def isInsideCentralPathPerLine(self,matrix,object,x):
        if not (is_empty(matrix)):
            line = list(first(matrix))
            ans1 = self.isInsideCentralPathPerColumn(line,object,x,0)
            ans2 = self.isInsideCentralPathPerLine(rest(matrix),object,x+1)
            return ans2 or ans1
        else:
            return False

    def isInsideCentralPathPerColumn(self,line,object,x,y):
        if not (is_empty(line)):
            rectID = first(line)[0]
            if rectID == config.Config.MAP_NUMBMATRIX_CENTRALPATH\
                    or rectID == config.Config.MAP_NUMBMATRIX_CHANGEDIRECTION:
                if first(line)[1].collide(object):
                    return True
            return self.isInsideCentralPathPerColumn(rest(line),object,x,y+1)
        else:
            return False

    def paintAllStuff(self, gameDisplay, mousePosition):
        if not self._loseGame:

            self.paintRectMap(gameDisplay)
            self.paintTowers(gameDisplay)
            self.paintTraps(gameDisplay)
            if self.isPurchasingTower():
                self.executePurchasingTower(gameDisplay, mousePosition)
            elif self.isPurchasingTrap():
                self.executePurchasingTrap(gameDisplay, mousePosition)
            self.paintTowerMenuBackground(gameDisplay)
            if self.isClickedInTower():
                self.executeClickedInTower(gameDisplay, mousePosition)
            if self.isClickedInTrap():
                self.executeClickedInTrap(gameDisplay, mousePosition)
            self.paintBuyingTowers(gameDisplay)
            self.paintBuyingTraps(gameDisplay)
            self.paintCash(gameDisplay)
            self.paintLife(gameDisplay)
            self.paintName(gameDisplay)
            self.paintWave(gameDisplay)
            if self.getTimer() > 0:
                self.paintHaveNoCashMess(gameDisplay, mousePosition)
            if self._enemieTimer == 0:
                self.spawnEnemie()
            self.paintShots(gameDisplay)
            self.paintEnemies(gameDisplay)


    def paintTowers(self, gameDisplay):
        list(map(lambda towerAux: towerAux.paint(gameDisplay), self.getTowers()))        
        

    def paintTraps(self, gameDisplay):
        list(map(lambda trapAux: trapAux.paint(gameDisplay), self.getTraps()))   

    def paintEnemies(self, gameDisplay):
        list(map(lambda enemiesAux: enemiesAux.move(self._matrix, self._rectMap, self,gameDisplay), self.getEnemies()))
        list(map(lambda enemiesAux: enemiesAux.paint(gameDisplay), self.getEnemies()))   
        
    def paintShots(self, gameDisplay):
        list(map(lambda towerAux: towerAux.shotEnemies(self.getEnemies()), self.getTowers()))
        list(map(lambda towerAux: towerAux.moveShots(gameDisplay, self.getEnemies(), self), self.getTowers()))
        
        list(map(lambda trapAux: trapAux.shotEnemies(self.getEnemies(), self), self.getTraps()))
        

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





    def paintTowerMenuBackground(self, gameDisplay):
        gameDisplay.blit(self._towerMenuBackground, (480, 0))

    def paintBuyingTowers(self, gameDisplay):
        list(map(lambda buyingTower: buyingTower.paint(gameDisplay), self._buyingTowers))     

    def paintBuyingTraps(self, gameDisplay):
        list(map(lambda buyingTrap: buyingTrap.paint(gameDisplay), self._buyingTraps))     
    
    def paintCash(self, gameDisplay):
        font = pygame.font.SysFont(None, 25)
        text = font.render("CASH: %d" % self._player.getCash(), True, (0, 0, 0))
        gameDisplay.blit(text, (495, 425))

    def paintHaveNoCashMess(self, gameDisplay, mousePosition):
        font = pygame.font.SysFont(None, 30, True, False)
        text = font.render("Not enougth cash!", True, (255, 255, 0))
        gameDisplay.blit(text, mousePosition)

    def paintMessage(self, gameDisplay, mousePosition, message):
        font = pygame.font.SysFont(None, 30, True, False)
        text = font.render(message, True, ((0, 0, 255)))
        gameDisplay.blit(text, (mousePosition[0]-50, mousePosition[1]-20))

    def paintLife(self, gameDisplay):
        font = pygame.font.SysFont(None, 25)
        text = font.render("LIFE: %d" % self._player.getLife(), True, (0, 0, 0))
        gameDisplay.blit(text, (585, 425))

    def paintName(self, gameDisplay):
        font = pygame.font.SysFont(None, 30)
        text = font.render("%s" % self._player.getName(), True, (0, 0, 0))
        gameDisplay.blit(text, (495, 402))

    def paintWave(self, gameDisplay):
        font = pygame.font.SysFont(None, 30)
        text = font.render("Wave:%d" % self._wave.getWaveNumber(), True, (0, 0, 0))
        gameDisplay.blit(text, (495, 445))

    def turnOnShift(self):
        self._shift = True

    def turnOffShift(self):
        self._shift = False

    def isShiftOn(self):
        return self._shift

    def paintLoseGameMessage(self, gameDisplay):
        font = pygame.font.SysFont(None, 100, True, False)
        text = font.render("YOU LOSE!", True, ((0, 0, 0)))
        gameDisplay.blit(text, (100, 100))
        text = font.render("WAVE:%d" % self._wave.getWaveNumber(), True, ((0, 0, 0)))
        gameDisplay.blit(text, (100, 150))


    def decTimer(self, gameDisplay):
        if not self._loseGame:
            self._timer -= 1

            if self._beginWaveTimer == 0 and not self._waveOn:
                self._wave.incWaveNumber()
                self._waveOn = True
            else:
                if not self._enemiesList and (self._spawnEnemieCount == 10 or self._spawnEnemieCount == 0):
                    self._waveOn = False
                    self._spawnEnemieCount = 0
                    self._beginWaveTimer -= 1

            if self._waveOn:
                self._enemieTimer -= 1

            list(map(lambda towerAux: towerAux.decReloadTime(), self.getTowers()))     
            list(map(lambda trapAux: trapAux.decReloadTime(), self.getTraps()))
            list(map(lambda enemieAux: enemieAux.executeEffects(self), self.getEnemies()))
        else:
            self._endTimer -= 1
            self.paintLoseGameMessage(gameDisplay)
            if self._endTimer == 0:
                pygame.quit()
                menu = MENU.Menu()
                menu.start()
    def getTimer(self):
        return self._timer

    def inicializeMatrix(self):
        f = open(self.getPlayerMap())
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
        
    def playerLose(self, gameDisplay):
        self._loseGame = True
