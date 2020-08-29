import arcade

arcade.open_window(800, 600, "My sample window")

# Background color
arcade.set_background_color((arcade.color.AIR_SUPERIORITY_BLUE))

arcade.start_render()

# Sky
arcade.draw_lrtb_rectangle_filled(0, 800, 450, 200, arcade.color.SAE)
arcade.draw_lrtb_rectangle_filled(0, 800, 375, 200, arcade.color.AMBER)
arcade.draw_lrtb_rectangle_filled(0, 800, 225, 200, arcade.color.MEDIUM_VERMILION)

# Sun
arcade.draw_circle_filled(550, 200, 80, arcade.color.MELLOW_YELLOW)
arcade.draw_circle_filled(550, 200, 55, arcade.color.LEMON_CHIFFON)

# Bird1
arcade.draw_arc_outline(600, 350, 35, 30, arcade.color.CHARLESTON_GREEN, 0, 180)
arcade.draw_arc_outline(635, 350, 35, 30, arcade.color.CHARLESTON_GREEN, 0, 180)

# Bird2
arcade.draw_arc_outline(550, 410, 30, 25, arcade.color.CHARLESTON_GREEN, 0, 180)
arcade.draw_arc_outline(580, 410, 30, 25, arcade.color.CHARLESTON_GREEN, 0, 180)

# Bird3
arcade.draw_arc_outline(525, 310, 15, 10, arcade.color.CHARLESTON_GREEN, 0, 180)
arcade.draw_arc_outline(540, 310, 15, 10, arcade.color.CHARLESTON_GREEN, 0, 180)

# Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color. BITTER_LIME)

# Concrete
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DIM_GRAY)

# House building
arcade.draw_lrtb_rectangle_filled(75, 425, 400, 120, arcade.color.FRENCH_BEIGE)

arcade.finish_render()

arcade.run()

