# coding=utf-8
# Classe Config:
#   Determina todas as propriedades do jogo.
#   É dessa classe que os valores numéricos que moldam o jogo
#   serão pegos. Basicamente, são os valores globais.

class Config:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    CK = (255, 0, 0)
    COLLIDE_COLOR = (255, 150, 0)
    NOT_COLLIDE_COLOR = (0, 255, 0)
    MOUSE_CIRCLE_SURFACE = (480, 480)
    FPS = 100
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 480
    DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
    PLAYER_CASH = 400
    PLAYER_LIFE = 30
    MENUTOWERS_IMAGE = "imagens/undo-menu-ingame.png"
    CREATIONMODE_IMAGE = "imagens/creation_menu.png"

    GRASS_IMAGE = "imagens/grass_outlined.png"


    #MENUS

    MENU_WIDTH = 380
    MENU_HEIGHT = 480

    MAIN_MENU_IMAGE = "imagens/main_menu.png"

    GRASS_IMAGE = "imagens/grass_outlined.png"

    MAIN_MENU_FONT = "fonts/Colleged.ttf"
    MENU_POINTER_2 = "imagens/demonho.png"

    #BUTTONS
    UPGRADEBUTTON_DAMAGE_POSITION = (493, 323)
    UPGRADEBUTTON_DAMAGE_WIDTH = 100
    UPGRADEBUTTON_DAMAGE_HEIGHT = 64
    UPGRADEBUTTON_DAMAGE_IMAGE = "imagens/damageupgrade.png"
    UPGRADEBUTTON_DAMAGE_MOUSEINSIDE_IMAGE = "imagens/damageupgrade2.png"

    UPGRADEBUTTON_RANGE_POSITION = (590, 323)
    UPGRADEBUTTON_RANGE_WIDTH = 100
    UPGRADEBUTTON_RANGE_HEIGHT = 64
    UPGRADEBUTTON_RANGE_IMAGE = "imagens/rangeupgrade.png"
    UPGRADEBUTTON_RANGE_MOUSEINSIDE_IMAGE = "imagens/rangeupgrade2.png"

    UPGRADEBUTTON_EFFECT_POSITION = (688, 323)
    UPGRADEBUTTON_EFFECT_WIDTH = 100
    UPGRADEBUTTON_EFFECT_HEIGHT = 64
    UPGRADEBUTTON_EFFECT_IMAGE = "imagens/effectupgrade.png"
    UPGRADEBUTTON_EFFECT_MOUSEINSIDE_IMAGE = "imagens/effectupgrade2.png"

    UPGRADEBUTTON_TRAP_POSITION = (493, 323)
    UPGRADEBUTTON_TRAP_WIDTH = 100
    UPGRADEBUTTON_TRAP_HEIGHT = 64
    UPGRADEBUTTON_TRAP_IMAGE = "imagens/trapupgrade.png"
    UPGRADEBUTTON_TRAP_MOUSEINSIDE_IMAGE = "imagens/trapupgrade2.png"

    #spawns
    SPAWN_IMAGE = "imagens/spawn.png"
    DESPAWN_IMAGE = "imagens/despawn.png"

    #paths
    CENTRAL_PATH_IMAGE = "imagens/center_path.png"
    REGULAR_PATH_IMAGE = "imagens/path.png"
    CHANGEDIR_IMAGE = "imagens/changedir.png"

    #MOUSE
    LEFT_BUTTON = 1
    MIDDLE_BUTTON = 2
    RIGHT_BUTTON = 3

    #RECTANGLE
    RECT_DIMX_px = 16
    RECT_DIMY_px = 16
    RECT_DIMS_px = (RECT_DIMX_px, RECT_DIMY_px)

    #MAP
    # -> NUMBER MATRIX
    MAP_NUMBMATRIX_GRASS = 0
    MAP_NUMBMATRIX_PATH = 1
    MAP_NUMBMATRIX_SPAWN = 2
    MAP_NUMBMATRIX_DESPAWN = 3
    MAP_NUMBMATRIX_CENTRALPATH = 4
    MAP_NUMBMATRIX_CHANGEDIRECTION = 5
    MAP_DIMX = 30
    MAP_DIMY = 30
    MAP_DIMS = (MAP_DIMX, MAP_DIMY)
    MAP_NUMBMATRIX_VALUES = [MAP_NUMBMATRIX_GRASS,
                             MAP_NUMBMATRIX_PATH,
                             MAP_NUMBMATRIX_SPAWN,
                             MAP_NUMBMATRIX_DESPAWN,
                             MAP_NUMBMATRIX_CENTRALPATH,
                             MAP_NUMBMATRIX_CHANGEDIRECTION]
    #TOWERS
    BLUETOWER_IMAGE_small = "imagens/lue.png"
    BLUETOWER_IMAGE_big = "imagens/lue-grande.png"
    BLUETOWER_WIDTH = 32
    BLUETOWER_HEIGHT = 32
    BLUETOWER_RANGE = 80
    BLUETOWER_DAMAGE = 10
    BLUETOWER_FIRERATE = 0.5
    BLUETOWER_PRICE = 100
    BLUETOWER_BUYER_POS = (567, 13)

    CLASSICTOWER_IMAGE_small = "imagens/sic.png"
    CLASSICTOWER_IMAGE_big = "imagens/sic-grande.png"
    CLASSICTOWER_WIDTH = 32
    CLASSICTOWER_HEIGHT = 32
    CLASSICTOWER_RANGE = 96
    CLASSICTOWER_DAMAGE = 25
    CLASSICTOWER_FIRERATE = 1.0
    CLASSICTOWER_PRICE = 60
    CLASSICTOWER_BUYER_POS = (493, 13)

    POISONTOWER_IMAGE_small = "imagens/poisontower_small.png"
    POISONTOWER_IMAGE_big = "imagens/poisontower_big.png"
    POISONTOWER_WIDTH = 32
    POISONTOWER_HEIGHT = 32
    POISONTOWER_RANGE = 96
    POISONTOWER_DAMAGE = 15
    POISONTOWER_FIRERATE = 0.25
    POISONTOWER_PRICE = 45
    POISONTOWER_BUYER_POS = (642, 13)

    THUNDERTOWER_IMAGE_small = "imagens/thundertower_small.png"
    THUNDERTOWER_IMAGE_big = "imagens/thundertower_big.png"
    THUNDERTOWER_WIDTH = 32
    THUNDERTOWER_HEIGHT = 32
    THUNDERTOWER_RANGE = 70
    THUNDERTOWER_DAMAGE = 25
    THUNDERTOWER_FIRERATE = 1.0
    THUNDERTOWER_PRICE = 120
    THUNDERTOWER_BUYER_POS = (722, 13)

    #SHOTS
    ##ICESHOT
    ICESHOT_WIDTH = 8
    ICESHOT_HEIGHT = 8
    ICESHOT_IMAGE = "imagens/iceshot.png"
    ICESHOT_SPEED = 0.5

    THUNDERSHOT_WIDTH = 8
    THUNDERSHOT_HEIGHT = 8
    THUNDERSHOT_IMAGE = "imagens/thundershot.png"
    THUNDERSHOT_SPEED = 0.5

    POISONSHOT_WIDTH = 8
    POISONSHOT_HEIGHT = 8
    POISONSHOT_IMAGE = "imagens/poisonshot.png"
    POISONSHOT_SPEED = 0.5

    #TRAPS
    FIRETRAP_IMAGE = "imagens/firetrap3.png"
    FIRETRAP_WIDTH = 16
    FIRETRAP_HEIGHT = 16
    FIRETRAP_DAMAGE = 15
    FIRETRAP_PRICE = 125
    FIRETRAP_BUYER_POS = (513, 120)

    ICETRAP_IMAGE = "imagens/icetrap.png"
    ICETRAP_WIDTH = 16
    ICETRAP_HEIGHT = 16
    ICETRAP_DAMAGE = 15
    ICETRAP_PRICE = 180
    ICETRAP_BUYER_POS = (591, 120)

    THUNDERTRAP_IMAGE = "imagens/thundertrap.png"
    THUNDERTRAP_WIDTH = 16
    THUNDERTRAP_HEIGHT = 16
    THUNDERTRAP_DAMAGE = 15
    THUNDERTRAP_PRICE = 180
    THUNDERTRAP_BUYER_POS = (665, 120)

    POISONTRAP_IMAGE = "imagens/poisontrap.png"
    POISONTRAP_WIDTH = 16
    POISONTRAP_HEIGHT = 16
    POISONTRAP_DAMAGE = 15
    POISONTRAP_PRICE = 150
    POISONTRAP_BUYER_POS = (745, 120)

    #EFFECTS
    ##BURN
    BURNEFFECT_NAME = "Burn"
    BURNEFFECT_DURATION = 5
    BURNEFFECT_DAMAGEPERSECOND = 10

    ##ICE
    ICEEFFECT_NAME = "Ice"
    ICEEFFECT_DURATION = 3
    ICEEFFECT_SLOW = 1.0

    ##POISON
    POISONEFFECT_NAME = "Poison"
    POISONEFFECT_DURATION = 10
    POISONEFFECT_DAMAGEPERSECOND = 3

    ##THUNDER
    THUNDEREFFECT_NAME = "Thunder"
    THUNDEREFFECT_DURATION = 1

    #ENEMIES
    ENEMIE_SPAWNPOSITION = (0, 160)
    ENEMIE_WIDTH = 16
    ENEMIE_HEIGHT = 16
    ENEMIE_LIFESWILLTOOK = 1

    ENEMIE_1_HEALTH = 30
    ENEMIE_1_SPEED = 2.0
    ENEMIE_1_EARNCASH = 4
    ENEMIE_1_IMAGE = "imagens/enemy1.png"

    ENEMIE_2_HEALTH = 70
    ENEMIE_2_SPEED = 1.0
    ENEMIE_2_EARNCASH = 4
    ENEMIE_2_IMAGE = "imagens/enemy2.png"

    ENEMIE_3_HEALTH = 125
    ENEMIE_3_SPEED = 2.0
    ENEMIE_3_EARNCASH = 4
    ENEMIE_3_IMAGE = "imagens/enemy3.png"

    ENEMIE_4_HEALTH = 45
    ENEMIE_4_SPEED = 4.0
    ENEMIE_4_EARNCASH = 4
    ENEMIE_4_IMAGE = "imagens/enemy4.png"

    ENEMIE_5_HEALTH = 100
    ENEMIE_5_SPEED = 1.5
    ENEMIE_5_EARNCASH = 4
    ENEMIE_5_IMAGE = "imagens/enemy5.png"

    #BOSS
    ENEMIE_BOSS_SPAWNPOSITION = (0, 160)
    ENEMIE_BOSS_WIDTH = 16
    ENEMIE_BOSS_HEIGHT = 16
    ENEMIE_BOSS_LIFESWILLTOOK = 15
    ENEMIE_BOSS_HEALTH = 1500
    ENEMIE_BOSS_SPEED = 1.5
    ENEMIE_BOSS_EARNCASH = 100
    ENEMIE_BOSS_IMAGE = "imagens/enemy6.png"
