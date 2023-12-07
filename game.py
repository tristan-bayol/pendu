import pygame

pygame.init()


ecran = pygame.display.set_mode((800,500))   	
logoapp = pygame.image.load("d:/WebDev/Projet/pendu/ressources/logoapp.png").convert()
pygame.display.set_icon(logoapp)

running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Vérifiez si la touche "F4" est enfoncée
            if event.key == pygame.K_F4:
                # Vérifiez si la touche "Alt" est également enfoncée
                if event.mod & pygame.KMOD_ALT:
                    running = False
        elif event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()