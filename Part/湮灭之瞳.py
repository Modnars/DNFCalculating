﻿from PublicReference.base import *
class 湮灭之瞳主动技能(技能):
    #只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    #如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    #固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    # Will添加
    CD倍率 = 1.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    元素之力蓄力数量 = 0
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    是否有护石 = 0
    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    关联技能4 = ['无']
    # Will添加
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']


    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)
    def 等效CD(self, 武器类型):
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.0, 1)
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)
class 湮灭之瞳被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    元素之力蓄力数量 = 0
    关联技能 = ['所有']
    # Will添加
    关联技能2 = ['无']
    关联技能3 = ['无']
    关联技能4 = ['无']

    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']

class 湮灭之瞳技能0(湮灭之瞳被动技能):
    名称 = '元素循环'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class 湮灭之瞳技能1(湮灭之瞳被动技能):
    名称 = '元素之力'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['无']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.055+0.014*self.等级,2)


class 湮灭之瞳技能2(湮灭之瞳主动技能):
    名称 = '元素环绕'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (6 + self.等级 * 3)


class 湮灭之瞳技能3(湮灭之瞳被动技能):
    名称 = '元素融合'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
            return 1.0

    def 属强加成(self):
        if self.等级 == 0:
            return 0
        else:
            return (37 + self.等级 * 3)


class 湮灭之瞳技能4(湮灭之瞳被动技能):
    名称 = '元素爆发'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.255 + 0.020 * (self.等级 - 16), 5)


