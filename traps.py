import rectangle
import abc
import config
import pygame
import effects

class Trap(rectangle.Rectangle):
    _mouseCircleSurface = pygame.Surface(config.Config.MOUSE_CIRCLE_SURFACE)

    def __init__(self, position, width, height, image, damage, price):
        super(Trap, self).__init__(position, width, height, image)
        self._damage = damage
        self._reloadTime = 2.0
        self._price = price
        self._level = 1
        self._priceToUpgrade = 100

    def getFirstClass(self):
        return "Trap"

    @abc.abstractmethod
    def getClass(self):
        return

    @abc.abstractmethod
    def newCopy(self):
        return

    @abc.abstractmethod
    def shot(self, enemie):
        pass

    def upgrade(self):
        self._level += 1
        self._priceToUpgrade = self._priceToUpgrade + (self._level - 1) * 50

    def getDamage(self):
        return self._damage

    def setDamage(self, damage):
        self._damage = damage

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def doublePrice(self):
        self._price = self._price * 2

    def getLevel(self):
        return self._level

    def getPriceToUpgrade(self):
        return self._priceToUpgrade

    def decReloadTime(self):
        self._reloadTime -= 2.0

    def resetReloadTime(self):
        self._reloadTime = 3
    #print self._reloadTime

    def shotEnemies(self, enemies, towerDefense):
        if self._reloadTime <= 0:
            for enemieAux in enemies:
                if self.collide(enemieAux):
                    self.shot(enemieAux)
                    self.resetReloadTime()
                    break

    def paintRange(self, gameDisplay, color):
        self._mouseCircleSurface.fill(config.Config.CK)
        self._mouseCircleSurface.set_colorkey(config.Config.CK)
        pygame.draw.circle(self._mouseCircleSurface, color, self.getCenter(), 16, 16)
        self._mouseCircleSurface.set_alpha(150)
        gameDisplay.blit(self._mouseCircleSurface, (0, 0))

    @abc.abstractmethod
    def paintAtributes(self, gameDisplay):
        pass


class FireTrap(Trap):
    def __init__(self, position):
        super(FireTrap, self).__init__(position,
                                           config.Config.FIRETRAP_WIDTH,
                                           config.Config.FIRETRAP_HEIGHT,
                                           config.Config.FIRETRAP_IMAGE,
                                           config.Config.FIRETRAP_DAMAGE,
                                           config.Config.FIRETRAP_PRICE)

    def getClass(self):
        return "FireTrap"

    def newCopy(self):
        return FireTrap(self._position)

    def shot(self, enemie):
        burnEffect = effects.BurnEffect(enemie, self.getLevel())
        enemie.setBurn(burnEffect)

    def paintAtributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render("Damage per second:%d" % (config.Config.BURNEFFECT_DAMAGEPERSECOND * (1.3 ** (self.getLevel() - 1))), True, (0, 0, 0))
        text2 = font.render("Duration:%d" % (config.Config.BURNEFFECT_DURATION + self.getLevel()), True, (0, 0, 0))
        gameDisplay.blit(text, (497, 177))
        gameDisplay.blit(text2, (497, 197))


class FireTrapBuyer(Trap):
    def __init__(self, position):
        super(FireTrapBuyer, self).__init__(position,
                                            config.Config.FIRETRAP_WIDTH,
                                            config.Config.FIRETRAP_HEIGHT,
                                            config.Config.FIRETRAP_IMAGE,
                                            config.Config.FIRETRAP_DAMAGE,
                                            config.Config.FIRETRAP_PRICE)

    def getClass(self):
        return "FireTrapBuyer"

    def newCopy(self):
        return FireTrapBuyer(self._position)

    def shot(self, enemie):
        pass

    def paintAtributes(self, gameDisplay):
        pass


class IceTrap(Trap):
    def __init__(self, position):
        super(IceTrap, self).__init__(position,
                                       config.Config.ICETRAP_WIDTH,
                                       config.Config.ICETRAP_HEIGHT,
                                       config.Config.ICETRAP_IMAGE,
                                       config.Config.ICETRAP_DAMAGE,
                                       config.Config.ICETRAP_PRICE)

    def getClass(self):
        return "IceTrap"

    def newCopy(self):
        return IceTrap(self._position)

    def shot(self, enemie):
        iceEffect = effects.IceEffect(enemie, self.getLevel())
        enemie.setIce(iceEffect)

    def paintAtributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text2 = font.render("Duration:%d" % (config.Config.ICEEFFECT_DURATION + self.getLevel()), True, (0, 0, 0))
        gameDisplay.blit(text2, (497, 177))


