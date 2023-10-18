import requests
import hashlib

secret_key = 'JniWQjitRfQZntCH'
domain_name = 'https://api.e.mi.com'
# 请求的 URL
update_url = '/openapi/tools/userPackage/update/tag'  # 请替换为实际的上传 URL

update_list_url = '/openapi/tools/userPackage/updateInfo/availableUpdateList'

state_url = '/openapi/tools/userPackage/updateInfo/get'
# 要上传的文件路径
file_path = '/data/apps/rta-package-upload/jd/20231008/oaidOrigin_only_1173456292.txt-xiaomi-tmp/oaidOrigin_only_1173456292.txt.split.2.txt'  # 请替换为实际的文件路径

# 请求参数
params = {
    'customerId': 482232,  # 第一个参数
    'model': 'overwrite',
    'signId': 'b741ef165103518ef3fe23a3aeaea071',
    'tagId': 281811,   # 第二个参数
}


available_params = {
    'customerId': 482232,  # 第一个参数
    'signId': 'b741ef165103518ef3fe23a3aeaea071',
    # 'tagId': 273003,
  # 第二个参数
}

state_params = {
    'customerId': 475802,  # 第一个参数
    'signId': 'b741ef165103518ef3fe23a3aeaea071',
    'tagId': 273018,
  # 第二个参数
}



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


def get_md5(base_str):
    md5_hash = hashlib.md5()
    md5_hash.update(base_str.encode('utf-8'))
    return md5_hash.hexdigest().lower()


params['sign'] = get_str(params)
print(params['sign'])
available_params['sign'] = get_str(available_params)
print(available_params['sign'])
# 使用字典构建 formData
# form_data = {
#     'targetFile': (file_path, open(file_path, 'rb'))  # 将文件添加到 formData
# }


def post_req(url, params, files):
    response = requests.post(domain_name + url, files=form_data, params=params)

    response.encoding = 'utf-8'
    # 打印响应
    print(response.status_code)
    print(response.text)


def get_req(url, params):
    response = requests.get(url=domain_name + update_list_url, params=available_params)
    response.encoding = 'utf-8'
    # 打印响应
    print(response.status_code)
    print(response.text)


get_req(update_list_url, available_params)
#get_req(state_url, state_params)
# post_req(update_url, params, form_data)
#get_req(state_url, state_params)