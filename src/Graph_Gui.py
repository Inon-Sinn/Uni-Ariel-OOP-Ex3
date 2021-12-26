import math

import pygame

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
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


class Graph_GUI:

    def __init__(self, Graph: DiGraph, width: int, height: int):
        self.graph = Graph
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), depth=32, flags=pygame.constants.RESIZABLE)
        self.MainRun()

    def MainRun(self):
        # variables
        pygame.display.set_caption('The Ultimate Graph GUI?!?')
        # Colors
        screenColor = (70, 70, 255)  # BLue
        NodeColor = (200, 200, 50)  # Yellow
        NodeIdColor = (0, 0, 0)  # Black
        ArrowColor = (255, 255, 255)  # White
        # Parameters
        ArrowWidth = 1
        NodeRadius = 15
        margin = 50
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
                    pygame.draw.line(self.screen, pygame.Color(ArrowColor), (src_x, src_y), (dest_x, dest_y),
                                     width=ArrowWidth)
                    pygame.draw.line(self.screen, pygame.Color(ArrowColor), (src_x, src_y), (dest_x, dest_y), ArrowWidth)
                    # rotation = math.degrees(math.atan2(src_y - dest_y, dest_x - src_x)) + 90
                    # pygame.draw.polygon(self.screen, pygame.Color(ArrowColor), (
                    # (dest_x + 20 * math.sin(math.radians(rotation)), dest_y + 20 * math.cos(math.radians(rotation))), (
                    # dest_x + 20 * math.sin(math.radians(rotation - 120)),
                    # dest_y + 20 * math.cos(math.radians(rotation - 120))), (
                    # dest_x + 20 * math.sin(math.radians(rotation + 120)),
                    # dest_y + 20 * math.cos(math.radians(rotation + 120)))))

            # Draw the nodes
            for v in self.graph.get_all_v().values():
                x = scale(v.pos[0], margin, self.screen.get_width() - margin, min_x, max_x)
                y = scale(v.pos[1], margin, self.screen.get_height() - margin, min_y, max_y)
                pygame.draw.circle(self.screen, pygame.Color(NodeColor), (x, y), NodeRadius)
                id_srf = FONT.render(str(v.Id), True, pygame.Color(NodeIdColor))
                rect = id_srf.get_rect(center=(x, y))
                self.screen.blit(id_srf, rect)

            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(0, (0, 10, 0))
    graph.add_node(1, (5, 5, 0))
    graph.add_node(2, (10, 0, 0))
    graph.add_edge(0, 1, 0)
    graph.add_edge(1, 2, 0)
    gui = Graph_GUI(graph, WIDTH, HEIGHT)
