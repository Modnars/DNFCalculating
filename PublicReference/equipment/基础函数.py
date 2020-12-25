#看看就行, 计算细节通用的数据

##############增幅################

增幅系数 = [0, 1, 2, 3, 4, 6, 8, 10, 12, 13, 17, 33, 50, 67, 108, 150, 192, 267, 342, 417, 500, 583, 667, 750, 833, 917, 1000, 1083, 1167, 1250, 1333, 1417]
增幅成长系数 = {'稀有': 1, '神器': 1.3, '勇者': 1.1, '传说': 1.4, '史诗': 1.5, '神话': 1.6}
增幅品级加分 = {'稀有': 45, '神器': 45, '勇者': 45, '传说': 46, '史诗': 46, '神话': 46}
增幅品级底数 = {'稀有': 5, '神器': 6, '勇者': 5, '传说': 6, '史诗': 7, '神话': 8}

def 增幅计算(装备等级, 品质, 强化等级): 
    return int((装备等级 + 增幅品级加分[品质]) * 增幅成长系数[品质] * 增幅系数[强化等级] / 100 - 0.00000001) + 增幅品级底数[品质]

###########特殊装备&勋章###########

耳环强化系数 = [0, 83, 124, 166, 207, 248, 314, 370, 426, 482, 621, 970, 1455, 1941, 2911, 4043, 5175, 7116, 9056, 10997, 13099, 15363, 17627, 19891, 22155, 24420, 26684, 28948, 31212, 33476, 35740, 38004]
左右强化系数 = [0, 60, 90, 120, 150, 180, 210, 247, 285, 322, 360, 675, 1013, 1350, 2025, 2813, 3600, 4950, 6300, 7650, 9113, 10688, 12263, 13838, 15413, 16988, 18563, 20138, 21713, 23288, 24863, 26438]
勋章强化系数 = [0, 100, 120, 144, 173, 208, 250, 300, 320, 360, 400, 610, 1220, 2440, 2684, 2952, 3838, 4989, 6486, 8432, 10962]
特殊成长系数 = {'普通': 0.4, '高级': 0.7, '稀有': 1, '神器': 1.25, '传说': 1.35, '史诗': 1.45, '神话': 1.55}
特殊品级加分 = {'普通': 24, '高级': 30, '稀有': 26, '神器': 28, '传说': 29, '史诗': 30, '神话': 31}

def 耳环计算(装备等级, 品质, 强化等级): 
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 耳环强化系数[强化等级])

def 左右计算(装备等级, 品质, 强化等级): 
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 左右强化系数[强化等级])

def 勋章计算(装备等级, 品质, 强化等级): 
    return int((装备等级 + 特殊品级加分[品质]) / 2400 * 特殊成长系数[品质] * 勋章强化系数[强化等级])

###############武器###############

武器强化系数 = [0, 2, 2.6, 3.6, 4.7, 5.8, 6.9, 8.2, 11, 14.6, 18.7, 26.9, 36.7, 43, 49.2, 55.4, 61.7, 68, 74.3, 80.6, 86.9, 93.2, 99.5, 105.8, 112.1, 118.3, 124.6, 130.9, 137.1, 14.34, 149.7, 156.0]
武器锻造系数 = [0, 2, 3, 4, 6, 8, 13, 18, 25, 32, 41]
武器成长系数 = {'普通': 0.4, '高级': 0.7, '稀有': 1, '神器': 1.25, '勇者': 1.1, '传说': 1.35, '史诗': 1.45, '神话': 1.55}
武器品级加分 = {'普通': 8, '高级': 8, '稀有': 10, '神器': 12, '勇者': 11, '传说': 13, '史诗': 14, '神话': 15}
武器类型系数 = {
    '短剑': [1.095, 1.115], 
    '太刀': [1.095, 1.105], 
    '钝器': [1.11, 1.095], 
    '巨剑': [1.12, 1.09], 
    '光剑': [1.093, 1.09], 
    '手套': [1.095, 1.115], 
    '臂铠': [1.12, 1.09], 
    '爪': [1.1, 1.1], 
    '拳套': [1.105, 1.095], 
    '东方棍': [1.095, 1.1], 
    '左轮枪': [1.087, 1.077], 
    '自动手枪': [1.064, 1.094], 
    '步枪': [1.1, 1.085], 
    '手炮': [1.106, 1.064], 
    '手弩': [1.075, 1.085], 
    '矛': [1.12, 1.085], 
    '棍棒': [1.108, 1.09], 
    '魔杖': [1.09, 1.11], 
    '法杖': [1.095, 1.12], 
    '扫把': [1.1, 1.11], 
    '十字架': [1.1, 1.095], 
    '念珠': [1.09, 1.115], 
    '图腾': [1.105, 1.09], 
    '镰刀': [1.105, 1.105], 
    '战斧': [1.12, 1.085], 
    '匕首': [1.09, 1.089], 
    '双剑': [1.102, 1.08], 
    '手杖': [1.081, 1.115], 
    '苦无': [1.09, 1.11], 
    '长枪': [1.105, 1.09], 
    '战戟': [1.12, 1.085], 
    '光枪': [1.095, 1.115], 
    '暗矛': [1.095, 1.105], 
    '长刀': [1.108, 1.09], 
    '小太刀': [1.1, 1.1], 
    '重剑': [1.12, 1.09], 
    '源力剑': [1.095, 1.115]}

