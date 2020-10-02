import pygame
import math
from library import *

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    origen = [400, 300]
    radio = 150
    a = 150
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True


        pCart = polar_a_cartesiano(radio, a)
        Punto(pantalla, pCart, VERDE)

        pp = CartesianoAPantalla(origen, pCart)
        Punto(pantalla, pp)
        Plano(pantalla, origen)

        pygame.display.flip()
        a += 5
        reloj.tick(30)

    pygame.quit()