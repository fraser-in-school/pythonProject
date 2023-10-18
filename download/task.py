import os
import subprocess
import config


class Task:
    def __init__(self, oss_bucket, oss_directory, local_directory, filter_func, interval):
        self.oss_bucket = oss_bucket
        self.oss_directory = oss_directory
        self.local_directory = local_directory
        self.filter_func = filter_func
        self.interval = interval

    def download(self):
        try:
            # 使用 ossutil 列出指定目录下的文件
            oss_list_command = f"ossutil ls {self.oss_bucket}/{self.oss_directory}"
            oss_files = subprocess.check_output(oss_list_command, shell=True).decode("utf-8").split("\n")

            # 根据过滤规则选择文件
            selected_files = [file for file in oss_files if self.filter_func(file)]

            # 下载选定的文件到本地
            for file in selected_files:
                file_name = file.split()[-1]
                download_command = f"ossutil cp -r {file_name} {self.local_directory}"
                subprocess.call(download_command, shell=True)
        except Exception as e:
            print(f"Error: {str(e)}")

    def merge(self):
        # 合并下载的文件成一个大文件
        merged_file_path = os.path.join(self.local_directory, f"merged.{config.get_data_str()}.txt")
        local_files = []
        for root, dirs, files in os.walk(self.local_directory):
            # root 是当前遍历的目录
            # dirs 是当前目录下的子目录列表
            # files 是当前目录下的文件列表
            # 遍历当前目录下的文件

            selected_files = [file for file in files if self.filter_func(file)]
            with open(merged_file_path, "wb") as merged_file:
                for file in selected_files:
                    file_name = file.split()[-1]
                    local_file_path = os.path.join(self.local_directory, file_name)
                    with open(local_file_path, "rb") as f:
                        merged_file.write(f.read())

            # 清理下载的临时文件
            for file in selected_files:
                file_name = file.split()[-1]
                local_file_path = os.path.join(self.local_directory, file_name)
                os.remove(local_file_path)

        print("Task completed successfully.")

    def upload(self):
        import subprocess

        # 定义 curl 命令
        curl_command = [
            'curl',
            '--location',
            '--request', 'POST',
            f'http://172.22.16.27:8091/jd/uploadMedia?filePath=%2Fdata%2Fzlong%2Factive%2Fdata%2Fdevice%2Foaid%2Ftd%2Fdevices%2Fdown_files%2Fmerged.{config.get_data_str()}.txt&deviceType=OAID_MD5&ttAccounts=1773837481097223%2C1773837480348679&dataName=oaid_OSS_xzy3_'
        ]

        try:
            # 执行 curl 命令
            result = subprocess.run(curl_command, capture_output=True, text=True, check=True)

            # 输出命令的标准输出
            print("标准输出:")
            print(result.stdout)

            # 输出命令的标准错误
            print("标准错误:")
            print(result.stderr)

            # 获取命令的返回码
            print("返回码:", result.returncode)
        except subprocess.CalledProcessError as e:
            # 如果命令执行失败，捕获异常并打印错误信息
            print("命令执行失败:", e)


# 示例用法：
def filter_txt_files(file):
    return file.endswith(".txt")


def contains_767460(file):
   # return f'767460.20230902' in file
   return f'767460.{config.get_data_str()}' in file


task = Task(
    oss_bucket="oss://dahanghai-open",
    oss_directory="channel.2200803434968/taobao/oaid_download",
    local_directory="./down_files",
    filter_func=contains_767460,
    interval=3600  # 执行间隔为1小时（3600秒）
)


def run():
    print("run")
    task.download()
    task.merge()
    task.upload()

run()