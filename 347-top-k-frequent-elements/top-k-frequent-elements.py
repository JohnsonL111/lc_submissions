from collections import Counter
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list of ints, an integer K
        # output: list of k most freq elements
        #  nums =1,2,3,4,5 | k = 3
        # expected = 3,4,5 (any order)
        # insert into heap
            # 1,2,3
        # insert 4
            # 1,2,3,4
            # size > k, pop
            # 2,3,4
        # insert 5
            # 2,3,4,5
            # size > k, pop
            # 3,4,5
        # return 3,4,5

        # convert nums into Counter
        count = Counter(nums)

        # init min heap
        top_k = []
        heapify(top_k)

        # loop the dict
        for num, count in count.items():
            # insert (val,key) into heap since heap will sort by the key
            heappush(top_k, (count, num))
            # if size of heap > k
            if len(top_k) > k:
                # pop from heap (removes min).
                heappop(top_k)

        # convert the heap into a list
        # l = []
        # for count,num in top_k:
        #     l.append(num)
        # return []

        return [num for count, num in top_k]
