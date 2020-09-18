import pygame

from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	p = [50, 120]
	a = 5
	reloj = pygame.time.Clock()

	fin = False

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		Punto(pantalla, p)
		pr = rotacionHoraria(p, a)
		Punto(pantalla, pr, MORADO)
		a += 5
		pygame.display.flip()