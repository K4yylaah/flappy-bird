import pygame

import assets
import configs
from objects.background import Background

#Initialisation de Pygame
pygame.init()

#Création de la fenêtre
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

#Configuration de l'horloge
clock = pygame.time.Clock()
running = True

#Chargement des sprites
assets.load_sprites()

try:
    # Récupération du sprite de fond
    background = assets.get_sprite("background")
except KeyError as e:
    print(f"Erreur : {e}")
    pygame.quit()
    exit()

#Création d'un groupe de sprites
sprites = pygame.sprite.LayeredUpdates()

#ajout du background au groupe de sprites
Background(sprites)

# Boucle principale du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplissage de l'écran avec une couleur de fond
    screen.fill("pink")  

    # Dessin des sprites
    sprites.draw(screen)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Contrôle de la fréquence d'images
