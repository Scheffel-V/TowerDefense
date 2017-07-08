import config

class Effect:
    def __init__(self, name, duration, enemie):
        self._name = name
        self._duration = duration
        self._enemie = enemie

    def getName(self):
        return self._name

    def getDuration(self):
        return self._duration

    def decDuration(self):
        if self._duration == 0:
            self.destroy()
        else:
            self._duration -= 1

    def getEnemie(self):
        return self._enemie

    def destroy(self):
        self._enemie.delEffect(self)

class BurnEffect(Effect):
    def __init__(self, enemie, level):
        super(BurnEffect, self).__init__(config.Config.BURNEFFECT_NAME, config.Config.BURNEFFECT_DURATION + level, enemie)
        self._damagePerSecond = config.Config.BURNEFFECT_DAMAGEPERSECOND * (1.3 ** (level - 1))

    def getDamagePerSecond(self):
        return self._damagePerSecond

class IceEffect(Effect):
    def __init__(self, enemie, level):
        super(IceEffect, self).__init__(config.Config.ICEEFFECT_NAME, config.Config.ICEEFFECT_DURATION + level, enemie)
        self._slow = config.Config.ICEEFFECT_SLOW

    def getSlow(self):
        return self._slow

class PoisonEffect(Effect):
    def __init__(self, enemie, level):
        super(PoisonEffect, self).__init__(config.Config.POISONEFFECT_NAME, config.Config.POISONEFFECT_DURATION + 2 * level, enemie)
        self._damagePerSecond = config.Config.POISONEFFECT_DAMAGEPERSECOND * (1.25 ** (level - 1))

    def getDamagePerSecond(self):
        return self._damagePerSecond

class ThunderEffect(Effect):
    def __init__(self, enemie, level):
        super(ThunderEffect, self).__init__(config.Config.THUNDEREFFECT_NAME, config.Config.THUNDEREFFECT_DURATION + level, enemie)

