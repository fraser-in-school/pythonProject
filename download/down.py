import os
import subprocess

# 定义 OSS 存储桶名称和目录
oss_bucket = "your-oss-bucket"
oss_directory = "your-oss-directory/"

# 定义本地合并后的文件名
local_merged_file = "merged.txt"

# 过滤规则函数，这里示例为选择以 ".txt" 结尾的文件
def filter_files(files):
    return [file for file in files if file.endswith(".txt")]

# 使用 ossutil 列出指定目录下的文件
oss_list_command = f"ossutil ls oss://{oss_bucket}/{oss_directory}"
oss_files = subprocess.check_output(oss_list_command, shell=True).decode("utf-8").split("\n")

# 根据过滤规则选择文件
selected_files = filter_files(oss_files)

# 下载选定的文件到本地
for file in selected_files:
    file_name = file.split()[-1]
    local_file_path = os.path.join(".", file_name)
    download_command = f"ossutil cp {file} {local_file_path}"
    subprocess.call(download_command, shell=True)

# 合并下载的文件成一个大文件
with open(local_merged_file, "wb") as merged_file:
    for file in selected_files:
        file_name = file.split()[-1]
        local_file_path = os.path.join(".", file_name)
        with open(local_file_path, "rb") as f:
            merged_file.write(f.read())

# 清理下载的临时文件
for file in selected_files:
    file_name = file.split()[-1]
    local_file_path = os.path.join(".", file_name)
    os.remove(local_file_path)
