def res():
    print("Which resolution would you like to play in? (Choose an option)")
    print(""" 
                 '4:3'    |     '16:9'  
           1. 1600 x 1200 | 6. 1920 x 1080 
           2. 1280 x 960  | 7. 1600 x 900 
           3. 1152 x 864  | 8. 1280 x 720 
           4. 1024 x 768  | 9. 1024 x 576 
           5. 800 x 600   | 10. 960 x 540 
            ------------- | ------------- 
    """)
    option = input("Enter the option: ")
    while option == '':
        option = int(input("This option doesnt exist, enter another option: "))

    option = int(option)
    while option > 10 or option == 0:
        option = int(input("This option doesnt exist, enter another option: "))

    if option == 1:
        WIDTH = 1600
        HEIGHT = 1200
    elif option == 2:
        WIDTH = 1280
        HEIGHT = 960
    elif option == 3:
        WIDTH = 1152
        HEIGHT = 864
    elif option == 4:
        WIDTH = 1024
        HEIGHT = 768
    elif option == 5:
        WIDTH = 800
        HEIGHT = 600
    elif option == 6:
        WIDTH = 1920
        HEIGHT = 1080
    elif option == 7:
        WIDTH = 1600
        HEIGHT = 900
    elif option == 8:
        WIDTH = 1280
        HEIGHT = 720
    elif option == 9:
        WIDTH = 1024
        HEIGHT = 576
    elif option == 10:
        WIDTH = 960
        HEIGHT = 540
    else:
        pass

    return WIDTH, HEIGHT
