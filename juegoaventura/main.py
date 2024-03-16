from sprites import *
import pygame

pygame.init()

ANCHO_VENTANA, ALTO_VENTANA = 680, 480

VENTANA_PRINCIPAL = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

#cartero = Personaje(nombre="Juan", imagen=imagen_personaje, coordenadas=(100, 250), tamaño=( 125, 55), velocidad=2)


reloj = pygame.time.Clock()

juego_terminado = False
while juego_terminado != True:

    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    VENTANA_PRINCIPAL.fill((255, 255, 255))

    VENTANA_PRINCIPAL.blit(sprites[0], (20, 10))
    VENTANA_PRINCIPAL.blit(sprites[1], (20, 70))
    VENTANA_PRINCIPAL.blit(sprites[2], (20, 120))
    VENTANA_PRINCIPAL.blit(sprites[3], (20, 190))
    #for sprite in range(0, len(sprites_correr)):
        #VENTANA_PRINCIPAL.blit(sprite, (120, 100))
    #cartero.draw(VENTANA_PRINCIPAL)
    #cartero.update()

    pygame.display.flip()