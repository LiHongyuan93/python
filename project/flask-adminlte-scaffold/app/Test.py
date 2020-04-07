# temp = input("开始玩游戏了，猜一下想的数字:")
# guess = int(temp)
# if guess ==8 :
#     print("你怎么知道我心里是8")
# else:
#     print("猜错了吧 哈哈哈哈哈")
#
# print("好了，我不玩了哈")

#1.输入一个数字
#2.如果输入的不是数字，提示请输入数字。如果数字不在1-999范围内，提示需输入1-999的数字。
#3.如果数字是7的倍数（可选：包含7），打印"过"，否则打印这个数字

#temp = input("请输入一个数字:")

def check7(num):
    if isinstance(num,int)==False:
        print(str(num)+"不是一个数字,请重新运行输入")
    else:
        guess = int(num)
        if guess<1 or guess>999:
            print("请重新运行输入1-999的数字")
        else:
            if guess%7==0:
                print(str(num)+":是7的倍数")
            else:
                first=guess//100    #百位
                second=guess//10    #十位
                if guess>=100:
                    second=guess%100//10
                third=guess%10      #个位

                if first==7 or second==7 or third==7:
                    print(str(num)+":含7数字")
                else:
                    print(str(num)+":不含7也不是7的倍数")

for num in (1,6,7,17,21,22,71,701,671,687):
    check7(num)