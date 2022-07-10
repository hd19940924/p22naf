import requests
# webhook地址
url = "https://oapi.dingtalk.com/robot/send?access_token=845da39d4e781518fde554d06301182793fafbccd65ab19506a31a0c98a31ba5"
url1 = "https://oapi.dingtalk.com/robot/send?access_token=214f1e49711ae0f5450db8a6dd7205feb74a8e4b0fac47ab03453857b8bd809a"
# 发送的消息
data = { "msgtype": "text", "text":
    {  "content": "接口测试结果："+f'\n总共运行500条用例'
               + f'\n成功451条用例'
               + f'\n失败49条用例'
               +f'\n有瓜吃吗？'
+f'\n有瓜吃吗？志恒'
+f'\n有瓜吃吗？大佬们'
+f'\n有瓜吃吗？大佬们'
    },
"at": { "atMobiles": [], "isAtAll": True } }
#发送请求获取结果
res = requests.post(url=url1, json=data)
print(res.text)

