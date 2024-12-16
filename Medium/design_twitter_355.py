from collections import defaultdict
import datetime
import heapq
import time
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((datetime.datetime.now(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.following[userId] | {userId}
        recent_tweets = []

        for followee in followees:
            recent_tweets.append(self.tweets[followee][-10:])

        merged_tweets = heapq.merge(
            *recent_tweets, reverse=True, key=lambda x: x[0])

        return [tweetId for _, tweetId in list(merged_tweets)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


class Twitter2(object):

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId].append((time.time(), tweetId))

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        users = self.following[userId] | {userId}
        posts = []

        for user in users:
            posts.extend(self.tweets[user])

        posts.sort(key=lambda x: x[-1])

        return [i for _, i in posts[:10]]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId != followerId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.following[followerId].discard(followeeId)


obj = Twitter2()
print(obj.postTweet(1, 5))
print(obj.getNewsFeed(1))
print(obj.follow(1, 2))
print(obj.postTweet(2, 6))
print(obj.getNewsFeed(1))
print(obj.unfollow(1, 2))
print(obj.getNewsFeed(1))
