import os
import redis

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis.data-pipeline.svc.cluster.local"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    password=os.getenv("REDIS_PASSWORD"),  # k8s Secret에서 주입
    db=int(os.getenv("REDIS_DB", "0")),
    decode_responses=True,  # str로 받고 싶을 때
    socket_connect_timeout=2,
    socket_timeout=2,
)

print(r.ping())  # True
r.set("hello", "world", ex=60)  # TTL 60s
print(r.get("hello"))

