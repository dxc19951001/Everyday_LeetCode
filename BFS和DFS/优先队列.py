import heapq
pqeueue = list()

heapq.heappush(pqeueue, (1, 'A'))
heapq.heappush(pqeueue, (7, 'B'))
heapq.heappush(pqeueue, (3, 'C')) 
heapq.heappush(pqeueue, (6, 'D'))
heapq.heappush(pqeueue, (2, 'E'))

print(pqeueue)

while pqeueue:
    print(heapq.heappop(pqeueue))

   
