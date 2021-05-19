import cv2 as cv
import numpy as np
import random


key = cv.waitKey(1)


res_x = 500 #x resolution
res_y = 500 #y resolution

x = 0
y = 0
img = np.zeros((res_x, res_y, 3), np.uint8)

already_drawn = {"x": [], "y": []}
one = False

p_counter = 0

rand_colors = input("random colors? y/n: ")


while(True):
    x = random.randint(0, res_x -1)
    y = random.randint(0, res_y -1)

    for key, values in already_drawn.items():
        while (key == "x" and values == x) and (key == "y" and values == y):  #if there is already a point drawn on this location
            x = random.randint(0, res_x -1)
            y = random.randint(0, res_y -1)
        else:
            one = True

    if one == True: #if new pixel
        if rand_colors == "n":
            img[y,x] = (255,255,255)
        else:
            img[y,x] = (random.randint(100, 254), random.randint(100, 254), random.randint(100, 254))
        p_counter += 1
        one = False
    
    p_done = (p_counter/(res_x * res_y)) * 100 #calculate %
    print(f'{int(p_done)}% Done')

    
    cv.imshow('random_pixel_gen', img) #draw frame

    key = cv.waitKey(1)

    if key == ord('q'): #if key q pressed quit
        break