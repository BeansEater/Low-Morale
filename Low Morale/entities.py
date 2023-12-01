import pygame
import math
from settings import *
from utilities import *

class Entity(pygame.sprite.Sprite):

    def __init__(self, game, image, loc=[0, 0]):
        super().__init__()

        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.cooldown = 0

        self.move_to(loc)

    def move_to(self, loc):
        self.rect.centerx = loc[0] * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = loc[1] * GRID_SIZE + GRID_SIZE // 2

#class Anim_Entity(Entity):
    #def __init__(self, game, images, loc):
        #super().__init__(game, images(0), loc)
        

        

class Hero(Entity):

    def __init__(self, game, image):
        super().__init__(game, image)

        self.vx = 0
        self.vy = 0
    
        self.speed = HERO_SPEED
        self.ammo = HERO_AMMO

        self.anim_index = 0

        self.on_platform = False

        self.image = Image(HERO_IMG)
        if self.vy > 0:
            self.image = Image(HERO_AIR_IMG)

    def anim(self):
        if self.vy > 0:
            self.anim_index = 2

    def ticks(self):
        self.cooldown -=1

    def go_left(self):
        if self.on_platform == True:
            self.vx = -self.speed
            self.image = Image(HERO_ANIM[self.anim_index]).flip_x()
    
    def go_right(self):
        if self.on_platform == True:
            self.vx = self.speed
            self.image = Image(HERO_ANIM[self.anim_index])

    def stop(self):
        if self.vx > 0:
            if self.on_platform == True:
                self.vx -= .5
            else:
                self.vx += .05
            if self.vx < 0:
                self.vx = 0
        if self.vx < 0:
            if self.on_platform == True:
                self.vx += .5
            else:
                self.vx += .05
            if self.vx > 0:
                self.vx = 0

    def can_jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        return len(hits) > 0
        
    def jump(self):
        if self.can_jump():
            self.vy = -1 * HERO_JUMP_POWER

    def apply_gravity(self):
        self.vy += GRAVITY

        if self.vy > TERM_VELO_Y:
            self.vy = TERM_VELO_Y
        if self.vy < -TERM_VELO_Y:
            self.vy = -TERM_VELO_Y
        if self.vx > TERM_VELO_X:
            self.vx = TERM_VELO_X
        if self.vx < -TERM_VELO_X:
            self.vx = -TERM_VELO_X

    def move_and_check_platforms(self):
        self.rect.x += self.vx
        self.on_platform = False

        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)

        for platform in hits:
            if self.vx > 0:
                self.rect.right = platform.rect.left
            elif self.vx < 0:
                self.rect.left = platform.rect.right
            #self.on_platform = True

        self.rect.y += self.vy

        
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)

        for platform in hits:
            if self.vy > 0:
                self.rect.bottom = platform.rect.top
            elif self.vy < 0:
                self.rect.top = platform.rect.bottom
            self.vy = 0
            self.on_platform = True
            # if landed on platform, reload
            self.ammo = 3
        
            


    def check_world_edges(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.game.world_width:
            self.rect.right = self.game.world_width

    def can_shoot(self):
        offset_y = self.game.get_offsets()
        if self.cooldown < 0:
                self.cooldown = 20
                
                mx,my = pygame.mouse.get_pos()
                dx = (self.game.hero.rect.centerx - mx)
                dy = (self.game.hero.rect.centery - my)

                if dy > 0:
                    self.vy = TERM_VELO_Y
                if dy < 0:
                    self.vy = -TERM_VELO_Y
                    
                
                self.vy = dy - offset_y
                self.vx = dx/15

                self.game.screen_shake = 15
                self.game.blast_snd.play()
                self.ammo -= 1

    def shoot(self):
        if self.ammo > 0:
            self.can_shoot()
            


    def reached_goal(self):
        hits = pygame.sprite.spritecollide(self, self.game.goals, False)

        return len(hits) > 0
        
    def update(self):
        self.apply_gravity()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.ticks()
        
class Gun(Entity):
    def __init__(self, game, image):
        super().__init__(game, image)

        self.image = Image(GUN_IMG)

    def update(self):
        offset_y = self.game.get_offsets()
        x, y = pygame.mouse.get_pos()
        self.angle = math.atan2(y - (self.rect.centery-offset_y),
                                x - self.rect.centerx)
        self.image = Image(GUN_IMG)
        gun_copy = pygame.transform.rotate(self.image,-(self.angle)*60)
        self.image = gun_copy
        self.rect.top = self.game.hero.rect.bottom - 40
        self.rect.left = self.game.hero.rect.left
        
class Bullet(Entity):

    def __init__(self, game, image):

        self.speed = 10
        w, h = pygame.display.get_surface().get_size()

        x,y = pygame.mouse.get_pos()

        self.dx = (x - self.rect.centerx)
        self.dy = (y - self.rect.centery)
        self.hyp = math.sqrt(((self.dx)**2)+((self.dy)**2))

        self.vx = (self.speed*self.dx)/self.hyp
        self.vy = (self.speed*self.dy)/self.hyp

        self.angle = math.atan2(y - self.rect.centery,
                                x - self.rect.centerx)*(180/math.pi)

        arrow_copy = pygame.transform.rotate(self.image,-(self.angle-270))
        self.image = arrow_copy

    def drop(self):
        self.rect.y += self.vy
        self.rect.x += self.vx

# Tiles
class Platform(Entity):

    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Not_Platform(Entity):

    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Goal(Entity):

    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Babe(Entity):

    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)