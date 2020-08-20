from PublicReference.base import *

class 极诣·流浪武士主动技能(主动技能):
    武器CD = {'短剑':1.0, '光剑':0.9 * 0.9, '巨剑':1.1, '钝器':1.05, '太刀':0.95}
    def 等效CD(self, 武器类型):
        return round(self.CD / self.恢复  * self.武器CD[武器类型], 1)

class 极诣·流浪武士技能0(被动技能):
    名称 = '返本归元'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.04 * self.等级, 5)

class 极诣·流浪武士技能1(被动技能):
    名称 = '三花聚顶'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.065 + 0.02 * self.等级, 5)

class 极诣·流浪武士技能2(被动技能):
    名称 = '七星耀华'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 极诣·流浪武士技能3(被动技能):
    名称 = '剑仙之境'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 极诣·流浪武士技能4(极诣·流浪武士主动技能):
    名称 = '四象引'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    数据 = [0, 3928.0, 4331.0, 4714.0, 5118.0, 5520.0, 5912.0, 6314.0, 6718.0, 7120.0, 7511.0, 7913.0, 8306.0, 8700.0, 9102.0, 9504.0, 9897.0, 10300.0, 10702.0, 11104.0, 11490.0, 11889.0, 12292.0, 12686.0, 13087.0, 13489.0, 13882.0, 14285.0, 14685.0, 15068.0, 15473.0, 15875.0, 16278.0, 16669.0, 17073.0, 17474.0, 17867.0, 18261.0, 18663.0, 19056.0, 19458.0, 19861.0, 20263.0, 20655.0, 21058.0, 21458.0, 21844.0, 22247.0, 22647.0, 23039.0, 23443.0, 23845.0, 24239.0, 24640.0, 25042.0, 25434.0, 25828.0, 26230.0, 26634.0, 27028.0, 27428.0, 27830.0, 28213.0, 28617.0, 29019.0, 29423.0, 29812.0, 30216.0, 30618.0, 31010.0, 31412.0]
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能5(极诣·流浪武士主动技能):
    名称 = '一花渡江'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5
    数据 = [0, 1191.0, 1311.0, 1432.0, 1552.0, 1674.0, 1794.0, 1915.0, 2036.0, 2157.0, 2277.0, 2398.0, 2520.0, 2640.0, 2761.0, 2881.0, 3003.0, 3123.0, 3244.0, 3365.0, 3486.0, 3606.0, 3727.0, 3848.0, 3969.0, 4089.0, 4211.0, 4332.0, 4452.0, 4573.0, 4694.0, 4815.0, 4935.0, 5057.0, 5177.0, 5298.0, 5418.0, 5540.0, 5660.0, 5781.0, 5902.0, 6023.0, 6144.0, 6264.0, 6386.0, 6506.0, 6627.0, 6747.0, 6869.0, 6989.0, 7110.0, 7230.0, 7352.0, 7473.0, 7593.0, 7715.0, 7835.0, 7956.0, 8076.0, 8198.0, 8318.0, 8439.0, 8559.0, 8681.0, 8801.0, 8922.0, 9043.0, 9164.0, 9285.0, 9405.0, 9527.0]
    攻击次数 = 3
    def 等效百分比(self, 武器类型):
        return self.攻击次数 * self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能6(极诣·流浪武士主动技能):
    名称 = '樱落斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 463.0, 507.0, 556.0, 603.0, 656.0, 698.0, 750.0, 795.0, 842.0, 893.0, 936.0, 986.0, 1033.0, 1082.0, 1127.0, 1175.0, 1226.0, 1269.0, 1320.0, 1367.0, 1414.0, 1462.0, 1510.0, 1558.0, 1604.0, 1653.0, 1700.0, 1747.0, 1798.0, 1842.0, 1891.0, 1940.0, 1986.0, 2035.0, 2080.0, 2130.0, 2177.0, 2223.0, 2272.0, 2319.0, 2366.0, 2414.0, 2464.0, 2507.0, 2559.0, 2606.0, 2655.0, 2701.0, 2747.0, 2798.0, 2842.0, 2891.0, 2937.0, 2985.0, 3036.0, 3079.0, 3130.0, 3177.0, 3225.0, 3270.0, 3319.0, 3368.0, 3414.0, 3462.0, 3509.0, 3557.0, 3608.0, 3651.0, 3702.0, 3750.0]
    data2 = [0, 619.0, 680.0, 742.0, 805.0, 871.0, 933.0, 994.0, 1061.0, 1124.0, 1188.0, 1247.0, 1317.0, 1378.0, 1440.0, 1504.0, 1569.0, 1631.0, 1692.0, 1757.0, 1822.0, 1888.0, 1949.0, 2012.0, 2076.0, 2139.0, 2201.0, 2265.0, 2330.0, 2395.0, 2455.0, 2523.0, 2584.0, 2647.0, 2710.0, 2775.0, 2839.0, 2899.0, 2965.0, 3027.0, 3093.0, 3156.0, 3221.0, 3282.0, 3345.0, 3408.0, 3472.0, 3536.0, 3601.0, 3662.0, 3728.0, 3792.0, 3853.0, 3917.0, 3979.0, 4045.0, 4106.0, 4170.0, 4234.0, 4299.0, 4363.0, 4427.0, 4490.0, 4551.0, 4616.0, 4678.0, 4743.0, 4810.0, 4869.0, 4934.0, 4997.0]
    data3 = [0, 176.0, 194.0, 212.0, 229.0, 250.0, 266.0, 286.0, 303.0, 320.0, 338.0, 356.0, 375.0, 394.0, 410.0, 430.0, 447.0, 466.0, 485.0, 503.0, 519.0, 539.0, 556.0, 577.0, 595.0, 609.0, 630.0, 647.0, 666.0, 683.0, 701.0, 720.0, 739.0, 755.0, 775.0, 792.0, 812.0, 830.0, 848.0, 865.0, 883.0, 900.0, 920.0, 936.0, 955.0, 974.0, 992.0, 1010.0, 1028.0, 1045.0, 1066.0, 1083.0, 1100.0, 1121.0, 1137.0, 1154.0, 1174.0, 1189.0, 1209.0, 1228.0, 1246.0, 1266.0, 1284.0, 1300.0, 1319.0, 1337.0, 1356.0, 1373.0, 1390.0, 1411.0, 1427.0]
    data4 = [0, 1230.0, 1357.0, 1482.0, 1609.0, 1741.0, 1860.0, 1992.0, 2119.0, 2247.0, 2374.0, 2498.0, 2626.0, 2752.0, 2878.0, 3010.0, 3135.0, 3264.0, 3387.0, 3516.0, 3640.0, 3770.0, 3896.0, 4022.0, 4154.0, 4273.0, 4405.0, 4533.0, 4658.0, 4787.0, 4910.0, 5039.0, 5165.0, 5291.0, 5423.0, 5550.0, 5676.0, 5802.0, 5927.0, 6055.0, 6183.0, 6309.0, 6434.0, 6566.0, 6687.0, 6819.0, 6944.0, 7072.0, 7203.0, 7324.0, 7455.0, 7578.0, 7707.0, 7836.0, 7962.0, 8090.0, 8214.0, 8341.0, 8467.0, 8595.0, 8724.0, 8847.0, 8979.0, 9099.0, 9231.0, 9359.0, 9484.0, 9615.0, 9736.0, 9867.0, 9993.0]
    数据 = [data1, data2, data3, data4]
    次数 = [1, 1, 3, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能7(极诣·流浪武士主动技能):
    名称 = '圆舞斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    CD = 11.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 2960.0, 3261.0, 3562.0, 3862.0, 4158.0, 4460.0, 4761.0, 5061.0, 5363.0, 5662.0, 5964.0, 6265.0, 6560.0, 6862.0, 7162.0, 7463.0, 7764.0, 8065.0, 8367.0, 8666.0, 8965.0, 9263.0, 9564.0, 9866.0, 10165.0, 10467.0, 10767.0, 11067.0, 11366.0, 11667.0, 11969.0, 12266.0, 12567.0, 12871.0, 13169.0, 13469.0, 13768.0, 14071.0, 14370.0, 14671.0, 14973.0, 15273.0, 15572.0, 15869.0, 16170.0, 16471.0, 16772.0, 17074.0, 17374.0, 17675.0, 17970.0, 18271.0, 18572.0, 18873.0, 19174.0, 19474.0, 19776.0, 20077.0, 20376.0, 20672.0, 20976.0, 21275.0, 21574.0, 21877.0, 22178.0, 22478.0, 22778.0, 23077.0, 23379.0, 23678.0]
    data2 = [0, 1774.0, 1956.0, 2134.0, 2314.0, 2496.0, 2675.0, 2854.0, 3036.0, 3214.0, 3394.0, 3578.0, 3755.0, 3933.0, 4116.0, 4297.0, 4474.0, 4657.0, 4837.0, 5015.0, 5195.0, 5376.0, 5553.0, 5736.0, 5916.0, 6094.0, 6277.0, 6456.0, 6635.0, 6816.0, 6997.0, 7175.0, 7356.0, 7535.0, 7713.0, 7896.0, 8076.0, 8259.0, 8437.0, 8617.0, 8796.0, 8977.0, 9156.0, 9340.0, 9515.0, 9697.0, 9878.0, 10056.0, 10235.0, 10418.0, 10596.0, 10776.0, 10959.0, 11136.0, 11317.0, 11498.0, 11677.0, 11855.0, 12039.0, 12220.0, 12396.0, 12579.0, 12758.0, 12937.0, 13117.0, 13298.0, 13476.0, 13658.0, 13837.0, 14016.0, 14198.0]
    data3 = [0, 1066.0, 1171.0, 1284.0, 1389.0, 1498.0, 1606.0, 1715.0, 1821.0, 1929.0, 2038.0, 2148.0, 2253.0, 2361.0, 2469.0, 2579.0, 2685.0, 2793.0, 2900.0, 3013.0, 3120.0, 3228.0, 3335.0, 3443.0, 3552.0, 3662.0, 3768.0, 3876.0, 3985.0, 4093.0, 4199.0, 4307.0, 4416.0, 4526.0, 4634.0, 4742.0, 4849.0, 4956.0, 5062.0, 5172.0, 5280.0, 5389.0, 5496.0, 5606.0, 5713.0, 5820.0, 5927.0, 6035.0, 6143.0, 6253.0, 6362.0, 6469.0, 6575.0, 6688.0, 6794.0, 6903.0, 7012.0, 7120.0, 7227.0, 7335.0, 7444.0, 7551.0, 7658.0, 7768.0, 7876.0, 7983.0, 8090.0, 8200.0, 8308.0, 8415.0, 8521.0]
    数据 = [data1, data2, data3]
    次数 = [1, 0, 1]
    #无法抓取敌人无冲撞攻击力
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能8(极诣·流浪武士主动技能):
    名称 = '碎岩裂地掌'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    CD = 12.0
    演出时间 = 0.5
    TP成长 = 0.10
    TP上限 = 5
    数据 = [0, 6371.0, 7014.0, 7661.0, 8307.0, 8954.0, 9600.0, 10248.0, 10893.0, 11542.0, 12186.0, 12833.0, 13478.0, 14126.0, 14770.0, 15418.0, 16061.0, 16711.0, 17354.0, 18006.0, 18650.0, 19295.0, 19942.0, 20588.0, 21235.0, 21878.0, 22527.0, 23169.0, 23817.0, 24462.0, 25112.0, 25757.0, 26405.0, 27048.0, 27696.0, 28340.0, 28989.0, 29633.0, 30281.0, 30924.0, 31575.0, 32220.0, 32867.0, 33512.0, 34160.0, 34805.0, 35451.0, 36096.0, 36740.0, 37389.0, 38033.0, 38684.0, 39327.0, 39974.0, 40621.0, 41266.0, 41913.0, 42559.0, 43204.0, 43851.0, 44495.0, 45146.0, 45790.0, 46439.0, 47082.0, 47729.0, 48375.0, 49023.0, 49666.0, 50316.0, 50959.0]
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能9(极诣·流浪武士主动技能):
    名称 = '游龙掌'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    CD = 12.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    数据 = [0, 838.0, 927.0, 1016.0, 1096.0, 1184.0, 1273.0, 1362.0, 1444.0, 1533.0, 1622.0, 1708.0, 1789.0, 1876.0, 1967.0, 2053.0, 2139.0, 2229.0, 2312.0, 2401.0, 2487.0, 2575.0, 2659.0, 2747.0, 2838.0, 2923.0, 3004.0, 3094.0, 3183.0, 3268.0, 3355.0, 3445.0, 3528.0, 3615.0, 3702.0, 3791.0, 3875.0, 3960.0, 4053.0, 4138.0, 4220.0, 4307.0, 4395.0, 4483.0, 4571.0, 4654.0, 4744.0, 4831.0, 4918.0, 4999.0, 5090.0, 5176.0, 5265.0, 5354.0, 5437.0, 5523.0, 5610.0, 5699.0, 5785.0, 5869.0, 5955.0, 6046.0, 6131.0, 6215.0, 6304.0, 6391.0, 6477.0, 6560.0, 6651.0, 6740.0, 6825.0]
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率 * 10 #攻击次数为10

class 极诣·流浪武士技能10(极诣·流浪武士主动技能):
    名称 = '乱花葬'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 24
    CD = 25.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 320.0, 370.0, 421.0, 472.0, 523.0, 575.0, 625.0, 676.0, 727.0, 778.0, 830.0, 880.0, 931.0, 982.0, 1033.0, 1085.0, 1135.0, 1186.0, 1237.0, 1288.0, 1340.0, 1390.0, 1441.0, 1492.0, 1543.0, 1594.0, 1645.0, 1696.0, 1747.0, 1798.0, 1849.0, 1900.0, 1951.0, 2002.0, 2053.0, 2104.0, 2155.0, 2205.0, 2257.0, 2308.0, 2359.0, 2410.0, 2460.0, 2512.0, 2563.0, 2614.0, 2665.0, 2715.0, 2767.0, 2818.0, 2868.0, 2920.0, 2970.0, 3022.0, 3073.0, 3123.0, 3175.0, 3225.0, 3277.0, 3328.0, 3378.0, 3430.0, 3480.0, 3532.0, 3583.0, 3633.0, 3685.0, 3735.0, 3787.0, 3838.0]
    data2 = [0, 3184.0, 3692.0, 4199.0, 4707.0, 5215.0, 5723.0, 6231.0, 6739.0, 7246.0, 7754.0, 8261.0, 8769.0, 9277.0, 9784.0, 10292.0, 10801.0, 11308.0, 11816.0, 12323.0, 12831.0, 13339.0, 13846.0, 14354.0, 14861.0, 15370.0, 15878.0, 16385.0, 16893.0, 17401.0, 17908.0, 18416.0, 18923.0, 19431.0, 19940.0, 20447.0, 20955.0, 21463.0, 21970.0, 22478.0, 22985.0, 23493.0, 24001.0, 24508.0, 25017.0, 25525.0, 26032.0, 26540.0, 27047.0, 27555.0, 28063.0, 28570.0, 29078.0, 29587.0, 30094.0, 30602.0, 31109.0, 31617.0, 32125.0, 32632.0, 33140.0, 33647.0, 34156.0, 34664.0, 35171.0, 35679.0, 36186.0, 36694.0, 37202.0, 37709.0, 38217.0]
    data3 = [0, 515.0, 597.0, 679.0, 760.0, 842.0, 925.0, 1007.0, 1089.0, 1171.0, 1254.0, 1336.0, 1417.0, 1499.0, 1582.0, 1664.0, 1746.0, 1828.0, 1911.0, 1993.0, 2074.0, 2156.0, 2238.0, 2321.0, 2403.0, 2485.0, 2567.0, 2650.0, 2731.0, 2813.0, 2895.0, 2977.0, 3060.0, 3142.0, 3224.0, 3306.0, 3388.0, 3470.0, 3552.0, 3634.0, 3717.0, 3799.0, 3881.0, 3963.0, 4044.0, 4127.0, 4209.0, 4291.0, 4373.0, 4456.0, 4538.0, 4620.0, 4701.0, 4783.0, 4866.0, 4948.0, 5030.0, 5112.0, 5195.0, 5277.0, 5358.0, 5440.0, 5523.0, 5605.0, 5687.0, 5769.0, 5852.0, 5934.0, 6016.0, 6097.0, 6179.0]
    data4 = [0, 5074.0, 5882.0, 6692.0, 7500.0, 8308.0, 9118.0, 9926.0, 10736.0, 11544.0, 12353.0, 13162.0, 13971.0, 14780.0, 15589.0, 16398.0, 17207.0, 18015.0, 18825.0, 19633.0, 20443.0, 21251.0, 22059.0, 22869.0, 23677.0, 24487.0, 25295.0, 26105.0, 26913.0, 27722.0, 28531.0, 29340.0, 30149.0, 30958.0, 31766.0, 32576.0, 33384.0, 34194.0, 35002.0, 35812.0, 36620.0, 37428.0, 38238.0, 39046.0, 39856.0, 40664.0, 41473.0, 42282.0, 43091.0, 43900.0, 44709.0, 45518.0, 46327.0, 47135.0, 47945.0, 48753.0, 49563.0, 50371.0, 51179.0, 51989.0, 52797.0, 53607.0, 54415.0, 55224.0, 56033.0, 56842.0, 57651.0, 58460.0, 59269.0, 60078.0, 60886.0]
    数据 = [data1, data2, data3, data4]
    次数 = [6, 1, 5, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [6 + 4, 1, 5 + 4, 1]
        elif x== 1:
            self.次数 = [6 + 4, 1, 5 + 4, 1]
            self.倍率 *= 1.07
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>花无语</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乱花葬]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "念气之花散开攻击效果强化<br>"
            temp += "- 多段攻击次数 +80%<br>"
            temp += "- 多段攻击间隔 -45%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "前冲动作可以击退霸体状态的敌人<br>"
            temp += "念气之花散开攻击时可以吸附敌人<br>"
            temp += "多段攻击强化<br>"
            temp += "- 多段攻击次数 +67%<br>"
            temp += "- 多段攻击间隔 -40%"
        elif x == 1:
            temp = "<font color='#FF00FF'>花无语</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[乱花葬]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "念气之花散开攻击效果强化<br>"
            temp += "- 多段攻击次数 +80%<br>"
            temp += "- 多段攻击间隔 -45%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "前冲动作可以击退霸体状态的敌人<br>"
            temp += "念气之花散开攻击时可以吸附敌人<br>"
            temp += "多段攻击强化<br>"
            temp += "- 多段攻击次数 +67%<br>"
            temp += "- 多段攻击间隔 -40%<br>"
            temp += "攻击力 +7%"
        return temp  

