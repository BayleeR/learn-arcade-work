""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_SNOWBALL = 0.1
SPRITE_SCALING_FIRE = 0.1
SNOWBALL_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#sound from OpenGameArt

class Snowball(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin(snowball)
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0 and self.change_x < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH and self.change_x > 0:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class Fire(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin(snowball)
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0 and self.change_x < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH and self.change_x > 0:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1



class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.snowball_list = None
        self.fire_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        #NEW- Load sound for collecting snowballs (good sprites)
        self.good_sound = arcade.load_sound("good_sound.wav")
        #Load sound for bad sprites
        self.bad_sound = arcade.load_sound("bad_sound.mp3")

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.snowball_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("snowman.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(SNOWBALL_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            snowball = Snowball("snowball.png", SPRITE_SCALING_PLAYER)

            # Position the coin
            snowball.center_x = random.randrange(SCREEN_WIDTH)
            snowball.center_y = random.randrange(SCREEN_HEIGHT)
            snowball.change_x = random.randrange(-3, 4)
            snowball.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.snowball_list.append(snowball)

        #Create the fire (bad sprite) #NEW everything under here
        for j in range(FIRE_COUNT):
            fire = Fire("fire.png", SPRITE_SCALING_FIRE)

            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)
            fire.change_x = random.randrange(-3, 4)
            fire.change_y = random.randrange(-3, 4)

            self.fire_list.append(fire)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.snowball_list.draw()
        self.player_list.draw()
        self.fire_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.snowball_list.update()
        self.fire_list.update()

        # Generate a list of all sprites that collided with the player.
        #Good sprite
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.snowball_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for snowball in hit_list:
            snowball.remove_from_sprite_lists()
            self.score += 1

            #NEW- Play the good sound
            arcade.play_sound(self.good_sound)

        #Bad sprite
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fire_list)
        for fire in hit_list:
            fire.remove_from_sprite_lists()
            self.score -= 1

            #NEW- Play the good sound
            arcade.play_sound(self.bad_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()