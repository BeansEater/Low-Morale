# Window settings
GRID_SIZE = 64
WIDTH = 12 * GRID_SIZE
HEIGHT = 15 * GRID_SIZE
TITLE = "Low Morale"
FPS = 60


# Define colors
CONCRETE_BG = (108, 122, 158)
SKY_BLUE = (135, 200, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Physics
GRAVITY = 1
TERM_VELO_X = 25
TERM_VELO_Y = 25

# Back Ground
BG_IMG = 'assets/images/backgrounds/concrete_bg.png'

# Fonts
PRIMARY_FONT = 'assets/fonts/Dinomouse-Regular.otf'
SECONDARY_FONT = 'assets/fonts/Dinomouse-Regular.otf'
BONER_FONT = 'assets/fonts/BONER.ttf'


# Images
''' hero '''
HERO_IMG = 'assets/images/characters/skeleton.png'
HERO_AIR_IMG = 'assets/images/characters/skeleton_air.png'

HERO_ANIM = [HERO_IMG, HERO_AIR_IMG]

'''gun'''
GUN_IMG = 'assets/images/characters/shotgun.png'


''' tiles '''
GRASS_IMG = 'assets/images/tiles/grass_dirt.png'
BLOCK_IMG = 'assets/images/tiles/block.png'
CONCRETE_IMG = 'assets/images/tiles/concrete.png'
POINTER_IMG = 'assets/images/tiles/pointer.png'
FLAG_IMG = 'assets/images/tiles/flag.png'
BABE_IMG = 'assets/images/tiles/skeleton_babe.png'

''' items '''
GEM_IMG = 'assets/images/items/diamond.png'

# Sounds
JUMP_SND = 'assets/sounds/jump.wav'
GEM_SND = 'assets/sounds/collect_point.wav'
BLAST_SND = 'assets/sounds/blast.ogg'

# Music
MENU_MUSIC = 'assets/music/menu_msc.ogg'
MAIN_MUSIC = 'assets/music/game_msc.ogg'
HOLY_MUSIC = 'assets/music/holy_msc.ogg'



# Levels
STARTING_LEVEL = 1

LEVELS = ['assets/levels/world-1.json',
          'assets/levels/world-2.json',
          'assets/levels/world-3.json']


# Stages
START = 0
PLAYING = 1
PAUSE = 2
LEVEL_COMPLETE = 3
WIN = 4
LOSE = 5


# Gameplay settings
HERO_HEARTS = 3
HERO_SPEED = 5
HERO_JUMP_POWER = 14.5
HERO_AMMO = 3
