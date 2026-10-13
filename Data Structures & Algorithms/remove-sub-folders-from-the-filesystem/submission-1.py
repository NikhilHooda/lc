class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path) -> None:
        curr = self.root
        for f in path.split("/"):
            if f not in curr.children:
                curr.children[f] = TrieNode()
            curr = curr.children[f]
        curr.word = True
    
    def prefix_search(self, path) -> Bool:
        curr = self.root
        folders = path.split("/")
        for i in range(len(folders) - 1):
            curr = curr.children[folders[i]]
            if curr.word:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f)
        
        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)
        return res
