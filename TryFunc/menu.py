#ok
import pygame
import config
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import pygame
import towerdefense as TD
import player as PLAYER
import game as GAME
import os
import random
import mapcreator as MP

class Menu:
    def __init__(self):
        self._gameDisplay = None
        self._gameExit = False
        self._optionPointer = [10, 100]
        self._optionImage = pygame.image.load(config.Config.MENU_POINTER_2)
        self._selectedOption = 0

    def _displayBackImage(self):
        mainMenuImage= pygame.image.load(config.Config.MAIN_MENU_IMAGE)
        self._gameDisplay.blit(mainMenuImage,(0,0))

    def _displayText(self):
        myfont = pygame.font.Font(config.Config.MAIN_MENU_FONT, 35)

        new_game = myfont.render("Novo jogo", 1, (255,0,0))
        quick_game = myfont.render("Jogo rapido", 1, (255,0,0))
        create_map = myfont.render("Novo mapa", 1, (255,0,0))
        edit_map = myfont.render("Editar mapa", 1, (255,0,0))
        exit = myfont.render("Sair", 1, (255,0,0))


        self._gameDisplay.blit(new_game, (65, 100))
        self._gameDisplay.blit(quick_game, (65, 150))
        self._gameDisplay.blit(create_map, (65, 200))
        self._gameDisplay.blit(edit_map, (65, 250))
        self._gameDisplay.blit(exit, (65, 300))

    def _movePointerDown(self):
        self._optionPointer[1] += 50
        if self._optionPointer[1] > 300:
            self._optionPointer[1] = 100

        self._selectedOption = (self._selectedOption + 1)%5


    def _movePointerUp(self):
        self._optionPointer[1] -= 50
        if self._optionPointer[1] < 100:
            self._optionPointer[1] = 300

        self._selectedOption -= 1
        if self._selectedOption < 0:
            self._selectedOption = 4

    def _start_new_game(self, player_name, filename):

            game = GAME.Game()
            game.start()

            player = PLAYER.Player(player_name)
            towerDefense = TD.TowerDefense(player, filename)
            while not game.getGameExit():
                mousePosition = game.getMousePosition()
                if towerDefense.isClickedInTower():
                    towerDefense.towerInsideButton(mousePosition)
                elif towerDefense.isClickedInTrap():
                    towerDefense.trapInsideButton(mousePosition)
                for event in game.getEvents():
                    if event.type == pygame.QUIT:
                        game.setGameExit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        towerDefense.mousePress(game.getMousePosition(), game.getGameDisplay())
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_f:
                            if game.isFPSOn():
                                game.turnOffFPS()
                            else:
                                game.turnOnFPS()
                        elif event.key == pygame.K_LSHIFT:
                            towerDefense.turnOnShift()
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LSHIFT:
                            towerDefense.turnOffShift()
                    if event.type == pygame.USEREVENT + 1:
                        towerDefense.decTimer((game.getGameDisplay()))

                towerDefense.paintAllStuff(game.getGameDisplay(), mousePosition)
                game.paintAllStuff(game.getGameDisplay(), game.getClock())
                game.getClock().tick()
                game.update()
                game.getClock().tick(config.Config.FPS)      # Determina o FPS máximo

            game.quit()
            quit()


    def _handle_menu_press(self):
        if self._selectedOption == 0:
            root = Tk()
            root.withdraw()
            filename = askopenfilename()
            root.destroy()
            self._start_new_game("Novo Jogador", filename)

        elif self._selectedOption == 1:
            maps = os.listdir("maps")
            if maps == []:
                print("No map was found!")
                raise
            else:
                filename = "maps/" + maps[random.randint(0, len(maps)-1)]
            self._start_new_game("Novo Jogador", filename)

        elif self._selectedOption == 2:
            mapcreator = MP.MapCreator()
            mapcreator.setWindowCaption("Map Creation Window !")
            mapcreator.start()

        elif self._selectedOption == 3:

            root = Tk()
            root.withdraw()
            filemap = askopenfilename()
            root.destroy()

            mapcreator = MP.MapCreator(filemap)
            mapcreator.setWindowCaption("Map Creation Window !")
            mapcreator.loadMap(filemap)
            mapcreator.start()
        elif self._selectedOption == 4:
            self._gameExit = True
        else:
            raise ("You somehow selected an invalid option !")

    def _handle_key_press(self, event):
        if event.key == pygame.K_DOWN:
            self._movePointerDown()

        if event.key == pygame.K_UP:
            self._movePointerUp()

        if event.key == pygame.K_SPACE:
            self._handle_menu_press()


    def _displaySelectedOption(self):

        self._gameDisplay.blit(self._optionImage, self._optionPointer)

    def _updateScreen(self):
        self._displayBackImage();
        self._displayText();
        self._displaySelectedOption();


    def start(self):
        pygame.init()
        self._gameDisplay = pygame.display.set_mode((config.Config.MENU_WIDTH, config.Config.MENU_HEIGHT))
        pygame.display.set_caption("Main Menu")


        self._updateScreen()

        while not self._gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._gameExit = True
                if event.type == pygame.KEYDOWN:
                    self._handle_key_press(event)

            self._updateScreen()
            pygame.display.update()
