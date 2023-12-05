import pygame

pygame.init()
#Liens vers les tuto :
#https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/
#https://www.youtube.com/watch?v=G8MYGDf_9ho

#Taille de la fenetre / Titre et Icone de mon Prog /
ecran = pygame.display.set_mode((800,500))   	
logoapp = pygame.image.load("d:/WebDev/Projet/pendu/ressources/logoapp.png").convert()
pygame.display.set_icon(logoapp)

#Background et Texte
background = pygame.image.load("d:/WebDev/Projet/pendu/ressources/background.jpg").convert()
font = pygame.font.SysFont("arialblack", 40)
font2 = pygame.font.SysFont("arialblack", 20)
image_title = font.render ("Menu Principal", 1, (255, 255, 255))
image_play = font2.render ("Nouvelle Partie", 1, (0, 0, 0))
image_mots = font2.render ("Ajouter un Mot", 1, (0, 0, 0))
image_exit = font2.render ("Quitter", 1, (255, 255, 255))
image_exit2 = font2.render ("Quitter", 1, (0, 0, 0))

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
        #donne les coordonnées de la souris dans ma fenetre
        #utile pour placez mes éléments
        # print (souris) 

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
word_button = Bouton (100, 100, new_word_img, 2)
game_button = Bouton (500, 100, new_game_img, 2)
exit_button = Bouton (350, 400, exit_img, 1)




#Boucles qui permettent de faire fonctionner mon jeu
def main_menu ():
    
    running = True
    while running:

        pygame.display.set_caption("Pendu THE Game")
        ecran.fill("black")
        #Defini la position de l'éléments avec les valeurs
        ecran.blit(background, (0, -60))
        ecran.blit(image_title, (240,50))
        ecran.blit(image_play, (520,280))
        ecran.blit(image_mots, (120,280))
        ecran.blit(image_exit, (450,450))
        
        if word_button.afficher():
            addword ()
        if game_button.afficher():
            newgame ()
        if exit_button.afficher():
            running = False

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

    #Quitte proprement pygame, libère les ressources
    pygame.quit()

def newgame ():
    game = True
    global running
    running = False

    while game :
        pygame.display.set_caption("Game")
        ecran.fill("white")
        ecran.blit(image_exit2, (450,450))

        if exit_button.afficher():
            game = False
            running = True


        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Vérifiez si la touche "F4" est enfoncée
                    if event.key == pygame.K_F4:
                        # Vérifiez si la touche "Alt" est également enfoncée
                        if event.mod & pygame.KMOD_ALT:
                            game = False
                            running = True
                    elif event.key == pygame.K_ESCAPE:
                        game = False
                        running = True
                elif event.type == pygame.QUIT:
                    pygame.quit()
        
        pygame.display.flip()

def addword ():
    word = True
    global running
    running = False

    while word :
        pygame.display.set_caption("Ajout d'un Mot")
        ecran.fill("white")
        ecran.blit(image_exit2, (450,450))

        if exit_button.afficher():
            word = False
            running = True


        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Vérifiez si la touche "F4" est enfoncée
                    if event.key == pygame.K_F4:
                        # Vérifiez si la touche "Alt" est également enfoncée
                        if event.mod & pygame.KMOD_ALT:
                            word = False
                            running = True
                    elif event.key == pygame.K_ESCAPE:
                        word = False
                        running = True        
                elif event.type == pygame.QUIT:
                    pygame.quit()
        
        pygame.display.flip()

main_menu ()
