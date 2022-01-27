import math

a = float(input())
b = float(input())
c = float(input())

theta = math.acos((1/2) * ((a-b) + (a-c)) / math.sqrt((a-b)**2 + (a-c) * (b-c)))
print(int(360 - math.degrees(theta)))
