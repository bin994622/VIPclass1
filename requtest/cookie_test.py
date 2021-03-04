"""
携带cookie发送请求

"""
import requests
# # # 方法一:
# # 请求地址--登录地址
# urlstr = 'https://wanandroid.com/user/login'
# # 添加登录参数
# datas = {'username':'DHB123', 'password':'150740'}
# # 发送post请求
# r = requests.post(url=urlstr, data=datas)
# # 输出响应结果-文本
# print(r.text)
# # 输出响应结果--携带cookie信息【r.cookies】为固定写法
# print(r.cookies)
# # 输出响应结果--headers头信息
# print(r.headers)
#
# # 获取上次请求中response中的cookie信息，传递个下次的请求
# cookie = r.cookies
# # 携带cookie发送请求
# new_r = requests.get(url='https://wanandroid.com/lg/todo/list/0', cookies=cookie)
# # 输出响应结果--文本
# print(new_r.text)
# # 输出响应结果--状态码
# print(new_r.status_code)

# ----------------------------------------------------------------------------------------------
# 方法二【通过requests.session】方法自动设置cookie访问
# # 请求登录地址
urlstr = 'https://wanandroid.com/user/login'
# # 添加登录参数
datas = {'username':'DHB123', 'password':'150740'}
# # 初始化session对象
s = requests.session()
# # 发送登录请求数据
r = s.post(url=urlstr, data=datas)
# # 输出响应结果--文本
print(r.text)
# # 输出响应数据--状态码
print(r.status_code)
# # 通过session继续发送post请求，自动携带上一个请求返回的cookie信息
r2 = s.get('https://wanandroid.com/lg/todo/list/0')
# # 输出响应结果--文本
print(r2.text)
# # 输出响应数据--状态码
print(r2.status_code)