def 武器计算(装备等级, 品质, 强化等级, 武器类型, 类型): 
    武器系数 = (武器类型系数[武器类型][0 if 类型 == '物理' else 1])
    return int((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器强化系数[强化等级] * 武器系数)

def 锻造计算(装备等级, 品质, 锻造等级): 
    return round((装备等级 + 武器品级加分[品质]) / 8 * 武器成长系数[品质] * 武器锻造系数[锻造等级])

def 锻造四维(装备等级, 品质, 锻造等级): 
    return round((装备等级 + 武器品级加分[品质]) / 80 * 武器成长系数[品质] * 武器锻造系数[锻造等级])

武器冷却惩罚系数 = {
    '短剑': [1, 1.05, 1], 
    '太刀': [0.95, 1, 1], 
    '钝器': [1.05, 1, 1], 
    '巨剑': [1.1, 1, 1], 
    '光剑': [0.9, 1, 1], 
    '手套': [0.9, 1.05, 1], 
    '臂铠': [1.1, 1, 1], 
    '爪': [1, 1, 1], 
    '拳套': [0.9, 1, 1], 
    '东方棍': [1, 1, 1], 
    '左轮枪': [1, 1, 1], 
    '自动手枪': [0.9, 1, 1], 
    '步枪': [1.05, 1, 1], 
    '手炮': [1.1, 1, 1], 
    '手弩': [0.9, 1, 1], 
    '矛': [1.05, 0.95, 1], 
    '棍棒': [1, 1, 1], 
    '魔杖': [0.95, 1, 1], 
    '法杖': [1, 1.1, 1], 
    '扫把': [1 ,1, 1], 
    '十字架': [0.95, 1, 1], 
    '念珠': [0.95, 1.05, 1], 
    '图腾': [1, 0.95, 1], 
    '镰刀': [0.95, 1, 1], 
    '战斧': [1.1, 0.9, 1], 
    '匕首': [0.9, 0.95, 1], 
    '双剑': [1.1, 0.9, 1], 
    '手杖': [1, 1.1, 1], 
    '苦无': [1, 1.05, 1], 
    '长枪': [1.05, 1, 1], 
    '战戟': [1.1, 0.9, 1], 
    '光枪': [1, 1.05, 1], 
    '暗矛': [0.95, 1, 1], 
    '长刀': [1.05, 1, 1], 
    '小太刀': [1, 1, 1], 
    '重剑': [1.1, 1, 1], 
    '源力剑': [1, 1.05, 1]}

武器冷却惩罚系数_HF = {
    '短剑': [1, 1.05, 1], 
    '太刀': [0.95, 1, 1], 
    '钝器': [1.05, 1, 1], 
    '巨剑': [1.1, 1, 1], 
    '光剑': [0.9, 1, 1], 
    '手套': [0.9, 1.05, 1], 
    '臂铠': [1.1, 1, 1], 
    '爪': [1, 1, 1], 
    '拳套': [0.9, 1, 1], 
    '东方棍': [1, 1, 1], 
    '左轮枪': [1, 1, 1], 
    '自动手枪': [0.9, 1, 1], 
    '步枪': [1.05, 1, 1], 
    '手炮': [1.1, 1, 1], 
    '手弩': [0.9, 1, 1], 
    '矛': [1.05, 0.95, 1], 
    '棍棒': [1, 1, 1], 
    '魔杖': [0.95, 1, 1], 
    '法杖': [1, 1.1, 1], 
    '扫把': [1 ,1, 1], 
    '十字架': [0.95, 1, 1], 
    '念珠': [0.95, 1.05, 1], 
    '图腾': [1, 0.95, 1], 
    '镰刀': [0.95, 1, 1], 
    '战斧': [1.1, 0.9, 1], 
    '匕首': [0.9, 0.95, 1], 
    '双剑': [1.1, 0.9, 1], 
    '手杖': [1, 1.1, 1], 
    '苦无': [1, 1.05, 1], 
    '长枪': [1, 1, 1], 
    '战戟': [1.1, 0.9, 1], 
    '光枪': [1, 1.05, 1], 
    '暗矛': [0.95, 1, 1], 
    '长刀': [1.05, 1, 1], 
    '小太刀': [1, 1, 1], 
    '重剑': [1.1, 1, 1], 
    '源力剑': [1, 1.05, 1]}

def 武器冷却惩罚(武器类型, 输出类型,版本='GF'):
    类型系数 = (0 if 输出类型 == '物理百分比' else ( 1 if 输出类型 =='魔法百分比' else 2))
    if 版本 == 'GF':
        return 武器冷却惩罚系数[武器类型][类型系数]
    else:
        return 武器冷却惩罚系数_HF[武器类型][类型系数]

#################防具################

部位系数 = {'上衣': 0.30, '头肩': 0.20, '下装': 0.25, '腰带': 0.10, '鞋': 0.15}
品级加分 = {'稀有': 5, '神器': 8, '勇者': 11, '传说': 14, '史诗': 17, '神话': 18}

def 精通计算(装备等级, 品质, 强化等级, 部位): 
    return round((20 + 2.5 * (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)

def 精通体力(装备等级, 品质, 强化等级, 部位): 
    return round((4 + (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)

def 精通精神(装备等级, 品质, 强化等级, 部位): 
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2

def 精通智力(装备等级, 品质, 强化等级, 部位): 
    return 精通体力(装备等级, 品质, 强化等级, 部位) * 2

#############角色基础属性##############

当前等级 = 100

角色基础系数 = {
    '魔枪士': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5], 
    '格斗家(女)': [5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5], 
    '格斗家(男)': [5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5], 
    '枪剑士': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5], 
    '神枪手(女)': [4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5], 
    '神枪手(男)': [4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5], 
    '守护者': [4.8, 4.8, 4.2, 4.2, 7, 7, 5, 5], 
    '魔法师(女)': [4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5], 
    '魔法师(男)': [3.5, 4, 5.5, 5, 4, 4.5, 8, 7.5], 
    '暗夜使者': [5, 4, 5, 4, 7.5, 5.5, 6.5, 4.5], 
    '缔造者': [4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5], 
    '黑暗武士': [4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5], 
    '鬼剑士(男)': [4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5], 
    '鬼剑士(女)': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5], 
    '圣职者(男)': [4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5], 
    '圣职者(女)': [4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5]}

职业基础数据 = {
    '征战者-魔枪士': [5.5, 5.5, 3.5, 3.5], 
    '决战者-魔枪士': [5, 5, 4, 4], 
    '狩猎者-魔枪士': [3, 4.5, 6, 4.5], 
    '暗枪士-魔枪士': [3.5, 3.5, 5.5, 5.5], 
    '气功师-格斗家(女)': [3.5, 3.5, 5.5, 5.5], 
    '散打-格斗家(女)': [5.5, 5.5, 3.5, 3.5], 
    '街霸-格斗家(女)': [5, 4, 5, 4], 
    '柔道家-格斗家(女)': [5, 6, 3.5, 3.5], 
    '气功师-格斗家(男)': [3.5, 3.5, 5.5, 5.5], 
    '散打-格斗家(男)': [5.5, 5.5, 3.5, 3.5], 
    '街霸-格斗家(男)': [5, 4, 5, 4], 
    '柔道家-格斗家(男)': [5, 6, 3.5, 3.5], 
    '暗刃-枪剑士': [5.5, 5.5, 3.5, 3.5], 
    '特工-枪剑士': [5, 5, 4, 4], 
    '战线佣兵-枪剑士': [5.2, 5, 3.5, 4.3], 
    '源能专家-枪剑士': [3.5, 3.5, 5.5, 5.5], 
    '漫游枪手-神枪手(女)': [5.5, 5.5, 3.5, 3.5], 
    '枪炮师-神枪手(女)': [5.5, 5.5, 3.5, 3.5], 
    '机械师-神枪手(女)': [3.5, 3.5, 5.5, 5.5], 
    '弹药专家-神枪手(女)': [4.7, 4.3, 4.7, 4.3], 
    '漫游枪手-神枪手(男)': [5.5, 5.5, 3.5, 3.5], 
    '枪炮师-神枪手(男)': [5.5, 5.5, 3.5, 3.5], 
    '机械师-神枪手(男)': [3.5, 3.5, 5.5, 5.5], 
    '弹药专家-神枪手(男)': [4.7, 4.3, 4.7, 4.3], 
    '精灵骑士-守护者': [5, 5, 4, 4], 
    '混沌魔灵-守护者': [3.5, 3.5, 5.5, 5.5], 
    '帕拉丁-守护者': [5, 5.5, 2, 5.5], 
    '龙骑士-守护者': [5, 5, 4, 4], 
    '元素师-魔法师(女)': [3.5, 3.5, 5.5, 5.5], 
    '召唤师-魔法师(女)': [3.8, 3.7, 5.3, 5.2], 
    '战斗法师-魔法师(女)': [5, 4, 5, 4], 
    '魔道学者-魔法师(女)': [4.5, 4, 5.2, 4.3], 
    '小魔女-魔法师(女)': [4.7, 4.8, 5.5, 4.5], 
    '元素爆破师-魔法师(男)': [3.5, 3.5, 5.5, 5.5], 
    '冰结师-魔法师(男)': [3.5, 3.7, 5.5, 5.2], 
    '血法师-魔法师(男)': [5.5, 5.5, 3.5, 3.5], 
    '逐风者-魔法师(男)': [5.5, 5.2, 3.5, 3.8], 
    '次元行者-魔法师(男)': [3.5, 3.5, 5.5, 5.5], 
    '刺客-暗夜使者': [5.3, 4.5, 4.2, 4], 
    '死灵术士-暗夜使者': [4.7, 3.5, 5.3, 4.5], 
    '忍者-暗夜使者': [4.5, 3.5, 5.5, 4.5], 
    '影舞者-暗夜使者': [5.5, 4.5, 4, 4], 
    '缔造者-缔造者': [4, 4, 5, 5], 
    '黑暗武士-黑暗武士': [4.8, 4.8, 4.2, 4.2], 
    '剑魂-鬼剑士(男)': [5, 5, 4, 4], 
    '鬼泣-鬼剑士(男)': [3.5, 3.5, 5.5, 5.5], 
    '狂战士-鬼剑士(男)': [5.5, 5.5, 3.5, 3.5], 
    '阿修罗-鬼剑士(男)': [3, 4.5, 6, 4.5], 
    '剑影-鬼剑士(男)': [5, 5, 4, 4], 
    '驭剑士-鬼剑士(女)': [5, 5, 4, 4], 
    '暗殿骑士-鬼剑士(女)': [3.5, 3.5, 5.5, 5.5], 
    '契魔者-鬼剑士(女)': [5.5, 5.5, 3.5, 3.5], 
    '流浪武士-鬼剑士(女)': [5.5, 5.5, 3.5, 3.5], 
    '圣骑士-圣职者(男)': [3.5, 5.5, 3.5, 5.5], 
    '蓝拳圣使-圣职者(男)': [5.2, 5, 3.9, 3.9], 
    '驱魔师-圣职者(男)': [5, 4, 5, 4], 
    '复仇者-圣职者(男)': [3.5, 3.5, 5.5, 5.5], 
    '圣骑士-圣职者(女)': [3.5, 5.5, 5.5, 3.5], 
    '异端审判者-圣职者(女)': [5.2, 5, 3.5, 4.3], 
    '巫女-圣职者(女)': [3.5, 3.5, 5.5, 5.5], 
    '诱魔者-圣职者(女)': [3.5, 3.5, 5.5, 5.5]}

def 基础属性输入(属性):

    角色数据 = 角色基础系数[属性.角色]
    职业数据 = 职业基础数据[属性.职业 + '-' + 属性.角色]

    唤醒 = (275 if 当前等级 >= 75 else (145 if 当前等级 >= 15 else 0))

    属性.基础力量 = int(角色数据[4] + 角色数据[0] * min(14, 当前等级 - 1) + 职业数据[0] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
    属性.基础体力 = int(角色数据[5] + 角色数据[1] * min(14, 当前等级 - 1) + 职业数据[1] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))
    属性.基础智力 = int(角色数据[6] + 角色数据[2] * min(14, 当前等级 - 1) + 职业数据[2] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
    属性.基础精神 = int(角色数据[7] + 角色数据[3] * min(14, 当前等级 - 1) + 职业数据[3] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))

    属性.力量 = 属性.基础力量
    属性.智力 = 属性.基础智力
    属性.体力 = 属性.基础体力
    属性.精神 = 属性.基础精神
    