class 湮灭之瞳技能5(湮灭之瞳被动技能):
    名称 = '黑瞳'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class 湮灭之瞳技能6(湮灭之瞳被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 湮灭之瞳技能7(湮灭之瞳被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 湮灭之瞳技能8(湮灭之瞳被动技能):
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


class 湮灭之瞳技能9(湮灭之瞳主动技能):
    名称 = '元素炮'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    基础 = 490
    成长 = 10
    CD = 4.0



class 湮灭之瞳技能10(湮灭之瞳主动技能):
    名称 = '属性变换'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 19
    是否有伤害 = 1
    是否主动 = 1
    基础 = 195
    成长 = 58.7
    TP成长 = 0.08
    TP上限 = 7
    关联技能 = ['元素炮','魔球连射']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round((1.95 + 0.587 * self.等级 )* (1+0.08 * self.TP等级), 5)

class 湮灭之瞳技能11(湮灭之瞳主动技能):
    名称 = '魔球连射'
    所在等级 = 5
    等级上限 = 11
    基础等级 = 1
    基础 = 108
    成长 = 2
    攻击次数 = 5
    CD = 2.4

class 湮灭之瞳技能12(湮灭之瞳主动技能):
    名称 = '幻魔四重奏'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 42510
    成长 = 12850
    CD = 145.0

class 湮灭之瞳技能13(湮灭之瞳主动技能):
    名称 = '末日湮灭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 95595.6
    成长 = 28856.4
    CD = 180.0

class 湮灭之瞳技能14(湮灭之瞳主动技能):
    名称 = '地炎'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1753.702
    成长 = 198.297
    CD = 4.0
    TP成长 = 0.04
    TP上限 = 7

class 湮灭之瞳技能15(湮灭之瞳主动技能):
    名称 = '冰晶坠'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2956.143
    成长 = 333.857
    CD = 6.4
    TP成长 = 0.10
    TP上限 = 7

class 湮灭之瞳技能16(湮灭之瞳主动技能):
    名称 = '雷光链'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 3723.636
    成长 = 420.364
    CD = 9.6
    TP成长 = 0.20
    TP上限 = 7

class 湮灭之瞳技能17(湮灭之瞳主动技能):
    名称 = '暗域扩张'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 5289.705
    成长 = 597.295
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 7


class 湮灭之瞳技能18(湮灭之瞳主动技能):
    名称 = '冰晶之浴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5459.317
    成长 = 616.683
    CD = 12.0
    TP成长 = 0.0
    TP上限 = 1
    def 等效CD(self, 武器类型):
        if self.TP等级 == 0:
            if 武器类型 == '魔杖':
                return round (self.CD * 0.8,2)
            if 武器类型 == '法杖':
                return round (self.CD * 0.8  * 1.1 ,2)
        else:
            if 武器类型 == '魔杖':
                return round (self.CD *0.75 *0.8 ,2)
            if 武器类型 == '法杖':
                return round (self.CD *0.75 *0.8 * 1.1 ,2)


class 湮灭之瞳技能19(湮灭之瞳主动技能):
    名称 = '旋炎破'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6199.512
    成长 = 700.488
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.22


class 湮灭之瞳技能20(湮灭之瞳主动技能):
    名称 = '雷光屏障'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6881.948
    成长 = 777.052
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23

class 湮灭之瞳技能21(湮灭之瞳主动技能):
    名称 = '黑暗禁域'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6500.105
    成长 = 733.895
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 7

class 湮灭之瞳技能22(湮灭之瞳主动技能):
    名称 = '元素轰炸'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 16196.139
    成长 = 1833.861
    CD = 32
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23

class 湮灭之瞳技能23(湮灭之瞳主动技能):
    名称 = '元素浓缩球'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14117.087
    成长 = 1593.913
    CD = 24
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.26


class 湮灭之瞳技能24(湮灭之瞳主动技能):
    名称 = '元素幻灭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 22054.889
    成长 = 2490.111
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.23

class 湮灭之瞳技能25(湮灭之瞳主动技能):
    名称 = '元素禁域'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 36737.1875
    成长 = 4147.8125
    CD = 32.0

class 湮灭之瞳技能26(湮灭之瞳主动技能):
    名称 = '聚能魔炮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 45659.769
    成长 = 5155.231
    CD = 36.0

    
湮灭之瞳技能列表 = []
i = 0
while i >= 0:
    try:
        exec('湮灭之瞳技能列表.append(湮灭之瞳技能' + str(i) + '())')
        i += 1
    except:
        i = -1

湮灭之瞳技能序号 = dict()
for i in range(len(湮灭之瞳技能列表)):
    湮灭之瞳技能序号[湮灭之瞳技能列表[i].名称] = i

湮灭之瞳一觉序号 = 0
湮灭之瞳二觉序号 = 0
湮灭之瞳三觉序号 = 0
for i in 湮灭之瞳技能列表:
    if i.所在等级 == 50:
        湮灭之瞳一觉序号 = 湮灭之瞳技能序号[i.名称]
    if i.所在等级 == 85:
        湮灭之瞳二觉序号 = 湮灭之瞳技能序号[i.名称]
    if i.所在等级 == 100:
        湮灭之瞳三觉序号 = 湮灭之瞳技能序号[i.名称]

湮灭之瞳护石选项 = ['无']
for i in 湮灭之瞳技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        湮灭之瞳护石选项.append(i.名称)

湮灭之瞳符文选项 = ['无']
for i in 湮灭之瞳技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        湮灭之瞳符文选项.append(i.名称)


class 湮灭之瞳角色属性(角色属性):
    职业名称 = '湮灭之瞳'

    武器选项 = ['魔杖', '法杖']

    # '物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']

    # 默认
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 2.07

    # 基础属性(含唤醒)
    基础力量 = 774
    基础智力 = 976

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    def __init__(self):
        self.技能栏 = copy.deepcopy(湮灭之瞳技能列表)
        self.技能序号 = copy.deepcopy(湮灭之瞳技能序号)

    def 属性强化加成(self):
        属性强化值 = 0
        for i in self.技能栏:
            if i.名称 != '元素环绕':
              属性强化值 += 0
            else:
              属性强化值 += i.属强加成()
        return (属性强化值)

    def 伤害指数计算(self):
        self.冰属性强化 += self.技能栏[self.技能序号['元素环绕']].属强加成()
        self.光属性强化 += self.技能栏[self.技能序号['元素环绕']].属强加成()
        self.火属性强化 += self.技能栏[self.技能序号['元素环绕']].属强加成()
        self.暗属性强化 += self.技能栏[self.技能序号['元素环绕']].属强加成()
        self.冰属性强化 += self.技能栏[self.技能序号['元素融合']].属强加成()
        self.光属性强化 += self.技能栏[self.技能序号['元素融合']].属强加成()
        self.火属性强化 += self.技能栏[self.技能序号['元素融合']].属强加成()
        self.暗属性强化 += self.技能栏[self.技能序号['元素融合']].属强加成()



        基准倍率 = 1.5 * self.主BUFF * (1 - 443215 / (443215 + 20000))

        面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)

        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        self.伤害指数=面板*属性倍率*增伤倍率*基准倍率/100

    def 被动倍率计算(self):
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else :
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            # Will添加
            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else :
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)
            # Will添加
            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else :
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)

    def 伤害计算(self, x=0):

        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()

        技能释放次数 = []
        技能单次伤害 = []
        技能总伤害 = []

        # 技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if self.次数输入[self.技能序号[i.名称]] == '/CD':
                    技能释放次数.append(int(self.时间输入 / i.等效CD(self.武器类型) + 1 + i.基础释放次数))
                else:
                    技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]) + i.基础释放次数)
            else:
                技能释放次数.append(0)

        for i in self.技能栏:
            if i.关联技能4 != ['无']:
                    for j in i.关联技能4:
                        i.元素之力蓄力数量 += 技能释放次数[self.技能序号[j]]
        # 技能单次伤害计算
        for i in self.技能栏:
            if i.是否主动 == 1 and i.名称 != '元素炮' :
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率)
            elif i.名称 == '元素炮':
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率*
                                  self.技能栏[self.技能序号['元素循环']].加成倍率(self.武器类型)*
                              self.技能栏[self.技能序号['超卓之心']].加成倍率(self.武器类型)*
                              self.技能栏[self.技能序号['卓越之力']].加成倍率(self.武器类型)*
                                 (1.0 + self.技能栏[self.技能序号['元素之力']].加成倍率(self.武器类型)*5))
            else:
                技能单次伤害.append(0)


        # 单技能伤害合计

        for i in self.技能栏:
            if i.是否主动 == 1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]] * 技能释放次数[self.技能序号[i.名称]] * (
                            1 + self.白兔子技能 * 0.20 + self.年宠技能 * 0.10 * self.宠物次数[self.技能序号[i.名称]] / 技能释放次数[
                        self.技能序号[i.名称]] + self.斗神之吼秘药 * 0.12))
            else:
                技能总伤害.append(0)

        总伤害 = 0
        for i in self.技能栏:
            总伤害 += 技能总伤害[self.技能序号[i.名称]]

        if x == 0:
            return 总伤害

        if x == 1:
            详细数据 = []
            for i in range(0, len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i] != 0:
                    详细数据.append(技能总伤害[i] / 技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害 != 0:
                    详细数据.append(技能总伤害[i] / 总伤害 * 100)
                else:
                    详细数据.append(0)
            return 详细数据

class 湮灭之瞳(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 湮灭之瞳角色属性()
        self.角色属性A = 湮灭之瞳角色属性()
        self.角色属性B = 湮灭之瞳角色属性()
        self.一觉序号 = 湮灭之瞳一觉序号
        self.二觉序号 = 湮灭之瞳二觉序号
        self.三觉序号 = 湮灭之瞳三觉序号
        self.护石选项 = copy.deepcopy(湮灭之瞳护石选项)
        self.符文选项 = copy.deepcopy(湮灭之瞳符文选项)


