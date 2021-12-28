import math

import pygame
import sys


import sys
from pygame import gfxdraw
from src.DiGraph import DiGraph

# Load and initialize the modules here
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

FONT = pygame.font.SysFont('Arial', 15, bold=True)

WIDTH, HEIGHT = 900, 740


def scale(data, min_screen, max_screen, min_data, max_data):
    """get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions"""
    if max_data - min_data == 0:
        return min_screen
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


class Button:

    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.rect = pygame.Rect((0, 0), (100, 80))
        self.on_click = None

    def add_click_listener(self, func):
        self.on_click = func

    def render(self, surface, pos, color, newSize):
        self.rect.update(self.rect.left, self.rect.top, newSize[0], newSize[1])
        self.rect.topleft = pos
        title_srf = FONT.render(self.title, True, pygame.Color(color))
        title_rect = title_srf.get_rect(center=self.rect.center)
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(title_srf, title_rect)

    def check(self, click) -> bool:
        if self.rect.collidepoint(*click):
            return True
        return False

    def runTheFunc(self):
        self.on_click()


class GUI:

    def __init__(self, Algo, width: int, height: int):
        self.algo = Algo
        self.graph = self.algo.get_graph()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), depth=32, flags=pygame.constants.RESIZABLE)
        self.MainRun()

    def MainRun(self):

        # variables - special
        Path = []
        MarkedNodes = {}
        NodeRects = {}
        center_id = 0
        next_id = max(self.graph.get_all_v().values(), key=lambda n: n.Id).Id + 1
        pygame.display.set_caption('I AM THE GUI, FEEL MY POWER!!!')

        # Booleans
        added_A_Node = False
        centerExists = False

        # Colors
        screenColor = (255, 255, 255)  # white
        NodeColor = (0, 48, 142)  # #00308E
        NodeIdColor = (255, 255, 255)  # white
        ArrowColor = (120, 81, 185)  # #7851B9
        MarkedNodeColor = (254, 223, 0)  # #FEDF00
        MarkedArrowColor = (0, 0, 0)  # Black (137, 108, 5)  # #896c05
        ButtonColor = NodeColor  # Blue
        ButtonTextColor = screenColor
        CenterNodeColor = (0, 0, 0)  # Black

        # Buttons
        Add_Edge = Button('Add Edge', ButtonColor)
        Add_Node = Button('Add Node', ButtonColor)
        Coor = Button('Coordinates:', (255, 255, 255))
        Clean = Button('Clean', ButtonColor)
        Center = Button('Center', ButtonColor)
        Shortest_Path = Button('Shortest Path', ButtonColor)
        TSP = Button('TSP', ButtonColor)

        # Parameters
        ArrowWidth = 1
        NodeRadius = 10
        OuterMargin = 7
        upperOuterMargin = self.screen.get_height() * (1 / OuterMargin)
        lowerOuterMargin = self.screen.get_height() * ((OuterMargin - 1) / OuterMargin)
        ButtonMargin = 6
        margin = + 50 + (self.screen.get_height() * (1 / OuterMargin))
        ArrowSize = 10
        MarkedWidth = int(ArrowWidth * 10)
        MarkedArrowSize = int(ArrowSize*1.5)

        # Compact
        MarkedArrowSettings = {'size': MarkedArrowSize, 'width': MarkedWidth, 'color': MarkedArrowColor}
        ArrowSettings = {'size': ArrowSize, 'width': ArrowWidth, 'color': ArrowColor}

        # Coordinates
        add_x = 0
        add_y = 0
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
                if event.type == pygame.MOUSEBUTTONUP:
                    click = pygame.mouse.get_pos()

                    # Get the Coordinates for Adding a Node
                    if upperOuterMargin < click[1] < lowerOuterMargin:
                        add_x = scale(click[0], min_x, max_x, margin, self.screen.get_width() - margin)
                        add_y = scale(click[1], min_y, max_y, margin, self.screen.get_height() - margin)
                        Coor.title = "({},{})".format(add_x, add_y)
                        Add_Node.add_click_listener(lambda: self.algo.get_graph().add_node(next_id, (add_x, add_y)))

                    # Add a new Node to the Graph
                    if Add_Node.check(click) is True:
                        if Add_Node.on_click is not None:
                            Add_Node.title = "Add Node"
                            Add_Node.runTheFunc()
                            next_id += 1
                            added_A_Node = True
                        else:
                            Add_Node.title = "No Coordinates"

                    # Add a new Edge to the Graph
                    if Add_Edge.check(click) is True:
                        if len(MarkedNodes) == 2:
                            Add_Edge.title = "Add Edge"
                            Add_Edge.runTheFunc()
                            MarkedNodes.clear()
                        elif len(MarkedNodes) < 2:
                            Add_Edge.title = "Needs 2 nodes"
                        else:
                            Add_Edge.title = "Too many nodes"

                    # Show the Shortest Path
                    if Shortest_Path.check(click) is True:
                        if len(MarkedNodes) == 2:
                            dist, Path = Shortest_Path.on_click()
                            Shortest_Path.title = "Dist: {:.5f}".format(dist)
                            Path = self.arrangePath(Path)
                        elif len(MarkedNodes) < 2:
                            Shortest_Path.title = "Needs 2 nodes"
                        else:
                            Shortest_Path.title = "Too many nodes"

                    # show the TSP
                    if TSP.check(click) is True:
                        if len(MarkedNodes) == 0:
                            TSP.title = "Needs a node"
                        else:
                            Path, dist = TSP.on_click()
                            TSP.title = "Dist: {:.5f}".format(dist)
                            if dist != math.inf:
                                Path = self.arrangePath(Path)
                            else:
                                TSP.title = "No Path"
                                Path = []

                    # show the Center
                    if Center.check(click) is True:
                        center_id, dist = self.algo.centerPoint()
                        if dist == math.inf:
                            Center.title = "No Center"
                        else:
                            Center.title = "{}, Dist: {:.5f}".format(center_id,dist)
                            centerExists = True

                    # Check if the user Clicked on a Node
                    for v in NodeRects.items():
                        if v[1].collidepoint(*click):
                            MarkedNodes[v[0]] = 1
                            TSP.add_click_listener(lambda: self.algo.TSP(list(MarkedNodes)))
                            break

                    # Checks if we have Exactly two marked nodes
                    if len(MarkedNodes) == 2:
                        node1 = list(MarkedNodes)[0]
                        node2 = list(MarkedNodes)[1]
                        Add_Edge.add_click_listener(lambda: self.algo.get_graph().add_edge(node1, node2, 0))
                        Shortest_Path.add_click_listener(lambda: self.algo.shortest_path(node1, node2))

                    # Clean the screen
                    if Clean.check(click) is True:
                        MarkedNodes.clear()
                        Path.clear()
                        centerExists = False
                        Add_Edge.title = "Add Edge"
                        Add_Node.title = "Add Node"
                        Shortest_Path.title = "Shortest path"
                        TSP.title = "TSP"
                        Center.title = "Center"

            self.screen.fill(pygame.Color(screenColor))

            # Update the variables if we added a new Node
            if added_A_Node is True:
                added_A_Node = False
                min_x = min(self.graph.get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
                max_x = max(self.graph.get_all_v().values(), key=lambda n: n.pos[0]).pos[0]
                min_y = min(self.graph.get_all_v().values(), key=lambda n: n.pos[1]).pos[1]
                max_y = max(self.graph.get_all_v().values(), key=lambda n: n.pos[1]).pos[1]

            # Render the Margins
            upperOuterMargin = self.screen.get_height() * (1 / OuterMargin)
            lowerOuterMargin = self.screen.get_height() * ((OuterMargin - 1) / OuterMargin)

            pygame.draw.aaline(self.screen, pygame.Color((0, 0, 0)), (0, upperOuterMargin),
                               (self.screen.get_width(), upperOuterMargin), 1)
            pygame.draw.aaline(self.screen, pygame.Color((0, 0, 0)),
                               (0, lowerOuterMargin),
                               (self.screen.get_width(), lowerOuterMargin),
                               1)

            # Render The Buttons - 8 blocks
            upperButtonMargin = upperOuterMargin * (1 / ButtonMargin)
            lowerButtonMargin = lowerOuterMargin + upperButtonMargin
            Add_Edge.render(self.screen, ((2 / 32) * self.screen.get_width(), upperButtonMargin), ButtonTextColor,
                            ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            Add_Node.render(self.screen, ((10 / 32) * self.screen.get_width(), upperButtonMargin), ButtonTextColor,
                            ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            Coor.render(self.screen, ((17 / 32) * self.screen.get_width(), upperButtonMargin), (0, 0, 0),
                        ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            Clean.render(self.screen, ((25 / 32) * self.screen.get_width(), upperButtonMargin), ButtonTextColor,
                         ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            Center.render(self.screen, ((4 / 64) * self.screen.get_width(), lowerButtonMargin), ButtonTextColor,
                          ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            Shortest_Path.render(self.screen, ((27 / 64) * self.screen.get_width(), lowerButtonMargin), ButtonTextColor,
                                 ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))
            TSP.render(self.screen, ((50 / 64) * self.screen.get_width(), lowerButtonMargin), ButtonTextColor,
                       ((5 / 32) * self.screen.get_width(), upperOuterMargin - 2 * upperButtonMargin))

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

            # Draw the Marked Edges
            for src_id, dest_id in Path:
                src_x = scale(self.graph.getNode(src_id).pos[0], margin, self.screen.get_width() - margin, min_x,
                              max_x)
                src_y = scale(self.graph.getNode(src_id).pos[1], margin, self.screen.get_height() - margin, min_y,
                              max_y)
                dest_x = scale(self.graph.getNode(dest_id).pos[0], margin, self.screen.get_width() - margin, min_x,
                               max_x)
                dest_y = scale(self.graph.getNode(dest_id).pos[1], margin, self.screen.get_height() - margin, min_y,
                               max_y)
                self.drawArrow(src_x, src_y, dest_x, dest_y, NodeRadius, MarkedArrowSettings)

            # Draw the nodes
            NodeRects = {}
            for v in self.graph.get_all_v().values():
                x = scale(v.pos[0], margin, self.screen.get_width() - margin, min_x, max_x)
                y = scale(v.pos[1], margin, self.screen.get_height() - margin, min_y, max_y)
                if v.Id in MarkedNodes:
                    pygame.gfxdraw.aacircle(self.screen, int(x), int(y), NodeRadius, pygame.Color(MarkedNodeColor))
                    pygame.gfxdraw.filled_circle(self.screen, int(x), int(y), NodeRadius, pygame.Color(MarkedNodeColor))
                else:
                    pygame.gfxdraw.aacircle(self.screen, int(x), int(y), NodeRadius, pygame.Color(NodeColor))
                    pygame.gfxdraw.filled_circle(self.screen, int(x), int(y), NodeRadius, pygame.Color(NodeColor))
                id_srf = FONT.render(str(v.Id), True, pygame.Color(NodeIdColor))
                rect = id_srf.get_rect(center=(x, y))
                NodeRects[v.Id] = rect
                self.screen.blit(id_srf, rect)

            # Draw the center
            if centerExists is True:
                x = scale(self.graph.getNode(center_id).pos[0], margin, self.screen.get_width() - margin, min_x, max_x)
                y = scale(self.graph.getNode(center_id).pos[1], margin, self.screen.get_height() - margin, min_y, max_y)
                pygame.gfxdraw.aacircle(self.screen, int(x), int(y), NodeRadius, pygame.Color(CenterNodeColor))
                pygame.gfxdraw.filled_circle(self.screen, int(x), int(y), NodeRadius, pygame.Color(CenterNodeColor))
                id_srf = FONT.render(str(self.graph.getNode(center_id).Id), True, pygame.Color(NodeIdColor))
                rect = id_srf.get_rect(center=(x, y))
                NodeRects[self.graph.getNode(center_id).Id] = rect
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

    def arrangePath(self, path: list):
        newPath = []
        for i in range(len(path) - 1):
            newPath.append((path[i], path[i + 1]))
        return newPath


if __name__ == '__main__':
    print("hi")
    # jsonFileName = "A1.json"
    # algo = GraphAlgo()
    # algo.load_from_json("../data/{}".format(jsonFileName))
    # gui = GUI(algo, WIDTH, HEIGHT)
