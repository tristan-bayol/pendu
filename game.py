import pygame
import random

pygame.init()
def newgame():
    #Choisi un mot aléatoire dans le fichier et l'ajoute à la liste
    liste = []

    with open("d:/WebDev/Projet/pendu/mots.txt", "r") as mot:
        for x in mot:
            liste.append(x.strip())#.strip() formate x pour retirer les sauts de lignes

    random_word = random.choice(liste)
    print(random_word)

    ecran = pygame.display.set_mode((800,500))   	
    logoapp = pygame.image.load("d:/WebDev/Projet/pendu/ressources/logoapp.png").convert()
    pygame.display.set_icon(logoapp)

    running = True

    font = pygame.font.Font(None, 40)
    cadre_mot_deviner = pygame.Rect(100, 400, 200, 40)
    color = pygame.Color('black')
    mot_deviner =  " ".join("_" for _ in random_word)


    #Boucle principale qui permet d'executer le jeu
    while running :
        pygame.display.set_caption("Game")
        ecran.fill("white")
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Vérifiez si la touche "F4" est enfoncée
                if event.key == pygame.K_F4:
                    # Vérifiez si la touche "Alt" est également enfoncée
                    if event.mod & pygame.KMOD_ALT:
                        running = False
            elif event.type == pygame.QUIT:
                running = False

    #Paramètres de la zone de du mot a deviner
        txt_surface = font.render(mot_deviner, True, color)
        width = max(100, txt_surface.get_width()+10)
        cadre_mot_deviner.w = width
        ecran.blit(txt_surface, (cadre_mot_deviner.x+5, cadre_mot_deviner.y+5))
        pygame.draw.rect(ecran, color, cadre_mot_deviner, 4)
        pygame.display.flip()
    pygame.quit()

newgame()