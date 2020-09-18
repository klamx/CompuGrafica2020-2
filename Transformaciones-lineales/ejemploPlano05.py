import pygame

from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	origen = [ANCHO // 2, ALTO // 2]
	ls = [[50, 120], [100, 120]]
	
	a = 0
	reloj = pygame.time.Clock()

	fin = False

	Plano(pantalla, origen)

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		# Aplica rotacion a elementos de la lista
		ls_r = []
		for p in ls:
			pr = rotacionHoraria(p, a)
			ls_r.append(pr)

		# Trasnforma a cartesiano
		ls_c = []
		for p in ls_r:
			pc = CartesianoAPantalla(origen, p)
			ls_c.append(pc)


		pygame.draw.line(pantalla, VERDE, ls_c[0], ls_c[1])
		pygame.display.flip()
		a += 5
		reloj.tick(60)