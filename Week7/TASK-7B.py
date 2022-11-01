import random

ordered = []
randomed = []

for a in range(0,10000,10):
    ordered.append('T')
    ordered.append('T')
    ordered.append('T')
    ordered.append('T')
    ordered.append('T')
    ordered.append('H')
    ordered.append('H')
    ordered.append('H')
    ordered.append('H')
    ordered.append('H')



print("Pre Defined Sequence is : ")
print(ordered)
print("For Defined Sequnce  P(H):")
num_head_ord = 0
num_tail_ord = 0
for a in range(0,10000):
    if ordered[a] == 'H':
        num_head_ord += 1
print(num_head_ord/10000)
print("For Defined Sequnce  P(T):")
for a in range(0,10000):
    if ordered[a] == 'T':
        num_tail_ord += 1
print(num_tail_ord/10000)
num_tail_given_head_ord = 0
print("For Defined Sequence P(T|H)")
for a in range(0,9999):
    if ordered[a] == 'H':
        if ordered[a+1] == 'T':
            num_tail_given_head_ord += 1
print(num_tail_given_head_ord / num_head_ord)
num_head_given_tail_ord = 0
print("For Defined Sequence P(H|T)")
for a in range(0,9999):
    if ordered[a] == 'T':
        if ordered[a+1] == 'H':
            num_head_given_tail_ord += 1
print(num_head_given_tail_ord / num_tail_ord )
print("For Defined Sequence P(H|H)")
print(1 - (num_tail_given_head_ord / num_head_ord) )
print("For Defined Sequence P(H|H)")
print(1 - (num_head_given_tail_ord / num_tail_ord ) )




print("\n")
for a in range(0,10000):
    randomvalue = random.randint(0,1)
    if randomvalue == 0:
        randomed.append('T')
    elif randomvalue == 1:
        randomed.append('H')
    else:
        print("Debug 2 ")
print("Random Sequence is :")
print(randomed)
print("For Random  P(H):")
num_head_rand = 0
num_tail_rand = 0
for a in range(0,10000):
    if randomed[a] == 'H':
        num_head_rand += 1
print(num_head_rand/10000)
print("For Random  P(T):")
for a in range(0,10000):
    if randomed[a] == 'T':
        num_tail_rand += 1
print(num_tail_rand/10000)
num_tail_given_head_rand = 0
print("For Random Sequence P(T|H)")
for a in range(0,9999):
    if randomed[a] == 'H':
        if randomed[a+1] == 'T':
            num_tail_given_head_rand += 1
printValue = 0
printValue = num_tail_given_head_rand / num_head_rand
print("{0:.6f}".format(printValue))
num_head_given_tail_rand = 0
print("For Random Sequence P(H|T)")
for a in range(0,9999):
    if randomed[a] == 'T':
        if randomed[a+1] == 'H':
            num_head_given_tail_rand += 1
printValue = num_head_given_tail_rand / num_tail_rand
print( "{0:.6f}".format(printValue))
print("For Random Sequence P(H|H)")
printValue = 1 - (num_tail_given_head_rand / num_head_rand)
print ("{0:.6f}".format(printValue))
print("For Random Sequence P(H|H)")
printValue = 1 - (num_head_given_tail_rand / num_tail_rand )
print("{0:.6f}".format(printValue))