import baidu_realtime_bidding_pb2  # 导入生成的代码
import json
import os

json_file_path = '/Users/zhanghao/PycharmProjects/pythonProject/protobuf/request.json'
request = {}
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        request = json.load(json_file)

# 封装 JSON 数据到 Protocol Buffers 消息中
message = baidu_realtime_bidding_pb2._globals.
message. = json.dumps(request)

# 将消息序列化为二进制数据
binary_data = message.SerializeToString()
