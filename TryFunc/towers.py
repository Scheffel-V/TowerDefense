# coding=utf-8
import config
import rectangle
import pygame
import abc
import shot
import effects


# Classe Tower estende de Rectangle:
# Essa classe define as Torres do jogo, tanto as que serão postas no mapa,
# como as que ficam na aba de compras.
class Tower(rectangle.Rectangle, metaclass=abc.ABCMeta):
    _mouseCircleSurface = pygame.Surface(config.Config.MOUSE_CIRCLE_SURFACE)

    def __init__(self, position, width, height, image, range, damage, fireRate, price):
        super(Tower, self).__init__(position, width, height, image)
        self._range = range
        self._rangeLevel = 1
        self._upgradeRangePrice = 40
        self._damage = damage
        self._damageLevel = 1
        self._upgradeDamagePrice = 50
        self._fireRate = fireRate
        self._effectLevel = 1
        self._upgradeEffectPrice = 40
        self._reloadTime = 1 / fireRate
        self._price = price
        self._shotList = []

    def getFirstClass(self):
        return "Tower"

    @abc.abstractmethod
    def getClass(self):
        return

    @abc.abstractmethod
    def newCopy(self):
        return

    def getRange(self):
        return self._range

    def setRange(self, range):
        self._range = range

    def getDamage(self):
        return self._damage

    def setDamage(self, damage):
        self._damage = damage

    def getFireRate(self):
        return self._fireRate

    def setFireRate(self, fireRate):
        self._fireRate = fireRate

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def getShotList(self):
        return self._shotList

    def getUpgradeDamagePrice(self):
        return self._upgradeDamagePrice

    def upgradeDamage(self):
        self._damageLevel += 1
        self._damage = config.Config.CLASSICTOWER_DAMAGE * 1.3 ** (self._damageLevel - 1)
        self._upgradeDamagePrice = self._upgradeDamagePrice + 10 * self._damageLevel ** 1.5

    def getUpgradeRangePrice(self):
        return self._upgradeRangePrice

    def upgradeRange(self):
        self._rangeLevel += 1
        self._range += 10
        self._upgradeRangePrice = self._upgradeRangePrice + 10 * self._rangeLevel ** 1.5

    def getUpgradeEffectPrice(self):
        return self._upgradeEffectPrice

    def upgradeEffect(self):
        self._effectLevel += 1
        self._upgradeEffectPrice = self._upgradeEffectPrice + 10 * self._effectLevel ** 1.5

    def doublePrice(self):
        self._price *= 2

    def decReloadTime(self):
        self._reloadTime -= 1.0

    def resetReloadTime(self):
        self._reloadTime = 1.0 / self._fireRate
        #print self._reloadTime

    def shotEnemies(self, enemies):
        if self._reloadTime <= 0:
            for enemieAux in enemies:
                if self.isInsideRange(enemieAux.getPosition()):
                    self.shot(enemieAux)
                    self.resetReloadTime()
                    break

    @abc.abstractmethod
    def shot(self, enemie):
        pass

    def moveShots(self, gameDisplay, enemieList, towerDefense):
        for shotAux in self._shotList:
            shotAux.move()
            for enemieAux in enemieList:
                if enemieAux.collide(shotAux):
                    if shotAux.getEffect() != "NULL":
                        enemieAux.setEffect(shotAux.getEffect())
                    enemieAux.hit(shotAux.getDamage(), towerDefense)
                    shotAux.destroy(self)
                    break
        self.paintShots(gameDisplay)

    def delShot(self, shot):
        try:
            self._shotList.remove(shot) #Dar uma olhada aqui
        except:
            pass

    def paintShots(self, gameDisplay):
        for shotAux in self._shotList:
            shotAux.paint(gameDisplay)

    def isInsideRange(self, position):
        center = self.getCenter()
        if center[0] - self._range <= position[0] < center[0] + self._range:
            if center[1] - self._range <= position[1] < center[1] + self._range:
                return True
        return False

    def paintRange(self, gameDisplay, color):
        self._mouseCircleSurface.fill(config.Config.CK)
        self._mouseCircleSurface.set_colorkey(config.Config.CK)
        pygame.draw.circle(self._mouseCircleSurface, color, self.getCenter(), self._range, self._range)
        self._mouseCircleSurface.set_alpha(150)
        gameDisplay.blit(self._mouseCircleSurface, (0, 0))

    def paintAtributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render("Damage:%d" % self._damage, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 177))
        text = font.render("Range:%d" % self._range, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 197))
        text = font.render("Fire Rate:%.2f" % self._fireRate, True, (0, 0, 0))
        gameDisplay.blit(text, (497, 217))


class ClassicTower(Tower):
    def __init__(self, position):
        super(ClassicTower, self).__init__(position,
                                           config.Config.CLASSICTOWER_WIDTH,
                                           config.Config.CLASSICTOWER_HEIGHT,
                                           config.Config.CLASSICTOWER_IMAGE_small,
                                           config.Config.CLASSICTOWER_RANGE,
                                           config.Config.CLASSICTOWER_DAMAGE,
                                           config.Config.CLASSICTOWER_FIRERATE,
                                           config.Config.CLASSICTOWER_PRICE)

    def getClass(self):
        return "ClassicTower"

    def newCopy(self):
        return ClassicTower(self._position)

    def shot(self, enemie):
        self._shotList.append(shot.Shot(self.getPosition(), 8, 8, "imagens/shot.png", 0.5, enemie.getPosition(), self.getDamage(), "NULL"))