class 极诣·流浪武士技能11(极诣·流浪武士主动技能):
    名称 = '回天璇鸣剑'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 20.0
    演出时间 = 1
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 3132.0, 3433.0, 3778.0, 4099.0, 4400.0, 4699.0, 5045.0, 5345.0, 5665.0, 5989.0, 6312.0, 6611.0, 6911.0, 7258.0, 7579.0, 7878.0, 8224.0, 8523.0, 8824.0, 9167.0, 9468.0, 9791.0, 10089.0, 10436.0, 10733.0, 11057.0, 11380.0, 11702.0, 12002.0, 12303.0, 12646.0, 12946.0, 13268.0, 13615.0, 13915.0, 14212.0, 14513.0, 14859.0, 15181.0, 15481.0, 15825.0, 16124.0, 16425.0, 16747.0, 17070.0, 17393.0, 17692.0, 18037.0, 18337.0, 18660.0, 18983.0, 19303.0, 19603.0, 19948.0, 20249.0, 20549.0, 20893.0, 21216.0, 21517.0, 21861.0, 22162.0, 22461.0, 22806.0, 23105.0, 23427.0, 23774.0, 24074.0, 24372.0, 24718.0, 25017.0]
    data2 = [0, 9126.0, 10051.0, 10979.0, 11906.0, 12829.0, 13758.0, 14680.0, 15608.0, 16536.0, 17459.0, 18382.0, 19312.0, 20234.0, 21162.0, 22089.0, 23012.0, 23942.0, 24865.0, 25792.0, 26720.0, 27642.0, 28570.0, 29493.0, 30422.0, 31351.0, 32275.0, 33197.0, 34124.0, 35046.0, 35975.0, 36899.0, 37828.0, 38754.0, 39678.0, 40605.0, 41529.0, 42456.0, 43385.0, 44308.0, 45236.0, 46159.0, 47087.0, 48014.0, 48938.0, 49862.0, 50791.0, 51713.0, 52640.0, 53568.0, 54492.0, 55420.0, 56342.0, 57270.0, 58199.0, 59122.0, 60046.0, 60972.0, 61901.0, 62826.0, 63753.0, 64678.0, 65603.0, 66525.0, 67455.0, 68378.0, 69304.0, 70233.0, 71156.0, 72085.0, 73008.0]
    数据 = [data1, data2]
    次数 = [1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率

class 极诣·流浪武士技能12(极诣·流浪武士主动技能):
    名称 = '湮烈掌'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 1589.0, 1750.0, 1911.0, 2072.0, 2233.0, 2396.0, 2557.0, 2718.0, 2879.0, 3040.0, 3201.0, 3363.0, 3524.0, 3686.0, 3847.0, 4008.0, 4169.0, 4331.0, 4492.0, 4653.0, 4814.0, 4975.0, 5136.0, 5298.0, 5459.0, 5620.0, 5781.0, 5942.0, 6105.0, 6266.0, 6428.0, 6589.0, 6750.0, 6911.0, 7073.0, 7234.0, 7395.0, 7556.0, 7717.0, 7878.0, 8040.0, 8201.0, 8362.0, 8523.0, 8684.0, 8845.0, 9007.0, 9168.0, 9329.0, 9490.0, 9651.0, 9813.0, 9975.0, 10136.0, 10297.0, 10458.0, 10619.0, 10780.0, 10943.0, 11104.0, 11265.0, 11426.0, 11587.0, 11748.0, 11910.0, 12071.0, 12232.0, 12393.0, 12555.0, 12716.0]
    data2 = [0, 11126.0, 12255.0, 13385.0, 14513.0, 15641.0, 16771.0, 17899.0, 19029.0, 20157.0, 21286.0, 22415.0, 23543.0, 24671.0, 25802.0, 26930.0, 28059.0, 29187.0, 30316.0, 31446.0, 32574.0, 33702.0, 34832.0, 35960.0, 37090.0, 38218.0, 39348.0, 40476.0, 41604.0, 42735.0, 43863.0, 44991.0, 46120.0, 47248.0, 48378.0, 49507.0, 50635.0, 51764.0, 52893.0, 54021.0, 55151.0, 56279.0, 57409.0, 58537.0, 59665.0, 60796.0, 61924.0, 63053.0, 64181.0, 65309.0, 66440.0, 67568.0, 68697.0, 69825.0, 70954.0, 72083.0, 73212.0, 74341.0, 75470.0, 76598.0, 77727.0, 78857.0, 79986.0, 81114.0, 82242.0, 83371.0, 84501.0, 85629.0, 86758.0, 87886.0, 89016.0]
    数据 = [data1, data2]
    次数 = [3, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1 + 3.11, 1 + 0.14]
        elif x== 1:
            self.次数 = [1 + 3.11, 1 + 0.27]
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>湮灭掌</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[湮烈掌]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "内劲被吸收至爆炸的时间 +1秒<br>"
            temp += "内劲爆炸攻击强化<br>"
            temp += "- 多段攻击次数 -2次<br>"
            temp += "- 攻击力 +311%<br>"
            temp += "- 大小 +50%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "蓄气时间 -40%<br>"
            temp += "内劲释放攻击力 +14%"
        elif x == 1:
            temp = "<font color='#FF00FF'>湮灭掌</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[湮烈掌]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "内劲被吸收至爆炸的时间 +1秒<br>"
            temp += "内劲爆炸攻击强化<br>"
            temp += "- 多段攻击次数 -2次<br>"
            temp += "- 攻击力 +311%<br>"
            temp += "- 大小 +50%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "蓄气时间 -40%<br>"
            temp += "内劲释放攻击力 +27%"
        return temp  

