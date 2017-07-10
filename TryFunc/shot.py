#ok
import rectangle
import config
from func import*

class Shot(rectangle.Rectangle):
    def __init__(self, position, width, height, image, speed, targetPosition, damage, effect):
        super(Shot, self).__init__(position, width, height, image)
        self._speed = speed
        self._direction = self.calculateDirection(targetPosition)
        self._damage = damage
        self._effect = effect

    def getSpeed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed = speed

    def getDamage(self):
        return self._damage

    def getEffect(self):
        return self._effect

    def calculateDirection(self, targetPosition):
        return (first(targetPosition) - first(self._position))/4, (second(targetPosition) - second(self._position))/4

    def move(self):
        self.setPosition((first(self._position) + first(self._direction), second(self._position) + second(self._direction)))

    def destroy(self, tower):
        tower.delShot(self)

class IceShot(Shot):
    def __init__(self, position, damage, targetPosition, effect):
        super(IceShot, self).__init__(position,
                                      config.Config.ICESHOT_WIDTH,
                                      config.Config.ICESHOT_HEIGHT,
                                      config.Config.ICESHOT_IMAGE,
                                      config.Config.ICESHOT_SPEED,
                                      targetPosition,
                                      damage,
                                      effect)

class PoisonShot(Shot):
    def __init__(self, position, damage, targetPosition, effect):
        super(PoisonShot, self).__init__(position,
                                      config.Config.POISONSHOT_WIDTH,
                                      config.Config.POISONSHOT_HEIGHT,
                                      config.Config.POISONSHOT_IMAGE,
                                      config.Config.POISONSHOT_SPEED,
                                      targetPosition,
                                      damage,
                                      effect)

class ThunderShot(Shot):
    def __init__(self, position, damage, targetPosition, effect):
        super(ThunderShot, self).__init__(position,
                                      config.Config.THUNDERSHOT_WIDTH,
                                      config.Config.THUNDERSHOT_HEIGHT,
                                      config.Config.THUNDERSHOT_IMAGE,
                                      config.Config.THUNDERSHOT_SPEED,
                                      targetPosition,
                                      damage,
                                      effect)


