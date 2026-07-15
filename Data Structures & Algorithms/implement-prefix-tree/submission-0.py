class TrieNode:
    def __init__(self):
        #hashmap
        self.children={}
        #mark end of word is false
        self.endOfWord=False 

class PrefixTree:

    def __init__(self):
        #creating root
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endOfWord=True

    def search(self, word: str) -> bool:
        cur=self.root

        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True

        
        