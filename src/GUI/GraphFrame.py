import math

import pygame
import time

from src.DiGraph import DiGraph, Node
from src.GUI import Constants
from pygame.locals import *
constants = Constants
width = constants.screenWidth
height = constants.screenHeight
pygame.init()
screen = pygame.display.set_mode((width, height))
g = DiGraph
n = Node


# def __init__(dwg, dwgalgo):
#     self.g = dwg
#     self.DWGAlgo = dwgalgo


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
    pygame.draw.circle(screen, constants.nodeColor, pos, 5)


def draw_arrow(src, dest):
    pygame.draw.line(src, dest)
    # get the angle of the line
    angle = math.atan(dest.y - src.y)
    # get first point
    point1 = (dest.y - math.sin(angle + math.pi / 6) * 5, dest.x - math.cos(angle + math.pi / 6) * 5)
    # get second point
    point2 = (dest.y - math.sin(angle - math.pi / 6) * 5, dest.x - math.sin(angle - math.pi / 6) * 5)
    # draw the lines
    pygame.draw.line(screen, constants.arrowColor, dest, point1)
    pygame.draw.line(screen, constants.arrowColor, dest, point2)


def drawGraph():
    for n in g.get_all_v().values():
        pos = n.getPos()
        draw_circle(pos)
        for e in g.all_in_edges_of_node(n):
            drawEdges(e)

def drawEdges(edge):
        src = edge.src
        dest = edge.dest
        draw_arrow(src, dest)


if __name__ == '__main__':
    main()
