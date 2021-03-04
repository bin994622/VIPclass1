import requests
# # # 查看requests模块的详细内容使用help
# # help(requests)
# # 请求地址
# urlstr = 'https://wanandroid.com/user/login'
# datas = {'username':'DHB123', 'password':'150740'}
# # 发送请求
# r = requests.post(url=urlstr,data=datas)
# # 输出响应结果--状态码
# print(r.status_code)
# # 输出响应结果——文本
# print(r.text)


# ---------------------------------------------------------------------------------------------------------------------------

# # @@@ 判断登录
# 请求地址
urlstr = 'https://wanandroid.com/user/login'
# 请求的参数
datas = {'username':'DHB123', 'password':'150740'}
# 发送请求
r = requests.post(url=urlstr,data=datas)
# 输出响应结果--状态码
print(r.status_code)
# 输出响应结果——文本!!!!r.text输出为字符串
print(r.text)
# 输出响应结果--返回json类型查看结果
print(r.json())
# 输出响应结果---响应结果为res_result(名字随便取)
res_result = r.json()  # 将json类型转换为字典[dict]类型
print(type(res_result))
# 输出响应结果--用r.json取出想要的value值，那么就要先知道对应的key值是什么，使用的是['']
print(res_result['errorCode'])
# 输出响应结果--用r.json取出想要的value值，那么就要先知道对应的key值是什么，使用的是['']，如果属于嵌套就用逐步取key的方法获取想要的结果
print(res_result['data']['username'])
# 输出响应结果--响应断言
# # 判断errorCode和username是否成立
errorCode = res_result['errorCode']
username = res_result['data']['username']
if errorCode == 0 and username == datas['username']:
    print('登录成功')



