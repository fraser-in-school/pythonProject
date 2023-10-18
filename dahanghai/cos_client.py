import os
from qcloud_cos import CosConfig, CosServiceError
from qcloud_cos import CosS3Client


secret_id = 'AKIDhIm5HwNoHj9OOBqHVaRFuPkuuvPnDf5O'
secret_key = 'FFH6jDXksyz0oQqB1kIH2Zsyqk5Sn47z'
region = 'ap-beijing'  # 例如，'ap-guangzhou'

config = CosConfig(
    Region=region,
    SecretId=secret_id,
    SecretKey=secret_key
)

cos_client = CosS3Client(config)


def upload_file(bucket, local_path, target_location):
    try:
        # 发送请求来检查文件是否存在
        response = cos_client.head_object(
            Bucket=bucket,
            Key=target_location,
        )
        # 如果文件存在，head_object 方法不会抛出异常

        print(f"文件 {target_location} 存在")
        return None
    except CosServiceError as e:
        if e.get_status_code() == 404:
            print(f"上传文件--{target_location}")
            response = cos_client.upload_file(
                Bucket=bucket,
                LocalFilePath=local_path,
                Key=target_location,
            )
        else:
            print(f"检查文件 {target_location} 存在时出现错误：{e}")



# upload_file('hadoop-1319813010', '/Users/zhanghao/PycharmProjects/pythonProject/processed_lines.json', '/data/crowd/20230904/test.txt ')