from sense_hat import SenseHat
import time
import random
import math

s = SenseHat()
s.clear()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255 ,0)
yellow = (255, 255, 0)
nothing = (0, 0, 0)
s.set_pixel(1, 1, red)

alive = True
def move():
  x1 = 1
  y1 = 1
  
  while alive == True:
    i = input()
    s.set_pixel(x1, y1, nothing)
    
    if i == 'd':
      x1 += 1
      positionD = True
      positionA = False
      positionS = False
      positionW = False
      
    elif i == 'a':
      x1 -= 1
      positionD = False
      positionA = True
      positionS = False
      positionW = False
      
    elif i == 's':
      y1 += 1
      positionD = False
      positionA = False
      positionS = True
      positionW = False
      
    elif i == 'w':
      y1 -= 1
      positionD = False
      positionA = False
      positionS = False
      positionW = True
      
    s.set_pixel(x1, y1, yellow)
    time.sleep(1)
    s.set_pixel(x1, y1, nothing)
    
    while positionD == True:
      s.set_pixel(x1, y1, nothing)
      x1 += 1
      s.set_pixel(x1, y1, blue)
      time.sleep(1)
      
    while positionA == True:
      s.set_pixel(x1, y1, nothing)
      x1 -= 1
      s.set_pixel(x1, y1, blue)
      time.sleep(1)
      
    while positionS == True:
      s.set_pixel(x1, y1, nothing)
      y1 += 1
      s.set_pixel(x1, y1, blue)
      time.sleep(1)
    
    while positionW == True:
      s.set_pixel(x1, y1, nothing)
      y1 -= 1
      s.set_pixel(x1, y1, blue)
      time.sleep(1)
move()
  
  