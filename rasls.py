"""
程序目标:RPSLS游戏
程序作者:张文聪
"""
import random
def name_to_number(name):  #将游戏对象对应到不同的整数
    if name=="石头" :
        name=0
    if name=="史波克" :
        name=1
    if name=="纸" :
        name=2
    if name=="蜥蜴" :
        name=3
    if name=="剪刀" :
        name=4
    return name
def number_to_name(number):    #将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    if number==0 :
        number="石头"
    if number==1 :
        number="史波克"
    if number==2 :
        number="纸"
    if number==3 :
        number="蜥蜴"
    if number==4 :
        number="剪刀"
    return number
def rpsls(player_choice):
    computer=random.randint(0,5)
    player_choice=choice_name
    player=name_to_number(player_choice)
    while player == name_to_number("石头"):
        print("您的选择为" + number_to_name(0))
        print("计算机的选择为"+number_to_name(computer))
        if computer == 3 or computer == 4:
            print("您赢了!")
        if player==computer:
            print("您和计算机出的一样")
        if computer==1 or computer==2:
            print("机器赢了")
        break
    while player==name_to_number("史波克"):
        print("您的选择为" + number_to_name(1))
        print("计算机的选择为" + number_to_name(computer))
        if computer==4 or computer==0:
           print("您赢了!")
        if player==computer:
           print("您和计算机出的一样")
        if computer==2 or computer== 3:
           print("机器赢了")
        break
    while player==name_to_number("纸") :
        print("您的选择为" + number_to_name(2))
        print("计算机的选择为" + number_to_name(computer))
        if computer==1 or computer==0 :
            print("您赢了!")
        if player==computer:
            print("您和计算机出的一样")
        if computer==3 or computer==4 :
            print("机器赢了")
        break
    while player==name_to_number("蜥蜴") :
        print("您的选择为" + number_to_name(3))
        print("计算机的选择为" + number_to_name(computer))
        if computer==1 or computer==2 :
            print("您赢了!")
        if player==computer :
            print("您和计算机出的一样")
        if computer==0 or computer==4 :
            print("计算机赢了")
        break
    while player==name_to_number('剪刀') :
        print("您的选择为" + number_to_name(4))
        print("计算机的选择为" + number_to_name(computer))
        if computer==2 or computer==3 :
            print("您赢了!")
        if player==computer :
            print("您和计算机出的一样")
        if computer==0 or computer==1 :
            print("计算机赢了")
        break
    return player
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name != "石头" and choice_name !="剪刀" and choice_name !="纸" and choice_name !="蜥蜴" and choice_name !="史波克":
    print('Error: No Correct Name')
result=rpsls(choice_name)

