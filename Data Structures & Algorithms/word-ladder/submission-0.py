class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        steps=1
        q=deque([(beginWord,1)])

        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            chars=list(word)
            for i in range(len(word)):
                original=word[i]
                for j in range(97,123):
                    chars[i]=chr(j)
                    new_word="".join(chars)
                    if new_word in wordList:
                        q.append((new_word,step+1))
                        wordList.remove(new_word)
                
                chars[i]=original
        return 0


        
        