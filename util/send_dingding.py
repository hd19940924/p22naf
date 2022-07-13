import requests
class sendDing():
# webhook地址
   global url1
   global url
   #global data
   url = "https://oapi.dingtalk.com/robot/send?access_token=111111111111111111111111111111"
   url1 = "https://oapi.dingtalk.com/robot/send?access_token=1111111111111111111111111111111111"
# 发送的消息
   """data = { "msgtype": "text", "text":
     {  "content": "接口测试结果："+f'\n总共运行500条用例'
               + f'\n成功451条用例'
               + f'\n失败49条用例'
               +f'\n有瓜吃吗？'
+f'\n有瓜吃吗？大佬'
+f'\n有瓜吃吗？大佬们'
+f'\n有瓜吃吗？大佬们'
    },
"at": { "atMobiles": [], "isAtAll": True } }"""
#发送请求获取结果
   #res = requests.post(url=url1, json=data)
   #print(res.text)
   def send_ding(self,data):
          #res=requests.post(url1,data)
          res = requests.post(url=url, json=data)
          print("已发送")
          #return res
         # print(res.text)
   def Send_Ding(self,pass_list,fail_list):
         pass_num = float(len(pass_list))
         fail_num = float(len(fail_list))
         count_num = pass_num + fail_num
         pass_result = "%.2f%%" % (pass_num / count_num * 100)
         fail_result = "%.2f%%" % (fail_num / count_num * 100)
         #data1 = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
         data = {"msgtype": "text", "text":
             {"content": "接口测试结果：" + f'\n总共运行{count_num}条用例'
                         + f'\n成功{pass_num}条用例'
                         + f'\n失败{fail_num}条用例'
              },
                 "at": {"atMobiles": [], "isAtAll": True}}
         self.send_ding(data)

if __name__ == '__main__':
    sd=sendDing()
    sd.Send_Ding([1,2,3,4],[2,3,4,5,6,7])

