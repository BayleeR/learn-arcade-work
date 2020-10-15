""" Sprite Sample Program """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        # Sprite Lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Player
        self.player_sprite = None

        # Physics Engine
        self.physics_engine = None

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        #This code sets up player

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList ()
        self.coin_list = arcade.SpriteList ()


        self.score = 0

        self.player_sprite = arcade.Sprite("character1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # individually placing a wall (4 lines of code)
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        wall.angle #NEW --------------------------------------------
        self.wall_list.append(wall)

        # Place walls with a loop, used to place top, bottom, etc walls
        for x in range(173, 650, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        #Place walls using a list of coordinates
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for i in range(50):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_BOX)

            done = False
            while not done:
                coin.center_x = random.randrange(-100, 1200)
                coin.center_y = random.randrange(-100, 1200)
                hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                if len(hit_list) == 0:
                    done = True

            self.coin_list.append(coin)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)


    def update(self, delta_time):
        self.physics_engine.update()

    def on_draw(self):
            arcade.start_render()

            self.player_list.draw()
            self.wall_list.draw()
            self.coin_list.draw()


    """Called whenever a key is pressed. """

    def on_key_press(self, key, modifiers):
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


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()