import os
import sys

file_path = './rtb_behavior.20231020_18.log'
# 获取第一个命令行参数
if len(sys.argv) > 1:
    file_path = file_path + sys.argv[1]

log_count_map = {}

def add_to_dict(record):
    global log_count_map
    print(record[4], record[5])
    print(f'price={record[19]}, cost={record[20]}, type={record[21]}')
    action = record[0].split()[-1]
    media = record[2]
    key = media + '-' +  action
    if key in log_count_map:
        log_count_map[key] += 1
    else:
        log_count_map[key] = 1


if not os.path.exists(file_path):
    print(f"文件{file_path}不存在")
with open(file_path, 'r') as log_file:
    for line in log_file:
        record = line.split("\t")
        add_to_dict(record)


print(log_count_map)