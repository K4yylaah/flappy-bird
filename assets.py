import os
import pygame

# Dictionnaire global pour stocker les sprites
sprites = {}

def load_sprites():
    """
    Charge tous les sprites nécessaires dans le dictionnaire global `sprites`.
    """
    global sprites
    
    # Chemin relatif ou absolu pour les ressources
    background_path = os.path.join("assets", "background-day.png")
    
    # Vérifier si le fichier existe avant de le charger
    if not os.path.exists(background_path):
        print(f"Erreur : le fichier '{background_path}' est introuvable.")
        return

    try:
        # Charger l'image et la stocker dans le dictionnaire `sprites`
        sprites["background"] = pygame.image.load(background_path).convert()
        print(f"Sprite 'background' chargé avec succès depuis '{background_path}'.")
    except pygame.error as e:
        print(f"Erreur lors du chargement de '{background_path}': {e}")

def get_sprite(name):
    """
    Récupère un sprite par son nom dans le dictionnaire `sprites`.
    
    :param name: Nom du sprite à récupérer
    :return: L'objet sprite correspondant
    :raises KeyError: Si le sprite n'est pas trouvé
    """
    if name not in sprites:
        raise KeyError(f"Sprite '{name}' introuvable dans les assets.")
    return sprites[name]
