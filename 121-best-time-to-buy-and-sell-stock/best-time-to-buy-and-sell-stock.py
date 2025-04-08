class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 999999
        # either buy or sell on a day
        # keep track of lowest price seen and profit you would get if you sold on this day
        for p in prices:
            # buy
            if p < minPrice:
                minPrice = p
            # sell
            else:
                maxProfit = max(maxProfit, p - minPrice)

        return maxProfit
        