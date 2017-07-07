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
    PLAYER_LIFE = 50
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
    BLUETOWER_RANGE = 64
    BLUETOWER_DAMAGE = 50
    BLUETOWER_FIRERATE = 1.0
    BLUETOWER_PRICE = 100
    BLUETOWER_BUYER_POS = (567, 13)
    CLASSICTOWER_IMAGE_small = "imagens/sic.png"
    CLASSICTOWER_IMAGE_big = "imagens/sic-grande.png"
    CLASSICTOWER_WIDTH = 32
    CLASSICTOWER_HEIGHT = 32
    CLASSICTOWER_RANGE = 96
    CLASSICTOWER_DAMAGE = 25
    CLASSICTOWER_FIRERATE = 1.0
    CLASSICTOWER_PRICE = 50
    CLASSICTOWER_BUYER_POS = (493, 13)

    #TRAPS
    FIRETRAP_IMAGE = "imagens/firetrap3.png"
    FIRETRAP_WIDTH = 16
    FIRETRAP_HEIGHT = 16
    FIRETRAP_DAMAGE = 15
    FIRETRAP_PRICE = 75
    FIRETRAP_BUYER_POS = (505, 108)
    ICETRAP_IMAGE = "imagens/icetrap.png"
    ICETRAP_WIDTH = 16
    ICETRAP_HEIGHT = 16
    ICETRAP_DAMAGE = 15
    ICETRAP_PRICE = 100
    ICETRAP_BUYER_POS = (595, 108)

    #EFFECTS
    ##BURN
    BURNEFFECT_NAME = "Burn"
    BURNEFFECT_DURATION = 5
    BURNEFFECT_DAMAGEPERSECOND = 10

    ##ICE
    ICEEFFECT_NAME = "Ice"
    ICEEFFECT_DURATION = 3
    ICEEFFECT_SLOW = 1.0

    #ENEMIES
    ENEMIE_SPAWNPOSITION = (0, 160)
    ENEMIE_IMAGE = "imagens/enemy.png"
    ENEMIE_WIDTH = 16
    ENEMIE_HEIGHT = 16
    ENEMIE_HEALTH = 30
    ENEMIE_SPEED = 2.0 # ENTRE 1 E !0
    ENEMIE_EARNCASH = 0
    ENEMIE_LIFESWILLTOOK = 0