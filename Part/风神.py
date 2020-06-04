from PublicReference.base import *

class 风神主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '棍棒':
            return round(self.CD / self.恢复 * 1, 1)
        

class 风神技能0(被动技能):
    名称 = '疾风之棍棒精通'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.80 + 0.02 *self.等级 , 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 风神技能1(被动技能):
    名称 = '御风之力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 风神技能2(被动技能):
    名称 = '风神诀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 风神技能3(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 风神技能4(被动技能):
    名称 ='风之意志'
    所在等级= 30
    等级上限 =15
    基础等级 =5
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025+0.015*self.等级, 5)


class 风神技能5(风神主动技能):
    名称 = '狂风冲刺'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    基础 = 603
    成长 = 66
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

class 风神技能6(风神主动技能):
    名称 = '回风斩'
    所在等级= 15
    等级上限 =60
    基础等级 =46
    基础 = 1920
    成长 = 216
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 5

class 风神技能7(风神主动技能):
    名称 = '朔风牵引'
    所在等级= 20
    等级上限 =60
    基础等级 =43
    基础 = 1650
    成长 = 186
    CD = 10
    TP成长 = 0.10
    TP上限 = 5

class 风神技能8(风神主动技能):
    名称 = '风鸣冲击'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    基础 = 3215
    成长 = 364
    CD = 8.5
    TP成长 = 0.10
    TP上限 = 5

class 风神技能9(风神主动技能):
    名称 = '游离之风'
    所在等级 =25
    等级上限 =60
    基础等级 =41
    基础 = 2716
    成长 = 308
    CD = 6.7
    TP成长 = 0.10
    TP上限 = 5


class 风神技能10(风神主动技能):
    名称 = '双翼风刃'
    所在等级= 30
    等级上限 =60
    基础等级 =38
    基础 = 4948
    成长 = 560
    CD = 14
    TP成长 = 0.10
    TP上限 = 5


class 风神技能11(风神主动技能):
    名称 = '风暴之眼'
    所在等级= 35
    等级上限 =60
    基础等级 =36
    基础 = 5270
    成长 = 594
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    def 装备护石(self):
        self.基础 *= 1.28
        self.成长 *= 1.28
        self.CD *= 0.9

class 风神技能12(风神主动技能):
    名称 = '刃风'
    所在等级= 35
    等级上限 =60
    基础等级 =36
    基础 = 7439
    成长 = 843
    CD = 18
    TP成长 = 0.10
    TP上限 = 5

class 风神技能13(风神主动技能):
    名称 = '真空旋风破'
    所在等级= 40
    等级上限 =60
    基础等级 =33
    基础 = 7275
    成长 = 827
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    def 装备护石(self):
        self.基础 *= 1.1
        self.成长 *= 1.1
        self.CD *= 0.8

class 风神技能14(风神主动技能):
    名称 = '风暴之拳'
    所在等级= 45
    等级上限 =60
    基础等级 =31
    基础 = 16553
    成长 = 1863
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    def 装备护石(self):
        self.基础 *= 1.25
        self.成长 *= 1.25

class 风神技能15(风神主动技能):
    名称 = '万象风龙阵'
    所在等级= 50
    等级上限 =60
    基础等级 =12
    基础 = 38776
    成长 = 11760
    CD = 145

class 风神技能16(风神主动技能):
    名称 = '疾风瞬影闪'
    所在等级= 60
    等级上限 =60
    基础等级 =23
    基础 = 14949
    成长 = 1692
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    def 装备护石(self):
        self.基础 *= 1.18
        self.成长 *= 1.18

class 风神技能17(风神主动技能):
    名称 = '风卷残云'
    所在等级= 70
    等级上限 =40
    基础等级 =18
    基础 = 26570
    成长 = 3007
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    def 装备护石(self):
        self.基础 *= 1.22
        self.成长 *= 1.22

class 风神技能18(风神主动技能):
    名称 = '游龙惊风破'
    所在等级= 75
    等级上限 =40
    基础等级 =16
    基础 = 38344
    成长 = 4325
    CD = 40

class 风神技能19(风神主动技能):
    名称 = '九霄风雷'
    所在等级= 80
    等级上限 =40
    基础等级 =13
    基础 = 48994
    成长 = 5521
    CD = 45

class 风神技能20(风神主动技能):
    名称 = '无限风域'
    所在等级= 85
    等级上限 =40
    基础等级 =5
    基础 = 84529
    成长 = 25501
    CD = 180

class 风神技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 风神技能22(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

风神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('风神技能列表.append(风神技能'+str(i)+'())')
        i += 1
    except:
        i = -1

风神技能序号 = dict()
for i in range(len(风神技能列表)):
    风神技能序号[风神技能列表[i].名称] = i

风神一觉序号 = 0
风神二觉序号 = 0
风神三觉序号 = 0
for i in 风神技能列表:
    if i.所在等级 == 50:
        风神一觉序号 = 风神技能序号[i.名称]
    if i.所在等级 == 85:
        风神二觉序号 = 风神技能序号[i.名称]
    if i.所在等级 == 100:
        风神三觉序号 = 风神技能序号[i.名称]

风神护石选项 = ['无']
for i in 风神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        风神护石选项.append(i.名称)

风神符文选项 = ['无']
for i in 风神技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        风神符文选项.append(i.名称)

class 风神角色属性(角色属性):

    职业名称 = '风神'

    武器选项 = ['棍棒']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.11
   
    #基础属性(含唤醒)
    基础力量 = 944.0
    基础智力 = 806.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= copy.deepcopy(风神技能列表)
        self.技能序号= copy.deepcopy(风神技能序号)

class 风神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 风神角色属性()
        self.角色属性A = 风神角色属性()
        self.角色属性B = 风神角色属性()
        self.一觉序号 = 风神一觉序号
        self.二觉序号 = 风神二觉序号
        self.三觉序号 = 风神三觉序号
        self.护石选项 = copy.deepcopy(风神护石选项)
        self.符文选项 = copy.deepcopy(风神符文选项)

    def 输出界面(self, index):
        self.行高 = 27
        super().输出界面(index)
