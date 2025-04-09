import heapq
class MedianFinder:

    def __init__(self):
        # use two heaps to store the values
        # max heap then min heap
        # python has no built in max heap so store negatives
        # median if even # -> mean of top of min/max heap
        # median if odd # -> top of the max heap. Add 
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
        # Step 1: Decide where to initially add the number
        if (len(self.max) + len(self.min)) % 2 == 0:
            # Add to max heap first (as negative)
            heapq.heappush(self.max, -num)
            # Balance: largest in max heap should not be greater than smallest in min heap
            if self.min and -self.max[0] > self.min[0]:
                # Swap tops between heaps
                to_min = -heapq.heappop(self.max)
                to_max = heapq.heappop(self.min)
                heapq.heappush(self.max, -to_max)
                heapq.heappush(self.min, to_min)
        else:
            # Add to min heap
            heapq.heappush(self.min, num)
            # Balance: if new number is smaller than max of max heap, swap
            if -self.max[0] > self.min[0]:
                to_min = -heapq.heappop(self.max)
                to_max = heapq.heappop(self.min)
                heapq.heappush(self.max, -to_max)
                heapq.heappush(self.min, to_min)
        
    def findMedian(self) -> float:
        # if even then median is mean of top of max and min heap
        if (len(self.max) + len(self.min)) % 2 == 0:
            return (self.min[0] + self.max[0] *-1) / 2
        else:
            return self.max[0] * -1 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()