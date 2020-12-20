import sys
import math
values = sys.stdin.readlines()

numbers = [int(i) for i in values]

amount = numbers.pop(0)

def prime(i):
    value = i*2
    for x in range(2,round(value/2)):
        w = value - x
        if (w + x)/2 == i:
            counter = 0
            for y in range(3, int(math.sqrt(x) + 1)):
                if x%y == 0:
                    counter += 1
                    break
            for z in range(2, int(math.sqrt(w) + 1)):
                if w%z == 0:
                    counter += 1
                    break
            if counter == 0:
                return(str(x)+' '+str(w)+'\n')  
                     
for i in numbers:
    sys.stdout.write(prime(i))
