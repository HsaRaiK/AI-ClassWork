import random
import operator as op
from functools import reduce


def cointoss():
    return  random.choice(["H","T"])

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def main():
    numb_Heads = 0
    numb_Tails = 0

    n = int(input("Enter number of Coin flip states: "))

    for i in range(n):
        result = cointoss()
        print(result)
        if result =="H":
            numb_Heads += 1
        if result =="T":
            numb_Tails += 1
    comb1res = ncr(n, numb_Heads)
    p_value = comb1res * ( 0.5 ** numb_Heads) * (0.5 ** numb_Tails)


    print("number of Heads ", numb_Heads,". number of Tails ",numb_Tails)
    print("{0:.3f}" .format(p_value))
    if (p_value < 0.05 ):
        print("Data implies an anomaly case ")
    elif (p_value >= 0.05 ):
        print("Data does not support that the coin is unfair ")

if __name__ == '__main__':
     main()
