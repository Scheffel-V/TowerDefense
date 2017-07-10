#ok
import rectangle
import pygame
import config
import abc


class UpgradeButton(rectangle.Rectangle, metaclass=abc.ABCMeta):
    _mouseCircleSurface = pygame.Surface(config.Config.MOUSE_CIRCLE_SURFACE)

    def __init__(self, position, width, height, image, initialPrice):
        super(UpgradeButton, self).__init__(position, width, height, image)
        self._initialPrice = initialPrice

    def getInitialPrice(self):
        return self._price

    def setInitialPrice(self, price):
        self._initialPrice = price

    @abc.abstractmethod
    def upgradeTower(self, tower):
        pass


class UpgradeDamageButton(UpgradeButton):
    def __init__(self, tower):
        super(UpgradeDamageButton, self).__init__(config.Config.UPGRADE_DAMAGE_POS,
                                                  config.Config.UPGRADE_DAMAGE_WIDTH,
                                                  config.Config.UPGRADE_DAMAGE_HEIGHT,
                                                  config.Config.UPGRADE_DAMAGE_IMAGE,
                                                  config.Config.UPGRADE_DAMAGE_INITIAL_PRICE)
        self._maxLevel = config.Config.UPGRADE_DAMAGE_MAX_LEVEL
        self._damageLevel = tower.getUpgradeDamageLevel()
        self._priceToUpgrade = self.calculatePrice(tower.getUpgradeDamageLevel())
        self._tower = tower

    def upgradeDamage(self, player):
        self._tower.upgradeDamage()
        player.purchaseObject(self._priceToUpgrade)

    def calculatePrice(self, damageLevel):
        return self.getPrice() * 2**damageLevel



