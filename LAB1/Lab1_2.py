"""
Lab1 - PART 2
2/9/2019 - Ken Amamori
CS2302 MW 10:30 - 11:50
"""
#importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math

#ax, center: centre, rad: radius of a circle
def circle(ax,center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    ax.plot(x,y,color='k') #draw a circle
  
#n times, centre, radius, next circle line
def draw_circles(ax,n,center,radius,w):
    if n>0:
        circle(ax,center,radius) #draw a circle with given center and radius
        draw_circles(ax,n-1,[center[0]*w,center[1]],radius*w,w) #call the method with new center and radius

plt.close("all") #clse a figure window
fig, ax = plt.subplots()

#call a method called draw_circles(ax, number of circles, centre, radius, interval)
draw_circles(ax, 10, [100,0], 100,.6) #for 2a
#draw_circles(ax, 50, [100,0], 100,.9) #for 2b
#draw_circles(ax, 100, [100,0], 100,.95) #for 2c

ax.set_aspect(1.0) #x:y=1:1
ax.axis('off') #x,y-axis
plt.show() #display figure
#fig.savefig('lab1_2a.png') #save the figure
