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
    #i = input()
    #s.set_pixel(x1, y1, nothing)
    for event in s.stick.get_events():
      print(event.direction, event.action)
      
      if event.action == 'pressed' and event.direction == 'right':
        x1 += 1
        positionD = True
        positionA = False
        positionS = False
        positionW = False
        
      if event.action == 'pressed' and event.direction == 'left':
        x1 -= 1
        positionD = False
        positionA = True
        positionS = False
        positionW = False
        
      if event.action == 'pressed' and event.direction == 'down':
        y1 += 1
        positionD = False
        positionA = False
        positionS = True
        positionW = False
        
      if event.action == 'pressed' and event.direction == 'up':
        y1 -= 1
        positionD = False
        positionA = False
        positionS = False
        positionW = True
      
      s.set_pixel(x1, y1, yellow)
move()
