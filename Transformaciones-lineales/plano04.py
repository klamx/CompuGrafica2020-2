import pygame
from library import *

def Escala(punto, s):
	xp = p[0] * s[0]
	yp = p[1] * s[1]
	return [xp, yp]


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	fin = False

	origen = [100, 500]

	ls = [[100, 60], [200, 60], [200, 90]]
	S = [2, 2]

	ls_e = []
	for p in ls:
		pe = Escala(p, S)
		ls_e.append(pe)

	ls_e_car = []
	for p in ls_e:
		pe = CartesianoAPantalla(origen, p)
		ls_e_car.append(pe)


	print ls_e
	# pygame.draw.polygon(pantalla, BLANCO, ls, 1)
	# pygame.draw.polygon(pantalla, VERDE, ls_e, 1)
	pygame.draw.polygon(pantalla, VERDE, ls_e_car, 1)
	Plano(pantalla, origen)
	pygame.display.flip()



	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True