class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start (nlogn)
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        merged = []

        # go through each interval
        i = 0
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]

            # keep merging as long as end1 >= start2
            while i+1 < n and end >= intervals[i+1][0]:
                end = max(end, intervals[i+1][1])
                i+=1

            merged.append([start, end])
            i+=1
        
        return merged




        