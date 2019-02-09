import matplotlib.pyplot as plt
import numpy as np
import math

def draw_5circles(ax, n, center, rad):
    if n>0:
        newrad = rad/3
        x,y=circle([center[0]+rad-newrad,center[1]],newrad)
        ax.plot(x,y,color='k')
        draw_5circles(ax,n-1,[center[0]+rad-newrad,center[1]],newrad)

        x,y=circle([center[0]-rad+newrad,center[1]],newrad)
        ax.plot(x,y,color='k')
        draw_5circles(ax,n-1,[center[0]-rad+newrad,center[1]],newrad)

        x,y=circle(center,newrad)
        ax.plot(x,y,color='k')
        draw_5circles(ax,n-1,center,newrad)

        x,y=circle([center[0],center[1]+rad-newrad],newrad)
        ax.plot(x,y,color='k')
        draw_5circles(ax,n-1,[center[0],center[1]+rad-newrad],newrad)

        x,y=circle([center[0],center[1]-rad+newrad],newrad)
        ax.plot(x,y,color='k')
        draw_5circles(ax,n-1,[center[0],center[1]-rad+newrad],newrad)

        x,y=circle(center,rad) #big circle
        ax.plot(x,y,color='k')
        
def draw_tree(ax, c, n, dx, dy):
    if n>0:
        ax.plot([c[0],c[0]-dx],[c[1],c[1]-dy], color='k')
        ax.plot([c[0],c[0]+dx],[c[1],c[1]-dy], color='k')
        draw_tree(ax,[c[0]-dx,c[1]-dy],n-1,dx*0.5,dy*0.9)
        draw_tree(ax,[c[0]+dx,c[1]-dy],n-1,dx*0.5,dy*0.9)

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

#n times, centre, radius, next circle line
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        center[0]=center[0]*w
        draw_circles(ax,n-1,center,radius*w,w)

def draw_squares(ax,c,r,n):
    if n>0:
        p=np.array([[c[0]-r,c[1]-r], [c[0]+r,c[1]-r], [c[0]+r,c[1]+r], [c[0]-r,c[1]+r], [c[0]-r,c[1]-r]])
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax, [c[0]-r, c[1]-r], r/2, n-1)
        draw_squares(ax, [c[0]+r, c[1]-r], r/2, n-1)
        draw_squares(ax, [c[0]+r, c[1]+r], r/2, n-1)
        draw_squares(ax, [c[0]-r, c[1]+r], r/2, n-1)

plt.close("all") #clse a figure window
fig, ax = plt.subplots()

#for part 1
#draw_squares(ax,[500,500],500,2) #part 1a
#draw_squares(ax,[500,500],500,3) #part 1b
#draw_squares(ax,[500,500],500,4) #part 1c

#for part 2
#draw_circles(ax, 10, [100,0], 100,.6) #for 2a
#draw_circles(ax, 50, [100,0], 100,.9) #for 2b
#draw_circles(ax, 100, [100,0], 100,.95) #for 2c

#part 3
#c=np.array([0,0])
#draw_tree(ax, c, 3, 50, 50) #for 3a
#draw_tree(ax, c, 4, 50, 50) #for 3b
#draw_tree(ax, c, 7, 50, 50) #for 3c

#part 4
#draw_5circles(ax, 2, [0,0], 100)
#draw_5circles(ax, 3, [0,0], 100)
#draw_5circles(ax, 4, [0,0], 100)

ax.set_aspect(1.0) #x:y=1:1
ax.axis('on')
plt.show()
#fig.savefig('lab1_2c.png')