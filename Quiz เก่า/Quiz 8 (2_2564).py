def get_secret(t):
    t = t.split(t[0])[2::2]
    return ''.join(t)
  
def print_secret(filename):
    for line in open(filename, "r"): print(get_secret(line))
exec(input().strip()) # DON'T remove this line
