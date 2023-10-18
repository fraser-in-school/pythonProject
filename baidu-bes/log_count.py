import os


file_path = '/Users/zhanghao/PycharmProjects/pythonProject/baidu-bes/rta_behavior.20231017_00.log'
log_count_map = {}
if not os.path.exists(file_path):
    print(f"文件{file_path}不存在")
with open(file_path, 'r') as log_file:
    for line in log_file:
        record = line.split("\t")
        print(record)


def add_to_dict(record):
    global log_count_map