class 极诣·流浪武士技能13(极诣·流浪武士主动技能):
    名称 = '花舞千魂杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 10944.0, 12088.0, 13170.0, 14317.0, 15485.0, 16590.0, 17755.0, 18855.0, 19992.0, 21131.0, 22242.0, 23398.0, 24513.0, 25669.0, 26816.0, 27908.0, 29059.0, 30166.0, 31302.0, 32458.0, 33572.0, 34711.0, 35854.0, 36977.0, 38109.0, 39256.0, 40385.0, 41529.0, 42619.0, 43759.0, 44902.0, 46006.0, 47164.0, 48273.0, 49419.0, 50556.0, 51679.0, 52838.0, 53958.0, 55085.0, 56229.0, 57333.0, 58469.0, 59605.0, 60728.0, 61868.0, 63016.0, 64119.0, 65266.0, 66393.0, 67607.0, 68751.0, 69892.0, 71035.0, 72156.0, 73279.0, 74440.0, 75572.0, 76684.0, 77829.0, 78965.0, 80093.0, 81248.0, 82379.0, 83504.0, 84639.0, 85796.0, 86935.0, 88055.0, 89212.0]
    data2 = [0, 1504.0, 1661.0, 1816.0, 1971.0, 2131.0, 2286.0, 2444.0, 2595.0, 2753.0, 2912.0, 3062.0, 3221.0, 3374.0, 3532.0, 3691.0, 3842.0, 4001.0, 4153.0, 4307.0, 4466.0, 4620.0, 4775.0, 4934.0, 5094.0, 5245.0, 5404.0, 5558.0, 5718.0, 5866.0, 6025.0, 6181.0, 6333.0, 6492.0, 6643.0, 6801.0, 6956.0, 7114.0, 7270.0, 7429.0, 7583.0, 7740.0, 7893.0, 8051.0, 8207.0, 8360.0, 8519.0, 8674.0, 8827.0, 8985.0, 9139.0, 9309.0, 9467.0, 9620.0, 9778.0, 9935.0, 10087.0, 10246.0, 10403.0, 10554.0, 10713.0, 10874.0, 11024.0, 11185.0, 11343.0, 11494.0, 11651.0, 11811.0, 11964.0, 12118.0, 12280.0]
    data3 = [0, 6018.0, 6650.0, 7254.0, 7887.0, 8519.0, 9139.0, 9769.0, 10383.0, 11013.0, 11635.0, 12251.0, 12883.0, 13503.0, 14132.0, 14765.0, 15370.0, 16002.0, 16611.0, 17235.0, 17865.0, 18480.0, 19101.0, 19735.0, 20364.0, 20973.0, 21607.0, 22230.0, 22863.0, 23462.0, 24098.0, 24727.0, 25332.0, 25963.0, 26575.0, 27206.0, 27827.0, 28460.0, 29092.0, 29705.0, 30325.0, 30956.0, 31568.0, 32192.0, 32824.0, 33439.0, 34066.0, 34698.0, 35303.0, 35934.0, 36557.0, 37222.0, 37854.0, 38475.0, 39104.0, 39735.0, 40349.0, 40980.0, 41612.0, 42218.0, 42846.0, 43478.0, 44100.0, 44732.0, 45359.0, 45975.0, 46607.0, 47238.0, 47859.0, 48473.0, 49120.0]
    数据 = [data1, data2, data3]
    次数 = [1, 2, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1 + 1.19, 0, 0]
        elif x== 1:
            self.次数 = [1 + 1.33, 0, 0]
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>花飞万里</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[花舞千魂杀]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "删除剑插地攻击和最后下斩攻击<br>"
            temp += "一闪攻击力 +100%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "一闪攻击后僵直时间 -30%<br>"
            temp += "一闪攻击后转换角色朝向<br>"
            temp += "一闪攻击力 +19%"
        elif x == 1:
            temp = "<font color='#FF00FF'>花飞万里</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[花舞千魂杀]<br>"
            temp += "攻击范围 +25%<br>"
            temp += "删除剑插地攻击和最后下斩攻击<br>"
            temp += "一闪攻击力 +100%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "一闪攻击后僵直时间 -30%<br>"
            temp += "一闪攻击后转换角色朝向<br>"
            temp += "一闪攻击力 +33%"
        return temp  

