class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort by meeting start
        # if end1 > star2 then conflict

        intervals.sort(key=lambda x: x[0])
        lastEnd = float('-inf')
        for start, end in intervals:
            if lastEnd > start:
                return False
            lastEnd = end
        return True
        