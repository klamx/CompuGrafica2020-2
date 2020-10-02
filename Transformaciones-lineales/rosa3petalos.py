import pygame
import math
from library import *
# r = amplitud cos n teta

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    origen = [400, 300]
    angulo = 0
    amplitud = 100
    radio = amplitud * math.cos(3 * math.radians(angulo))
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True


        pCart = polar_a_cartesiano(radio, angulo)
        # Punto(pantalla, pCart, VERDE)

        pp = CartesianoAPantalla(origen, pCart)
        Punto(pantalla, pp)
        Plano(pantalla, origen)

        pygame.display.flip()
        angulo += 2
        radio = amplitud * math.cos(3 * math.radians(angulo))
        reloj.tick(30)

    pygame.quit()