class ClassicTowerBuyer(Tower):
    def __init__(self, position):
        super(ClassicTowerBuyer, self).__init__(position,
                                                config.Config.CLASSICTOWER_WIDTH * 2,
                                                config.Config.CLASSICTOWER_HEIGHT * 2,
                                                config.Config.CLASSICTOWER_IMAGE_big,
                                                config.Config.CLASSICTOWER_RANGE,
                                                config.Config.CLASSICTOWER_DAMAGE,
                                                config.Config.CLASSICTOWER_FIRERATE,
                                                config.Config.CLASSICTOWER_PRICE)

    def getClass(self):
        return "ClassicTowerBuyer"

    def newCopy(self):
        return ClassicTowerBuyer(self._position)

    def shot(self, enemie):
        pass


class BlueTower(Tower):
    def __init__(self, position):
        super(BlueTower, self).__init__(position,
                                        config.Config.BLUETOWER_WIDTH,
                                        config.Config.BLUETOWER_HEIGHT,
                                        config.Config.BLUETOWER_IMAGE_small,
                                        config.Config.BLUETOWER_RANGE,
                                        config.Config.BLUETOWER_DAMAGE,
                                        config.Config.BLUETOWER_FIRERATE,
                                        config.Config.BLUETOWER_PRICE)

    def getClass(self):
        return "BlueTower"

    def newCopy(self):
        return BlueTower(self._position)

    def shot(self, enemie):
        self._shotList.append(shot.IceShot(self.getPosition(), self.getDamage(), enemie.getPosition(), effects.IceEffect(enemie, self._effectLevel)))


class BlueTowerBuyer(Tower):
    def __init__(self, position):
        super(BlueTowerBuyer, self).__init__(position,
                                             config.Config.BLUETOWER_WIDTH * 2,
                                             config.Config.BLUETOWER_HEIGHT * 2,
                                             config.Config.BLUETOWER_IMAGE_big,
                                             config.Config.BLUETOWER_RANGE,
                                             config.Config.BLUETOWER_DAMAGE,
                                             config.Config.BLUETOWER_FIRERATE,
                                             config.Config.BLUETOWER_PRICE)

    def getClass(self):
        return "BlueTowerBuyer"

    def newCopy(self):
        return BlueTowerBuyer(self._position)

    def shot(self, enemie):
        pass

class PoisonTower(Tower):
    def __init__(self, position):
        super(PoisonTower, self).__init__(position,
                                        config.Config.POISONTOWER_WIDTH,
                                        config.Config.POISONTOWER_HEIGHT,
                                        config.Config.POISONTOWER_IMAGE_small,
                                        config.Config.POISONTOWER_RANGE,
                                        config.Config.POISONTOWER_DAMAGE,
                                        config.Config.POISONTOWER_FIRERATE,
                                        config.Config.POISONTOWER_PRICE)

    def getClass(self):
        return "PoisonTower"

    def newCopy(self):
        return PoisonTower(self._position)

    def shot(self, enemie):
        self._shotList.append(shot.PoisonShot(self.getPosition(), self.getDamage(), enemie.getPosition(), effects.PoisonEffect(enemie, self._effectLevel)))


class PoisonTowerBuyer(Tower):
    def __init__(self, position):
        super(PoisonTowerBuyer, self).__init__(position,
                                             config.Config.POISONTOWER_WIDTH * 2,
                                             config.Config.POISONTOWER_HEIGHT * 2,
                                             config.Config.POISONTOWER_IMAGE_big,
                                             config.Config.POISONTOWER_RANGE,
                                             config.Config.POISONTOWER_DAMAGE,
                                             config.Config.POISONTOWER_FIRERATE,
                                             config.Config.POISONTOWER_PRICE)

    def getClass(self):
        return "PoisonTowerBuyer"

    def newCopy(self):
        return PoisonTowerBuyer(self._position)

    def shot(self, enemie):
        pass

class ThunderTower(Tower):
    def __init__(self, position):
        super(ThunderTower, self).__init__(position,
                                        config.Config.THUNDERTOWER_WIDTH,
                                        config.Config.THUNDERTOWER_HEIGHT,
                                        config.Config.THUNDERTOWER_IMAGE_small,
                                        config.Config.THUNDERTOWER_RANGE,
                                        config.Config.THUNDERTOWER_DAMAGE,
                                        config.Config.THUNDERTOWER_FIRERATE,
                                        config.Config.THUNDERTOWER_PRICE)

    def getClass(self):
        return "ThunderTower"

    def newCopy(self):
        return ThunderTower(self._position)

    def shot(self, enemie):
        self._shotList.append(shot.ThunderShot(self.getPosition(), self.getDamage(), enemie.getPosition(), effects.ThunderEffect(enemie, self._effectLevel)))


class ThunderTowerBuyer(Tower):
    def __init__(self, position):
        super(ThunderTowerBuyer, self).__init__(position,
                                             config.Config.THUNDERTOWER_WIDTH * 2,
                                             config.Config.THUNDERTOWER_HEIGHT * 2,
                                             config.Config.THUNDERTOWER_IMAGE_big,
                                             config.Config.THUNDERTOWER_RANGE,
                                             config.Config.THUNDERTOWER_DAMAGE,
                                             config.Config.THUNDERTOWER_FIRERATE,
                                             config.Config.THUNDERTOWER_PRICE)

    def getClass(self):
        return "ThunderTowerBuyer"

    def newCopy(self):
        return ThunderTowerBuyer(self._position)

    def shot(self, enemie):
        pass