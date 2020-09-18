import pygame

ANCHO = 800
ALTO = 600

VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
ROJO = [255, 0, 0]
NEGRO = [0, 0, 0]
BLANCO = [255, 255, 255]
MORADO = [107, 27, 154]

ColorList = [VERDE, AZUL, ROJO, BLANCO, MORADO]

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])
	pointList = [[100, 100], [200, 100], [100, 150]]		
	vel_x = 8
	reloj = pygame.time.Clock()
	fin = False

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		ls_aux = []

		for p in pointList:
			p[0] += vel_x

		pantalla.fill(NEGRO)
		pygame.draw.polygon(pantalla, VERDE, pointList, 1)
		pygame.display.flip()
		reloj.tick(60)