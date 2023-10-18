import os
import subprocess
import datetime

# 定义 OSS 存储桶名称和文件夹路径
bucket_name = 'your-bucket-name'
folder_path = 'oss://dahanghai-open/taobao/channel.2200803434968'


device_list = ['idfa', 'oaid']


def get_tomarrow_str():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y%m%d')


def get_data_str():
    today = datetime.date.today()
    return today.strftime('%Y%m%d')

date_str = get_tomarrow_str()

index = 0


def write_index(index):
    file_path = '/data/zlong/active/data/device/oaid/td/devices/dahanghai_day_index.txt'
    with open(file_path, 'w') as file:
        file.write(str(index % 15))


def read_index():
    global index
    file_path = 'dahanghai_day_index.txt'
    if os.path.exists(file_path):
    # 在脚本启动时读取昨天最大的编号
        with open('dahanghai_day_index.txt', 'r') as file:
            index = int(file.read())


def filter(file_name):
    global index
    x = int(file_name.split('.')[-1])
    return x % 15 == index


for device in device_list:
    # 列出 OSS 存储桶中的文件列表
    try:
        output = subprocess.check_output(['ossutil', 'ls', f'{folder_path}/{device}'])
        existing_files = [line.split()[-1] for line in output.decode('utf-8').split('\n') if line]
        # print(f'oss 已存在{existing_files}')
    except subprocess.CalledProcessError as e:
        print(f"Error listing files: {e}")
        existing_files = []

    read_index()
    # 遍历本地文件夹
    for root, _, files in os.walk(f'{device}.20230824'): # 只切一次，后面重复上传
        count = 0
        for file in files:
            local_file_path = os.path.join(root, file)
            file = file.replace('20230824', get_tomarrow_str())
            if not filter(file):
                continue
            print(f"本地文件--{file}")
            oss_object_name = f'{folder_path}/{device}_upload/{file}'

            # 如果文件已存在于 OSS 中，跳过上传
            if oss_object_name in existing_files:
                print(f"Skipping {file} as it already exists in OSS.")
            else:
                # 使用 ossutil cp 命令上传文件
                try:
                    subprocess.check_call(['ossutil', 'cp', local_file_path, oss_object_name])
                    count += 1
                    print(f"Uploaded {file} to {oss_object_name}.")
                except subprocess.CalledProcessError as e:
                    print(f"Error uploading {file}: {e}")


write_index(index + 1)
            # if count % 7 == 0:
            #     break