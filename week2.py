# WEEK 2  CODING CHALLENGES 


# def calculate_area(width, height):
#     input_width = input("Width of area: ")
#     input_height = input("Height of area: ")
#     width = int(input_width)
#     height = int(input_height)
#     area = width * height 
#     return area 


# def calculate_areas ():
#     # calculates area 
#     width = int(input("width of area: "))
#     height = int(input("Height of area: "))
#     area = width * height
#     print(f"\nWidth: {width}")
#     print(f"Height: {height}")
#     print(f"Calculated surface area: {area}")

# calculate_areas()


def get_width():
    width = int(input("width of area: "))
    return width 

def get_height():
    height = int(input("Height of area: "))
    return height 


def calculate_area():
    width = get_width()
    height = get_height()
    area = width * height
    print(f"\nWidth: {width}")
    print(f"Height: {height}")
    print(f"Calculated surface area: {area}")

calculate_area()