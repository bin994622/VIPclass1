"""

快递
"""
import requests
# 请求地址
urlstr = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-UUCAO1614829806052.html'
# get方法其他价格user-Ayent
hearders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# session初始化
s = requests.session()
# 发送请求
r = s.get(url=urlstr, headers=hearders, verify=False)
# 将json转换成字典类型
result = r.json()
# 请求参数--获取data中的内容、
data = result['data']
print(data)
# 获取data中第一个状态--以内是列表所以按照下表查询
print(data[0])
# 获取context的内容
new_data = data[0]['context']
print(new_data)
