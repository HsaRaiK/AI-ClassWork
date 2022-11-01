# The Answer to this Problem is using a specific formula



def formula(n):
    lemma = float(1)
    for i in range(0,n-1):
        lemma *= ((365-i)/365)
    result = float(1 - lemma)
    return result



def main():
    a = 0
    isFound = False
    n = 1
    while (isFound != True):
        a = formula(n)
        #print(a)
        if a < 0.5:
            print(n)
            n += 1
        elif a > 0.5:
            isFound = True
            print(n, "Students")
            print("More than 0.5 probability is found")
            print("{0:.6f}".format(a))
    print("The calculation suggests that atleast {} students should enter".format(n-1))
    print("For the probability of atleast 2 people having the same birthday be more than half")

if __name__ == '__main__':
     main()