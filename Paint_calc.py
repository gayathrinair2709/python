#Calculate the number of paint cans required for the area
import math
def paint_calc(height, cover, width):
    area = height * width
    paint_can = math.ceil(area /cover)
    print(f"For {area} cm^2 we need {paint_can} paint cans")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

