import heapq
nums = [4, 1, 7, 3, 8, 5]
heap = []
pick = 3

def kth_smallest(nums, pick) :
    heap = []
    for num in nums :
        heapq.heappush(heap, num)
    
    print(heap)

    kth_min = None

    for _ in range(pick) :
        kth_min = heapq.heappop(heap)
        print(kth_min)
    return kth_min


print(kth_smallest(nums, pick))