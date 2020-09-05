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

# Cloud 1
arcade.draw_ellipse_filled(500, 550, 140, 70, arcade.color.ISABELLINE)
 #Cloud 2
arcade.draw_ellipse_filled(650, 500, 100, 50, arcade.color.ISABELLINE)

# Cloud 3
arcade.draw_ellipse_filled(100, 530, 120, 70, arcade.color.ISABELLINE)

# Bird1
arcade.draw_arc_outline(600, 350, 35, 30, arcade.color.CHARLESTON_GREEN, 0, 180, 4)
arcade.draw_arc_outline(635, 350, 35, 30, arcade.color.CHARLESTON_GREEN, 0, 180, 4)

# Bird2
arcade.draw_arc_outline(550, 410, 30, 25, arcade.color.CHARLESTON_GREEN, 0, 180, 4)
arcade.draw_arc_outline(580, 410, 30, 25, arcade.color.CHARLESTON_GREEN, 0, 180, 4)

# Bird3
arcade.draw_arc_outline(525, 310, 15, 10, arcade.color.CHARLESTON_GREEN, 0, 180, 4)
arcade.draw_arc_outline(540, 310, 15, 10, arcade.color.CHARLESTON_GREEN, 0, 180, 4)

# Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color. BITTER_LIME)

# Concrete
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.DIM_GRAY)

# Sidewalk
arcade.draw_polygon_filled(((210, 120),
                            (290, 120),
                            (320, 100),
                            (180, 100)
                            ),
                           arcade.color.DIM_GRAY)

# House building
# Building
arcade.draw_lrtb_rectangle_filled(75, 425, 400, 120, arcade.color.FRENCH_BEIGE)
# Roof
arcade.draw_triangle_filled(250, 500, 50, 400, 450, 400, arcade.color.DARK_BROWN)
# Left window
arcade.draw_lrtb_rectangle_filled(130, 200, 340, 265, arcade.color.GLITTER)
arcade.draw_line(165, 340, 165, 265, arcade.color.DIM_GRAY, 4)
arcade.draw_line(130, 305, 200, 305, arcade.color.DIM_GRAY, 4)
# Right window
arcade.draw_lrtb_rectangle_filled(300, 370, 340, 265, arcade.color.GLITTER)
arcade.draw_line(335, 340, 335, 265, arcade.color.DIM_GRAY, 4)
arcade.draw_line(300, 305, 370, 305, arcade.color.DIM_GRAY, 4)
# Door
arcade.draw_lrtb_rectangle_filled(210, 290, 230, 120, arcade.color.CG_RED)
# Door knob
arcade.draw_ellipse_filled(265, 190, 10, 10, arcade.color.KOBE)

# Left bush
arcade.draw_ellipse_filled(140, 140, 115, 70, arcade.color.JUNE_BUD)

# Right bush
arcade.draw_ellipse_filled(360, 140, 115, 70, arcade.color.JUNE_BUD)

# Car
# Car body
arcade.draw_polygon_filled(((580, 110),
                            (580, 150),
                            (610, 150),
                            (610, 190),
                            (685, 190),
                            (685, 150),
                            (720, 150),
                            (720, 110)
                            ),
                            arcade.color.AQUA)
# Left car wheel
arcade.draw_circle_filled(610, 110, 15, arcade.color.BLACK_OLIVE)
# Right car wheel
arcade.draw_circle_filled(690, 110, 15, arcade.color.BLACK_OLIVE)
# left car window
arcade.draw_lrtb_rectangle_filled(620, 641, 180, 150, arcade.color.ASH_GREY)
# right car window
arcade.draw_lrtb_rectangle_filled(654, 675, 180, 150, arcade.color.ASH_GREY)

arcade.finish_render()

arcade.run()

