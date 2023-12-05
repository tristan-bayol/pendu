import pygame
from main import *

pygame.init()


#Taille de la fenetre / Titre et Icone de mon Prog /
ecran_game = pygame.display.set_mode((800,500))   	
logoapp = pygame.image.load("d:/WebDev/Projet/pendu/ressources/logoapp.png").convert()
pygame.display.set_icon(logoapp)

d