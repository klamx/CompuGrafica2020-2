import pygame

from library import *


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	fin = False

	pointIndex = 0
	points = [[0, 0], [0, 0]]
	pointList = []

	tx = 0
	ty = 0
	T = [tx, ty]

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if pointIndex < 3:
					pointList.append(event.pos)
					pygame.draw.circle(pantalla, MORADO, event.pos, 3, 1)
					pointIndex += 1

				#if pointIndex == 3:
				#	pygame.draw.polygon(pantalla, VERDE, pointList, 1)
				#	pointIndex = 0
					#pointList = []

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pointIndex = 0
					pointList = []
					T[0] = 0
					T[1] = 0
					pantalla.fill(NEGRO)

				if event.key == pygame.K_RIGHT:
					T[0] += 5

				if event.key == pygame.K_LEFT:
					T[0] -= 5


		# Linea
		#for p in pointList:
		#	Punto(pantalla, p)	

		pointList2 = pointList

		ls_t = []
		for p in pointList2:
			pt = traslacion(p, T)
			# Punto(pantalla, pt, VERDE)
			ls_t.append(pt)

		pantalla.fill(NEGRO)
		if pointIndex == 3:
			pygame.draw.polygon(pantalla, VERDE, pointList, 1)
			pygame.draw.polygon(pantalla, BLANCO, ls_t, 1)

		pygame.display.flip()