class IceTrapBuyer(Trap):
    def __init__(self, position):
        super(IceTrapBuyer, self).__init__(position,
                                           config.Config.ICETRAP_WIDTH,
                                           config.Config.ICETRAP_HEIGHT,
                                           config.Config.ICETRAP_IMAGE,
                                           config.Config.ICETRAP_DAMAGE,
                                           config.Config.ICETRAP_PRICE)

    def getClass(self):
        return "IceTrapBuyer"

    def newCopy(self):
        return IceTrapBuyer(self._position)

    def paintAtributes(self, gameDisplay):
        pass

class ThunderTrap(Trap):
    def __init__(self, position):
        super(ThunderTrap, self).__init__(position,
                                       config.Config.THUNDERTRAP_WIDTH,
                                       config.Config.THUNDERTRAP_HEIGHT,
                                       config.Config.THUNDERTRAP_IMAGE,
                                       config.Config.THUNDERTRAP_DAMAGE,
                                       config.Config.THUNDERTRAP_PRICE)

    def getClass(self):
        return "ThunderTrap"

    def newCopy(self):
        return ThunderTrap(self._position)

    def shot(self, enemie):
        thunderEffect = effects.ThunderEffect(enemie, self.getLevel())
        enemie.setThunder(thunderEffect)

    def paintAtributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text2 = font.render("Duration:%d" % (config.Config.THUNDEREFFECT_DURATION + self.getLevel()), True, (0, 0, 0))
        gameDisplay.blit(text2, (497, 177))


class ThunderTrapBuyer(Trap):
    def __init__(self, position):
        super(ThunderTrapBuyer, self).__init__(position,
                                           config.Config.THUNDERTRAP_WIDTH,
                                           config.Config.THUNDERTRAP_HEIGHT,
                                           config.Config.THUNDERTRAP_IMAGE,
                                           config.Config.THUNDERTRAP_DAMAGE,
                                           config.Config.THUNDERTRAP_PRICE)

    def getClass(self):
        return "ThunderTrapBuyer"

    def newCopy(self):
        return ThunderTrapBuyer(self._position)

    def shot(self, enemie):
        pass

    def paintAtributes(self, gameDisplay):
        pass


class PoisonTrap(Trap):
    def __init__(self, position):
        super(PoisonTrap, self).__init__(position,
                                       config.Config.POISONTRAP_WIDTH,
                                       config.Config.POISONTRAP_HEIGHT,
                                       config.Config.POISONTRAP_IMAGE,
                                       config.Config.POISONTRAP_DAMAGE,
                                       config.Config.POISONTRAP_PRICE)

    def getClass(self):
        return "PoisonTrap"

    def newCopy(self):
        return PoisonTrap(self._position)

    def shot(self, enemie):
        poisonEffect = effects.PoisonEffect(enemie, self.getLevel())
        enemie.setPoison(poisonEffect)

    def paintAtributes(self, gameDisplay):
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render("Damage per second:%d" % (config.Config.POISONEFFECT_DAMAGEPERSECOND * (1.25 ** (self.getLevel() - 1))), True, (0, 0, 0))
        text2 = font.render("Duration:%d" % (config.Config.POISONEFFECT_DURATION + 2 * self.getLevel()), True, (0, 0, 0))
        gameDisplay.blit(text, (497, 177))
        gameDisplay.blit(text2, (497, 197))

class PoisonTrapBuyer(Trap):
    def __init__(self, position):
        super(PoisonTrapBuyer, self).__init__(position,
                                           config.Config.POISONTRAP_WIDTH,
                                           config.Config.POISONTRAP_HEIGHT,
                                           config.Config.POISONTRAP_IMAGE,
                                           config.Config.POISONTRAP_DAMAGE,
                                           config.Config.POISONTRAP_PRICE)

    def getClass(self):
        return "PoisonTrapBuyer"

    def newCopy(self):
        return PoisonTrapBuyer(self._position)

    def shot(self, enemie):
        pass

    def paintAtributes(self, gameDisplay):
        pass