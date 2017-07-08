import rectangle
import config

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
        vector = targetPosition[0] - self._position[0], targetPosition[1] - self._position[1]
        vector = vector[0] / 4, vector[1] / 4
        return vector

    def move(self):
        newPositionX = self._position[0] + self._direction[0]
        newPositionY = self._position[1] + self._direction[1]
        self.setPosition((newPositionX, newPositionY))

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


