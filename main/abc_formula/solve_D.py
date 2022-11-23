import math

def main(a, b, c): # FORGIVE ME FOR MY SINS
    a = int(a)
    b = int(b)
    c = int(c) 
    print("D is: ",end='')
    d = int(b**2 - 4*a*c)
    print(d)

    if d <= 1:
        print("No solution")
    else:
        print("answer 1")
        print((-b + math.sqrt(d)) / (2 * a))
        print((-b - math.sqrt(d)) / (2 * a))