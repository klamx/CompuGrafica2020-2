import pygame
from library import *

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    reloj = pygame.time.Clock()
    origen = [ANCHO // 2, ALTO // 2]
    ls = ([50, 100], [100, 100], [100, 150])
    r = 0

    # Pasar el triangulo original a cartesiano
    ls_to = []
    for i in ls:
        pc = CartesianoAPantalla(origen, i)
        ls_to.append(pc)

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        # Rotar Triangulo cartesiano
        ls_r = []
        for i in ls_to:
            pr = rotacionpfah(ls_to[1], i, origen, r)
            ls_r.append(pr)

        pantalla.fill(NEGRO)
        pygame.draw.polygon(pantalla, BLANCO, ls_to, 1)
        Plano(pantalla, origen)
        pygame.draw.polygon(pantalla, VERDE, ls_r, 1)
        pygame.display.flip()
        reloj.tick(30)
        r += 5

    pygame.quit()