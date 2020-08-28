import arcade

# This is a comment
# The computer will ignore

"""
This is a sample drawing file, another way to comment
"""

arcade.open_window(800, 600, "My sample window")

arcade.set_background_color((117, 237, 255))
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.GREEN)

arcade.finish_render()
arcade.run()
