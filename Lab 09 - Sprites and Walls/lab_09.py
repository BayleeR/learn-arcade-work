

import random
import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.1
SPRITE_SCALING_WALL = 1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

VIEWPORT_MARGIN = 40

COIN_COUNT = 80

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0
        self.coin_list = None
        self.wall_list = None

        # Coin sound from OpenGameArt
        self.coin_sound = arcade.load_sound("coin_sound.wav")

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        # Set up the player
        # Player image from DeviantArt
        self.player_sprite = arcade.Sprite("girl.png", 0.3)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        # All wall imigaes from kenny.nl
        # bottom border
        for x in range(30, 1000, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 30
            self.wall_list.append(wall)
        # left border
        for y in range(90, 800, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = 30
            wall.center_y = y
            self.wall_list.append(wall)
        # top border
        for x in range(30, 1000, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 856
            self.wall_list.append(wall)
        # right border
        for y in range(90, 800, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = 936
            wall.center_y = y
            self.wall_list.append(wall)

        # inside walls
        for x in range(150, 400, 64):
            wall = arcade.Sprite("mapTile_188.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_087.png", SPRITE_SCALING_WALL)
        wall.center_x = 480
        wall.center_y = 250
        self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_087.png", SPRITE_SCALING_WALL)
        wall.center_x = 480
        wall.center_y = 186
        self.wall_list.append(wall)

        for x in range(650, 800, 64):
            wall = arcade.Sprite("mapTile_087.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
        wall.center_x = 300
        wall.center_y = 90
        self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
        wall.center_x = 700
        wall.center_y = 90
        self.wall_list.append(wall)

        coordinate_list = [[496, 395],
                           [496, 459],
                           [560, 395],
                           [560, 459]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("mapTile_077.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(94, 210, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 520
            self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_188.png", SPRITE_SCALING_WALL)
        wall.center_x = 200
        wall.center_y = 385
        self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_188.png", SPRITE_SCALING_WALL)
        wall.center_x = 345
        wall.center_y = 385
        self.wall_list.append(wall)

        coordinate_list = [[596, 659],
                           [660, 595],
                           [660, 659]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("mapTile_017.png", SPRITE_SCALING_WALL)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for x in range(700, 900, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 420
            self.wall_list.append(wall)

        wall = arcade.Sprite("mapTile_017.png", SPRITE_SCALING_WALL)
        wall.center_x = 800
        wall.center_y = 560
        self.wall_list.append(wall)

        for y in range(550, 670, 64):
            wall = arcade.Sprite("mapTile_027.png", SPRITE_SCALING_WALL)
            wall.center_x = 345
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(700, 830, 64):
            wall = arcade.Sprite("mapTile_022.png", SPRITE_SCALING_WALL)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(175, 460, 64):
            wall = arcade.Sprite("mapTile_027.png", SPRITE_SCALING_WALL)
            wall.center_x = x
            wall.center_y = 740
            self.wall_list.append(wall)

            wall = arcade.Sprite("mapTile_027.png", SPRITE_SCALING_WALL)
            wall.center_x = 200
            wall.center_y = 676
            self.wall_list.append(wall)

        for i in range(80):
            # Coin image from IconArchive
            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(0, 1000)  # SCREEN_WIDTH
                coin.center_y = random.randrange(0, 800)  # SCREEN_HEIGHT

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10 + self.view_left, 20 + self.view_bottom, arcade.color.BLACK, 14)

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

        # Call update on all sprites
        self.physics_engine.update()

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

        # Coin section
        self.coin_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

            # Play coin sound when coin is picked up
            arcade.play_sound(self.coin_sound)

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()