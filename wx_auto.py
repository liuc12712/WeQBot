from qwen_bot import qwen2_5
from wxauto import WeChat
import time


wx = WeChat()
# 普通用法
def listening_reply (monitor):
    listen_list = [
        monitor
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

                if msgtype == 'friend':
                    print(f'【{who}】：{content}')
                    response = qwen2_5(content)
                    chat.SendMsg(response[0])  # 回复消息
        time.sleep(wait)

def log_write(s1,s2,s3):
    # (1)打开(创建文件)文件
    file=open('log.txt','a',encoding='utf-8')
    # (2)写入内容
    file.write(f"用户:{s1}\n回答:{s2}\n用时:{s3:.2f}秒\n")
    file.write('\n')
    # (3)关闭
    file.close()

# 日志模式
def listening_reply_log (monitor):
    listen_list = [
        monitor
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

                if msgtype == 'friend':
                    print(f'【{who}】：{content}')
                    response = qwen2_5(content)
                    log_write(content, response[0], response[1])
                    chat.SendMsg(response[0])  # 回复消息

        time.sleep(wait)
