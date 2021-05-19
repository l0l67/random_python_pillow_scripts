import cv2 as cv
import numpy as np
import random

res_x, res_y = 1000, 1000

x,y = int(res_x/2), int(res_y/2)
img = np.zeros((res_x, res_y, 3), np.uint8)

coords = []

frame_count = 0

while(True):


    y_tmp = random.randint(-1,1)
    x_tmp = random.randint(-1,1)
    
    if x < res_x and y < res_y:
        y += y_tmp 
        x += x_tmp
        if (x,y) in coords:
            img[y,x] = 255,0,0
        else:
            coords.append(tuple((x,y)))
            img[y,x] = 255,255,255


        
    print(f"frame {frame_count} from {res_x*res_y} frames total or {(frame_count/(res_y*res_x) * 100):.2f}% frames drawn")
    
    
    frame_count += 1

    cv.imshow('RGB', img)
    
    key = cv.waitKey(1)

    if key == ord('q'):
        break
