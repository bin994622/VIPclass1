import requests, json
"""
由Python类型转换成json类型

"""
payload = {
    'yoyo':True,
    'json':False,
    'python':'7611'
}
print(payload)
print(type(payload))
# 转换类型--转换成json格式（首字母由大写转换成小写,数据类型由字典[dict]转换成字符串[str]）
new_payload = json.dumps(payload)
print(new_payload)
print(type(new_payload))



"""

由json类型转换成python类型
   参考post_test文件 
"""

