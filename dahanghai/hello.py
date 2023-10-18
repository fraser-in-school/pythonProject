import sys

try:
    if __name__ == '__main__':
        # 打开一个文件以写入输出
        output_file = open('/data/zlong/active/data/device/oaid/td/devices/output.txt', 'w')

        # 保存原始的标准输出对象
        original_stdout = sys.stdout

        # 将标准输出重定向到文件
        sys.stdout = output_file

        print("hello")

except Exception as e:
    print(f"An exception occurred: {e}")