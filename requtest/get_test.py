import requests
# # 请求地址--不带参数
# urlstr = 'https://wanandroid.com/'
#
# # 发送请求
# r = requests.get(url=urlstr)
# # 输出响应结果--状态码
# print(r.status_code)
# # 输出响应结果--文本
# print(r.text)
# # 输出响应结果--打印当前编码
# print(r.encoding)

# -------------------------------------------------------------------------------------

# # 请求地址——带参数
# urlstr = 'https://wanandroid.com/article/query?k=android'
# # 参数
# param = {'k':'android'}
# # 发送请求
# r = requests.get(url=urlstr, params=param)
# # 输出响应结果--状态码
# print(r.status_code)
# # 输出响应结果--文本
# print(r.text)


# ====================================================================================


# # 百度首页
# 请求地址
urlstr = 'https://www.baidu.com/'
# 发送请求
r = requests.get(url=urlstr)
# 输出响应结果——状态码
print(r.status_code)
# 输出响应结果——文本
print(r.text)
# 输出响应结果--打印当前编码
print(r.encoding)
# 输出响应结果--编码为UTF8
print(r.apparent_encoding)
# 将编码为UTF8赋值给当前编码
r.encoding = r.apparent_encoding
# 输出响应结果--文本为编码UTF-8
print(r.text)

