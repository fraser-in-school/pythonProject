import json
import zipfile
import datetime
import requests
import hashlib
import os
import time
import asyncio


secret_key = 'JniWQjitRfQZntCH'
sign_id = 'b741ef165103518ef3fe23a3aeaea071'
domain_name = 'https://api.e.mi.com'
# 请求的 URL
update_url = '/openapi/tools/userPackage/update/tag'  # 请替换为实际的上传 URL

available_url = '/openapi/tools/userPackage/updateInfo/availableUpdateList'

state_url = '/openapi/tools/userPackage/updateInfo/get'

split_rows = 40000000

zip_map = {'/data/apps/rta-package-upload/jd/20230916/oaidOrigin.txt': '/data/apps/rta-package-upload/jd/20230916/oaidOrigin.txt-xiaomi'}


def post_req(url, params, file):
    form_data = {
        'targetFile': (file, open(file, 'rb'))  # 将文件添加到 formData
    }
    response = requests.post(domain_name + url, files=form_data, params=params)

    response.encoding = 'utf-8'
    # 打印响应
    print(response.status_code)
    print(response.text)
    return json.loads(response.text)


def get_req(url, params):
    response = requests.get(url=domain_name + url, params=params)
    response.encoding = 'utf-8'
    # 打印响应
    print(response.status_code)
    print(response.text)
    return json.loads(response.text)


def split(file, split_size):
    if file in zip_map:
        return zip_map[file]
    zips = []
    dir = os.path.dirname(file)
    file_name = os.path.basename(file)
    out_path = f'{dir}/{file_name}-xiaomi'
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    with open(file, 'r') as large_file:
        file_counter = 0
        line_counter = 0
        output_file = None
        for line in large_file:
            if line_counter % split_size == 0:
                # 达到拆分大小，关闭当前文件，创建下一个文件
                if output_file:
                    output_file.close()
                    zips.append(save_zip(output_file))
                file_counter += 1
                output_file = open(f'{out_path}/{file_name}.split.{file_counter}.txt', 'w')
                print(f"生成文件{output_file.name}")


            # 写入当前行到输出文件
            output_file.write(line)
            line_counter += 1

        # 关闭最后一个文件
        if output_file:
            output_file.close()
            zips.append(save_zip(output_file))
        print("文件分割成功")
        # 创建一个 Zip 文件来存储分割后的小文件
    zip_map[file] = zips
    return zips


def save_zip(output_file):
    zip_file_name = f'{output_file.name}.zip'
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(output_file.name, os.path.basename(output_file.name))
    print(f'创建压缩包成功')
    return zip_file_name


def get_str(param_map):
    base_str = ''
    keys = param_map.keys()
    keys = sorted(keys)
    for key in keys:
        base_str += key + str(param_map[key])
    base_str += secret_key
    print(base_str)
    md5_hash = hashlib.md5()
    md5_hash.update(base_str.encode('utf-8'))
    return md5_hash.hexdigest().lower()


def get_available_list(customer_id):
    available_params = {
        'customerId': customer_id,  # 第一个参数
        'signId': sign_id,
    }
    available_params['sign'] = get_str(available_params)
    return get_req(available_url, available_params)


def check_update_status(response_json, tag_id):
    if response_json['success']:
        result = response_json['result']
        for item in result:
            if item['tagId'] == tag_id:
                return True
    else:
        print('查询可用列表失败')
    return False


def check_upload_result(response_json):
    if response_json['success']:
        return True
    return False


async def upload_file(customer_id, tag_id, file, model):
    try_times = 0
    while try_times < 10:
        json_data = get_available_list(customer_id)
        if check_update_status(json_data, tag_id):
            params = {
                'customerId': customer_id,  # 第一个参数
                'model': model,
                'signId': sign_id,
                'tagId': tag_id,  # 第二个参数
            }
            params['sign'] = get_str(params)
            json_data = post_req(update_url, params, file)
            if check_upload_result(json_data):
                return True
        print(f'当前tagid--{tag_id}不可更新，等待60s--try_times={try_times}')
        try_times += 1
        time.sleep(60)

    return False


# json_data = get_available_list(475802)
# print(json_data['success'])

def get_tomorrow_str():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y%m%d')


def get_data_str():
    today = datetime.date.today()
    return today.strftime('%Y%m%d')


def get_yesterday():
    today = datetime.date.today()
    tomorrow = today - datetime.timedelta(days=1)
    return tomorrow.strftime('%Y%m%d')


async def execute_task(task_item):
    file = task_item['file']
    file = file.replace('$today$', get_data_str())
    file = file.replace('$yesterday$', get_yesterday())
    zips = split(file, split_rows)
    tag_ids = task_item['tagIds']
    i = 0
    rets = []
    for zip in zips:
        rets.append(upload_file(task_item['customerId'], tag_ids[i], zip, 'overwrite'))
        i += 1
        time.sleep(60)
    await asyncio.gather(*rets)


async def do_task(tasks):
    rets = []
    for task_item in tasks:
        rets.append(execute_task(task_item))
    await asyncio.gather(*rets)


async def main():
    await upload_file(482192, 276614,
                      '/data/apps/rta-package-upload/jd/20230919/oaidOrigin.txt-xiaomi/oaidOrigin.txt.split.5.txt.zip',
                      'overwrite')

if __name__ == '__main__':
    asyncio.run(main())


