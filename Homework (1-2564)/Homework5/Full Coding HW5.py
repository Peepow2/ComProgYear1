import matplotlib.pyplot as plt
from matplotlib import animation, rc
import random
import math

def main():
    import sys
    # check if this code is running in colab
    in_colab = 'google.colab' in sys.modules
    
    random.seed(1111)
    W, H = 120, 100
    # 200 birds on a WxH window
    x,y,dx,dy = gen_data(200, W, H)

    fig = plt.figure(figsize=(4*W/H, 4))
    anim = animation.FuncAnimation(fig, animate, 
                    fargs=(x, y, dx, dy, W, H),
                    frames=(60 if in_colab else None), 
                    repeat=False, interval=50)
    if in_colab:
        rc('animation', html='jshtml')
        return anim
    else:
        plt.show()

def animate(n, x, y, dx, dy, W, H):   
    NOISE = 0.3        # +/- direction noise radians
    R = 0.10*min(W, H) # neighbors within R
    V = 0.02*min(W, H) # velocity -> displacement in each time step  
    move_all(x, y, dx, dy, V, W, H)
    ax = [0.0]*len(x)
    ay = [0.0]*len(x)
    for k in range(len(x)):
        ax[k],ay[k] = neighbor_average_direction(x, y, dx, dy, k, R)
        t = math.atan2(ay[k],ax[k]) + (NOISE - 2*NOISE*random.random())
        ax[k] = math.cos(t)
        ay[k] = math.sin(t)
    dx[:] = ax   # update the orginal dir vector
    dy[:] = ay
    plt.clf()    # clear figure
    plt.quiver(x, y, dx, dy) # plot a 2D field of arrows
    plt.xlim((0, W))
    plt.ylim((0, H))

#-------------------------------------------

# HW5: Vicsek Model
def gen_data(N, W, H):
    x = []; y = []; dx = []; dy = []
    for i in range (N):
        posX = random.random() * W;
        posY = random.random() * H;
        x += [posX]; y += [posY];
        theta = float(random.random() * 2 * math.pi)
        dx += [math.cos(theta)]
        dy += [math.sin(theta)]
    return x, y, dx, dy
#-------------------------------------------
def move_all(x, y, dx, dy, d, W, H):
    size = len(x)
    for i in range(size):
        _dx = dx[i]; _dy = dy[i];
        if _dx > 0 and _dy > 0: # (0, 90)
            angle = math.atan(_dy/_dx)    
        elif _dx < 0 and _dy > 0: # (90, 180)
            angle = math.pi - math.atan(_dy/-_dx)
        elif _dx < 0 and _dy < 0: # (180, 270)
            angle = math.pi + math.atan(_dy/_dx)    
        elif _dx > 0 and _dy < 0: # (270, 360)
            angle = (2 * math.pi) - math.atan(-_dy/_dx)
        elif _dx == 0 and _dy > 0: # 90
            angle = math.pi/2      
        elif _dx == 0 and _dy < 0: # 270
            angle = (3/2) * math.pi      
        elif _dx < 0 and _dy == 0: # 180
            angle = math.pi     
        else:
            angle = 0
        x[i] = (x[i] + d * math.cos(angle)) % W
        y[i] = (y[i] + d * math.sin(angle)) % H

#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
  u = 0; v = 0; n = 0;
  size = len(x);
  for i in range(size):
      if (math.sqrt((x[k] - x[i])**2 + (y[k] - y[i])**2)) <= R:
          u += dx[i]; v += dy[i]
          n += 1
          
  mx = (u/n)/math.sqrt((u/n)**2 + (v/n)**2)
  my = (v/n)/math.sqrt((u/n)**2 + (v/n)**2)
  return mx, my;
#-------------------------------------------
main()
