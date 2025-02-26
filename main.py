from wx_auto import listening_reply,listening_reply_log
# 模式选择
while True:
    mods = input('是否启用日志模式(Y/N):')
    # 判断选择+调用相关代码
    if mods == 'N' or mods == 'n':
        monitor = input('请输入要回复的目标:')
        listening_reply(monitor)
    elif mods == 'Y' or mods == 'y':
        monitor_log = input('请输入要回复的目标:')
        listening_reply_log(monitor_log)
    else:
        print('\033[1;31m**输入有误(只能输入y,n)请重新输入**\033[0m')
        input('按任意键返回...')