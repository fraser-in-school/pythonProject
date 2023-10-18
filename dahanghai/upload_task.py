import sys

import oss_client
import cos_client
import re

"""
target：需要将大航海的撞库结果上传到 cos上
doc: https://zhi-long.feishu.cn/wiki/AhOXwEVJ3iQDzKkg3qRcGcPanLg oss 数据产出
1. 将 OSS 路径下的文件都按下载下来，按 日期/设备分组
2. 按日期/设备 处理，提取出该天的所有文件，从文件中提取出 tag
3. 将文件上传到 cos
"""

oss_bucket = 'oss://dahanghai-open'
cos_bucket = 'hadoop-1319813010'
down_directory = '/data/zlong/active/data/device/oaid/td/devices/dahanghai'
success_file = '/Users/zhanghao/PycharmProjects/pythonProject/dahanghai/_SUCCESS'


class DahanghaiFile:
    def __init__(self, oss_location, device):
        self.device = device
        self.oss_location = oss_location
        self.file_name = oss_client.get_name(oss_location)
        self.tag = get_tag(self.file_name)
        self.date_str = get_data_str(self.file_name)
        self.local_location = f'{down_directory}/{self.date_str}/{self.device}/{self.file_name}'
        self.cos_directory = f'/data/crowd/{self.date_str}/offline/dahanghai/{self.device}Md5/{self.tag}'
        self.cos_key = f'{self.date_str}:{self.device}:{self.tag}'

    def download(self):
        print(f'download--{self.oss_location} {self.local_location}')
        # oss_client.download_file(self.oss_location, self.local_location)

    def upload(self, index):
        cos_file_name = f'{self.date_str}_offline_dahanghai_{self.device}Md5_{self.tag}.{index}.txt'
        print(f'upload--{self.local_location} {self.cos_directory}/{cos_file_name}')
        # cos_client.upload_file(cos_bucket, self.local_location, f'{self.cos_directory}/{cos_file_name}')


def get_tag(file_name):
    # 使用正则表达式匹配并提取数字部分
    match = re.search(r'result_cuhuo_(\d+)\.', file_name)

    if match:
        extracted_string = match.group(1)  # 提取第一个匹配组中的字符串
        return extracted_string
    else:
        print("未找到匹配的字符串")


def get_data_str(file_name):
    # 使用正则表达式匹配并提取数字部分
    match = re.search(r'\.(\d+)__', file_name)
    if match:
        extracted_string = match.group(1)  # 提取第一个匹配组中的字符串
        return extracted_string
    else:
        print("未找到匹配的字符串")


def get_objs(date_str, device):
    oss_directory = f'channel.2200803434968/taobao/{device}_download'
    oss_locations = oss_client.list_filtered_file(oss_bucket, oss_directory, date_str)
    dahanghai_objs = []
    for oss_location in oss_locations:
        dahanghai_objs.append(DahanghaiFile(oss_location=oss_location, device=device))

    return dahanghai_objs


if __name__ == '__main__':
    # 打开一个文件以写入输出
    output_file = open('output.txt', 'w')

    # 保存原始的标准输出对象
    original_stdout = sys.stdout

    # 将标准输出重定向到文件
    sys.stdout = output_file
    date_str1 = ''
    if len(sys.argv) > 1:
        date_str1 = sys.argv[1]
    dahanghai_objs = get_objs(date_str1, 'oaid')
    dahanghai_objs.extend(get_objs(date_str1, 'idfa'))

    # 创建一个空字典来存储分组后的对象
    grouped_objects = {}

    # 遍历对象数组并分组
    for obj in dahanghai_objs:
        cos_key = obj.cos_directory
        if cos_key not in grouped_objects:
            grouped_objects[cos_key] = []
        grouped_objects[cos_key].append(obj)

    for key, value in grouped_objects.items():
        index = 1
        for dahanghai_obj in value:
            dahanghai_obj.download()
            dahanghai_obj.upload(index)
            index += 1
        print(key)
        print(f'create success:{cos_bucket} {success_file} {key}/_SUCCESS')
        # cos_client.upload_file(cos_bucket, success_file, f'{cos_key}/_SUCCESS')

    output_file.close()