class 极诣·流浪武士技能14(极诣·流浪武士主动技能):
    名称 = '花开寒影'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    CD = 145
    data1 = [0, 6249.0, 7698.0, 9147.0, 10596.0, 12045.0, 13495.0, 14943.0, 16392.0, 17841.0, 19290.0, 20740.0, 22188.0, 23637.0, 25086.0, 26536.0, 27985.0, 29433.0, 30882.0, 32331.0, 33781.0, 35229.0, 36678.0, 38127.0, 39578.0, 41027.0, 42476.0, 43924.0, 45374.0, 46823.0, 48272.0, 49721.0, 51169.0, 52619.0, 54068.0, 55517.0, 56966.0, 58415.0, 59864.0, 61313.0, 62762.0]
    data2 = [0, 960.0, 1184.0, 1406.0, 1630.0, 1853.0, 2075.0, 2297.0, 2522.0, 2744.0, 2967.0, 3190.0, 3413.0, 3636.0, 3858.0, 4082.0, 4305.0, 4527.0, 4751.0, 4974.0, 5196.0, 5419.0, 5643.0, 5865.0, 6088.0, 6312.0, 6534.0, 6758.0, 6980.0, 7203.0, 7425.0, 7649.0, 7871.0, 8094.0, 8318.0, 8540.0, 8762.0, 8987.0, 9209.0, 9431.0, 9656.0]
    data3 = [0, 39767.0, 48987.0, 58209.0, 67431.0, 76652.0, 85873.0, 95095.0, 104316.0, 124891.0, 135036.0, 145178.0, 155322.0, 165466.0, 175609.0, 185753.0, 195895.0, 206040.0, 216182.0, 226326.0, 236471.0, 246613.0, 256757.0, 266899.0, 277044.0, 287188.0, 297330.0, 307475.0, 317618.0, 327761.0, 337906.0, 348048.0, 358192.0, 368335.0, 378479.0, 388623.0, 398765.0, 408910.0, 419053.0, 429196.0, 439341.0]
    数据 = [data1, data2, data3]
    次数 = [1, 13, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率 

class 极诣·流浪武士技能15(极诣·流浪武士主动技能):
    名称 = '啸空十字斩'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 5188.0, 5715.0, 6241.0, 6767.0, 7294.0, 7820.0, 8346.0, 8872.0, 9399.0, 9926.0, 10451.0, 10978.0, 11504.0, 12030.0, 12555.0, 13082.0, 13609.0, 14135.0, 14661.0, 15187.0, 15714.0, 16238.0, 16765.0, 17292.0, 17818.0, 18344.0, 18871.0, 19397.0, 19924.0, 20449.0, 20977.0, 21504.0, 22030.0, 22556.0, 23082.0, 23609.0, 24135.0, 24660.0, 25187.0, 25713.0, 26240.0, 26766.0, 27292.0, 27819.0, 28345.0, 28871.0, 29398.0, 29924.0, 30451.0, 30978.0, 31503.0, 32030.0, 32554.0, 33081.0, 33607.0, 34134.0, 34659.0, 35186.0, 35713.0, 36239.0, 36765.0, 37292.0, 37818.0, 38345.0, 38870.0, 39397.0, 39924.0, 40450.0, 40976.0, 41502.0]
    data2 = [0, 6053.0, 6666.0, 7281.0, 7894.0, 8508.0, 9123.0, 9737.0, 10349.0, 10964.0, 11579.0, 12193.0, 12807.0, 13421.0, 14035.0, 14649.0, 15262.0, 15878.0, 16490.0, 17104.0, 17720.0, 18334.0, 18947.0, 19562.0, 20175.0, 20790.0, 21404.0, 22017.0, 22632.0, 23246.0, 23860.0, 24473.0, 25087.0, 25701.0, 26316.0, 26930.0, 27543.0, 28158.0, 28771.0, 29386.0, 30000.0, 30613.0, 31228.0, 31842.0, 32456.0, 33070.0, 33683.0, 34297.0, 34913.0, 35527.0, 36140.0, 36755.0, 37369.0, 37984.0, 38596.0, 39210.0, 39825.0, 40439.0, 41053.0, 41667.0, 42281.0, 42894.0, 43508.0, 44123.0, 44736.0, 45351.0, 45965.0, 46580.0, 47192.0, 47806.0, 48421.0]
    data3 = [0, 6918.0, 7619.0, 8321.0, 9022.0, 9725.0, 10425.0, 11128.0, 11830.0, 12533.0, 13233.0, 13936.0, 14637.0, 15338.0, 16041.0, 16742.0, 17444.0, 18145.0, 18848.0, 19550.0, 20251.0, 20953.0, 21656.0, 22356.0, 23059.0, 23760.0, 24462.0, 25164.0, 25866.0, 26567.0, 27268.0, 27971.0, 28674.0, 29374.0, 30076.0, 30779.0, 31479.0, 32182.0, 32883.0, 33585.0, 34287.0, 34989.0, 35691.0, 36392.0, 37094.0, 37797.0, 38496.0, 39199.0, 39902.0, 40601.0, 41305.0, 42005.0, 42707.0, 43409.0, 44111.0, 44813.0, 45514.0, 46216.0, 46919.0, 47619.0, 48321.0, 49024.0, 49724.0, 50427.0, 51128.0, 51831.0, 52532.0, 53234.0, 53936.0, 54637.0, 55339.0]
    数据 = [data1, data2, data3]
    次数 = [1, 1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1, 0, 1 + 0.88]
            self.CD *= 0.80
        elif x== 1:
            self.次数 = [1, 0, 1 + 0.88]
            self.CD *= 0.80
            self.倍率 *= 1.09
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>日落黄昏</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[啸空十字斩]<br>"
            temp += "删除垂直斩击<br>"
            temp += "爆炸攻击力 +88%<br>"
            temp += "冷却时间 -20%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸攻击范围 +25%<br>"
            temp += "水平斩击持续时间 +1.5秒<br>"
            temp += "再次按技能键时， 立即引发爆炸"
        elif x == 1:
            temp = "<font color='#FF00FF'>日落黄昏</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += "[啸空十字斩]<br>"
            temp += "删除垂直斩击<br>"
            temp += "爆炸攻击力 +88%<br>"
            temp += "冷却时间 -20%<br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "爆炸攻击范围 +25%<br>"
            temp += "水平斩击持续时间 +1.5秒<br>"
            temp += "再次按技能键时， 立即引发爆炸<br>"
            temp += "攻击力 +9%"
        return temp  

