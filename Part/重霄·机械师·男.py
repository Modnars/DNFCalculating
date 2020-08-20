from PublicReference.base import *

class 重霄·机械师·男技能0(被动技能):
    名称 = '方舟反应堆'
    所在等级=25
    等级上限=20
    基础等级=10
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级,3)

class 重霄·机械师·男技能1(主动技能):
    名称 = 'G1科罗纳'
    所在等级=20
    等级上限=60
    基础等级=43  
    基础=245.75/0.50
    成长=16.52/0.50
    CD=1.0
    TP成长=0.10
    TP上限 = 5
   
    def 等效CD(self, 武器类型):
        return round(1.0,1)
    
    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.59+0.01*self.等级,3)
    
class 重霄·机械师·男技能2(主动技能):
    名称='G2旋雷者'
    所在等级=25
    等级上限=60
    基础等级=41  
    基础=800
    成长=100
    CD=6.0
    TP成长=0.10
    TP上限 = 5
    
    def 等效CD(self, 武器类型):
        return round(6.0,1)

    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.50+0.01*self.等级,3)

class 重霄·机械师·男技能3(主动技能):
    名称='毒蛇炮'
    所在等级=25
    等级上限=60
    基础等级=41  
    基础=2910
    成长=330
    CD=2.975
    TP成长=0.10
    TP上限 = 5
    演出时间 =4

class 重霄·机械师·男技能4(被动技能):
    名称='机械概论'
    所在等级=15
    等级上限=11
    基础等级=1
    关联技能=['RX78追击者','Ez8自爆者','RX60陷阱追击者','毒蛇炮', '护石风暴', '空战机械：风暴', '空投支援', '拦截机工厂', '光反应能量模块', '盖波加之拳', 'EZ10反击者', 'EXSZero毒蛇炮', 'TN80终结者', 'TX-45特工队', '超时空行军','HS1全息机械猎手','GW16-瓦尔德斯坦']
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.085+0.015*self.等级,3)

class 重霄·机械师·男技能5(主动技能):
    名称='RX78追击者'
    所在等级=5
    等级上限=60
    基础等级=50
    基础=1056.62
    成长=119.38
    CD=2.125
    TP成长=0.08
    TP上限 = 5
    演出时间 =4

class 重霄·机械师·男技能6(主动技能):
    名称='Ez8自爆者'
    所在等级=15
    等级上限=60
    基础等级=46 
    基础=1881.68
    成长=212.5
    CD=5.525
    TP成长=0.10
    TP上限 = 5
    演出时间 =4

class 重霄·机械师·男技能7(主动技能):
    名称='G3捕食者'
    所在等级=30
    等级上限=60
    基础等级=38
    基础=416.54
    成长=47.45    
    CD=1
    TP成长=0.10
    TP上限 = 5
    
    def 等效CD(self, 武器类型):
        return round(1.0,1)

    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.48+0.01*self.等级,3)

class 重霄·机械师·男技能8(主动技能):
    名称='RX60陷阱追击者'
    所在等级=30
    等级上限=60
    基础等级=38  
    基础=4320.16
    成长=487.81
    CD=10.2
    TP成长=0.10
    TP上限 = 5
    演出时间 =1
   
class 重霄·机械师·男技能9(主动技能):
    名称='护石风暴'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=17488.8
    成长=1978.2
    CD=25.5
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =1.5
   
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1
        elif x == 1:
            self.倍率 *= 1.0672  


class 重霄·机械师·男技能10(主动技能):
    名称='空战机械：风暴'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=1729.09/3
    成长=220.91/3
    CD=1.0
    TP成长=0.10
    TP上限 = 5

    def 等效CD(self, 武器类型):
        return round(1.0,1)

class 重霄·机械师·男技能11(主动技能):
    名称='空投支援'
    所在等级=40
    等级上限=60
    基础等级=33  
    基础=14091.74
    成长=1430.35
    CD=29.75
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.21
        elif x == 1:
            self.倍率 *= 1.30  

class 重霄·机械师·男技能12(主动技能):
    名称='拦截机工厂'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础=19110.96
    成长=2158.29
    CD=38.25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27  

class 重霄·机械师·男技能13(主动技能):
    名称='光反应能量模块'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础=21016.24
    成长=2373.05
    CD=38.25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27  

class 重霄·机械师·男技能14(被动技能):
    名称='斗志之歌'
    所在等级=48
    等级上限=40
    基础等级=20
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        if self.等级<17:
            return round(1.01+0.015*self.等级,3)
        else:
            return round(1.25+0.02*(self.等级-16),3)

class 重霄·机械师·男技能15(主动技能):
    名称='盖波加之拳'
    所在等级=50
    等级上限=40
    基础等级=12  
    基础=51094.05
    成长=15440.25
    CD=145.0

