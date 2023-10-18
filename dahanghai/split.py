import os
import datetime
import json
import zipfile

import config


def split(file, out_path, split_size):
    with open(file, 'r') as large_file:
        file_counter = 0
        line_counter = 0
        output_file = None
        file_name = os.path.basename(file)
        for line in large_file:
            if line_counter % split_size == 0:
                # 达到拆分大小，关闭当前文件，创建下一个文件
                if output_file:
                    output_file.close()
                file_counter += 1
                output_file = open(f'{out_path}/{file_name}.split.{file_counter}.txt', 'w')
                print(f"生成文件{output_file.name}")
                zip_file_name = f'{output_file.name}.zip'
                with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(output_file.name, os.path.basename(output_file.name))

            # 写入当前行到输出文件
            output_file.write(line)
            line_counter += 1
        print("文件分割成功")


split('/Users/zhanghao/PycharmProjects/pythonProject/dahanghai/20230905/oaid/result_cuhuo_381109.20230823__0951402db4654538979475e49d5fb62b_4.txt',
      '/Users/zhanghao/PycharmProjects/pythonProject/dahanghai/20230905/oaid',
      100000)