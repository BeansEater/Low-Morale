# Imports
import json
import pygame
import random
import math

from entities import *
from overlays import *
from settings import *
from utilities import *


# Main game class 
class Game:

    def __init__(self):
        pygame.mixer.pre_init()
        pygame.init()
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.load_assets()
        self.make_overlays()
        self.new_game()

        self.screen_shake = 0
        self.render_offset = [0,0]

    def load_assets(self):
        self.hero_img = Image(HERO_IMG)
        self.hero_air_img = Image(HERO_AIR_IMG)
        self.grass_dirt_img = Image(GRASS_IMG)
        self.block_img = Image(BLOCK_IMG)
        self.pointer_img = Image(POINTER_IMG)
        self.gem_img = Image(GEM_IMG)
        self.concrete_img = Image(CONCRETE_IMG)
        self.babe_img = Image(BABE_IMG)
        self.gun_img = Image(GUN_IMG)
        self.bg_img = Image(BG_IMG)
        self.flag_img = Image(FLAG_IMG)
        self.blast_snd = Sound(BLAST_SND)
        self.menu_msc = Music(MENU_MUSIC)
        self.main_msc = Music(MAIN_MUSIC)
        self.holy_msc = Music(HOLY_MUSIC)

    def make_overlays(self):
        self.title_screen = TitleScreen(self)
        self.win_screen = WinScreen(self)
        self.lose_screen = LoseScreen(self)
        self.level_complete_screen = LevelCompleteScreen(self)
        self.pause_screen = PauseScreen(self)
        self.hud = HUD(self)
        self.grid = Grid(self)
        
    def new_game(self):
        # Make the hero here so it persists across levels
        self.player = pygame.sprite.Group()
        self.hero = Hero(self, self.hero_img)
        self.gun = Gun(self, self.gun_img)
        self.player.add(self.hero)

        # Go to first level
        self.stage = START
        self.level = STARTING_LEVEL
        self.load_level()
    
    def load_level(self):
        # Make sprite groups
        self.platforms = pygame.sprite.Group()
        self.not_platforms = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.menu_msc.play()

        # Load the level data
        with open(LEVELS[self.level - 1]) as f:
            self.data = json.load(f)

        # World settings
        self.world_width = self.data['width'] * GRID_SIZE
        self.world_height = self.data['height'] * GRID_SIZE

        # Position the hero
        loc = self.data['start']
        self.hero.move_to(loc)

        # Add the platforms
        if 'grass' in self.data:   
            for loc in self.data['grass']:
                self.platforms.add( Platform(self, self.grass_dirt_img, loc) )

        if 'blocks' in self.data:    
            for loc in self.data['blocks']:
                self.platforms.add( Platform(self, self.block_img, loc) )

        if 'concrete' in self.data:    
            for loc in self.data['concrete']:
                self.platforms.add( Platform(self, self.concrete_img, loc) )

        if 'pointers' in self.data:    
            for loc in self.data['pointers']:
                self.not_platforms.add( Not_Platform(self, self.pointer_img, loc) )

        # Add the goal

        if 'flags' in self.data:    
            for loc in self.data['flags']:
                self.goals.add( Goal(self, self.flag_img, loc) )
        
        if 'babes' in self.data:    
            for loc in self.data['babes']:
                self.goals.add( Goal(self, self.babe_img, loc) )
    
        # Make one big sprite group for easy updating and drawing
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player, self.platforms, self.not_platforms, self.gun, self.goals)

    def start_level(self):
        self.stage = PLAYING
        self.holy_msc.play()
        
    def toggle_pause(self):
        if self.stage == PLAYING:
            self.stage = PAUSE
        elif self.stage == PAUSE:
            self.stage = PLAYING

    def complete_level(self):
        self.stage = LEVEL_COMPLETE

    def advance(self):
        self.level += 1
        self.load_level()
        self.start_level()

    def win(self):
        self.stage = WIN
        self.main_msc.play()

    def lose(self):
        self.stage = LOSE

    def process_input(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.hero.shoot()

            if event.type == pygame.KEYDOWN:
                # for editing
                if event.key == pygame.K_g:
                    self.grid.toggle()

                # start/restart
                elif self.stage == START:
                    if event.key == pygame.K_SPACE:
                        self.start_level()
                elif self.stage in [WIN, LOSE]:
                    if event.key == pygame.K_r:
                        self.new_game()

                # pause/unpause
                elif event.key == pygame.K_p:
                    self.toggle_pause() 

                # actual gameplay
                elif self.stage == PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.hero.jump()
                        

        # player movement
        if self.stage == PLAYING:
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_a]:
                self.hero.go_left()
            elif pressed[pygame.K_d]:
                self.hero.go_right()
            else:
                self.hero.stop()
    
    def run_screen_shake(self):
        if self.screen_shake > 0:
            self.screen_shake -= 1

        self.render_offset = [0,0]
        if self.screen_shake:
            self.render_offset[0] = random.randint(-4,4)
            self.render_offset[1] = random.randint(-4,4)
     
    def update(self):
        if self.stage == PLAYING:
            self.run_screen_shake()
            self.all_sprites.update()

            if self.hero.reached_goal():
                if self.level < len(LEVELS):
                    self.advance()
                else:
                    self.win()

    def get_offsets(self):

        if self.hero.rect.centery > HEIGHT // 2:
            offset_y = 0
        elif self.hero.rect.centery > self.world_height - HEIGHT // 2:
            offset_y = self.world_height - HEIGHT
        else:
            offset_y = self.hero.rect.centery - HEIGHT // 2

        return offset_y

    def render(self):
        offset_y = self.get_offsets()
        
        self.screen.blit(self.bg_img, [0, 0])
        for sprite in self.all_sprites:
            x = sprite.rect.x
            y = sprite.rect.y - offset_y
            self.screen.blit(sprite.image, [x, y])

        if self.stage != START:
            self.hud.draw(self.screen)

        if self.stage == START:
            self.title_screen.draw(self.screen)
        elif self.stage == LEVEL_COMPLETE:
            self.level_complete_screen.draw(self.screen)
        elif self.stage == WIN:
            self.win_screen.draw(self.screen)
        elif self.stage == LOSE:
            self.lose_screen.draw(self.screen)
        elif self.stage == PAUSE:
            self.pause_screen.draw(self.screen)

        self.grid.draw(self.screen, 0, offset_y)
        
    def play(self):
        while self.running:
            self.process_input()     
            self.update()     
            self.render()

            self.screen.blit(pygame.transform.scale(self.screen,(WIDTH, HEIGHT)),self.render_offset)
            
            pygame.display.update()
            self.clock.tick(FPS)


# Let's do this!
if __name__ == "__main__":
   g = Game()
   g.play()
   pygame.quit()   
