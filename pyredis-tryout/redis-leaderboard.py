import redis
import sys
import random
import names
redisClient = redis.Redis(
    host= 'REPLACE THIS BY REDIS HOST',
    port= 'REPLACE THIS BY REDIS PORT',
    password= 'REPLACE THIS BY REDIS PASSWORD')

def getRandomUsersAndScores():
    users = []
    for i in range(1, 15):
        player = {}
        player["playerID"] = names.get_first_name()
        player["score"] = random.randint(1, 100)
        users.append(player)
    return users


try:
    redisClient.ping()
    users = []
    users = getRandomUsersAndScores()
    playerSortedSet = "players"
    # Add the users in Sorted Set
    for user in users:
        # print(user["playerID"], user["score"] )
        redisClient.zadd(playerSortedSet, {user["playerID"]:user["score"]})
    print("Contents of the Redis sorted set in ascending order:")
    print(redisClient.zrange(playerSortedSet, 0, -1))
    print("Cardinality of the Redis sorted set:")
    print(redisClient.zcard(playerSortedSet))
    print("Count of playerSortedSet between a score/vote of 50 to 100:")
    print(redisClient.zcount(playerSortedSet, 50, 100))
    print("Count of playerSortedSet between a score/vote of 0 to 50:")
    print(redisClient.zcount(playerSortedSet, 0, 50))
    print("Find the rank/score of an element in the Redis sorted set:")
    elementValue = "1"
    print("Score of the element with value '{}' is ".format(elementValue))
    print(redisClient.zscore(playerSortedSet, "1"))
    print("Retrieve elements from the Redis sorted set based on a range of scores:")
    print(redisClient.zrangebyscore(playerSortedSet, min=0, max=100, withscores=True))
    print("Retrieve elements from the Redis sorted set based on a range of scores in reverse orders:")
    print(redisClient.zrevrangebyscore(playerSortedSet, min=0, max=100, withscores=True))
    print(redisClient.zrange(playerSortedSet, 0, -1, withscores=True))

except redis.ConnectionError as connectionException:
    print("Redis is down! Check Redis server")
    print(connectionException)

# print(users)


