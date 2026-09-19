class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # {userId -> list of [count, tweetId]}
        self.followMap = defaultdict(set) # {userId -> set of followeeId}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ans, minHeap = [], []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])
        
        heapq.heapify(minHeap)
        while minHeap and len(ans) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            ans.append(tweetId)
            index -= 1
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
 
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
