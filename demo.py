# -*- coding：utf-8 -*-
'''
时间：2017-11-25
作者：小丸子
标题：第一天的演示文件
'''
'''
print ("hello world!")
hstr = "我是字符串" # 字符串
hnum = 123 # 数字
hlist = [1, 2, 3, "四", "五"] # 数组
hdict = {"a": "啊", "b": "波"} # 字典
hfloat = 3.1415 # 浮点
hnull = None # 空，不存在的
print(type(hstr))
'''
'''
print("------------------------")
print("|                      |")
print("|-----欢迎登陆xx系统----|")
print("|                      |")
print("------------------------")
username = input("请输入账号：")
if username == "TomBigOld":
    password = input("请输入密码：")
    if password =="123456":
        print("登陆成功！！！")
    else:
        print("密码错误！！")
else:
    print("对不起，账号不存在！")
'''

for i in range(4):
    if i !=3:
        print("------------------------")
        print("|                      |")
        print("|-----欢迎登陆xx系统----|")
        print("|                      |")
        print("------------------------")
        username = input("请输入账号：")
        if username == "TomBigOld":
            password = input("请输入密码：")
            if password == "123456":
                print("登陆成功！！")
                print("欢迎你, %s" % username)
                break
            else:
                print("密码错误，请重新登陆")
        else:
            print("对不起，账号不存在！")
    else:
        print("错误次数太多，等待五分钟！")
        exit()
user = {"name": username, "age": "23岁", "high": "170cm", "job": "测试工程师", "sex": "女"}
for key in user:
    print(key, ":\t", user[key])       