class 重霄·机械师·男技能16(主动技能):
    名称='EZ10反击者'
    所在等级=60
    等级上限=40
    基础等级=23  
    基础=13761.42
    成长=1554.16
    CD=25.5
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =0.5

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.334

class 重霄·机械师·男技能17(主动技能):
    名称='EXSZero毒蛇炮'
    所在等级=70
    等级上限=40
    基础等级=18  
    基础=40096.07
    成长=4526.3
    CD=42.5
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 =2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.273

class 重霄·机械师·男技能18(被动技能):
    名称='HS1机械助手'
    所在等级=75
    等级上限=40
    基础等级=11
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级,3)


class 重霄·机械师·男技能19(主动技能):
    名称='TN80终结者'
    所在等级=75
    等级上限=40
    基础等级=16
    基础=54607.2
    成长=6165.5
    CD=34
    演出时间 =2
    是否有护石 = 1
    演出时间 =2
    
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.352

class 重霄·机械师·男技能20(主动技能):
    名称='TX-45特工队'
    所在等级=80
    等级上限=40
    基础等级=13  
    基础=35274.11
    成长=3982.4
    CD=38.25
    演出时间 =0.5
    是否有护石 = 1
    
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率*=1.29

class 重霄·机械师·男技能21(主动技能):
    名称='超时空行军'
    所在等级=85
    等级上限=40
    基础等级=5  
    基础=111387.67
    成长=35066.68
    CD=180

class 重霄·机械师·男技能22(被动技能):
    名称 = 'SOPHIA'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 重霄·机械师·男技能23(主动技能):
    名称 = 'HS1全息机械猎手'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    基础=111647.6
    成长=12605.4
    CD=51
    演出时间 =1.5

class 重霄·机械师·男技能24(主动技能):
    名称 = 'GW16-瓦尔德斯坦'
    所在等级=100
    等级上限=40
    基础等级=2  
    基础=346641
    成长=104659
    CD=290

    def 加成倍率(self,武器类型):
         return 0.0

class 重霄·机械师·男技能25(被动技能):
    名称 = '机械引爆'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 5
    是否主动 = 1
    关联技能=['RX78追击者','Ez8自爆者','RX60陷阱追击者','空投支援', '拦截机工厂',   'EZ10反击者', 'TX-45特工队']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.40


重霄·机械师·男技能列表 = []
i = 0
while i >= 0:
    try:
        exec('重霄·机械师·男技能列表.append(重霄·机械师·男技能'+str(i)+'())')
        i += 1
    except:
        i = -1

重霄·机械师·男技能序号 = dict()
for i in range(len(重霄·机械师·男技能列表)):
    重霄·机械师·男技能序号[重霄·机械师·男技能列表[i].名称] = i

重霄·机械师·男一觉序号 = 0
重霄·机械师·男二觉序号 = 0
重霄·机械师·男三觉序号 = 0
for i in 重霄·机械师·男技能列表:
    if i.所在等级 == 50:
        重霄·机械师·男一觉序号 = 重霄·机械师·男技能序号[i.名称]
    if i.所在等级 == 85:
        重霄·机械师·男二觉序号 = 重霄·机械师·男技能序号[i.名称]
    if i.所在等级 == 100:
        重霄·机械师·男三觉序号 = 重霄·机械师·男技能序号[i.名称]

重霄·机械师·男护石选项 = ['无']
for i in 重霄·机械师·男技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        重霄·机械师·男护石选项.append(i.名称)

重霄·机械师·男符文选项 = ['无']
for i in 重霄·机械师·男技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        重霄·机械师·男符文选项.append(i.名称)

class 重霄·机械师·男角色属性(角色属性):

    实际名称 = '重霄·机械师·男'
    角色 = '神枪手(男)'
    职业 = '机械师'

    武器选项 = ['自动手枪']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.850
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(重霄·机械师·男技能列表)
        self.技能序号= deepcopy(重霄·机械师·男技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['G1科罗纳']].被动倍率 *= 1+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G2旋雷者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G3捕食者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']].G系加成倍率()+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()

class 重霄·机械师·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 重霄·机械师·男角色属性()
        self.角色属性A = 重霄·机械师·男角色属性()
        self.角色属性B = 重霄·机械师·男角色属性()
        self.一觉序号 = 重霄·机械师·男一觉序号
        self.二觉序号 = 重霄·机械师·男二觉序号
        self.三觉序号 = 重霄·机械师·男三觉序号
        self.护石选项 = deepcopy(重霄·机械师·男护石选项)
        self.符文选项 = deepcopy(重霄·机械师·男符文选项)