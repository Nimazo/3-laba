import random
import time

def swap(i, j):
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():
    t1 = time.time()
    q = 0
    k = 0
    end = len(sqc)   
    start = end // 2 - 1 
    for i in range(start, -1, -1):
        q += 1
        heapify(end, i)   
    for i in range(end-1, 0, -1):
        k += 1
        swap(i, 0)   
        heapify(i, 0)
    print('Кол-во сравнений ',q)
    print('Кол-во перестановок ', k)
    print('Кол-во времени ', time.time() - t1)
n = int(input())
sqc = list([random.randint(1, 999) for i in range(n)])
heap_sort()
print(sqc)