class 极诣·流浪武士技能16(极诣·流浪武士主动技能):
    名称 = '如来神掌'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    data1 = [0, 13098.0, 14427.0, 15758.0, 17085.0, 18414.0, 19741.0, 21073.0, 22399.0, 23730.0, 25061.0, 26386.0, 27715.0, 29043.0, 30374.0, 31703.0, 33030.0, 34362.0, 35687.0, 37018.0, 38348.0, 39676.0, 41004.0, 42331.0, 43664.0, 44993.0, 46319.0, 47650.0, 48977.0, 50307.0, 51632.0, 52965.0, 54294.0, 55622.0, 56953.0, 58281.0, 59608.0, 60935.0, 62267.0, 63595.0, 64923.0, 66254.0, 67583.0, 68910.0, 70237.0, 71570.0, 72897.0, 74224.0, 75555.0, 76884.0, 78212.0, 79540.0, 80871.0, 82198.0, 83526.0, 84858.0, 86185.0, 87513.0, 88844.0, 90173.0, 91499.0, 92829.0, 94159.0, 95486.0, 96814.0, 98147.0, 99474.0, 100801.0, 102130.0, 103462.0, 104788.0]
    data2 = [0, 19648.0, 21641.0, 23635.0, 25628.0, 27623.0, 29610.0, 31606.0, 33598.0, 35593.0, 37586.0, 39580.0, 41572.0, 43568.0, 45560.0, 47551.0, 49546.0, 51538.0, 53533.0, 55525.0, 57520.0, 59512.0, 61507.0, 63496.0, 65491.0, 67483.0, 69478.0, 71469.0, 73464.0, 75457.0, 77452.0, 79446.0, 81436.0, 83430.0, 85422.0, 87417.0, 89409.0, 91405.0, 93397.0, 95392.0, 97380.0, 99375.0, 101367.0, 103361.0, 105354.0, 107350.0, 109343.0, 111337.0, 113329.0, 115319.0, 117313.0, 119306.0, 121302.0, 123295.0, 125289.0, 127281.0, 129276.0, 131268.0, 133259.0, 135251.0, 137247.0, 139238.0, 141234.0, 143226.0, 145220.0, 147214.0, 149204.0, 151198.0, 153192.0, 155187.0, 157178.0]
    数据 = [data1, data2]
    次数 = [1, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * (1 + self.TP成长 * self.TP等级) * self.倍率  

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.次数 = [1 + 1.71 + 0.25, 0]
        elif x== 1:
            self.次数 = [1 + 1.71 + 0.45, 0]
    def 护石描述(self, x):
        if x == 0:
            temp = "<font color='#FF00FF'>如影随形</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += " [如来神掌]<br>"
            temp += "在地面施放时跳跃后发射掌风<br>"
            temp += "掌风变更为无形状， 删除爆炸攻击<br>"
            temp += "增加发射距离和速度<br>"
            temp += "掌风发射准备时间 -50%<br>"
            temp += "攻击范围 +50%<br>"
            temp += "命中敌人时攻击力 +171% <br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "可以在后跳过程中施放， 减少施放所需的最低高度<br>"
            temp += "在地面施放时， 减少角色跳跃高度<br>"
            temp += "施放掌风后的僵直时间 -30%<br>"
            temp += "命中敌人时攻击力 +25%"
        elif x == 1:
            temp = "<font color='#FF00FF'>如影随形</font>"
            temp += "<br><br><font color='#68D5ED'>"
            temp += " [如来神掌]<br>"
            temp += "在地面施放时跳跃后发射掌风<br>"
            temp += "掌风变更为无形状， 删除爆炸攻击<br>"
            temp += "增加发射距离和速度<br>"
            temp += "掌风发射准备时间 -50%<br>"
            temp += "攻击范围 +50%<br>"
            temp += "命中敌人时攻击力 +171% <br>"
            temp += "<br>-护石附加效果：<br>"
            temp += "可以在后跳过程中施放， 减少施放所需的最低高度<br>"
            temp += "在地面施放时， 减少角色跳跃高度<br>"
            temp += "施放掌风后的僵直时间 -30%<br>"
            temp += "命中敌人时攻击力 +45%"
        return temp  
            
class 极诣·流浪武士技能17(极诣·流浪武士主动技能):
    名称 = '莲花剑舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    CD = 40.0
    data1 = [0, 2717.0, 2992.0, 3268.0, 3545.0, 3819.0, 4095.0, 4370.0, 4647.0, 4921.0, 5197.0, 5473.0, 5749.0, 6023.0, 6300.0, 6575.0, 6852.0, 7129.0, 7404.0, 7677.0, 7954.0, 8229.0, 8503.0, 8783.0, 9058.0, 9332.0, 9606.0, 9882.0, 10157.0, 10433.0, 10712.0, 10986.0, 11260.0, 11538.0, 11811.0, 12087.0, 12362.0, 12640.0, 12914.0, 13192.0, 13466.0, 13741.0, 14015.0, 14295.0, 14570.0, 14844.0, 15122.0, 15395.0, 15670.0, 15947.0, 16225.0, 16498.0, 16775.0, 17050.0, 17324.0, 17602.0, 17875.0, 18153.0, 18430.0, 18705.0, 18978.0, 19253.0, 19530.0, 19805.0, 20082.0, 20358.0, 20634.0, 20907.0, 21184.0, 21459.0, 21733.0]
    data2 = [0, 4075.0, 4488.0, 4901.0, 5315.0, 5728.0, 6144.0, 6556.0, 6969.0, 7382.0, 7795.0, 8209.0, 8623.0, 9037.0, 9449.0, 9863.0, 10277.0, 10689.0, 11103.0, 11518.0, 11932.0, 12343.0, 12756.0, 13173.0, 13586.0, 13997.0, 14413.0, 14827.0, 15237.0, 15653.0, 16066.0, 16481.0, 16889.0, 17304.0, 17717.0, 18129.0, 18545.0, 18958.0, 19373.0, 19784.0, 20198.0, 20614.0, 21027.0, 21438.0, 21853.0, 22268.0, 22678.0, 23093.0, 23508.0, 23921.0, 24333.0, 24749.0, 25162.0, 25574.0, 25988.0, 26401.0, 26816.0, 27228.0, 27642.0, 28055.0, 28470.0, 28882.0, 29295.0, 29709.0, 30123.0, 30536.0, 30949.0, 31365.0, 31774.0, 32189.0, 32603.0]
    data3 = [0, 4075.0, 4488.0, 4901.0, 5315.0, 5728.0, 6144.0, 6556.0, 6969.0, 7382.0, 7795.0, 8209.0, 8623.0, 9037.0, 9449.0, 9863.0, 10277.0, 10689.0, 11103.0, 11518.0, 11932.0, 12343.0, 12756.0, 13173.0, 13586.0, 13997.0, 14413.0, 14827.0, 15237.0, 15653.0, 16066.0, 16481.0, 16889.0, 17304.0, 17717.0, 18129.0, 18545.0, 18958.0, 19373.0, 19784.0, 20198.0, 20614.0, 21027.0, 21438.0, 21853.0, 22268.0, 22678.0, 23093.0, 23508.0, 23921.0, 24333.0, 24749.0, 25162.0, 25574.0, 25988.0, 26401.0, 26816.0, 27228.0, 27642.0, 28055.0, 28470.0, 28882.0, 29295.0, 29709.0, 30123.0, 30536.0, 30949.0, 31365.0, 31774.0, 32189.0, 32603.0]
    data4 = [0, 16301.0, 17956.0, 19609.0, 21264.0, 22917.0, 24570.0, 26224.0, 27877.0, 29532.0, 31185.0, 32839.0, 34492.0, 36146.0, 37800.0, 39454.0, 41109.0, 42760.0, 44414.0, 46067.0, 47724.0, 49378.0, 51028.0, 52683.0, 54339.0, 55992.0, 57644.0, 59298.0, 60953.0, 62605.0, 64259.0, 65913.0, 67568.0, 69221.0, 70875.0, 72528.0, 74182.0, 75836.0, 77490.0, 79142.0, 80796.0, 82451.0, 84106.0, 85759.0, 87411.0, 89067.0, 90717.0, 92371.0, 94028.0, 95682.0, 97335.0, 98989.0, 100644.0, 102296.0, 103949.0, 105603.0, 107255.0, 108910.0, 110564.0, 112217.0, 113872.0, 115528.0, 117179.0, 118832.0, 120485.0, 122140.0, 123793.0, 125448.0, 127103.0, 128757.0, 130410.0]
    数据 = [data1, data2, data3, data4]
    次数 = [2, 2, 2, 2]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率 

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33

class 极诣·流浪武士技能18(极诣·流浪武士主动技能):
    名称 = '樱花劫'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    CD = 45.0
    数据 = [0, 64519.0, 71064.0, 77606.0, 84153.0, 90698.0, 97245.0, 103790.0, 110336.0, 116880.0, 123428.0, 129972.0, 136519.0, 143063.0, 149607.0, 156153.0, 162700.0, 169244.0, 175792.0, 182334.0, 188881.0, 195427.0, 201972.0, 208519.0, 215064.0, 221607.0, 228153.0, 234698.0, 241246.0, 247789.0, 254336.0, 260880.0, 267428.0, 273972.0, 280519.0, 287062.0, 293608.0, 300152.0, 306699.0, 313244.0, 319789.0, 326335.0, 332881.0, 339427.0, 345973.0, 352516.0, 359064.0, 365608.0, 372150.0, 378697.0, 385242.0, 391788.0, 398335.0, 404880.0, 411424.0, 417972.0, 424516.0, 431063.0, 437607.0, 444152.0, 450696.0, 457244.0, 463788.0, 470334.0, 476878.0, 483425.0, 489971.0, 496516.0, 503062.0, 509608.0, 516153.0]
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35
            self.CD *= 0.9

class 极诣·流浪武士技能19(极诣·流浪武士主动技能):
    名称 = '飞花逐月'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    CD = 180.0
    data1 = [0, 3322.0, 4092.0, 4862.0, 5633.0, 6403.0, 7173.0, 7944.0, 8711.0, 9483.0, 10254.0, 11024.0, 11793.0, 12563.0, 13335.0, 14105.0, 14873.0, 15646.0, 16413.0, 17184.0, 17956.0, 18724.0, 19496.0, 20267.0, 21033.0, 21806.0, 22576.0, 23345.0, 24116.0, 24886.0, 25657.0, 26426.0, 27196.0, 27966.0, 28737.0, 29508.0, 30280.0, 31046.0, 31817.0, 32588.0, 33358.0, 34128.0, 34899.0, 35667.0, 36439.0, 37209.0, 37979.0, 38749.0, 39520.0, 40288.0, 41059.0, 41829.0, 42600.0, 43369.0, 44141.0, 44909.0, 45679.0, 46452.0, 47219.0, 47990.0, 48762.0, 49529.0, 50301.0, 51072.0, 51842.0, 52613.0, 53382.0, 54151.0, 54922.0, 55691.0, 56463.0]
    data2 = [0, 69749.0, 85921.0, 102096.0, 118267.0, 134441.0, 150617.0, 166789.0, 182963.0, 199135.0, 215308.0, 231483.0, 247656.0, 263830.0, 280002.0, 296178.0, 312352.0, 328523.0, 344698.0, 360870.0, 377046.0, 393217.0, 409391.0, 425565.0, 441739.0, 457912.0, 474085.0, 490260.0, 506434.0, 522604.0, 538781.0, 554953.0, 571125.0, 587298.0, 603473.0, 619648.0, 635821.0, 651995.0, 668167.0, 684340.0, 700515.0, 716687.0, 732860.0, 749034.0, 765208.0, 781385.0, 797555.0, 813728.0, 829901.0, 846076.0, 862249.0, 878423.0, 894598.0, 910768.0, 926942.0, 943113.0, 959290.0, 975463.0, 991637.0, 1007811.0, 1023985.0, 1040159.0, 1056329.0, 1072502.0, 1088676.0, 1104851.0, 1121025.0, 1137197.0, 1153372.0, 1169546.0, 1185715.0]
    数据 = [data1, data2]
    次数 = [20, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率    

class 极诣·流浪武士技能20(极诣·流浪武士主动技能):
    名称 = '落英惊鸿掌'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    CD = 60.0
    data1 = [0, 10545.0, 11615.0, 12684.0, 13754.0, 14824.0, 15894.0, 16964.0, 18034.0, 19103.0, 20173.0, 21243.0, 22313.0, 23383.0, 24453.0, 25522.0, 26592.0, 27662.0, 28732.0, 29802.0, 30871.0, 31941.0, 33011.0, 34081.0, 35151.0, 36221.0, 37290.0, 38360.0, 39430.0, 40500.0, 41570.0, 42639.0, 43709.0, 44779.0, 45849.0, 46919.0, 47989.0, 49058.0, 50128.0, 51198.0, 52268.0]
    data2 = [0, 5272.0, 5807.0, 6342.0, 6877.0, 7412.0, 7947.0, 8482.0, 9017.0, 9551.0, 10086.0, 10621.0, 11156.0, 11691.0, 12226.0, 12761.0, 13296.0, 13831.0, 14366.0, 14901.0, 15435.0, 15970.0, 16505.0, 17040.0, 17575.0, 18110.0, 18645.0, 19180.0, 19715.0, 20250.0, 20785.0, 21319.0, 21854.0, 22389.0, 22924.0, 23459.0, 23994.0, 24529.0, 25064.0, 25599.0, 26134.0]
    data3 = [0, 73817.0, 81306.0, 88794.0, 96283.0, 103772.0, 111261.0, 118749.0, 126238.0, 133727.0, 141216.0, 148704.0, 156193.0, 163682.0, 171171.0, 178659.0, 186148.0, 193637.0, 201125.0, 208614.0, 216103.0, 223592.0, 231080.0, 238569.0, 246058.0, 253547.0, 261035.0, 268524.0, 276013.0, 283501.0, 290990.0, 298479.0, 305968.0, 313456.0, 320945.0, 328434.0, 335923.0, 343411.0, 350900.0, 358389.0, 365878.0]
    数据 = [data1, data2, data3]
    次数 = [1, 4, 1]
    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.次数)):
            sum += self.数据[i][self.等级] * self.次数[i]
        return sum * self.倍率 

