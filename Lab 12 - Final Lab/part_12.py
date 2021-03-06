"""
Mother Nature's Crisis
"""


import arcade
import random
import os
import math

SPRITE_SCALING = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SCALING_FLOWER_COIN = 0.2
SPRITE_SCALING_SNOWBALL_COIN = 0.2
SPRITE_SCALING_LEAF_COIN = 0.2
SPRITE_SCALING_SUN_COIN = 0.2
SPRITE_SCALING_ENEMY_WASP = 0.4
SPRITE_SCALING_ENEMY_CRAB = 0.35
SPRITE_SCALING_ENEMY_PUMPKIN = 0.4
SPRITE_SCALING_ENEMY_BEAR = 2.5
SPRITE_SCALING_PLAYER = 0.15
SPRITE_SCALING_PLAYER_BULLET = 0.5
SPRITE_SCALING_ENEMY_BULLET = 0.5
SPRITE_SCALING_HEALTH_STAR = 0.2
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Mother Nature's Crisis"

MOVEMENT_SPEED = 8
TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1

BULLET_SPEED = 5

VIEWPORT_MARGIN = 60

# Coin Count
FLOWER_COIN_COUNT = 10
SUN_COIN_COUNT = 10
LEAF_COIN_COUNT = 10
ICE_CUBE_COIN_COUNT = 10
# HEALTH_STAR_COUNT = 1
# TOTAL_COIN_COUNT = 40


