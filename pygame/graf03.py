import pygame

ANCHO = 800
ALTO = 600

if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO, ALTO])

	fin = False
	ancho_obj = 20
	pos_x = 200
	pos_y = 200
	vel_x = 0
	vel_y = 0
	reloj = pygame.time.Clock()

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					vel_x = 10
					vel_y = 0

				if event.key == pygame.K_LEFT:
					vel_x = -10
					vel_y = 0

				if event.key == pygame.K_UP:
					vel_x = 0
					vel_y = -10

				if event.key == pygame.K_DOWN:
					vel_x = 0
					vel_y = 10

				if event.key == pygame.K_SPACE:
					vel_x = 0
					vel_y = 0

			# if event.type == pygame.KEYUP:
			#	vel_x = 0
			#	vel_y = 0

		if pos_x >= ANCHO:
			vel_x = 0
			pos_x = pos_x - ancho_obj
		
		if pos_x <= 0:
			vel_x = 0
			pos_x = pos_x + ancho_obj

		if pos_y >= ALTO:
			vel_y = 0
			pos_y = pos_y - ancho_obj
		
		if pos_y <= 0:
			vel_y = 0
			pos_y = pos_y + ancho_obj

		pos_x += vel_x
		pos_y += vel_y

		pos = [pos_x, pos_y]
		pantalla.fill((0, 0, 0))
		pygame.draw.circle(pantalla, (0, 255, 0), pos, ancho_obj)
		pygame.display.flip()
		reloj.tick(30)

	pygame.quit()