class 极诣·流浪武士技能21(极诣·流浪武士主动技能):
    名称 = '轻云出月风静夜'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    CD = 290.0
    数据 = [0, 384840.0, 474079.0, 563317.0, 652556.0, 741794.0, 831033.0, 920271.0, 1009510.0, 1098748.0, 1187987.0, 1277225.0, 1366464.0, 1455702.0, 1544941.0, 1634179.0, 1723418.0, 1812656.0, 1901895.0, 1991133.0, 2080372.0, 2169610.0, 2258849.0, 2348087.0, 2437326.0, 2526564.0, 2615803.0, 2705041.0, 2794280.0, 2883518.0, 2972757.0, 3061995.0, 3151234.0, 3240472.0, 3329711.0, 3418949.0, 3508188.0, 3597426.0, 3686665.0, 3775903.0, 3865142.0]
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.倍率

    关联技能 = ['无']
    def 加成倍率(self, 武器类型):
        return 0.0

极诣·流浪武士技能列表 = []
i = 0
while i >= 0:
    try:
        exec('极诣·流浪武士技能列表.append(极诣·流浪武士技能'+str(i)+'())')
        i += 1
    except:
        i = -1

极诣·流浪武士技能序号 = dict()
for i in range(len(极诣·流浪武士技能列表)):
    极诣·流浪武士技能序号[极诣·流浪武士技能列表[i].名称] = i

