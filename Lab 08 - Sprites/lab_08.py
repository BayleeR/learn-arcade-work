""" Sprite Sample Program """

import random
import arcade


SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_SNOWBALL = 0.1
SPRITE_SCALING_FIRE = 0.2
SNOWBALL_COUNT = 50
FIRE_COUNT = 24

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#Fire from Vexels
#Snowball from FindIcons
#sound from OpenGameArt

class Snowball(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 and self.change_x < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH and self.change_x > 0:
            self.change_x *= -1
        if self.bottom < 0:
            self.change_y *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Fire(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.snowball_list = None
        self.fire_list = None #NEW

        self.player_sprite = None
        self.score = 0

        #Good sound form OpenGameArt
        self.good_sound = arcade.load_sound("good_sound.wav")
        #Bad sound from OpenGameArt
        self.bad_sound = arcade.load_sound("bad_sound.mp3")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AERO_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.player_list = arcade.SpriteList()
        self.snowball_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()

        self.score = 0

        #Snowman from ClipArtix
        self.player_sprite = arcade.Sprite("snowman.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins(snowballs)
        for i in range(SNOWBALL_COUNT):

            #Snowball from FindIcons
            snowball = Snowball("snowball.png", SPRITE_SCALING_PLAYER)

            snowball.center_x = random.randrange(SCREEN_WIDTH)
            snowball.center_y = random.randrange(SCREEN_HEIGHT)
            snowball.change_x = random.randrange(-3, 4)
            snowball.change_y = random.randrange(-3, 4)

            self.snowball_list.append(snowball)

        for j in range(FIRE_COUNT):
            #Fire from Vexels
            fire = Fire("fire.png", SPRITE_SCALING_FIRE)

            fire.center_x = random.randrange(SCREEN_WIDTH)
            fire.center_y = random.randrange(SCREEN_HEIGHT)

            self.fire_list.append(fire)


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.snowball_list.draw()
        self.fire_list.draw()
        self.player_list.draw()

        #On screen text
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        if len(self.snowball_list) == 0:
            arcade.draw_text("GAME OVER", 180, 260, arcade.color.BLACK, 70)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if len(self.snowball_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.snowball_list) > 0:

            self.snowball_list.update()
            self.fire_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.snowball_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for snowball in hit_list:
            snowball.remove_from_sprite_lists()
            self.score += 1

            arcade.play_sound(self.good_sound)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fire_list)
        for fire in hit_list:
            fire.remove_from_sprite_lists()
            fire.reset_pos()
            self.score -= 1

            arcade.play_sound(self.bad_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()