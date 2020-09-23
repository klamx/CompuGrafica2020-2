import pygame

from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	origen = [ANCHO // 2, ALTO // 2]
	
	ls = [[20, 80], [100, 80]]

	tx = 5
	ty = 0
	T = [tx, ty]

	fin = False

	Plano(pantalla, origen)

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					T[0] += 5
					print T

				if event.key == pygame.K_LEFT:
					T[0] -= 5
					print T

		# Linea
		for p in ls:
			Punto(pantalla, p)	

		ls_t = []
		for p in ls:
			pt = traslacion(p, T)
			# Punto(pantalla, pt, VERDE)
			ls_t.append(pt)


		pantalla.fill(NEGRO)
		pygame.draw.line(pantalla, BLANCO, ls_t[0], ls_t[1])
		pygame.draw.line(pantalla, VERDE, ls[0], ls[1])
		pygame.display.flip()

	pygame.quit()