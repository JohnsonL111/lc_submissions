class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by start date
        # use pq to store the end dates. 
        # you can reuse a room if the current start time of the interval > top of pq (min)
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        pq = []
        heapq.heappush(pq, intervals[0][1]) # first meeting end time

        for start, end in intervals[1:]:
            # check if earliest ending meeting is done. IF yes then can reuse
            if pq[0] <= start:
                heapq.heappop(pq) # remove it
                heapq.heappush(pq, end) # add current end time
            # else just add the current end time to the heap (need new room)
            else:
                heapq.heappush(pq, end)

        # size of heap is the min # of rooms needed
        return len(pq)


