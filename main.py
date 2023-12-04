import pygame

pygame.init()
#Liens vers les tuto :
#https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/
#https://www.youtube.com/watch?v=G8MYGDf_9ho

#Taille de la fenetre / Titre et Icone de mon Prog /
ecran = pygame.display.set_mode((800,500))
pygame.display.set_caption("Pendu THE Game")   	
logoapp = pygame.image.load("d:/WebDev/Projet/pendu/ressources/logoapp.png").convert()
pygame.display.set_icon(logoapp)

#Background et Police
background = pygame.image.load("d:/WebDev/Projet/pendu/ressources/background.jpg").convert()
font = pygame.font.SysFont("arialblack", 20)
text_color = (242, 190, 109)

#Images des boutons
new_word_img = pygame.image.load("d:/WebDev/Projet/pendu/ressources/new_word.png").convert_alpha()
new_game_img = pygame.image.load("d:/WebDev/Projet/pendu/ressources/new_game.png").convert_alpha()
exit_img = pygame.image.load("d:/WebDev/Projet/pendu/ressources/exit.png").convert_alpha()

#Classe des boutons
class Bouton():
    def __init__(self, x, y, image, scale):
          width = image.get_width()
          height = image.get_height()
          self.image = pygame.transform.scale (image, (int(width * scale), int(height * scale)))
          self.rect = self.image.get_rect()
          self.rect.topleft = (x, y)
          self.clicked = False

    def afficher(self):
        click = False
        #Affiche la positions de la souris
        souris = pygame.mouse.get_pos()

        #Mouseover et click
        if self.rect.collidepoint(souris):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                click = True
            if pygame.mouse.get_pressed()[0] == 0:
                 self.clicked = False
        #Affiche les boutons à l'ecran
        ecran.blit(self.image, (self.rect.x, self.rect.y))
        return click

#Creation des boutons
word_button = Bouton (150, 100, new_word_img, 2)
game_button = Bouton (450, 100, new_game_img, 2)
exit_button = Bouton (300, 300, exit_img, 2)




#Boucle qui permet de faire tourner mon programme
continuer = True
while continuer:

    ecran.blit(background, (0, 0))#defini la position avec les valeurs
    
    if word_button.afficher():
         print ("Word")
    if game_button.afficher():
         print ("Jouer")
    if exit_button.afficher():
         continuer = False

    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Vérifiez si la touche "F4" est enfoncée
                if event.key == pygame.K_F4:
                    # Vérifiez si la touche "Alt" est également enfoncée
                    if event.mod & pygame.KMOD_ALT:
                        continuer = False
            elif event.type == pygame.QUIT:
                continuer = False
    
    pygame.display.flip()

#Quitte proprement pygame, libère les ressources
pygame.quit()