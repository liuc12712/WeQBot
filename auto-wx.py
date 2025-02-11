# 本代码由wxauto官方提供的实力代码与api调用结合优化而来
# 算不上很精巧的代码设计，望大佬改进优化

from wxauto import WeChat
import time
import requests


wx = WeChat()


listen_list = [
    '小号' # 改成你希望监听的目标，可以多个
]
# 添加监听对象
for i in listen_list:
    wx.AddListenChat(who=i, savepic=True)

# 持续监听消息，并且收到消息后回复“收到”
wait = 1  # 设置1秒查看一次是否有新消息
while True:
    msgs = wx.GetListenMessage()
    for chat in msgs:
        who = chat.who  # 获取聊天窗口名（人或群名）
        one_msgs = msgs.get(chat)  # 获取消息内容
        # 回复收到
        for msg in one_msgs:
            msgtype = msg.type  # 获取消息类型
            content = msg.content  # 获取消息内容，字符串类型的消息内容
            a = content
            url = "http://127.0.0.1:5000/process"
            payload = {"a": a}

            response = requests.post(url, json=payload) #调用本地api接口

            # 检查响应
            if response.status_code == 200:
                # 提取返回结果
                b = response.json().get("b")
            else:
                print("Error:", response.json())

            if msgtype == 'friend':
                print(f'【{who}】：{b}')
                chat.SendMsg(b)  # 回复收到
    time.sleep(wait)