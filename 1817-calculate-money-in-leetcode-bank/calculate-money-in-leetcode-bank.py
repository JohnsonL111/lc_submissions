class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        m = 1
        d = 1
        day_before = 0

        while (d <= n):
            # check if monday
            if d % 7 == 1:
                day_before = m
                total += m
                m += 1
            # other days
            else:
                to_add = day_before + 1
                total += to_add
                day_before += 1
            d += 1  
        return total
        