import requests, json
# # 请求地址
# urlstr = 'http://httpbin.org/post'
# # 字典类型参数
# payload = {'cont':'selenium+jmeter+loadrunner', 'qq':'106014970'}
# # 接口文档要求传入--json类型需要进行转换
# # #方法1：dumps方法
# # # 通过json.dumps方法将python字符串转换成json类型
# payload = json.dumps(payload)
# # 发送请求
# r = requests.post(url=urlstr, data=payload)
# # 输出响应结果--状态码
# print(r.status_code)
# # 输出响应数据-- 当前响应编码
# print(r.encoding)
# # 输出响应数据--文本
# print(r.text)
# # 返回为json类型，可以通过r.json的方法查看结果
# print(r.json())


#  ------------------------------------------------------------------------------

# 请求地址
urlstr = 'http://httpbin.org/post'
# 字典类型参数
payload = {'cont':'selenium+jmeter+loadrunner', 'qq':'106014970'}
# 接口文档要求传入--json类型需要进行转换
# # 通过json.dumps方法将python字符串转换成json类型
# payload = json.dumps(payload)
# # 方法2:
# 发送请求
r = requests.post(url=urlstr, json=payload)
# 输出响应结果--状态码
print(r.status_code)
# 输出响应数据-- 当前响应编码
print(r.encoding)
# 输出响应数据--文本
print(r.text)
# 返回为json类型，可以通过r.json的方法查看结果
print(r.json())
