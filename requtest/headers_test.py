import requests, json
# 请求地址
urlstr = 'https://wanandroid.com/user/login'
datas = {'username':'DHB123', 'password':'150740'}
# 请求header头，浏览器或客户端
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# 发送请求
r = requests.post(url=urlstr, data=datas, headers=header)
# r.headers是响应头
print(r.headers)
# 输出响应结果--状态码
print(r.status_code)
# 输出响应结果--编码
print(r.encoding)
# 输出响应结果--文本
print(r.text)