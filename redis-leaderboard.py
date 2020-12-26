import redis
import sys
import random
redis_client = redis.Redis()
try:
    redis_client.ping()
    users = []
    i = 1
    for i in range(1,10):
        player = {}
        player["playerID"] = i
        player["score"] = random.randint(1,100)
        users.append(player)

except redis.ConnectionError as connectionException:
    print("Redis is down! Check Redis server")
    print(connectionException)
except Exception as exception:
    print(exception)

print(users)