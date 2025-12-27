class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end
        # max # of non overlapping ints = # intervals - min # of intervals to remove
        # therefore: min # of intervals to remove = # intervals - max # of non overlapping ints
        # to maximize max # of non-overlapping ints we want to greedy pick the non-overlapping interval with smallest end time (pick more intervals) -> this is EXACTLY the interval scheduling problem
        intervals.sort(key=lambda x: x[1]) 
        max_overlap = 0
        last_end = float('-inf')

        for start, end in intervals:
            # keep interval if valid
            if start >= last_end:
                last_end = end
                max_overlap += 1

        return len(intervals) - max_overlap
        