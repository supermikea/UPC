import math

def main(fll, sll):

    #S staat voor Square(kwadraat)
    fllS = (float(fll) * float(fll))
    sllS = (float(sll) * float(sll))

    ansS = sllS + fllS

    ans = math.sqrt(ansS)

    print(fll + "^2 + " + str(sll) + "^2 = " + str(ansS) + "\n" + "Square root of " + str(ansS) + " is: " + str(ans))