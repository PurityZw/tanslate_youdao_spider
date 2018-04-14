# tanslate_youdao_spider
基于python2.7 爬取youdao翻译接口

```
form_data = {
	"i": "你好",     
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "1523671254629",       # 判断为时间戳
	"sign":"b3dfc35348d64fe3dd7c13f8c1323de4",     # 加密后的字符串
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_REALTIME",
	"typoResult": "false"
}
```
#### 查看post请求,通过关键字查找到加密js  
```
salt = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))

s = "fanyideskweb"
n = 查询内容
r = salt
D = "ebSeFb%=XZ%T[KZ)c(sy!"
sign = md5(S + n + r + D)
```


