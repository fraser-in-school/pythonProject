import os
import hashlib
import time

# 获取当前时间戳
timestamp = time.time() * 1000

print(f"当前时间戳: {timestamp}")


filedsId = "CArN85EXCeae6dg0/1694761876236/0422554047f540f39d616fe71f14781a.zip,CArN85EXCeae6dg0/1694761887172/da437364ab5d45c1bb23ccc032a6cbbd.zip,CArN85EXCeae6dg0/1694761898553/6b355420dbac4b02bf145723f882e0ec.zip,CArN85EXCeae6dg0/1694761908657/9dfc588c77764b639464785341395a1b.zip,CArN85EXCeae6dg0/1694761919286/42336322101e47558f6a445703352f0a.zip,CArN85EXCeae6dg0/1694761930509/7f5b31abc0ac4865902e29225e859cbe.zip,CArN85EXCeae6dg0/1694761939197/568748d533ce4322834e94e5f5c598ff.zip,CArN85EXCeae6dg0/1694761947107/dd4c41cdddfe461ca26f90e1b8d7972a.zip,CArN85EXCeae6dg0/1694761956500/58166128ba0e4e078066cc9e4f10e035.zip,CArN85EXCeae6dg0/1694761966066/d7b571ca53714a1c8683c859985e25d5.zip,CArN85EXCeae6dg0/1694761977921/7bb3be4ae12c4bb6a5f652052db796f6.zip,CArN85EXCeae6dg0/1694761986843/556bc62db41f47aebce54ff3afe6560f.zip,CArN85EXCeae6dg0/1694761996431/b231a453800a4b6789286d9774278791.zip,CArN85EXCeae6dg0/1694762007676/9f935d8014234f269dca32f7f31ca9ec.zip,CArN85EXCeae6dg0/1694762024429/5be4ac1cb3154d73acf0de8735b275fc.zip,CArN85EXCeae6dg0/1694762049782/f035b98863e04b9692a1f0dea08c9b40.zip,CArN85EXCeae6dg0/1694762066213/e7a83c191f05418097d386419f587abf.zip,CArN85EXCeae6dg0/1694762075112/738fcff19dc64affa8f718723f0d0cf8.zip,CArN85EXCeae6dg0/1694762085334/8cb0eb54a7434e3a90422889619af752.zip,CArN85EXCeae6dg0/1694762104060/c2b2fd59089e4f42be912c029345dcdf.zip,CArN85EXCeae6dg0/1694762117104/c2565266cd784309b86743c66dbb4cf7.zip,CArN85EXCeae6dg0/1694762126961/6fc2cdd8a31d4badb63657f1743c6579.zip,CArN85EXCeae6dg0/1694762135657/f4a20e482b6845d6b493cec2c39b683e.zip,CArN85EXCeae6dg0/1694762148724/6144af81812e4c118e1fd8596f97ed49.zip,CArN85EXCeae6dg0/1694762159459/8fe8e36171574b20b8ef75ab07e6c2b8.zip,CArN85EXCeae6dg0/1694762171486/3eb2fbcd66be4759aa7129caf0ae8d58.zip,CArN85EXCeae6dg0/1694762180185/1b0be1c4b85346c8b6e448d888ea08a0.zip,CArN85EXCeae6dg0/1694762189437/1b510fd9755443a1b137b2727758e846.zip,CArN85EXCeae6dg0/1694762197910/fdbcbb938ee644ac97264e4b2dfaa916.zip,CArN85EXCeae6dg0/1694762210803/5ea73a85d6204f0a9ac2f76e700672c2.zip,CArN85EXCeae6dg0/1694762220485/bd55ecd98eb64a329608baaebfcb6bf7.zip,CArN85EXCeae6dg0/1694762228823/d4ee6da119e04da3b6028b37f461c50f.zip,CArN85EXCeae6dg0/1694762238007/b587e3f52fe347498f4300472e899f2a.zip,CArN85EXCeae6dg0/1694762246436/21418b048d974bcdba58ba5fc671a476.zip,CArN85EXCeae6dg0/1694762257460/80f50dd2a8d64d6aa59bd4ba92b8046e.zip,CArN85EXCeae6dg0/1694762268230/4e5a0356139945929e81ab736fae8c84.zip,CArN85EXCeae6dg0/1694762277350/b118facf7d574013b31c6dd3fea84c16.zip,CArN85EXCeae6dg0/1694762285559/05e94b51b8cb4a5faa90b3f5b26ed684.zip,CArN85EXCeae6dg0/1694762295031/ba5bd17a428b430f89f6afad3c99ffc3.zip,CArN85EXCeae6dg0/1694762306674/14bc57755def465785a712e166d0ee20.zip,CArN85EXCeae6dg0/1694762317899/5a3324441f9743e89e3396bc50c0349b.zip,CArN85EXCeae6dg0/1694762327298/445e5405d6d34202850da49f4328ca90.zip,CArN85EXCeae6dg0/1694762336855/045dbba881e84cfea5bfea07c4e20e29.zip,CArN85EXCeae6dg0/1694762345197/0266e511363a4c7a94f8654011b9a67a.zip,CArN85EXCeae6dg0/1694762359486/27780dc00662462d8acc093ca0f59970.zip,CArN85EXCeae6dg0/1694762369373/b4ea80c40a23471681a88e7f12daa498.zip,CArN85EXCeae6dg0/1694762392398/a777f0730747494ea72f1a5bdc85c9d2.zip,CArN85EXCeae6dg0/1694762400748/20b400d541a5464e8068af7ced8a77fe.zip,CArN85EXCeae6dg0/1694762410861/5de0b2e8c9c04db2ae678c6c66bd989d.zip,CArN85EXCeae6dg0/1694762421203/46d481674dab4d06a372d459dcc167c7.zip,CArN85EXCeae6dg0/1694762432173/511b405627b948d287781965c3f53bd7.zip,CArN85EXCeae6dg0/1694762443823/e2e3d3de455d465db47325078f60cbde.zip,CArN85EXCeae6dg0/1694762452891/a3b7ef92ef6948dd8599aa5cb04d13b9.zip,CArN85EXCeae6dg0/1694762461244/b30b2bc3036d4a44af816e3dfa2d595e.zip,CArN85EXCeae6dg0/1694762474081/e06c8a8b94134728b10040e2f7384898.zip,CArN85EXCeae6dg0/1694762484436/44315f719e904ef681169ed36734c8c6.zip,CArN85EXCeae6dg0/1694762493213/3340046af24b4fe0b988ce8daa06d4d7.zip,CArN85EXCeae6dg0/1694762501340/c9179f268b3048189c690ea85f4f25a8.zip,CArN85EXCeae6dg0/1694762509229/cf00a56407fe408e887ef7ad6d93f324.zip,CArN85EXCeae6dg0/1694762519732/b9a493e7d438409e9a99a08064eb3c1a.zip,CArN85EXCeae6dg0/1694762533416/5c5c19bf049a43129fd93b2ec039c90f.zip,CArN85EXCeae6dg0/1694762542950/482ef1636e164f1f9bc63ebb73680bab.zip,CArN85EXCeae6dg0/1694762551485/d11745143dd94b7cac61122ebed63bb4.zip,CArN85EXCeae6dg0/1694762561226/63bc23031ae04bddb7e8fd47b3a52273.zip,CArN85EXCeae6dg0/1694762572693/ea80c90e70d046129c9b257234c8e062.zip,CArN85EXCeae6dg0/1694762580854/1e11e74e1078457e94516c207e89655b.zip,CArN85EXCeae6dg0/1694762590640/1479daca02d0429fb9cf58a1edbdf466.zip,CArN85EXCeae6dg0/1694762603399/ea880cded6a247d5adb2c06029034f5d.zip,CArN85EXCeae6dg0/1694762615706/a6342cd488ae4cd590512bcd8d6e8e4e.zip,CArN85EXCeae6dg0/1694762624317/3606ebec6f3e486a881ff63ce12e3c1a.zip,CArN85EXCeae6dg0/1694762636316/8920bbd009664f2eb59c820a2ddf3d72.zip,CArN85EXCeae6dg0/1694762644352/bb27a09a8d734b99a7b710fe889f0e86.zip,CArN85EXCeae6dg0/1694762653861/00f75b76e94f4dc5b8f40249b75d01e7.zip,CArN85EXCeae6dg0/1694762662828/bbbffe278c16459b934f5d6f0ddeb98a.zip,CArN85EXCeae6dg0/1694762677625/72ead8539b424f32bb24df99f04a88df.zip,CArN85EXCeae6dg0/1694762686782/79e20bcff68445b784d8bd8599d201af.zip,CArN85EXCeae6dg0/1694762696374/5d7ab3f4110b450baede123975be4948.zip,CArN85EXCeae6dg0/1694762708107/0e6e71ba405647cfaae4c369a5ea2a1f.zip,CArN85EXCeae6dg0/1694762716593/0bf19f7e4f0142669830e60014f5891f.zip"
# 使用逗号分割字符串
split_strings = filedsId.split(',')

