class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # pos = [3, 5, 10, 3]
        # pos = [3, 3]

        # pos = [3, 5, (10-0)/5=2, 3]

        # position = [0,1,4,7]
        # speed = [5,2,2,1]

        #time = [2, 5, 3, 3]

        #stack = [5, 3]
        
        # calculate time array
        for i in range(len(position)):
            position[i] = (position[i], i)
        position = sorted(position)
        time = []
        for i in range(len(position)):
            time.append((target-position[i][0])/speed[position[i][1]])
        #make stack
        stack = []
        stack.append(time[0])
        for i in range(1, len(time)):
            while stack and stack[-1] <= time[i]:
                stack.pop()
            stack.append(time[i])
        return len(stack)

