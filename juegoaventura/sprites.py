import pygame

pygame.init()

def recortar_imagen(imagen_principal, coordenada_X, coordenada_Y, ancho, alto):
    return imagen_principal.subsurface(pygame.Rect(coordenada_X, coordenada_Y, ancho, alto))


class Personaje(pygame.sprite.Sprite):
    def __init__(self, nombre, objeto_spritesheets, coordenadas, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

        self.sprite_sheets = objeto_spritesheets

        self.rect = self.imagen.get_rect()
        self.rect.x = coordenadas[0]
        self.rect.y = coordenadas[1]

    def update(self):
        eventos = pygame.key.get_pressed()

        if eventos[pygame.K_LEFT]:
            self.rect.move_ip(-self.velocidad, 0)
        if eventos[pygame.K_RIGHT]:
            self.rect.move_ip(self.velocidad, 0)
        if eventos[pygame.K_UP]:
            self.rect.move_ip(0, -self.velocidad)
        if eventos[pygame.K_DOWN]:
            self.rect.move_ip(0, self.velocidad)

    def draw(self,ventana_juego):
        ventana_juego.blit(self.imagen, self.rect)

hoja_sprites = pygame.transform.scale(pygame.image.load("assets_villa/personaje.png"), (100, 200))
sprites = []

cordenada_y = 0
for _ in range(0, 4):
    sprite = recortar_imagen(hoja_sprites, 0, cordenada_y, 100, 50)

    sprites.append(sprite)

    cordenada_y += 50