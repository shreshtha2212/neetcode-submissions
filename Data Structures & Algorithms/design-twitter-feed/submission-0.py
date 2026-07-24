class Twitter:

    def __init__(self):
        self.counter=0
        from collections import defaultdict
        self.user_tweets=defaultdict(list)
        self.tweets=defaultdict(int)
        self.user_following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter+=1
        self.user_tweets[userId].append(tweetId)
        self.tweets[tweetId]=self.counter


        

    def getNewsFeed(self, userId: int) -> List[int]:
        following=set(self.user_following[userId])
        following.add(userId)
        heap=[]
        for i in following:
            for k in self.user_tweets[i][-10:]:
                heap.append(k)
        self.build_max_heap(heap)
        news_feed=[]
        while heap and len(news_feed)<10:
            newest_tweet=self.pop_max(heap)
            news_feed.append(newest_tweet)
        return news_feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
    
    def build_max_heap(self,heap:List[int])->None:
        for i in range(len(heap)//2-1,-1,-1):
            self.heapify_down(heap,i)
    def heapify_down(self,heap:List[int], index:int)->None:
        while True:
            largest=index
            left=2*index+1
            right=2*index+2
            if left<len(heap) and self.tweets[heap[left]]>self.tweets[heap[largest]]:
                largest=left
            if right<len(heap) and self.tweets[heap[right]]>self.tweets[heap[largest]]:
                largest=right
            if largest==index:
                break
            heap[largest], heap[index]= heap[index], heap[largest]
            index=largest
    def pop_max(self,heap:List[int])->int:
        newest_tweet=heap[0]
        heap[0]=heap[-1]
        heap.pop()
        if heap:
            self.heapify_down(heap,0)
        return newest_tweet
            



        
