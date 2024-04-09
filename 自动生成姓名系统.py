# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:36:41 2024

@author: Administrator
"""
import random
nameList = []
nmlst1 = "赵谦孙李周武郑王冯陈楚卫姜沈杭杨"
nmlst2 = "别后竹窗风雪夜一灯明暗覆吴图"
nmlst3 = "问渠那得清如许为有源头活水来"
#随机生成名字
name = random.choice(nmlst1) + random.choice(nmlst2) + random.choice(nmlst3)
nameList.append(name)
#随机生成年龄
yearList = []
year = random.randint(15,35)
yearList.append(year)
#随机生成家世
backList = []
blst1 = ("罪臣之后","一品官员之后","天潢贵胄","非人非鬼，非神非魔")
back = random.choice(blst1)
backList.append(back)
#输出
if input("请输入你的需求:"):
    print(nameList)
    print(yearList)
    print(backList)
else:
    print("无法识别，请重新输入您的需求")