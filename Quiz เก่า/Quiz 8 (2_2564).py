def get_secret(t):
    return ''.join(t.split(t[0])[2::2])
  
def print_secret(filename):
    for line in open(filename, "r"): print(get_secret(line))
        
exec(input().strip()) # DON'T remove this line
