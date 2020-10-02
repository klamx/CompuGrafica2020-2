import pygame
import math
from library import *
# r = amplitud cos n teta

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    reloj = pygame.time.Clock()
    origen = [400, 300]
    n = 5
    amp = 360 // n
    radio = 100
    valRot = 0
    ls = []
    for i in range(n):
        angulo = i * amp
        pc = polar_a_cartesiano(radio, angulo)
        pp = CartesianoAPantalla(origen, pc)
        ls.append(pp)
        print angulo
    
    Plano(pantalla, origen)
    pygame.draw.polygon(pantalla, VERDE, ls, 1)
    pygame.display.flip()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        ls = []
        for i in range(n):
            angulo = i * amp
            pc = polar_a_cartesiano(radio, angulo + valRot)
            pp = CartesianoAPantalla(origen, pc)
            ls.append(pp)
            print angulo
    
        pantalla.fill(NEGRO)
        Plano(pantalla, origen)
        pygame.draw.polygon(pantalla, VERDE, ls, 1)
        pygame.display.flip()
        valRot += 5
        reloj.tick(30)

    pygame.quit()