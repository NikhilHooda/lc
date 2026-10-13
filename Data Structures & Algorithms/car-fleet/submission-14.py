class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 1,4,7,10
        # 4,6,8,10

        # 4,6,8,10
        # 1,3,5,7,9,10
        # 0,1,2,3,4,5,6,7,8,9,10
        # 7,8,9,10

        # (7,1),(4,2),(1,2),(0,1)
        #   3  ,  3,   5,   10
        # stack = [3, 5, 10]
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        stack = []
        for position, speed in cars:
            time = (target - position) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        
