import requests
"""
注意:
    如果想访问一个接口，必须是在登陆后才可以访问，先登录必须要携带登录的状态进行访问
    采用session的方式访问--requests.session()相当于session对象s
"""
# 请求地址
# # 登录请求地址
urlstr1 = 'https://wanandroid.com/user/login'
urlstr = 'https://wanandroid.com/lg/todo/list/0'
# #  登录的参数
datas =  {'username':'DHB123', 'password':'150740'}
# 访问登陆后的接口。用session方式访问，session会自动显示登陆后的状态
s = requests.session()
# # 登录的请求--先session对象先发post进行登录
r = s.post(url=urlstr1, data=datas)
# 发送请求
# # 再用session对象获取get请求数据
r2 = s.get(url=urlstr)
# 输出响应结果--状态码
print(r2.status_code)
# 输出响应结果--文本
print(r2.text)
# 输出响应结果--编码
print(r2.encoding)