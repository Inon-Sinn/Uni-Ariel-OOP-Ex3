import math

import pygame
import time
import src.api
from pygame.locals import *

constants = Constants()
width = constants.screenWidth;
height = constants.screenHeigh;
pygame.init()
screen = pygame.display.set_mode((width, height))

def __init__(dwg, dwgalgo):
   self.DWG = dwg
   self.DWGAlgo = dwgalgo
def main():
    background_color = constants.screenColor
    screen.fill(background_color)
    pygame.display.flip()
    running = True
    while running:
        left = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_circle(pygame.mouse.get_pos())
        time.sleep(0.03)
        pygame.display.update()


def draw_circle(pos):
    pygame.draw.circle(screen,constants.nodeColor, pos, 5)
def draw_arrow(src, dest):
    pygame.draw.line(src,dest)
    # get the angle of the line
    angle = math.atan(dest.y-src.y,dest.x-src.x)
    # get first point
    point1 = (dest.y - math.sin(angle+math.pi/6) * 5, dest.x - math.cos(angle + math.py/6) * 5)
    #get second point
    point2 = (dest.y - math.sin(angle - math.pi/6) * 5, dest.x - math.sin(angle - math.pi/6) * 5)
    # draw the lines
    pygame.draw.line(screen,constants.arrowColor,dest, point1)
    pygame.draw.line(screen,constants.arrowColor,dest,point2)
def drawNodes():
    for node in self.DWG.get_all_v().values:
        pos = node.getPos()
        draw_circle(pos)
def drawEdges():
    for edge in self.DWG.get_all_e().values:
        src = edge.getSrcPos()
        dest = edge.getDestPos()
        draw_arrow(src,dest)


if __name__ == '__main__':
    main()