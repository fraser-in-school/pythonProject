import random

import redis

# 连接到Redis服务器
r = redis.Redis(host='120.48.170.108', port=6379, password='zlRsgmzX$', db=0)

# 获取所有键
all_keys = r.keys('b*')

# 从所有键中随机选择100个键
random_keys = random.sample(all_keys, 100)

# 打印随机选择的100个键
for key in random_keys:
    print(key)
