class Twitter:

    def __init__(self):

        self.timeStamp =0
        self.user_tweets = defaultdict(list)
        self.user_follow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.timeStamp+=1

        self.user_tweets[userId].append((-self.timeStamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:

        tweets = self.user_tweets[userId][-10:]

        for followee in self.user_follow[userId]:
            tweets+= self.user_tweets[followee][-10:]

        return [tweetId for _,tweetId in heapq.nsmallest(10,tweets)]
        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.user_follow[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.user_follow[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)