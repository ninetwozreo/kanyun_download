# kanyun_download
用于下载看云指定地址文档的爬虫
下载后修改目标url 和cookie （如果你购买了某个文档，需要登录后获取cookie才能下载完整的文档）

#目标url

turl = "https://www.kancloud.cn/zlt2000/microservices-platform/919412";

#设置请求头， cookie登陆后可换

form_header = {"cookie": ""}

运行 python info.py 即可

目标文档会被下载到、tdir中
