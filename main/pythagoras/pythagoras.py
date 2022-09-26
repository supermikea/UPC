import math
import sys

def main(fll, sll):

    #S staat voor Square(kwadraat)
    fllS = (float(fll)**2)
    sllS = (float(sll)**2)

    ansS = sllS + fllS

    ans = math.sqrt(sllS + fllS)

    print(fll + "^2 + " + str(sll) + "^2 = " + str(ansS))
    print("Square root of " + str(ansS) + " is: " + str(ans))
    sys.exit()