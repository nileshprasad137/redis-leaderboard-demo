# redis-leaderboard-demo

Was just trying out Redis. Came across Lambda Store (https://lambda.store/). Unlike AWS Elasticache, LambdaStore lets you have serverless Redis.
Tried it out, its quite good! 

Used datastore as Serverless Redis on Lambda Store, and just wrote a simple function to fetch top Players in Redis DB and exposed the service on AWS Lambda.
