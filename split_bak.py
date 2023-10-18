import os
import datetime
import json
import config

# 指定大文件路径和拆分大小

oaid_large_file = 'all_idfa.td.txt'
split_size = 10000000  # 一千万行一个小文件

# 获取今天的日期
date_str = config.get_tomarrow_str()

# 初始化计数器
file_counter = 0
line_counter = 0
output_file = None

# 用于记录已处理的行数
processed_lines = {'idfa_process_line': 0, 'oaid_process_line': 0}
# JSON 文件的路径
json_file_path = os.path.join('./', 'processed_lines.json')

# 检查是否存在 JSON 文件，如果存在则读取 processed_lines 的值
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        processed_lines = json.load(json_file)


device_list = ['idfa', 'oaid']
for device in device_list:

    large_file = f'all_{device}.td.txt'
    # 创建以日期命名的文件夹
    device_folder = f'{device}.{date_str}'
    os.makedirs(device_folder, exist_ok=True)
    # 打开大文件并逐行读取
    with open(large_file, 'r') as large_file:
        processed = 0
        if device == 'idfa':
            processed = processed_lines['idfa_process_line']
        if device == 'oaid':
            processed = processed_lines['oaid_process_line']

        for _ in range(processed):
            next(large_file)

        print(f"{device}跳过{processed}行")

        file_counter = int(processed // split_size)
        line_counter = int(processed % split_size)

        for line in large_file:
            if line_counter % split_size == 0:
                # 达到拆分大小，关闭当前文件，创建下一个文件
                if output_file:
                    output_file.close()
                file_counter += 1
                output_file = open(f'{device_folder}/idfa.{date_str}.{file_counter:05d}', 'a')
                print(f"生成文件{output_file.name}")

            # 写入当前行到输出文件
            output_file.write(line)
            line_counter += 1
        print("文件分割成功")

    # 关闭最后一个文件
    if output_file:
        output_file.close()

    print(f'成功拆分并保存到文件夹：{device_folder}')

with open(json_file_path, 'w') as json_file:
    json.dump(processed_lines, json_file)
