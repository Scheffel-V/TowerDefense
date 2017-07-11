#ok
import enemies
import config

class Waves:
    def __init__(self, enemieFirstDirection, enemieSpawnPosition):
        self._waveNumber = 0
        self._waveCicleNumber = 1
        self._waveIntraCicleNumber = 0
        self._enemieFirstDirection = enemieFirstDirection
        self._enemieSpawnPosition = enemieSpawnPosition
        self._bossWaveFlag = False

    def incWaveNumber(self):
        print("ENTREI")
        if self._waveNumber % 10 == 0 and self._waveNumber != 0:
            if not self._bossWaveFlag:
                self._bossWaveFlag = True
                self._waveIntraCicleNumber = 0
            else:
                self._bossWaveFlag = False
                self._waveNumber += 1
                self.incWaveIntraCicleNumber()
        else:
            self._waveNumber += 1
            self.incWaveIntraCicleNumber()

    def getWaveNumber(self):
        return self._waveNumber

    def incWaveCicleNumber(self):
        self._waveCicleNumber += 1

    def getWaveCicleNumber(self):
        return self._waveCicleNumber

    def incWaveIntraCicleNumber(self):
        if self._waveIntraCicleNumber == 5:
            self._waveIntraCicleNumber = 1
            self.incWaveCicleNumber()
        else:
            self._waveIntraCicleNumber += 1

    def getWaveIntraCicleNumber(self):
        return self._waveIntraCicleNumber

    def getEnemieToSpawn(self):
        return self.enemieToSpawn()

    def enemieToSpawn(self):
        if self._waveIntraCicleNumber == 1:
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_WIDTH,
                                  config.Config.ENEMIE_HEIGHT,
                                  config.Config.ENEMIE_1_IMAGE,
                                  config.Config.ENEMIE_1_HEALTH,
                                  config.Config.ENEMIE_1_SPEED,
                                  config.Config.ENEMIE_1_EARNCASH,
                                  config.Config.ENEMIE_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
        elif self._waveIntraCicleNumber == 2:
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_WIDTH,
                                  config.Config.ENEMIE_HEIGHT,
                                  config.Config.ENEMIE_2_IMAGE,
                                  config.Config.ENEMIE_2_HEALTH,
                                  config.Config.ENEMIE_2_SPEED,
                                  config.Config.ENEMIE_2_EARNCASH,
                                  config.Config.ENEMIE_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
        elif self._waveIntraCicleNumber == 3:
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_WIDTH,
                                  config.Config.ENEMIE_HEIGHT,
                                  config.Config.ENEMIE_3_IMAGE,
                                  config.Config.ENEMIE_3_HEALTH,
                                  config.Config.ENEMIE_3_SPEED,
                                  config.Config.ENEMIE_3_EARNCASH,
                                  config.Config.ENEMIE_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
        elif self._waveIntraCicleNumber == 4:
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_WIDTH,
                                  config.Config.ENEMIE_HEIGHT,
                                  config.Config.ENEMIE_4_IMAGE,
                                  config.Config.ENEMIE_4_HEALTH,
                                  config.Config.ENEMIE_4_SPEED,
                                  config.Config.ENEMIE_4_EARNCASH,
                                  config.Config.ENEMIE_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
        elif self._waveIntraCicleNumber == 5:
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_WIDTH,
                                  config.Config.ENEMIE_HEIGHT,
                                  config.Config.ENEMIE_5_IMAGE,
                                  config.Config.ENEMIE_5_HEALTH,
                                  config.Config.ENEMIE_5_SPEED,
                                  config.Config.ENEMIE_5_EARNCASH,
                                  config.Config.ENEMIE_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
        elif self._waveIntraCicleNumber == 0:
            #boss
            return enemies.Enemie(self._enemieSpawnPosition,
                                  config.Config.ENEMIE_BOSS_WIDTH,
                                  config.Config.ENEMIE_BOSS_HEIGHT,
                                  config.Config.ENEMIE_BOSS_IMAGE,
                                  config.Config.ENEMIE_BOSS_HEALTH,
                                  config.Config.ENEMIE_BOSS_SPEED,
                                  config.Config.ENEMIE_BOSS_EARNCASH,
                                  config.Config.ENEMIE_BOSS_LIFESWILLTOOK,
                                  self._enemieFirstDirection,
                                  self._waveCicleNumber)
