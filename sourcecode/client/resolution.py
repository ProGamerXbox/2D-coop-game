import pygame

def res():
    print("Here are some common examples of 'square' resolutions:")
    print("""
                     '4:3'    |     '16:9'  
                - 1600 x 1200 | 1920 x 1080 -
                - 1280 x 960  |  1600 x 900 -
                - 1152 x 864  |  1280 x 720 -
                - 1024 x 768  |  1024 x 576 -
                - 800 x 600   |   960 x 540 -
                ------------- | ------------- 
""")
    WIDTH = int(input("What width would you like to play in?: "))
    while WIDTH < 250:
        WIDTH = int(input("The width you've entered is too small, enter another width: "))
    while WIDTH > 1920:
        WIDTH = int(input("The width you've entered is bigger than the width of the screen, enter another width: "))
    HEIGHT = int(input("What height would you like to play in?: "))
    while HEIGHT < 250:
        HEIGHT = int(input("The width you've entered is too small, enter another width: "))
    while HEIGHT > 1080:
        HEIGHT = int(input("The width you've entered is too small, enter another width: "))

    while WIDTH / HEIGHT > 2:
        print("Resolution parameters you've entered are not 'Square'.")
        print("Here are some common examples of 'square' resolutions:")
        print("""
             '4:3'    |     '16:9'  
        - 1600 x 1200 | 1920 x 1080 -
        - 1280 x 960  |  1600 x 900 -
        - 1152 x 864  |  1280 x 720 -
        - 1024 x 768  |  1024 x 576 -
        - 800 x 600   |   960 x 540 -
        ------------- | ------------- 
""")

        WIDTH = int(input("What width would you like to play in?: "))
        while WIDTH < 250:
            WIDTH = int(input("The width you've entered is too small, enter another width: "))
        while WIDTH > 1920:
            WIDTH = int(input("The width you've entered is bigger than the width of the screen, enter another width: "))
        HEIGHT = int(input("What height would you like to play in?: "))
        while HEIGHT < 250:
            HEIGHT = int(input("The width you've entered is too small, enter another width: "))
        while HEIGHT > 1080:
            HEIGHT = int(input("The width you've entered is too small, enter another width: "))



    return WIDTH, HEIGHT












