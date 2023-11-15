import pygame
from constantes import *
import obtener_imagenes

class Player:
    def __init__(self,x:int,y:int,speed_walk:int,speed_run:int) -> None:

        self.mirando_der = True
        self.action = 'quieto'
        self.img_walk_right = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_walk.png',6,1)
        self.img_walk_left = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_walk.png',6,1,True)

        self.img_stand_up_right = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_idle.png',4,1)
        self.img_stand_up_left = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_idle.png',4,1, True)
        
        self.img_jump_right = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_jump.png',6,1)
        self.img_jump_left = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_jump.png',6,1,True)
        self.jumping = False
        self.height_jump = -20

        self.limite_velocidad_caida = self.height_jump * -1
        self.gravity = 3

        self.img_hurt = obtener_imagenes.get_surface_from_spritsheet
        ('assets/characters/GraveRobber/GraveRobber_hurt.png',3,1)
        self.img_death = obtener_imagenes.get_surface_from_spritsheet(
            'assets/characters/GraveRobber/GraveRobber_death.png',6,1)

        self.frame = 0
        self.lives = 3
        self.score = 0

        self.move_x = x
        self.move_y = y

        self.speed_walk = speed_walk 
        self.speed_run = speed_run


        self.animation = self.img_stand_up_right
        self.img = self.animation[self.frame]
        # self.img = pygame.transform.scale(self.img,(100,100))
        self.rect = self.img.get_rect()
        self.rect.x = 15
        self.rect.y = 500

    def control(self, velocidad_caminar):
        self.rect.x += velocidad_caminar 


    def aplicar_gravedad(self, screen, lista_img):
        if self.jumping ==  True:
            self.draw(screen,lista_img) 
            self.rect.y += self.move_y
            if (self.move_y + self.gravity) < self.limite_velocidad_caida:
                self.move_y += self.gravity

            if self.rect.y >= 480:
                self.jumping = False
                self.move_y = 0
            else:
                self.jumping = True

    def update(self,screen):

        if self.action == 'walk_right':
            self.mirando_der = True
            if  not self.jumping:
                self.draw(screen,self.img_walk_right )
            self.control(self.speed_walk)

        elif self.action == 'walk_left': 
            self.mirando_der = False
            if not self.jumping:
                self.draw(screen,self.img_walk_left )
            self.control(self.speed_walk * -1)

        elif self.action == 'jump':
            if self.jumping == False:
                self.jumping = True
                self.move_y = self.height_jump

        elif self.action == 'stand_up':
            if not self.jumping:
                if self.mirando_der == True:
                    self.draw(screen,self.img_stand_up_right )
                elif self.mirando_der == False: 
                    self.draw(screen,self.img_stand_up_left )
        
        if self.mirando_der == True:
            self.aplicar_gravedad(screen, self.img_jump_right)
        else:
            self.aplicar_gravedad(screen, self.img_jump_left)

        # self.rect.x += self.move_x
        # self.rect.y += self.move_y

    def draw(self, screen, lista_animaciones):
            
        if (self.frame >= len(lista_animaciones) - 1):
            self.frame = 0

        self.img = lista_animaciones[self.frame]
        self.img = pygame.transform.scale(self.img,(130,130))
        screen.blit(self.img, self.rect)
        self.frame += 1
        
        if self.jumping == True  and self.frame == 2:
            self.frame = 0

