import redis
import sys
import random
redisClient = redis.Redis()

def getRandomUsersAndScores():
    users = []
    for i in range(1, 10):
        player = {}
        player["playerID"] = str(i)
        player["score"] = random.randint(1, 100)
        users.append(player)
    return users


try:
    redisClient.ping()
    users = []
    users = getRandomUsersAndScores()
    redis
    playerSortedSet = "players"
    # Add the users in Sorted Set
    for user in users:
        print(user["playerID"], user["score"] )
        redisClient.zadd(playerSortedSet, {user["playerID"]:user["score"]})
    print("Contents of the Redis sorted set in ascending order:")

    print(redisClient.zrange(playerSortedSet, 0, -1, withscores=True))





except redis.ConnectionError as connectionException:
    print("Redis is down! Check Redis server")
    print(connectionException)

# print(users)


