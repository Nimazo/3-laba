import random
import time
def shellSort(alist):
    q = 0
    k = 0
    t1 = time.time()
    sublistcount = len(alist)//2
    
    while sublistcount > 0:
      k +=1  
        

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
        q += 1

  
      sublistcount = sublistcount // 2
    print('Кол-во перестановок ', q)
    print('Кол-во сравнений ',k)
    print('Кол-во времени ', time.time() - t1)
    

def gapInsertionSort(alist,start,gap):
    
    
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
     

n = int(input())
alist = list([random.randint(1, 999) for i in range(n)])
print(alist)
shellSort(alist)
print(alist)
