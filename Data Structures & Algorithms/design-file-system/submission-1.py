class TrieNode:
    def __init__(self):
        self.children = {} # c : ()
        self.val = -1 

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        
    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        path = path.split("/")
        for i, c in enumerate(path):
            if i == 0:
                continue
            if c not in curr.children:
                if i == len(path) - 1:
                    curr.children[c] = TrieNode()
                else:
                    return False
            curr = curr.children[c]
        
        if curr.val != -1:
            return False
        
        curr.val = value
        return True

    def get(self, path: str) -> int:
        curr = self.root

        path = path.split("/")
        for i, c in enumerate(path):
            if i == 0:
                continue
            if c not in curr.children:
                return -1
            curr = curr.children[c]
        return curr.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
