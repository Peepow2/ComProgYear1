def gen_data(N, W, H):
    x = []
    y = []
    dx = []
    dy = []
    for i in range (N):
        posX = random.random() * W;
        posY = random.random() * H;
        x += [posX];  y += [posY]
        theta = float(random.random() * 2 * math.pi )
        dx += [posX * math.cos(theta)]
        dy += [posY * math.sin(theta)]
    return x, y, dx, dy

#-------------------------------------------
def move_all(x, y, dx, dy, d, W, H):
    size = len(x)
    for i in range(size):
        _dx = dx[i]; _dy = dy[i];
        if _dx != 0 and _dy != 0:
          angle = math.atan(_dy/_dx);
        elif _dy < 0:
          angle = 3*(math.pi)/2;
        elif _dy > 0:
          angle  =  (math.pi)/2;
        else:
          angle = 0;
        x[i] = (x[i] + d*math.cos(angle))%W
        y[i] = (y[i] + d*math.sin(angle))%H

#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
  u = 0; p = 0; v = 0; q = 0;
  size = len(x);
  for i in range(size):
      if (math.sqrt((x[k] - x[i])**2 + (y[k] - y[i])**2)) <= R:
          u += dx[i]
          p += 1
          v += dy[i]
          q += 1
  mx = (u/p)/math.sqrt((u/p)**2 + (v/q)**2)
  my = (v/q)/math.sqrt((u/p)**2 + (v/q)**2)
  return mx, my;
#-------------------------------------------
main()
