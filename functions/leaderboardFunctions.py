import os
import redis
import json

def getTopPlayer(event, context):
    redisClient = redis.Redis(
        host=os.environ['REDIS_HOST'],
        port=os.environ['REDIS_PORT'],
        password=os.environ['REDIS_PASSWORD']
    )
    requestBody = json.loads(event["body"])
    rangeLimit = int(requestBody["top"])
    playerSortedSet = "players"
    outputList = list()
    topPlayers = redisClient.zrevrange(playerSortedSet, 0, rangeLimit, withscores=True)
    for player in topPlayers:
        playerName = player[0].decode("utf-8")
        playerScore = player[1]
        outputList.append({"playerName" : playerName, "playerScore": playerScore })

    topPlayersResponse = {
        "players": outputList
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(topPlayersResponse)
    }
    return response