极诣·流浪武士一觉序号 = 0
极诣·流浪武士二觉序号 = 0
极诣·流浪武士三觉序号 = 0
for i in 极诣·流浪武士技能列表:
    if i.所在等级 == 50:
        极诣·流浪武士一觉序号 = 极诣·流浪武士技能序号[i.名称]
    if i.所在等级 == 85:
        极诣·流浪武士二觉序号 = 极诣·流浪武士技能序号[i.名称]
    if i.所在等级 == 100:
        极诣·流浪武士三觉序号 = 极诣·流浪武士技能序号[i.名称]

极诣·流浪武士护石选项 = ['无']
for i in 极诣·流浪武士技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        极诣·流浪武士护石选项.append(i.名称)

极诣·流浪武士符文选项 = ['无']
for i in 极诣·流浪武士技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        极诣·流浪武士符文选项.append(i.名称)

class 极诣·流浪武士角色属性(角色属性):

    实际名称 = '极诣·流浪武士'
    角色 = '鬼剑士(女)'
    职业 = '流浪武士'

    武器选项 = ['光剑','巨剑','钝器','太刀','短剑']
    
    伤害类型选择 = ['物理百分比']
    
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.25
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(极诣·流浪武士技能列表)
        self.技能序号= deepcopy(极诣·流浪武士技能序号)

class 极诣·流浪武士(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 极诣·流浪武士角色属性()
        self.角色属性A = 极诣·流浪武士角色属性()
        self.角色属性B = 极诣·流浪武士角色属性()
        self.一觉序号 = 极诣·流浪武士一觉序号
        self.二觉序号 = 极诣·流浪武士二觉序号
        self.三觉序号 = 极诣·流浪武士三觉序号
        self.护石选项 = deepcopy(极诣·流浪武士护石选项)
        self.符文选项 = deepcopy(极诣·流浪武士符文选项)
