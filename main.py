import sys, random, time
# import matplotlib.pyplot as plt
# import numpy as np
sys.setrecursionlimit(1500)


def insert(_list, elem): # insert an element
    _list.append(elem)
    siftup(_list, (len(_list) - 1))
    
    
    
def remove(_list):
    if len(_list) > 1:
        t = _list[1]
        swap(_list, 1, (len(_list) - 1))
        _list.pop()
        siftdown(_list, 1)
        return t

def swap(_list, i, j): # swaps the values of i and j
    _list[i], _list[j] = _list[j], _list[i]


    
    
def siftup(_list, i): 
    while i >= 2:
        j = i // 2
        if _list[j] <= _list[i]:
            return
        swap(_list, i, j)
        i = j
        
def siftdown(_list, i):
    while i*2 < len(_list):
        left = i*2
        right = left+1
        
        j = left if right >= len(_list) or _list[left] <= _list[right] else right
        if _list[i] <= _list[j]:
            break
        swap(_list, i, j)
        i = j
def siftdown_mod(_list, i, _len):
    # modified siftdown procedure as per question 1 in Jon Bentley's: Thanks, Heaps
    while i*2 < _len:
        left = i*2
        right = left+1
        j = left if right >= _len or _list[left] <= _list[right] else right
        if _list[i] <= _list[j]:
            break
        swap(_list, i, j)
        i = j


def heapsort_original(data):

    
    x = [-1] # to be used to get the last element in the list
        
    for elem in data:
        insert(x, elem)
        
    r = []
    while True:
        t = remove(x)
        if t is None:
            break
        r.append(t)
        
    data[:] = r # slice the entire list to r

    
    
def heapsort_modified(data):
    data.insert(0, -1)

    _len = len(data)

    for i in range(2, _len):
        siftup(data, i)

    for i in range((_len - 1), 1, -1):
        swap(data, i, 1)
        siftdown_mod(data, 1, i)

    data.pop(0)  # O(N)

    # flip the array to turn into min-heap
    for i in range(len(data) // 2):
        swap(data, i, len(data)-i-1)

        
    
for sort in [heapsort_original, heapsort_modified]:
    for data_size in [100, 1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]:
        data_set = [[random.randint(1, 100) for i in range(data_size)],
                 [random.uniform(1, 100) for i in range(data_size)],
                 [1] * data_size,
                 list(range(data_size)),
                 list(reversed(range(data_size)))]
        for i, data in enumerate(data_set):
            t = time.time()
            sort(data)
            print('%-5d\t%d\t%.8f' % (data_size, i+1, time.time() - t))
            assert data == sorted(data)
    print('____________')



    
