class WordDictionary:

    def __init__(self):
        self.children={}
        self.word=False
        

    def addWord(self, word: str) -> None:
        root=self
        for char in word:
            if char not in root.children:
                root.children[char]=WordDictionary()
            root=root.children[char]
        root.word=True

        

    def search(self, word: str) -> bool:
        root=self
        def dfs(i,root):
            if i==len(word):
                return root.word
            if word[i]=='.':
                for j in root.children.values():
                    if dfs(i+1,j):
                        return True
                return False
            if word[i] not in root.children:
                return False
            return dfs(i+1,root.children[word[i]])
        return dfs(0,root)


        
