import os.path
import subprocess


def download_file(oss_location, local_location):
    if os.path.exists(local_location):
        return None
    download_command = f"ossutil cp {oss_location} {local_location}"
    subprocess.call(download_command, shell=True)


def list_file(bucket, directory):
    # 使用 ossutil 列出指定目录下的文件
    oss_list_command = f"ossutil ls {bucket}/{directory}"
    oss_files = subprocess.check_output(oss_list_command, shell=True).decode("utf-8").split("\n")[1:-1]
    oss_locations = []
    for oss_location in oss_files:
        if not oss_location.__contains__('oss://'):
            continue
        oss_locations.append(oss_location.split()[-1])
    return oss_locations


def list_filtered_file(bucket, directory, filter_str):
    # 使用 ossutil 列出指定目录下的文件
    oss_list_command = f'ossutil ls {bucket}/{directory} --include="*{filter_str}*"'
    oss_files = subprocess.check_output(oss_list_command, shell=True).decode("utf-8").split("\n")[1:-1]
    oss_locations = []
    for oss_location in oss_files:
        if not oss_location.__contains__('oss://'):
            continue
        oss_locations.append(oss_location.split()[-1])
    return oss_locations


def get_name(oss_location):
    return oss_location.split('/')[-1]



# ret = list_file('oss://dahanghai-open', 'channel.2200803434968/taobao/oaid_download')
# ret = list_filtered_file('oss://dahanghai-open', 'channel.2200803434968/taobao/oaid_download', '20230904')
# print(ret)