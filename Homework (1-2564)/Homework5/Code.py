# HW5: Vicsek Model
# ID: Name
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

