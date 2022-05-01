import turtle as t
import random
#import colorgram

# def get_colors(image, colors): 
#     """Function to get the colors on a image using the colorgarm method extract. to avoid
#        the with colors the if statement remove them from the final list. (RGB with color 
#        is 255, 255, 255 so we remove the higer to 240"""  
#     colors_img = colorgram.extract(image, colors)
#     color_list = []
#     for color in colors_img:
#         if color.rgb.r < 245 and color.rgb.g < 245 and color.rgb.b < 245:
#             color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#     return color_list
t.colormode(255)
tor = t.Turtle()
tor.penup()
tor.speed("fastest")
tor.hideturtle()
color_list = [(188, 19, 46), (243, 232, 66), (216, 237, 244), (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209), (13, 167, 214), (206, 153, 93), 
              (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96), (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220), 
              (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187)]

tor.setheading(225)
tor.forward(300)
tor.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tor.dot(20, random.choice(color_list))
    tor.forward(50)

    if dot_count % 10 == 0:
        tor.setheading(90)
        tor.forward(50)
        tor.setheading(180)
        tor.forward(500)
        tor.setheading(0)

screen = t.Screen()
screen.exitonclick()

