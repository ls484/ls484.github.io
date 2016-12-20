#Tic Tac Toe
#Lona Sharpstene


import os, sys
import random
import pygame
from pygame.locals import *

#need to def a method to create the empty board

My_red_color = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

APPLICATION_x_size = 600
APPLICATION_y_size = 600
screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
pygame.display.set_caption('Tic Tac Toe')
pygame.mouse.set_visible(True)
#pygame.mouse.set_visible(False)
black_square = pygame.Surface(screen.get_size())
black_square.fill((0, 0, 0))
screen.blit(black_square, (0, 0))
pygame.display.flip()

def drawX(x, y):
    pygame.draw.circle(screen, green, (x,y), 90)

def drawO(x, y):
    pygame.draw.circle(screen, blue, (x,y), 90)

#   11  12  13 
#   21  22  23
#   31  32  33
#if the turns time out, or if 3 in a row vertically, horizontally, diagonally x/o
def main():
    pygame.init()
    APPLICATION_x_size = 600
    APPLICATION_y_size = 600
    screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size))
    pygame.display.set_caption('Tic Tac Toe')
    pygame.mouse.set_visible(True)
    #pygame.mouse.set_visible(False)
    black_square = pygame.Surface(screen.get_size())
    black_square.fill((0, 0, 0))
    screen.blit(black_square, (0, 0))
    pygame.display.flip()
    turn = 0
    
    box11X = False; box110 = False
    box12X = False; box120 = False
    box13X = False; box130 = False
    box21X = False; box130 = False
    box22X = False; box220 = False
    box23X = False; box230 = False
    box31X = False; box310 = False
    box32X = False; box320 = False
    box33X = False; box330 = False
    
    while True:
        pygame.draw.rect(screen, My_red_color, (190, 0, 10, APPLICATION_y_size))
        pygame.draw.rect(screen, My_red_color, (390, 0, 10, APPLICATION_y_size))
        pygame.draw.rect(screen, My_red_color, (0, 190, APPLICATION_x_size, 10))
        pygame.draw.rect(screen, My_red_color, (0, 390, APPLICATION_x_size, 10))
        pygame.display.flip()
        
        mouseClicked = False
        
        for event in pygame.event.get():
         #this closes the window WOOHOO
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
             
         elif event.type == MOUSEBUTTONUP:
             mousex, mousey = event.pos
             if turn % 2 == 0:
                #box11
                if (mousex <= 190) and (mousey <= 190):
                    drawO(95, 95)
                    box110 = True
                #box12
                elif (mousex <= 390 and mousex > 190) and (mousey <= 190):
                    drawO(295, 95)
                    box120 = True
                #box13
                elif (mousex <= 600 and mousex > 390) and (mousey <= 190):
                    drawO(495, 95)
                    box130 = True
                    
                #box21
                elif (mousex <= 190) and (mousey <= 390 and mousey >190):
                    drawO(95, 295)
                    box210 = True
                #box22
                elif (mousex <= 390 and mousex > 190) and (mousey <= 390 and mousey >190):
                    drawO(295, 295)
                    box220 = True 
                #box23
                elif (mousex <= 600 and mousex > 390) and (mousey <= 390 and mousey >190):
                    drawO(495, 295)
                    box230 = True
                
                #box31
                elif (mousex <= 190) and (mousey <= 600 and mousey >390):
                    drawO(95, 495)
                    box310 = True
                #box32
                elif (mousex <= 390 and mousex > 190) and (mousey <= 600 and mousey >390):
                    drawO(295, 495)
                    box320 = True
                #box33
                elif (mousex <= 600 and mousex > 390) and (mousey <= 600 and mousey >390):
                    drawO(495, 495)
                    box330 = True
                 
             else:
                if (mousex <= 190) and (mousey <= 190):
                    drawX(95, 95)
                    box11X = True
                #box12
                elif (mousex <= 390 and mousex > 190) and (mousey <= 190):
                    drawX(295, 95)
                    box12X = True
                #box13
                elif (mousex <= 600 and mousex > 390) and (mousey <= 190):
                    drawX(495, 95)
                    box13X = True
                    
                #box21
                elif (mousex <= 190) and (mousey <= 390 and mousey >190):
                    drawX(95, 295)
                    box21X = True
                #box22
                elif (mousex <= 390 and mousex > 190) and (mousey <= 390 and mousey >190):
                    drawX(295, 295)
                    box22X = True
                #box23
                elif (mousex <= 600 and mousex > 390) and (mousey <= 390 and mousey >190):
                    drawX(495, 295)
                    box23X = True
                
                #box31
                elif (mousex <= 190) and (mousey <= 600 and mousey >390):
                    drawX(95, 495)
                    box31 = True
                #box32
                elif (mousex <= 390 and mousex > 190) and (mousey <= 600 and mousey >390):
                    drawX(295, 495)
                    box32X = True
                #box33
                elif (mousex <= 600 and mousex > 390) and (mousey <= 600 and mousey >390):
                    drawX(495, 495)
                    box33X = True
                 
                 
             turn += 1
             
         if (turn == 10) \
         or (box110 == True and box220 == True and box330 == True) \
         or (box11X == True and box22X == True and box33X == True) \
         or (box310 == True and box320 == True and box330 == True):
            #screen.fill((0,0,0))
            #pygame.display.update()
            fontObj = pygame.font.Font('freesansbold.ttf', 72)
            textSurfaceObj = fontObj.render('Green wins!', True, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (300, 300)
            pygame.draw.rect(screen, (0,0,0), (0, 0, APPLICATION_x_size, APPLICATION_y_size))
            pygame.display.set_caption('Winner!')
            screen.blit(textSurfaceObj, textRectObj)
            #pygame.display.update()
            
    #play again or exit buttons

#make a new screen that says who wins


if __name__ == '__main__':
    main()
    
