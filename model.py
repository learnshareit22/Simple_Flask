import math
 
# ax2 + bx + c = 0
def quadratic(a,b,c):
  if a==0:
    return -c/b
  delta = b**2 - 4*a*c
  if delta < 0:
    return None
  elif delta == 0:
    return -b/(2*a)
  else:
    return (-b+math.sqrt(delta))/(2*a), (-b-math.sqrt(delta))/(2*a)
 
