import heapq
x = [1,2,4,55,-1,5,65,99]
heap = list(x)
heapq.heapify(heap)
print(heap)

heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
heapq.heappop(heap)
print(heap)

# import time

# def deco(func):
#     def wrapper(*args, **keargs):
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print("time is {}" .format(res))
#         res = t2 - t1
#         return res
#     return wrapper