# 每个新字符串包含的子字符串数量不超过10个
max_substring_count = 10
output_strings = []

for i in range(0, len(split_strings), max_substring_count):
    substring = ",".join(split_strings[i:i + max_substring_count])
    output_strings.append(substring)
    print(substring)



print(os.getenv('OSS_ACCESS_KEY_ID'))

index = 0


def write_index(index):
    file_path = 'dahanghai_day_index.txt'
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


read_index()
print(index)
print(filter('oaid.20230905.00003'))
index += 1

write_index(index)

secret_key = 'JniWQjitRfQZntCH'
param_map = {}
param_map['customerId'] = 475802
param_map['signId'] = 'b741ef165103518ef3fe23a3aeaea071'


def get_str():
    base_str = ''
    for key,val in param_map.items():
        base_str += key + str(val)
    base_str += secret_key
    print(base_str)
    md5_hash = hashlib.md5()
    md5_hash.update(base_str.encode('utf-8'))
    return md5_hash.hexdigest().lower()


def get_md5(base_str):
    md5_hash = hashlib.md5()
    md5_hash.update(base_str.encode('utf-8'))
    return md5_hash.hexdigest().lower()


# print(get_str())
#
#
# print(get_md5('customerId475802signIdb741ef165103518ef3fe23a3aeaea071JniWQjitRfQZntCH'))
# print(get_md5('customerId475802signIdb741ef165103518ef3fe23a3aeaea071JniWQjitRfQZntCH'))

