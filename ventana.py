import pygame
from MaquinaTuring import *

class GUI:

    def __init__(self):
        pass
    
    maquina = MaquinaTuring()
    pygame.init()

    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    pygame.display.set_caption("Maquina de Turing")


    runnig = True
    rectangulo = pygame.Rect(50,50,45,45)
    rectangulo2 = pygame.Rect(100,50,100,45)

    rectangulo3 = pygame.Rect(50,100,45,45)
    rectangulo4 = pygame.Rect(100,100,100,45)

    rectangulo5 = pygame.Rect(50,150,45,45)
    rectangulo6 = pygame.Rect(100,150,100,45)

    rectangulo7 = pygame.Rect(50,200,45,45)
    rectangulo8 = pygame.Rect(100,200,100,45)

    rectangulo9 = pygame.Rect(450,450,100,45)

    textVar = "Variables"
    variable1 = "00"
    variable2 = "01"
    variable3 = "10"
    variable4 = "11"
    textEntrada = "Valor ingresado"
    
    color = (255,120,135)
    font = pygame.font.SysFont("ocraextended", 40)
    #COLORS
    BLACK = (0, 0, 0)

    while runnig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnig = False
        
        
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen,color,rectangulo)
        pygame.draw.rect(screen,color,rectangulo2)
        pygame.draw.rect(screen,color,rectangulo3)
        pygame.draw.rect(screen,color,rectangulo4)
        pygame.draw.rect(screen,color,rectangulo5)
        pygame.draw.rect(screen,color,rectangulo6)
        pygame.draw.rect(screen,color,rectangulo7)
        pygame.draw.rect(screen,color,rectangulo8)
        pygame.draw.rect(screen,color,rectangulo9
        )
        #Indice variables
        scoreplayer1 = font.render(str(variable1), True, BLACK)
        scoreplayer2 = font.render(str(variable2), True, BLACK)
        scoreplayer3 = font.render(str(variable3), True, BLACK)
        scoreplayer4 = font.render(str(variable4), True, BLACK)
        screen.blit(scoreplayer1, (50 ,50,10,10))
        screen.blit(scoreplayer2, (50,100,10,10))
        screen.blit(scoreplayer3, (50,150,10,10))
        screen.blit(scoreplayer4, (50,200,10,10))
        #valor variables
        score1 = font.render(str(maquina.getvariableA()), True, BLACK)
        score2 = font.render(str(maquina.getVariableB()), True, BLACK)
        score3 = font.render(str(maquina.getVariableC()), True, BLACK)
        score4 = font.render(str(maquina.getVariableT()), True, BLACK)
        screen.blit(score1, (100 ,50,10,10))
        screen.blit(score2, (100 ,100,10,10))
        screen.blit(score3, (100 ,150,10,10))
        screen.blit(score4, (100 ,200,10,10))
        #titulo
        textVari = font.render(str(textVar), True, BLACK)
        screen.blit(textVari, (30 ,10,10,10))

        #ingresado
        textEntre = font.render(str(textEntrada), True, BLACK)
        screen.blit(textEntre, (410 ,410,10,10))

        ingresar = font.render(str(maquina.getValor("")), True, BLACK)
        screen.blit(ingresar, (450 ,450,10,10))

        maquina.configurarMaquina()
        maquina.escribirPrograma()        
        pygame.display.update()








