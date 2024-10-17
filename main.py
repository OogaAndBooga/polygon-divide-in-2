from polygon import Polygon
import pygame, sys
import math as mt

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Polygon!')

screen.fill('white')

poly = []
points = []

poly = Polygon()

stage = 1


def dpoint(pos):
    pygame.draw.circle(screen, 'black', pos, 1)


def drawPoly(poly):
    if stage == 1:

        if poly.edges == 1:
            dpoint(poly.vrt[0])
        elif poly.edges > 1:
            if poly.isNearStart(pygame.mouse.get_pos()):
                pygame.draw.circle(screen, 'black', poly.vrt[0], 4)
            else:
                dpoint(poly.vrt[0])
            for p in poly.vrt[1:]:
                dpoint(p)
            pygame.draw.lines(screen, 'black', False, poly.vrt)
    else:
        pygame.draw.lines(screen, 'black', True, poly.vrt)


# pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])
while True:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if stage == 1:
            if poly.isNearStart(pygame.mouse.get_pos()):
                stage = 2
                print(poly.vrt)
            else:
                poly.addVert(event.pos)

        elif stage == 2:
            pass

    screen.fill('chartreuse' + str(stage + 1))
    drawPoly(poly)

    pygame.display.update()
