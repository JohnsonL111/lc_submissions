class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # we want to collect the most fruit available
        # we have 2 baskets and each can only hold a single type of fruit 
        # must pick exactly 1 fruit from every tree (moving left to right) starting from any tree of your choice
        # fruits = [0,1,2,2]
        # output = 3. Skip the first tree. Collect 1,2,2

        # we want to figure out what tree to start from where if we scan from its right we maximize the number of trees we pick from
        # the choice of tree selected previously does impact if the next tree can be selected (ex: full baskets) but its not recurisve in nature therefore this is not a dp problem.
        # we cant sort the array since that will break the order and we cant do that since we must scan left to right
        # we maintain a window between L and R pointers and keep adding the fruits on the Rth tree if we can. If we CANT add the fruits on the Rth tree (full basket) then we must reassess the current # of trees picked from so far between the window. We want to compare it the number of fruits selected previously on a different window and take the max of the two.
        # we want to slide the L pointer until we can add fruits to our basket again
        # we should use a hashmap to keep track of the type of/how many of it of the fruits we collected so far
        # when R reaches the end of the trees we return the max # of trees in a window found so far.

        collected = defaultdict(int)
        maxTrees = 0
        l, r = 0, 0
        end = len(fruits)-1
        MAX_BASKETS = 2

        while r <= end:
            fruit = fruits[r]
            collected[fruit] += 1

            # condition breaks
            while len(collected) > MAX_BASKETS:

                fruit_remove = fruits[l]
                collected[fruit_remove] -=1

                if collected[fruit_remove] == 0:
                    del collected[fruit_remove]
                l+=1
            # <= 2 baskets
            numTrees = r-l+1
            maxTrees = max(maxTrees, numTrees)
            r += 1
        return maxTrees
            



        