class InstructionView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("instruction-screen.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.

        # Maybe use this line of code instead of the one above?
        self.view_left = 0
        self.view_bottom = 0
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, x, y, button, modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class LoseView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("lose-screen.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.

        # Maybe use this line of code instead of the one above?
        self.view_left = 0
        self.view_bottom = 0
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class WinView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("win-screen.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        """arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)"""

        self.view_left = 0
        self.view_bottom = 0
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING_PLAYER
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        # Player image from OpenGameArt
        texture = arcade.load_texture("player-left.png")
        self.textures.append(texture)
        texture = arcade.load_texture("player-left.png",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = texture

    def update(self):
        
        # self.center_x += self.change_x
        # self.center_y += self.change_y
        
        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None
        self.enemy_list = None
        self.coin_list = None
        self.health_power_up_list = arcade.SpriteList()
        self.player_bullet_list = None
        self.enemy_bullet_list = arcade.SpriteList()

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():

    """Create and return room 1.
    If your program gets large, you may want to separate this into different
    files."""
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # -- Set up the walls
    # BORDERS
    """Borders"""
    # left wall
    # stoneCenter image from Kenny.nl
    for y in range(34, 700, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 34
        wall.center_y = y
        room.wall_list.append(wall)

    # right wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 866
        wall.center_y = y
        room.wall_list.append(wall)

    # right wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 866
        wall.center_y = y
        room.wall_list.append(wall)

    # bottom wall
    for x in range(34, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 34
        room.wall_list.append(wall)
    # top wall
    for x in range(34, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 738
        room.wall_list.append(wall)

    # INSIDE WALLS

    # If you want coins or monsters in a level, then add that code here.
    # Wasp image from OpenGameArt
    wasp_enemy = arcade.Sprite("enemy_wasp.png", SPRITE_SCALING_ENEMY_WASP)
    wasp_enemy.center_x = 150
    wasp_enemy.center_y = 600
    wasp_enemy.angle = 0
    room.enemy_list.append(wasp_enemy)

    wasp_enemy = arcade.Sprite("enemy_wasp.png", SPRITE_SCALING_ENEMY_WASP)
    wasp_enemy.center_x = 700
    wasp_enemy.center_y = 240
    wasp_enemy.angle = 0
    room.enemy_list.append(wasp_enemy)

    """Inner Walls"""
    # dirt image from Kenny.nl
    for x in range(80, 300, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)

    for x in range(430, 530, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)

    for x in range(650, 750, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 180
        room.wall_list.append(wall)

    coordinate_list = [[280, 320],
                       [350, 320],
                       [280, 390],
                       [350, 390]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = coordinate[0]
        wall.center_y = coordinate[1]
        room.wall_list.append(wall)

    for x in range(210, 240, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 350
        room.wall_list.append(wall)

    for y in range(320, 420, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = 580
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(510, 560, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)

    for x in range(600, 650, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 570
        room.wall_list.append(wall)

    for x in range(710, 780, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 450
        room.wall_list.append(wall)

    for x in range(720, 770, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 315
        room.wall_list.append(wall)

    for y in range(550, 650, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = 445
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(90, 140, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 490
        room.wall_list.append(wall)

    for x in range(250, 320, 64):
        wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 579
        room.wall_list.append(wall)

    # Scatter the coins
    # Flower image from IconBug.com
    for i in range(10):
        flower_coin = arcade.Sprite("flower_coin.png", SPRITE_SCALING_FLOWER_COIN)

        flower_coin_placed_successfully = False

        while not flower_coin_placed_successfully:
            # Position the coin
            flower_coin.center_x = random.randrange(0, 850)  # SCREEN_WIDTH
            flower_coin.center_y = random.randrange(0, 700)  # SCREEN_HEIGHT

            wall_hit_list = arcade.check_for_collision_with_list(flower_coin, room.wall_list)

            flower_coin_hit_list = arcade.check_for_collision_with_list(flower_coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(flower_coin_hit_list) == 0:
                # It is!
                flower_coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(flower_coin)

    # Background from OpenGameArt
    room.background = arcade.load_texture("backgroundextended.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.health_power_up_list = arcade.SpriteList()

    # -- Set up the walls
    # level 2
    # left wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # left wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # right wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)
    # right wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)
    # bottom wall
    for x in range(0, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 34
        room.wall_list.append(wall)
    # top wall
    for x in range(3, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 738
        room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Crab image from OpenGameArt
    crab_enemy = arcade.Sprite("enemy_crab.png", SPRITE_SCALING_ENEMY_CRAB)
    crab_enemy.center_x = 260
    crab_enemy.center_y = 400
    crab_enemy.angle = 180
    room.enemy_list.append(crab_enemy)

    crab_enemy = arcade.Sprite("enemy_crab.png", SPRITE_SCALING_ENEMY_CRAB)
    crab_enemy.center_x = 630
    crab_enemy.center_y = 625
    crab_enemy.angle = 180
    room.enemy_list.append(crab_enemy)

    # Star image from IconScout
    health_star = arcade.Sprite("health_star.png", SPRITE_SCALING_HEALTH_STAR)
    health_star.center_x = 410
    health_star.center_y = 620
    health_star.angle = 180
    room.health_power_up_list.append(health_star)

    """Inner walls"""
    # Grass image from kenny.nl
    for y in range(600, 700, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 130
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(200, 500, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 130
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(290, 420, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 170
        room.wall_list.append(wall)

    for x in range(200, 300, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for x in range(550, 700, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for y in range(300, 400, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 400
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(170, 270, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 560
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(515, 680, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 500
        room.wall_list.append(wall)

    for y in range(300, 380, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 745
        wall.center_y = y
        room.wall_list.append(wall)

    coordinate_list = [[270, 540],
                       [340, 540],
                       [270, 610],
                       [340, 610]]
    # Loop through coordinates
    for coordinate in coordinate_list:
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = coordinate[0]
        wall.center_y = coordinate[1]
        room.wall_list.append(wall)

    for x in range(500, 600, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 700
        room.wall_list.append(wall)

    for x in range(700, 800, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 170
        room.wall_list.append(wall)

    for y in range(600, 660, 64):
        wall = arcade.Sprite("grass.png", SPRITE_SCALING)
        wall.center_x = 750
        wall.center_y = y
        room.wall_list.append(wall)

    # Scatter the coins
    # Sun coins
    for i in range(10):
        # Sun image from IconExperience
        sun_coin = arcade.Sprite("sun_coin.png", SPRITE_SCALING_SUN_COIN)

        sun_coin_placed_successfully = False

        while not sun_coin_placed_successfully:
            # Position the coin
            sun_coin.center_x = random.randrange(0, 850)  # SCREEN_WIDTH
            sun_coin.center_y = random.randrange(0, 700)  # SCREEN_HEIGHT

            wall_hit_list = arcade.check_for_collision_with_list(sun_coin, room.wall_list)

            sun_coin_hit_list = arcade.check_for_collision_with_list(sun_coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(sun_coin_hit_list) == 0:
                # It is!
                sun_coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(sun_coin)
    # Background from OpenGameArt
    room.background = arcade.load_texture("backgroundextended.png")

    return room


def setup_room_3():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()
    room.health_power_up_list = arcade.SpriteList()

    # -- Set up the walls
    # level 3
    # left wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # left wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # right wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        room.wall_list.append(wall)
    # right wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)
    # bottom wall
    for x in range(0, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 34
        room.wall_list.append(wall)
    # top wall
    for x in range(3, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 738
        room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    # Pumpkin image from IconExperience
    pumpkin_enemy = arcade.Sprite("enemy_pumpkin.png", SPRITE_SCALING_ENEMY_PUMPKIN)
    pumpkin_enemy.center_x = 605
    pumpkin_enemy.center_y = 670
    pumpkin_enemy.angle = 180
    room.enemy_list.append(pumpkin_enemy)

    pumpkin_enemy = arcade.Sprite("enemy_pumpkin.png", SPRITE_SCALING_ENEMY_PUMPKIN)
    pumpkin_enemy.center_x = 440
    pumpkin_enemy.center_y = 170
    pumpkin_enemy.angle = 180
    room.enemy_list.append(pumpkin_enemy)

    health_star = arcade.Sprite("health_star.png", SPRITE_SCALING_HEALTH_STAR)
    health_star.center_x = 700
    health_star.center_y = 120
    health_star.angle = 180
    room.health_power_up_list.append(health_star)

    """Inner walls"""
    # Planet image from kenny.nl
    for x in range(140, 300, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 170
        room.wall_list.append(wall)

    for x in range(250, 300, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 320
        room.wall_list.append(wall)

    for x in range(120, 170, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 420
        room.wall_list.append(wall)

    for y in range(280, 440, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = 380
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(145, 330, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 560
        room.wall_list.append(wall)

    for x in range(250, 310, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 495
        room.wall_list.append(wall)

    for y in range(610, 675, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = 410
        wall.center_y = y
        room.wall_list.append(wall)

    for y in range(680, 720, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = 710
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(590, 640, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 570
        room.wall_list.append(wall)

    for x in range(440, 600, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)

    for x in range(440, 600, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 380
        room.wall_list.append(wall)

    coordinate_list = [[530, 170],
                       [600, 170],
                       [530, 240],
                       [600, 240]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = coordinate[0]
        wall.center_y = coordinate[1]
        room.wall_list.append(wall)

    for x in range(665, 770, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        room.wall_list.append(wall)

    for y in range(360, 550, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = 750
        wall.center_y = y
        room.wall_list.append(wall)

    for x in range(560, 640, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 510
        room.wall_list.append(wall)

    for x in range(570, 620, 64):
        wall = arcade.Sprite("planet.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 100
        room.wall_list.append(wall)

    # Scatter the coins
    # Leaf image from WikiMedia Commons
    for i in range(10):
        leaf_coin = arcade.Sprite("leaf_coin.png", SPRITE_SCALING_LEAF_COIN)

        leaf_coin_placed_successfully = False

        while not leaf_coin_placed_successfully:
            # Position the coin
            leaf_coin.center_x = random.randrange(0, 850)  # SCREEN_WIDTH
            leaf_coin.center_y = random.randrange(0, 700)  # SCREEN_HEIGHT

            wall_hit_list = arcade.check_for_collision_with_list(leaf_coin, room.wall_list)

            leaf_coin_hit_list = arcade.check_for_collision_with_list(leaf_coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(leaf_coin_hit_list) == 0:
                # It is!
                leaf_coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(leaf_coin)
    # Background from OpenGameArt
    room.background = arcade.load_texture("fallbackground.png")

    return room


def setup_room_4():
    """
    Create and return room 4
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.coin_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # -- Set up the walls
    # level 3
    # left wall (top part)
    for y in range(560, 730, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # left wall (bottom part)
    for y in range(34, 230, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 0
        wall.center_y = y
        room.wall_list.append(wall)
    # right wall
    for y in range(34, 700, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = 900
        wall.center_y = y
        room.wall_list.append(wall)
    # bottom wall
    for x in range(0, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 34
        room.wall_list.append(wall)
    # top wall
    for x in range(3, 900, 64):
        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 738
        room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    # Bear image from OpenGameArt
    bear_enemy = arcade.Sprite("bear_enemy.png", SPRITE_SCALING_ENEMY_BEAR)
    bear_enemy.center_x = 400
    bear_enemy.center_y = 670
    bear_enemy.angle = 0
    room.enemy_list.append(bear_enemy)

    bear_enemy = arcade.Sprite("bear_enemy.png", SPRITE_SCALING_ENEMY_BEAR)
    bear_enemy.center_x = 700
    bear_enemy.center_y = 200
    bear_enemy.angle = 0
    room.enemy_list.append(bear_enemy)

    """Inner walls"""
    # Snow image from OpenGameArt
    for x in range(140, 330, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 300
        room.wall_list.append(wall)

    for y in range(170, 380, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = 200
        wall.center_y = y
        room.wall_list.append(wall)
    for x in range(135, 275, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 540
        room.wall_list.append(wall)
    for x in range(330, 380, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 440
        room.wall_list.append(wall)
    for y in range(100, 200, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = 330
        wall.center_y = y
        room.wall_list.append(wall)
    for x in range(465, 555, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 185
        room.wall_list.append(wall)

    coordinate_list = [[460, 320],
                       [530, 320],
                       [460, 390],
                       [530, 390]]
    # Loop through coordinates
    for coordinate in coordinate_list:
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = coordinate[0]
        wall.center_y = coordinate[1]
        room.wall_list.append(wall)
    for x in range(180, 250, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 675
        room.wall_list.append(wall)
    for x in range(410, 480, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 590
        room.wall_list.append(wall)

    for y in range(400, 600, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = 600
        wall.center_y = y
        room.wall_list.append(wall)
    for y in range(550, 700, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = 750
        wall.center_y = y
        room.wall_list.append(wall)
    for y in range(400, 450, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = 750
        wall.center_y = y
        room.wall_list.append(wall)
    for x in range(670, 730, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 270
        room.wall_list.append(wall)
    for x in range(800, 840, 64):
        wall = arcade.Sprite("snow.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 170
        room.wall_list.append(wall)

    # Scatter the coins
    # Snowball image from FindIcons
    for i in range(10):
        snowball_coin = arcade.Sprite("snowball_coin.png", SPRITE_SCALING_SNOWBALL_COIN)

        snowball_coin_placed_successfully = False

        while not snowball_coin_placed_successfully:
            # Position the coin
            snowball_coin.center_x = random.randrange(0, 850)  # SCREEN_WIDTH
            snowball_coin.center_y = random.randrange(0, 700)  # SCREEN_HEIGHT

            wall_hit_list = arcade.check_for_collision_with_list(snowball_coin, room.wall_list)

            snowball_coin_hit_list = arcade.check_for_collision_with_list(snowball_coin, room.coin_list)

            if len(wall_hit_list) == 0 and len(snowball_coin_hit_list) == 0:
                # It is!
                snowball_coin_placed_successfully = True

        # Add the coin to the lists
        room.coin_list.append(snowball_coin)
    # Background from OpenSameArt
    room.background = arcade.load_texture("snowbackground.png")

    return room


class GameView(arcade.View): # was MyGame(arcade.Window)
    """ Main application class. """

    def __init__(self):
        # was (self, width, height, title)
        """
        Initializer
        """
        super().__init__()
        # was super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.enemy_list = None
        self.health_power_up_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None

        self.frame_count = 0

        # Total coin count
        self.total_coin_count = 0

        # Score
        self.score = 0

        # Lives
        self.hearts = 3

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        # Coin sound from OpenGameArt
        self.coin_sound = arcade.load_sound("coin_sound.ogg")
        # Enemy shoot sound from OpenGameArt
        self.enemy_shoot_sound = arcade.load_sound("enemy_shoot_sound.wav")
        # Player shoot sound from OpenGameArt
        self.player_shoot_sound = arcade.load_sound("player_shoot_sound.ogg")

        # Rooms
        self.current_room = 0
        self.rooms = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """
        # sprite list
        self.player_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.health_power_up_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # Score
        self.score = 0

        # Lives
        self.hearts = 3

        # total coin count
        self.total_coin_count = 0

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            900, 790,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()
        self.player_bullet_list.draw()
        self.rooms[self.current_room].health_power_up_list.draw()
        self.rooms[self.current_room].enemy_bullet_list.draw()
        self.rooms[self.current_room].coin_list.draw()
        self.rooms[self.current_room].enemy_list.draw()

        # Display score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10 + self.view_left, 20 + self.view_bottom, arcade.color.WHITE, 25)

        # Display hearts
        output = f"Hearts: {self.hearts}"
        arcade.draw_text(output, 10 + self.view_left, 50 + self.view_bottom, arcade.color.WHITE, 25)

    def on_mouse_press(self, x, y, button, modifiers):
        # Called whenever the mouse button is clicked.
        # self.window.set_mouse_visible(False)
        # Bullet code
        # Player bullet image from OpenGameArt
        player_bullet = arcade.Sprite("player_bullet.png", SPRITE_SCALING_PLAYER_BULLET)
        arcade.play_sound(self.player_shoot_sound)

        """MAKE IT SO YOU CAN'T HIT THE COINS""" #
        # Position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        player_bullet.center_x = start_x
        player_bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need #--------------------------------------------
        # to add in self.view_bottom and self.view_left.
        dest_x = x # self.view_left
        dest_y = y # self.view_bottom

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        player_bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {player_bullet.angle:.2f}")

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        player_bullet.change_x = math.cos(angle) * BULLET_SPEED
        player_bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.player_bullet_list.append(player_bullet)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()
        self.player_sprite.update()

        # GAME OVER STUFF
        # Maybe do this to pause the game once it is over
        if self.total_coin_count < 40 or self.hearts > 0:
            self.rooms[self.current_room].enemy_bullet_list.update()

        # lose
        if self.hearts == 0:
            view = LoseView()
            self.window.show_view(view)
            self.view_left = 0
            self.view_bottom = 0
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
            return     

        # win
        if self.total_coin_count == 40:
            view = WinView()
            self.window.show_view(view)
            # was self.window.show(view)

        # --- Manage Scrolling ---

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        # every time you add a room, you need to add two statements to be able to enter the next room and be able
        # to go back to the previous room, if you only had one elif statement, then you could enter the net room
        # but not able to go back to the previous room
        # print(self.player_sprite.center_x)
        if self.player_sprite.center_x > 880 and self.current_room == 0:
            self.current_room = 1 # Screen width = 800
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)

            self.player_sprite.center_x = 875 # was 875
        # -------------------------------------
        elif self.player_sprite.center_x > 880 and self.current_room == 1:
            self.current_room = 2  # Screen width = 800
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 2:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 875 # was 900
        # ------------------
        elif self.player_sprite.center_x > 880 and self.current_room == 2:
            self.current_room = 3  # Screen width = 800
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 3:
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 875  # was 900



        # Coins
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.rooms[self.current_room].coin_list)

        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            self.total_coin_count += 1
            arcade.play_sound(self.coin_sound)

        # Bullet ------------ may have to move this code to each room
        # Call update on all sprites
        self.player_bullet_list.update()

        # Loop through each bullet
        for player_bullet in self.player_bullet_list:

            # Check this bullet to see if it hit an enemy
            enemy_hit_list = arcade.check_for_collision_with_list(player_bullet,
                                                            self.rooms[self.current_room].enemy_list)

            for enemy in enemy_hit_list:
                enemy.remove_from_sprite_lists()

            # Check this bullet to see if it hit an enemy
            wall_hit_list = arcade.check_for_collision_with_list(player_bullet,
                                                                 self.rooms[self.current_room].wall_list)

            for wall in wall_hit_list:
                player_bullet.remove_from_sprite_lists()

            # If it did, get rid of the bullet
            """if len(hit_list) > 0:
                player_bullet.remove_from_sprite_lists()"""
            # Play player shooting sound
            # arcade.play_sound(self.player_shoot_sound) ---------------------------------- LOOK AT THIS------
            # If the bullet flies off-screen, remove it.
            if player_bullet.bottom > 1200 or player_bullet.top < 0 or player_bullet.right < 0 or player_bullet.left > 1200:
                # was if player_bullet.bottom > self.width or player_bullet.top < 0 or player_bullet.right < 0 or player_bullet.left > self.width:
                player_bullet.remove_from_sprite_lists()

        # For enemy bullets

        self.frame_count += 1

        # Loop through each enemy that we have
        for enemy in self.rooms[self.current_room].enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            # enemy.angle = math.degrees(angle) - 90

            # Check to see if an enemy bullet has hit the player
            # if it has, remove a heart
            enemy_bullet_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                         self.rooms[
                                                                             self.current_room].enemy_bullet_list)
            for enemy_bullet in enemy_bullet_hit_list:
                enemy_bullet.remove_from_sprite_lists()
                self.hearts -= 1

            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 120 == 0:
                enemy_bullet = arcade.Sprite("player_bullet.png", SPRITE_SCALING_ENEMY_BULLET)
                arcade.play_sound(self.enemy_shoot_sound)
                enemy_bullet.center_x = start_x
                enemy_bullet.center_y = start_y

                # Angle the bullet sprite
                enemy_bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                enemy_bullet.change_x = math.cos(angle) * BULLET_SPEED
                enemy_bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.rooms[self.current_room].enemy_bullet_list.append(enemy_bullet)

        # Get rid of the bullet when it flies off-screen
        for enemy_bullet in self.rooms[self.current_room].enemy_bullet_list:
            if enemy_bullet.top < 0:
                enemy_bullet.remove_from_sprite_lists()

        health_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.rooms[self.current_room].health_power_up_list)
        for health_star in health_hit_list:
            health_star.remove_from_sprite_lists()
            self.hearts += 1

        # get ride of the enemy if you shoot it


def main():
    """ Main method """
    # window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
