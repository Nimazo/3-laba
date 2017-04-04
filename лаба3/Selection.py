import time
import random
def selectionSort(alist):
   k = 0
   q = 0
   t1 = time.time()
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0    
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               k += 1
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       q +=1
   print('Кол-во сравнений ',k)
   print('Кол-во перестановок ', q)
   print('Кол-во времени ', time.time() - t1)
   

n = int(input())
alist = list([random.randint(1, 999) for i in range(n)])
print(alist)

selectionSort(alist)
print(alist)
