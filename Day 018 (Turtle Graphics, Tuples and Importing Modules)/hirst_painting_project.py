# import random
# import turtle as turtle_module
#
# # import colorgram
# #
# # # Extract 6 colors from an image.
# # colors = colorgram.extract('img.jpg', 30)
# # rgb_colors = []
# #
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_colors.append(new_color)
# #
# #
# # # colorgram.extract returns Color objects, which let you access
# #
# # print(rgb_colors)
# turtle_module.colormode()
# tim = turtle_module.Turtle()
# color_list = [(249, 248, 248), (231, 235, 241), (234, 242, 240), (247, 241, 246), (1, 9, 29), (122, 95, 41),
#               (238, 211, 73), (77, 34, 23), (221, 80, 59), (225, 117, 100), (92, 1, 21), (179, 139, 170),
#               (151, 92, 116), (35, 90, 26), (8, 154, 72), (205, 64, 92), (220, 177, 219), (167, 129, 75),
#               (1, 63, 146), (3, 80, 30), (4, 220, 217), (80, 134, 178), (77, 115, 147), (129, 157, 178),
#               (123, 185, 166), (124, 8, 30), (12, 213, 221), (245, 203, 5), (134, 221, 207), (229, 174, 167)]
#
# tim.dot(20, random.choice(color_list))
#
# screen = turtle_module.Screen()
# screen.exitonclick()

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.write("GRAPHICS, TUPLES : DAY 018", font=("Verdana", 15, "normal"), align='right')

# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
# (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233,
# 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148,
# 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
color_list = [(249, 248, 248), (231, 235, 241), (234, 242, 240), (247, 241, 246), (1, 9, 29), (122, 95, 41),
              (238, 211, 73), (77, 34, 23), (221, 80, 59), (225, 117, 100), (92, 1, 21), (179, 139, 170),
              (151, 92, 116), (35, 90, 26), (8, 154, 72), (205, 64, 92), (220, 177, 219), (167, 129, 75),
              (1, 63, 146), (3, 80, 30), (4, 220, 217), (80, 134, 178), (77, 115, 147), (129, 157, 178),
              (123, 185, 166), (124, 8, 30), (12, 213, 221), (245, 203, 5), (134, 221, 207), (229, 174, 167)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()