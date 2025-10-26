class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        # loop over length of list
        n = len(sensor1)
        drop1 = False
        drop2 = False
        # at the last idx it doesnt matter
        for i in range(0, n-1):
            if sensor1[i] != sensor2[i]:
                # check if sensor 1 dropped

                if sensor1[i:-1] == sensor2[i+1:]:
                    print(f'sensor1[i:-1]: {sensor1[i:-1]} sensor2[i+1]: {sensor2[i+1:]}')
                    drop1 = True

                # check if sensor 2 dropped 
                if sensor2[i:-1] == sensor1[i+1:]:
                    print(f'sensor2[i-1]: {sensor2[i:-1]} sensor1[i+1:]: {sensor1[i+1:]}')
                    drop2 = True
                break
                
        
        if drop1 and not drop2:
            return 1
        if drop2 and not drop1:
            return 2
        else:
            return -1