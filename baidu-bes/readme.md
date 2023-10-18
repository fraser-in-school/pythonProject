re_start 使用方法：
#1 依赖项
a. ./cos.conf 写好 cos 的配置
b. ./app.conf 写好相应的 app 的配置
c. app 的启动脚本 ./start.sh



#2 使用方法
first：
编辑 ./app.conf
例如：
app_name="ad-engine-service"
app_port="8074"
second:
将打好的包上传到 hadoop-1319813010/zhanghao_tmp/package/$app_name/ 文件夹中
third：
执行 restart.sh $version
例如：restart.sh 0.0.12-SNAPSHOT