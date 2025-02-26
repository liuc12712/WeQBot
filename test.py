mods = input('是否启用日志模式(Y/N):')
# 判断选择+调用相关代码
if mods == 'N'and'n':
    print('普通模式')
elif mods == 'Y'and'y':
    print('日志模式')
else:
    print('输入有误(只能输入y,n)')