import os

host = os.environ['HOST']
redis_hostA = os.environ['REDIS_HOST'] # 추가
redis_port = os.environ['REDIS_PORT']  # 추가

# $Env:HOST = "localhost:8000"
# $Env:REDIS_HOST = "localhost"
# $Env:REDIS_PORT = 6379