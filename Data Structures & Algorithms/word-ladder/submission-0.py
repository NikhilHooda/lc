class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjMap = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjMap[pattern].append(word)
        
        queue = collections.deque()
        queue.append(beginWord)
        visit = set()
        visit.add(beginWord)
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)): 
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjMap[pattern]:
                        if nei not in visit:
                            queue.append(nei)
                            visit.add(nei)
            res += 1
        return 0

