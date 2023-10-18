auth zhanghao

下游项目
    todo rta java 项目定时任务依赖这些脚本
项目结构
    cos_client.py 腾讯云连接相关
    oss_client.py 阿里云连接相关
    upload_task.py 上传和下载的逻辑，启动脚本
启动方式
    python upload_task.py argv1
    可以接受一个参数，当第一个参数存在的时候，date_str 会 = argv[1], 使用方法是日期，这样的化，会将
    OSS 目标路径下筛选出包含改日期的文件
    如果没有参数，则不会筛选，所以会拉取所有的文件

待优化项：
    1. 本地文件存在时，不下载
    2. cos 目标存在时，不上传