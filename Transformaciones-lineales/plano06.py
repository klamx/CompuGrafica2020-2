import pygame

from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	origen = [ANCHO // 2, ALTO // 2]
	p = [50, 120]
	
	a = 5
	reloj = pygame.time.Clock()

	fin = False

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True


		# animacion
		# rotacion pantalla
		pr = rotacionHoraria(p, a)
		Plano(pantalla, origen)
		# Punto(pantalla, p)
		# Punto(pantalla, pr, VERDE)
		
		# rotacion cartesiano
		pc = CartesianoAPantalla(origen, pr)
		Punto(pantalla, pc, VERDE)
		pygame.display.flip()
		a += 5
		reloj.tick(60)