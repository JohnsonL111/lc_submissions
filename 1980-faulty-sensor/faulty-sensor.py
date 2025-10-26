class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)

        # find first mismatch
        i = 0
        while i < n and sensor1[i] == sensor2[i]:
            i += 1
        if i == n:
            return -1  # identical

        # test both hypotheses at the first mismatch
        drop1 = (sensor1[i:-1] == sensor2[i+1:])  # s1 dropped at i
        drop2 = (sensor2[i:-1] == sensor1[i+1:])  # s2 dropped at i

        if drop1 and not drop2:
            return 1
        if drop2 and not drop1:
            return 2
        return -1  # ambiguous or neither fits
