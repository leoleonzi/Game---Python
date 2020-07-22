import pygame

TILESIZE = 50



class Tree:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./Texturas/trees/tree.png'), (150, 220))
        self.X_POS = 7*TILESIZE
        self.Y_POS = 3*TILESIZE

class Arbusto:
     def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./Texturas/trees/Arbusto.png'), (100, 100))
        self.X_POS = 13*TILESIZE
        self.Y_POS = 2*TILESIZE

class PortaoSecundario:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./Texturas/PortaoSecundario.png'), (150, 150))
        self.X_POS = 7*TILESIZE
        self.Y_POS = -1

class Lua:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./Texturas/Lua.png'), (300, 300))
        self.X_POS = 7*TILESIZE
        self.Y_POS = -1
# TILES
ParedeTijolosEscuros = 0
ChaoPedras = 1
Grama = 2
CeuNegro = 3
CeuComEstrela = 4

TEXTURES = {
    ParedeTijolosEscuros: pygame.image.load('./Texturas/ParedeTijolosEscuros.png'),
    ChaoPedras: pygame.image.load('./Texturas/ChaoPedras.png'),
    Grama: pygame.image.load('./Texturas/Grama.png'),
    CeuNegro: pygame.image.load('./Texturas/CeuNegro.png'),
    CeuComEstrela: pygame.image.load('./Texturas/CeuComEstrela.png')

}

class AmbienteExteriorDia:
    def __init__(self):
    # TILES TO BE DISPLAYED
        self.GRID = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],

        ]

        # GAME DIMENSIONS, CONFIG
        self.MAPWIDTH =20
        self.MAPHEIGHT = 7
        self.tamanhoDeMapa = [self.MAPWIDTH*TILESIZE,self.MAPHEIGHT*TILESIZE]
        self.tela = pygame.display.set_mode(self.tamanhoDeMapa, pygame.RESIZABLE)

        #ARVORES
        self.tree1 = Tree()
        self.tree1.X_POS = 7*TILESIZE
        self.tree1.Y_POS = 3.8*TILESIZE

        self.tree2 = Tree()
        self.tree2.X_POS = 4*TILESIZE
        self.tree2.Y_POS = 3.8*TILESIZE

        self.tree3 = Tree()
        self.tree3.X_POS = 10*TILESIZE
        self.tree3.Y_POS = 3.8*TILESIZE

        self.arbusto1 = Arbusto()

        self.portaosec = PortaoSecundario()

class SaguaoPrincipalNoite:
    def __init__(self):
        self.GRID = [
            [1,1],
            [1,1],
            [1,1],
            [1,1],
            [1,1]
        ]
 
    # GAME DIMENSIONS, CONFIG
        self.MAPWIDTH =2
        self.MAPHEIGHT = 5
        self.tamanhoDeMapa = [self.MAPWIDTH*TILESIZE,self.MAPHEIGHT*TILESIZE]
        self.tela = pygame.display.set_mode(self.tamanhoDeMapa, pygame.RESIZABLE)

class CorredorExternoNoite:
    def __init__(self):
        self.GRID = [
            [4,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,4,3,3,3],
            [3,3,3,3,3,4,3,3,3,3,3,3,3,4,3,3,3,3,4,3,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [4,3,3,4,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,4],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,3,3,3,3,3],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
 
    # GAME DIMENSIONS, CONFIG
        self.MAPWIDTH =21
        self.MAPHEIGHT = 8
        self.tamanhoDeMapa = [self.MAPWIDTH*TILESIZE,self.MAPHEIGHT*TILESIZE]
        self.tela = pygame.display.set_mode(self.tamanhoDeMapa, pygame.RESIZABLE)

        self.lua = Lua()