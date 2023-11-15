import pygame
from constantes import *
import obtener_imagenes


class Enemigo:
    def __init__(self,x:int,y:int,path:str,columnas:int=0,filas:int= 0):
        self.img_enemigo = obtener_imagenes.get_surface_from_spritsheet(path,columnas,filas,True,True)
        self.img_walk = obtener_imagenes.get_surface_from_spritsheet(path,columnas,filas)
        
        self.frame = 0

        self.animation = self.img_enemigo
        self.img = self.animation[self.frame]
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y  

    def update(self,screen) :
        self.draw(screen, self.animation )

    def draw(self,screen,animation):
        if (self.frame >= len(animation) - 1):
            self.frame = 0

        self.img = animation[self.frame]
        screen.blit(self.img, self.rect)
        self.frame += 1