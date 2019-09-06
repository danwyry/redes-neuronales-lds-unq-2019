import sys

def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

arr = [1,2,3,4,5,6,7,8,0]
matrix = [[1,2,3],[4,5,6],[7,8,0]]
s = "123456780012345678"
def t1():
    global arr
    str(arr)
    t = arr[0]
    arr[0] = arr[8]
    arr[8] = t

def t2():
    global matrix
    str(matrix)
    t = matrix[0][0]
    matrix[0][0] = matrix[2][2]
    matrix[2][2] = t

def t3():
    global s
    pos = 8
    new_pos = 0
    a = s[new_pos]
    pos1 = new_pos if new_pos < pos else pos
    pos2 = new_pos if new_pos > pos else pos
    e1 = '0' if new_pos < pos else a
    e2 = '0' if new_pos > pos else a
    s = s[0:pos1] + e1 + \
               s[pos1 + 1:pos2] + e2 + \
               s[pos2 + 1:9] + \
               str(new_pos)

import timeit
timeit.timeit(t1,number=100000)
timeit.timeit(t2,number=100000)
timeit.timeit(t3,number=100000)