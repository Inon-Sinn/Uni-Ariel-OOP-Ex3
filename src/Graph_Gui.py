import math

import pygame

from pygame import gfxdraw
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph

# Load and initialize the modules here
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

FONT = pygame.font.SysFont('Arial', 15, bold=True)

WIDTH, HEIGHT = 800, 600


def scale(data, min_screen, max_screen, min_data, max_data):
    """get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions"""
    if max_data - min_data == 0:
        return min_screen
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


class Button:

    def __init__(self, title, size, color):
        self.title = title
        self.size = size
        self.color = color
        self.rect = pygame.Rect((0, 0), size)
        self.on_click = None

    def add_click_listener(self, func):
        self.on_click = func

    def render(self, surface, pos, color):
        self.rect.topleft = pos
        title_srf = FONT.render(self.title, True, pygame.Color(color))
        title_rect = title_srf.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(title_srf, title_rect)

    def check(self):
        if self.on_click != None:
            mouse_pos = pygame.mouse.get_pos()



class Graph_GUI:

    def __init__(self, algo: GraphAlgo, width: int, height: int):
        self.algo = algo
        self.graph = self.algo.get_graph()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), depth=32, flags=pygame.constants.RESIZABLE)
        self.MainRun()

    def MainRun(self):
        b = Button('click', (70, 50), (0, 0, 0))
        # variables
        center_id = None
        pygame.display.set_caption('The Ultimate Graph GUI?!?')
        # Colors
        screenColor = (255, 255, 255)  # white
        NodeColor = (0, 48, 142)  # #00308E
        NodeIdColor = (255, 255, 255)  # black
        ArrowColor = (120, 81, 185)  # #7851B9
        MarkedColor = (254, 223, 0)  # #FEDF00
        # Parameters
        ArrowWidth = 1
        NodeRadius = 10
        margin = 50
        ArrowSize = 10
        MarkedWidth = ArrowWidth * 1.5
        # Compact
        MarkedSettings = {'width': MarkedWidth, 'color': MarkedColor}
        ArrowSettings = {'size': ArrowSize, 'width': ArrowWidth, 'color': ArrowColor}
        # Coordinates
        min_x = min(self.graph.get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
        max_x = max(self.graph.get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
        min_y = min(self.graph.get_all_v().values(), key=lambda n: n.pos[1]).pos[1]
        max_y = max(self.graph.get_all_v().values(), key=lambda n: n.pos[1]).pos[1]
        # Run the GUI
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            self.screen.fill(pygame.Color(screenColor))
            # Render The Buttons
            b.render(self.screen, (100, 100), (255, 255, 255))

            # Draw the edges
            for src in self.graph.get_all_v().values():
                for dest_id in self.graph.all_out_edges_of_node(src.Id):
                    src_x = scale(src.pos[0], margin, self.screen.get_width() - margin, min_x,
                                  max_x)
                    src_y = scale(src.pos[1], margin, self.screen.get_height() - margin, min_y,
                                  max_y)
                    dest_x = scale(self.graph.getNode(dest_id).pos[0], margin, self.screen.get_width() - margin, min_x,
                                   max_x)
                    dest_y = scale(self.graph.getNode(dest_id).pos[1], margin, self.screen.get_height() - margin, min_y,
                                   max_y)
                    self.drawArrow(src_x, src_y, dest_x, dest_y, NodeRadius, ArrowSettings)

            # Draw the nodes
            for v in self.graph.get_all_v().values():
                x = scale(v.pos[0], margin, self.screen.get_width() - margin, min_x, max_x)
                y = scale(v.pos[1], margin, self.screen.get_height() - margin, min_y, max_y)
                pygame.gfxdraw.aacircle(self.screen, int(x), int(y), NodeRadius, pygame.Color(NodeColor))
                pygame.gfxdraw.filled_circle(self.screen, int(x), int(y), NodeRadius, pygame.Color(NodeColor))
                pygame.draw.circle(self.screen, pygame.Color(NodeColor), (x, y), NodeRadius)
                id_srf = FONT.render(str(v.Id), True, pygame.Color(NodeIdColor))
                rect = id_srf.get_rect(center=(x, y))
                self.screen.blit(id_srf, rect)

            pygame.display.update()
            clock.tick(60)

    def drawArrow(self, src_x, src_y, dest_x, dest_y, nodeRadius, ArrowSettings):
        # Calculate the vector between source and dest
        vector_x = dest_x - src_x
        vector_y = dest_y - src_y
        # Normalize the Vector
        dist = math.dist([dest_x, dest_y], [src_x, src_y])
        if dist == 0:
            vector_x = 0
            vector_y = 0
        else:
            vector_x = vector_x / dist
            vector_y = vector_y / dist
        # Calculate a point before the node
        new_x = src_x + (dist - nodeRadius) * vector_x
        new_y = src_y + (dist - nodeRadius) * vector_y
        # draw the Arrow
        pygame.draw.aaline(self.screen, pygame.Color(ArrowSettings['color']), (src_x, src_y), (dest_x, dest_y),
                           ArrowSettings['width'])
        rotation = math.degrees(math.atan2(src_y - dest_y, dest_x - src_x)) + 90
        pygame.draw.polygon(self.screen, pygame.Color(ArrowSettings['color']), (
            (new_x, new_y), (
                new_x + ArrowSettings['size'] * math.sin(math.radians(rotation - 160)),
                new_y + ArrowSettings['size'] * math.cos(math.radians(rotation - 160))), (
                new_x + ArrowSettings['size'] * math.sin(math.radians(rotation - 200)),
                new_y + ArrowSettings['size'] * math.cos(math.radians(rotation - 200)))))


if __name__ == '__main__':
    algo = GraphAlgo()
    algo.load_from_json("../data/A1.json")
    gui = Graph_GUI(algo, WIDTH, HEIGHT)
