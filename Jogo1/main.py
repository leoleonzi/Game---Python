import pygame, sys
from pygame.locals import *
from ambientes import *

def main():
    pygame.init()
    pygame.display.set_caption("Jogo Medieval")
    sair = False
    relogio = pygame.time.Clock()

    #Cores:
    branco = ((255,255,255))
    azul = (108,194,236)
    verde = (152,231,114)
    cinza = (131,131,131)
    preto = (0,0,0)
    ambiente = 'exteriorDia'

    # DECLARAR E RENDERIZAR AMBIENTES

    saguaoPrincipalNoite = SaguaoPrincipalNoite()
    ambienteExteriorDia = AmbienteExteriorDia()
    corredorExternoNoite = CorredorExternoNoite()
    for row in range(ambienteExteriorDia.MAPHEIGHT):
        for column in range(ambienteExteriorDia.MAPWIDTH):
            ambienteExteriorDia.tela.blit(TEXTURES[ambienteExteriorDia.GRID[row][column]], (column*TILESIZE, row*TILESIZE))
    
    foto = pygame.image.load('./Aniellius/Aniellius_f0.png')
    
    posicao = [10,70]
    contagem = 0
    direcao = 'd'
    stringFoto = './Aniellius/Aniellius_f0.png'
    while sair != True:
        while ambiente == 'exteriorDia':
            keys = pygame.key.get_pressed()
            if (keys[K_DOWN]):
                if posicao[1]>=ambienteExteriorDia.tamanhoDeMapa[1]-50:
                        stringFoto = './Aniellius/Aniellius_f0.png'
                else:
                    if direcao == 'd' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'd'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_f' + str(contagem) + '.png'                     
                    posicao[1]+= TILESIZE/5
                pygame.time.delay(80)
            if (keys[K_UP]):
                if posicao[1]<=70:
                    stringFoto = './Aniellius/Aniellius_b0.png'
                else:
                    if direcao == 'u' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'u'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_b' + str(contagem) + '.png' 
                    posicao[1]-=TILESIZE/5
                    pygame.time.delay(80)
            if (keys[K_LEFT]):
                if posicao[0] <= 0:
                    stringFoto = './Aniellius/Aniellius_l0.png' 
                else:
                    if direcao == 'l' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'l'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_l' + str(contagem) + '.png' 
                    posicao[0]-=TILESIZE/5
                    pygame.time.delay(80)
            
            if (keys[K_RIGHT]):
                if posicao[0] >= ambienteExteriorDia.tamanhoDeMapa[0] -100:
                    stringFoto = './Aniellius/Aniellius_r0.png' 
                else:
                    if direcao == 'r' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'r'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_r' + str(contagem) + '.png' 
                    posicao[0]+=TILESIZE/5
                    pygame.time.delay(80)
        
            foto = pygame.image.load(stringFoto)

            for row in range(ambienteExteriorDia.MAPHEIGHT):
                for column in range(ambienteExteriorDia.MAPWIDTH):
                    ambienteExteriorDia.tela.blit(TEXTURES[ambienteExteriorDia.GRID[row][column]], (column*TILESIZE, row*TILESIZE))
        
            ambienteExteriorDia.tela.blit(ambienteExteriorDia.portaosec.SPRITE, (ambienteExteriorDia.portaosec.X_POS, ambienteExteriorDia.portaosec.Y_POS))

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    scrsize = event.size
                    width   = event.w
                    hight   = event.h
                    screen = pygame.display.set_mode(scrsize,RESIZABLE)
                    
                if event.type == pygame.QUIT:
                    sair = True
                    ambiente = 'sair'

            relogio.tick(27)
       

            #Render Arvores:

            if posicao[1] > ambienteExteriorDia.arbusto1.Y_POS - 15:
                ambienteExteriorDia.tela.blit(ambienteExteriorDia.arbusto1.SPRITE, (ambienteExteriorDia.arbusto1.X_POS, ambienteExteriorDia.arbusto1.Y_POS))
                ambienteExteriorDia.tela.blit(foto, posicao)
            else:
                ambienteExteriorDia.tela.blit(foto, posicao)
                ambienteExteriorDia.tela.blit(ambienteExteriorDia.arbusto1.SPRITE, (ambienteExteriorDia.arbusto1.X_POS, ambienteExteriorDia.arbusto1.Y_POS))
            

            ambienteExteriorDia.tela.blit(ambienteExteriorDia.tree1.SPRITE, (ambienteExteriorDia.tree1.X_POS, ambienteExteriorDia.tree1.Y_POS))
            ambienteExteriorDia.tela.blit(ambienteExteriorDia.tree2.SPRITE, (ambienteExteriorDia.tree2.X_POS, ambienteExteriorDia.tree2.Y_POS))
            ambienteExteriorDia.tela.blit(ambienteExteriorDia.tree3.SPRITE, (ambienteExteriorDia.tree3.X_POS, ambienteExteriorDia.tree3.Y_POS))

            if keys[K_SPACE]:
                if 320 <= posicao[0] <= 420 and posicao[1] == 70:
                    ambienteExteriorDia.tela.fill((0,0,0))
                    ambiente = 'corredorExternoNoite'
                    posicao = [0,300]

            pygame.display.update()
        
        
        while ambiente == 'corredorExternoNoite':

            for row in range(corredorExternoNoite.MAPHEIGHT):
                for column in range(corredorExternoNoite.MAPWIDTH):
                    corredorExternoNoite.tela.blit(TEXTURES[corredorExternoNoite.GRID[row][column]], (column*TILESIZE, row*TILESIZE))

            keys = pygame.key.get_pressed()
            if (keys[K_DOWN]):
                if posicao[1]>=corredorExternoNoite.tamanhoDeMapa[1]-100:
                        stringFoto = './Aniellius/Aniellius_f0.png'
                else:
                    if direcao == 'd' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'd'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_f' + str(contagem) + '.png'                     
                    posicao[1]+= TILESIZE/5
                pygame.time.delay(80)
            if (keys[K_UP]):
                if posicao[1]<=70:
                    stringFoto = './Aniellius/Aniellius_b0.png'
                else:
                    if direcao == 'u' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'u'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_b' + str(contagem) + '.png' 
                    posicao[1]-=TILESIZE/5
                    pygame.time.delay(80)
            if (keys[K_LEFT]):
                if posicao[0] <= 0:
                    stringFoto = './Aniellius/Aniellius_l0.png' 
                else:
                    if direcao == 'l' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'l'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_l' + str(contagem) + '.png' 
                    posicao[0]-=TILESIZE/5
                    pygame.time.delay(80)
            
            if (keys[K_RIGHT]):
                if posicao[0] >= corredorExternoNoite.tamanhoDeMapa[0] -100:
                    stringFoto = './Aniellius/Aniellius_r0.png' 
                else:
                    if direcao == 'r' and contagem != 1:
                        contagem = (contagem + 1) % 2
                    else:
                        direcao = 'r'
                        contagem = 0
                    stringFoto = './Aniellius/Aniellius_r' + str(contagem) + '.png' 
                    posicao[0]+=TILESIZE/5
                    pygame.time.delay(80)
        
            foto = pygame.image.load(stringFoto)

            corredorExternoNoite.tela.blit(foto, posicao)

            if keys[K_SPACE]:
                ambiente = 'corredorExternoNoite'

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    scrsize = event.size
                    width   = event.w
                    hight   = event.h
                    screen = pygame.display.set_mode(scrsize,RESIZABLE)

                if event.type == pygame.QUIT:
                    sair = True
                    ambiente = 'sair'

            relogio.tick(27)

            #Render Lua:
            corredorExternoNoite.tela.blit(corredorExternoNoite.lua.SPRITE, (corredorExternoNoite.lua.X_POS, corredorExternoNoite.lua.Y_POS))

            pygame.display.update()
            
    pygame.quit()

main()