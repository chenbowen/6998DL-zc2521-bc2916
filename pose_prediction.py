# predicting slouch

import numpy as np
import serial
import csv
import random
import time
import math

fieldnames = ["x_val", "y1"]
            
data = {}
data["x_val"] = [i for i in range(100)]
data["y1"] = [0 for i in range(100)]

# plt.style.use('fivethirtyeight')

SINGLE_POINT_THRES = 0 # 低通的滤波
THRES = 300000


def score_solo_itchy_1(input):
    if (input[146]) >= (1540.5):
        if (input[141]) >= (1594.5):
            if (input[153]) >= (2073.0):
                var0 = 0.14074074
            else:
                var0 = -0.18285714
        else:
            if (input[47]) >= (2439.5):
                var0 = -0.17419355
            else:
                var0 = 0.13664596
    else:
        if (input[233]) >= (1940.5):
            var0 = 0.14782609
        else:
            if (input[7]) >= (2313.5):
                var0 = -0.05
            else:
                var0 = -0.19751553
    if (input[146]) >= (1540.5):
        if (input[220]) >= (1844.5):
            var1 = 0.18128735
        else:
            if (input[141]) >= (1577.0):
                var1 = -0.10640036
            else:
                var1 = 0.06084288
    else:
        if (input[233]) >= (1940.5):
            var1 = 0.13624923
        else:
            if (input[39]) >= (1773.0):
                var1 = -0.057613313
            else:
                var1 = -0.17990917
    if (input[146]) >= (1537.5):
        if (input[2]) >= (2072.0):
            if (input[96]) >= (1895.5):
                var2 = -0.1549234
            else:
                var2 = 0.15280169
        else:
            if (input[55]) >= (1328.0):
                var2 = -0.06420814
            else:
                var2 = 0.16535626
    else:
        if (input[233]) >= (1965.5):
            var2 = 0.14133924
        else:
            if (input[45]) >= (1204.5):
                var2 = -0.16680332
            else:
                var2 = -0.05418135
    if (input[146]) >= (1537.5):
        if (input[199]) >= (1302.5):
            if (input[121]) >= (1272.5):
                var3 = 0.02471949
            else:
                var3 = 0.15004922
        else:
            if (input[9]) >= (1284.0):
                var3 = 0.02884451
            else:
                var3 = -0.16716115
    else:
        if (input[233]) >= (1965.5):
            var3 = 0.13269377
        else:
            if (input[80]) >= (2432.5):
                var3 = -0.04714852
            else:
                var3 = -0.1563651
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var4 = 0.15078484
        else:
            if (input[156]) >= (2333.0):
                var4 = -0.1299178
            else:
                var4 = 0.0364228
    else:
        if (input[233]) >= (1940.5):
            var4 = 0.11322641
        else:
            var4 = -0.14785415
    if (input[199]) >= (1302.5):
        if (input[162]) >= (1566.0):
            if (input[168]) >= (1468.0):
                var5 = -0.060972333
            else:
                var5 = 0.117545545
        else:
            if (input[23]) >= (2158.0):
                var5 = 0.078378364
            else:
                var5 = -0.08861407
    else:
        if (input[59]) >= (1612.0):
            if (input[119]) >= (2446.5):
                var5 = -0.03219013
            else:
                var5 = -0.14576285
        else:
            var5 = 0.04263814
    if (input[199]) >= (1302.5):
        if (input[208]) >= (1271.5):
            if (input[215]) >= (1490.0):
                var6 = 0.03950284
            else:
                var6 = 0.14277034
        else:
            if (input[172]) >= (2050.5):
                var6 = 0.11051009
            else:
                var6 = -0.033754256
    else:
        if (input[59]) >= (1612.0):
            if (input[119]) >= (2446.5):
                var6 = -0.030688727
            else:
                var6 = -0.13935338
        else:
            var6 = 0.04056857
    if (input[146]) >= (1540.5):
        if (input[141]) >= (1594.5):
            if (input[153]) >= (2073.0):
                var7 = 0.11714182
            else:
                var7 = -0.1435699
        else:
            if (input[47]) >= (2439.5):
                var7 = -0.14585069
            else:
                var7 = 0.090354376
    else:
        if (input[233]) >= (1965.5):
            var7 = 0.11827606
        else:
            if (input[88]) >= (1857.0):
                var7 = -0.03112868
            else:
                var7 = -0.13182479
    if (input[199]) >= (1301.5):
        if (input[208]) >= (1271.5):
            if (input[125]) >= (2001.5):
                var8 = 0.033461045
            else:
                var8 = 0.1327476
        else:
            if (input[116]) >= (1858.5):
                var8 = 0.018290073
            else:
                var8 = -0.13729766
    else:
        if (input[59]) >= (1612.0):
            var8 = -0.13016775
        else:
            var8 = 0.034073535
    if (input[2]) >= (1874.5):
        if (input[244]) >= (1183.5):
            if (input[87]) >= (1441.5):
                var9 = -0.11953332
            else:
                var9 = 0.12202497
        else:
            if (input[130]) >= (1560.5):
                var9 = 0.12217499
            else:
                var9 = -0.091962576
    else:
        if (input[108]) >= (2136.0):
            var9 = 0.13775733
        else:
            if (input[11]) >= (1255.5):
                var9 = -0.12031958
            else:
                var9 = 0.0955112
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var10 = 0.12493658
        else:
            if (input[156]) >= (2328.5):
                var10 = -0.10874301
            else:
                var10 = 0.028695166
    else:
        if (input[233]) >= (1940.5):
            var10 = 0.0968484
        else:
            var10 = -0.1222569
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1384.5):
            if (input[86]) >= (1946.0):
                var11 = 0.044420134
            else:
                var11 = -0.12826292
        else:
            if (input[141]) >= (1593.5):
                var11 = -0.0182782
            else:
                var11 = 0.12353338
    else:
        if (input[59]) >= (1612.0):
            var11 = -0.12116635
        else:
            var11 = 0.030653879
    if (input[2]) >= (1874.5):
        if (input[244]) >= (1183.5):
            if (input[87]) >= (1441.5):
                var12 = -0.1046166
            else:
                var12 = 0.11062057
        else:
            if (input[130]) >= (1560.5):
                var12 = 0.11151331
            else:
                var12 = -0.079906695
    else:
        if (input[108]) >= (2136.0):
            var12 = 0.12569241
        else:
            if (input[193]) >= (1924.0):
                var12 = 0.09066246
            else:
                var12 = -0.11109743
    if (input[199]) >= (1301.5):
        if (input[208]) >= (1271.5):
            if (input[71]) >= (1459.5):
                var13 = 0.032828
            else:
                var13 = 0.11726604
        else:
            if (input[107]) >= (2119.0):
                var13 = 0.10531489
            else:
                var13 = -0.021670226
    else:
        if (input[59]) >= (1612.0):
            var13 = -0.11606585
        else:
            var13 = 0.03114059
    if (input[2]) >= (1874.5):
        if (input[244]) >= (1183.5):
            if (input[87]) >= (1441.5):
                var14 = -0.09715478
            else:
                var14 = 0.10647483
        else:
            if (input[130]) >= (1560.5):
                var14 = 0.10539873
            else:
                var14 = -0.07337112
    else:
        if (input[108]) >= (2136.0):
            var14 = 0.11768611
        else:
            if (input[50]) >= (2437.5):
                var14 = 0.042303823
            else:
                var14 = -0.11172175
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var15 = 0.11370092
        else:
            if (input[23]) >= (2158.0):
                var15 = 0.08975299
            else:
                var15 = -0.02427959
    else:
        if (input[233]) >= (1940.5):
            var15 = 0.0841798
        else:
            var15 = -0.11218067
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1384.5):
            if (input[86]) >= (1946.0):
                var16 = 0.03489633
            else:
                var16 = -0.11443869
        else:
            if (input[141]) >= (1593.5):
                var16 = -0.010425812
            else:
                var16 = 0.112185
    else:
        if (input[60]) >= (1704.0):
            var16 = -0.11082979
        else:
            var16 = 0.018218176
    if (input[2]) >= (2087.5):
        if (input[168]) >= (1461.5):
            if (input[256]) >= (10.5):
                var17 = 0.04449187
            else:
                var17 = -0.1286668
        else:
            if (input[132]) >= (2280.0):
                var17 = 0.11588857
            else:
                var17 = -0.04127687
    else:
        if (input[108]) >= (2122.5):
            if (input[128]) >= (1599.0):
                var17 = 0.11788225
            else:
                var17 = -0.028620273
        else:
            if (input[23]) >= (2198.0):
                var17 = 0.041402895
            else:
                var17 = -0.093978964
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var18 = 0.10813426
        else:
            if (input[55]) >= (1328.5):
                var18 = -0.017887108
            else:
                var18 = 0.11410085
    else:
        if (input[233]) >= (1940.5):
            var18 = 0.07900361
        else:
            var18 = -0.10836754
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1384.5):
            if (input[86]) >= (1940.0):
                var19 = 0.030586993
            else:
                var19 = -0.10838171
        else:
            if (input[156]) >= (2437.5):
                var19 = -0.061300922
            else:
                var19 = 0.09734156
    else:
        if (input[60]) >= (1704.0):
            var19 = -0.1069242
        else:
            var19 = 0.015602774
    if (input[2]) >= (1874.5):
        if (input[244]) >= (1183.5):
            if (input[256]) >= (23.5):
                var20 = 0.10484301
            else:
                var20 = -0.08211763
        else:
            if (input[130]) >= (1560.5):
                var20 = 0.092168026
            else:
                var20 = -0.055026423
    else:
        if (input[119]) >= (1296.5):
            if (input[196]) >= (1172.5):
                var20 = -0.11493895
            else:
                var20 = 0.061773956
        else:
            if (input[48]) >= (1468.5):
                var20 = 0.07103275
            else:
                var20 = -0.09146489
    if (input[2]) >= (1874.5):
        if (input[244]) >= (1183.5):
            if (input[87]) >= (1441.5):
                var21 = -0.080543816
            else:
                var21 = 0.0932708
        else:
            if (input[130]) >= (1560.5):
                var21 = 0.08818596
            else:
                var21 = -0.05264018
    else:
        if (input[119]) >= (1296.5):
            if (input[88]) >= (1793.5):
                var21 = 0.038724508
            else:
                var21 = -0.11413405
        else:
            if (input[48]) >= (1468.5):
                var21 = 0.06575327
            else:
                var21 = -0.08857349
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var22 = 0.10332388
        else:
            if (input[156]) >= (2316.5):
                var22 = -0.07682585
            else:
                var22 = 0.022916853
    else:
        if (input[233]) >= (1940.5):
            var22 = 0.07134669
        else:
            var22 = -0.10426779
    if (input[199]) >= (1301.5):
        if (input[208]) >= (1271.5):
            var23 = 0.0986897
        else:
            if (input[123]) >= (1739.5):
                var23 = 0.045234516
            else:
                var23 = -0.035130728
    else:
        if (input[60]) >= (1778.0):
            var23 = -0.10244957
        else:
            var23 = 0.008825931
    if (input[2]) >= (2087.5):
        if (input[168]) >= (1468.0):
            if (input[256]) >= (19.5):
                var24 = 0.09610921
            else:
                var24 = -0.09779759
        else:
            if (input[96]) >= (1881.5):
                var24 = -0.04624085
            else:
                var24 = 0.10297736
    else:
        if (input[108]) >= (2122.5):
            if (input[160]) >= (1374.0):
                var24 = 0.10491826
            else:
                var24 = -0.013491887
        else:
            if (input[23]) >= (2203.5):
                var24 = 0.04187034
            else:
                var24 = -0.08352925
    if (input[146]) >= (1537.5):
        if (input[1]) >= (1293.5):
            if (input[51]) >= (1108.5):
                var25 = -0.07183447
            else:
                var25 = 0.08413709
        else:
            if (input[204]) >= (1455.0):
                var25 = 0.027574284
            else:
                var25 = -0.08114723
    else:
        if (input[233]) >= (1965.5):
            var25 = 0.07676806
        else:
            var25 = -0.100272775
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1384.5):
            if (input[22]) >= (1702.5):
                var26 = 0.035938002
            else:
                var26 = -0.08088766
        else:
            if (input[141]) >= (1593.5):
                var26 = -0.015487507
            else:
                var26 = 0.095737286
    else:
        if (input[59]) >= (1654.5):
            var26 = -0.0991235
        else:
            var26 = 0.0067480817
    if (input[32]) >= (1252.5):
        if (input[168]) >= (1468.0):
            if (input[256]) >= (19.5):
                var27 = 0.071975484
            else:
                var27 = -0.10179521
        else:
            if (input[44]) >= (1829.0):
                var27 = 0.016325008
            else:
                var27 = 0.10611474
    else:
        if (input[249]) >= (1228.5):
            if (input[139]) >= (2056.0):
                var27 = 0.09240898
            else:
                var27 = -0.061575484
        else:
            if (input[79]) >= (2199.0):
                var27 = 0.07007001
            else:
                var27 = -0.09243581
    if (input[146]) >= (1537.5):
        if (input[220]) >= (1844.5):
            var28 = 0.09664737
        else:
            if (input[55]) >= (1328.5):
                var28 = -0.014921158
            else:
                var28 = 0.093763806
    else:
        if (input[233]) >= (1965.5):
            var28 = 0.0712937
        else:
            var28 = -0.09766521
    if (input[146]) >= (1537.5):
        if (input[65]) >= (2243.0):
            var29 = -0.09798729
        else:
            if (input[156]) >= (2316.5):
                var29 = -0.039591294
            else:
                var29 = 0.047423773
    else:
        if (input[233]) >= (1940.5):
            var29 = 0.060475904
        else:
            var29 = -0.098237745
    if (input[2]) >= (2087.5):
        if (input[156]) >= (2333.5):
            if (input[256]) >= (22.5):
                var30 = 0.09674652
            else:
                var30 = -0.08629625
        else:
            if (input[99]) >= (999.5):
                var30 = 0.10487866
            else:
                var30 = -0.011306985
    else:
        if (input[108]) >= (2122.5):
            if (input[128]) >= (1612.0):
                var30 = 0.09601794
            else:
                var30 = -0.0021563703
        else:
            if (input[23]) >= (2203.5):
                var30 = 0.041177463
            else:
                var30 = -0.076996
    if (input[199]) >= (1301.5):
        if (input[208]) >= (1271.5):
            var31 = 0.090423964
        else:
            if (input[123]) >= (1739.5):
                var31 = 0.04050068
            else:
                var31 = -0.030811852
    else:
        if (input[256]) >= (29.5):
            var31 = 0.0027550592
        else:
            var31 = -0.09514027
    if (input[60]) >= (1452.5):
        if (input[77]) >= (2358.0):
            if (input[7]) >= (1432.5):
                var32 = 0.09884985
            else:
                var32 = -0.037438974
        else:
            if (input[204]) >= (1354.5):
                var32 = -0.001773593
            else:
                var32 = -0.08066289
    else:
        if (input[256]) >= (11.5):
            var32 = 0.10687391
        else:
            var32 = -0.047817886
    if (input[60]) >= (1452.5):
        if (input[77]) >= (2358.0):
            if (input[50]) >= (1464.5):
                var33 = 0.09639744
            else:
                var33 = -0.03614847
        else:
            if (input[108]) >= (2122.5):
                var33 = 0.07360034
            else:
                var33 = -0.044508275
    else:
        if (input[256]) >= (11.5):
            var33 = 0.10438713
        else:
            var33 = -0.044263452
    if (input[32]) >= (1251.5):
        if (input[168]) >= (1468.0):
            if (input[256]) >= (19.5):
                var34 = 0.06482165
            else:
                var34 = -0.0953392
        else:
            if (input[57]) >= (1571.0):
                var34 = -0.008318896
            else:
                var34 = 0.07838326
    else:
        if (input[249]) >= (1229.5):
            if (input[139]) >= (2056.0):
                var34 = 0.09781954
            else:
                var34 = -0.049427357
        else:
            if (input[79]) >= (2189.5):
                var34 = 0.058126807
            else:
                var34 = -0.08425708
    if (input[208]) >= (1271.5):
        var35 = 0.08701838
    else:
        if (input[11]) >= (1250.0):
            if (input[156]) >= (2037.0):
                var35 = 0.002536999
            else:
                var35 = -0.08302623
        else:
            var35 = 0.087543696
    if (input[146]) >= (1537.5):
        if (input[187]) >= (1261.5):
            if (input[82]) >= (1757.5):
                var36 = 0.08962751
            else:
                var36 = -0.06696453
        else:
            if (input[85]) >= (1209.5):
                var36 = -0.06283151
            else:
                var36 = 0.027991632
    else:
        if (input[233]) >= (1965.5):
            var36 = 0.061583627
        else:
            var36 = -0.0914528
    if (input[208]) >= (1271.5):
        var37 = 0.08429133
    else:
        if (input[11]) >= (1250.0):
            if (input[51]) >= (1088.5):
                var37 = 0.00021534249
            else:
                var37 = -0.08092697
        else:
            var37 = 0.08498367
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1384.5):
            if (input[86]) >= (1946.0):
                var38 = 0.023497451
            else:
                var38 = -0.08839165
        else:
            if (input[104]) >= (1416.0):
                var38 = -0.04075342
            else:
                var38 = 0.081671864
    else:
        if (input[60]) >= (1828.5):
            var38 = -0.08978694
        else:
            var38 = 0.0034910142
    if (input[130]) >= (1667.0):
        if (input[85]) >= (1209.5):
            if (input[25]) >= (1590.0):
                var39 = 0.05534343
            else:
                var39 = -0.0760799
        else:
            if (input[141]) >= (1592.5):
                var39 = -0.06250688
            else:
                var39 = 0.06770146
    else:
        if (input[145]) >= (1554.5):
            if (input[156]) >= (2059.0):
                var39 = 0.080008425
            else:
                var39 = -0.057900067
        else:
            if (input[256]) >= (29.5):
                var39 = -0.021294465
            else:
                var39 = -0.09762747
    if (input[146]) >= (1537.5):
        if (input[187]) >= (1273.5):
            if (input[82]) >= (1757.5):
                var40 = 0.09145082
            else:
                var40 = -0.061816406
        else:
            if (input[55]) >= (1384.5):
                var40 = -0.031345192
            else:
                var40 = 0.05605937
    else:
        if (input[233]) >= (1940.5):
            var40 = 0.04929318
        else:
            var40 = -0.090479076
    if (input[60]) >= (1452.5):
        if (input[103]) >= (1956.5):
            var41 = 0.07916364
        else:
            if (input[105]) >= (1497.5):
                var41 = 0.03490306
            else:
                var41 = -0.046256613
    else:
        if (input[256]) >= (11.5):
            var41 = 0.09878961
        else:
            var41 = -0.057250638
    if (input[32]) >= (1252.5):
        if (input[168]) >= (1459.5):
            if (input[256]) >= (15.5):
                var42 = 0.03339188
            else:
                var42 = -0.095246695
        else:
            if (input[35]) >= (1042.5):
                var42 = -0.018282196
            else:
                var42 = 0.07606969
    else:
        if (input[249]) >= (1229.5):
            if (input[139]) >= (2056.0):
                var42 = 0.08877378
            else:
                var42 = -0.04225498
        else:
            if (input[79]) >= (2189.5):
                var42 = 0.047794327
            else:
                var42 = -0.07258482
    if (input[208]) >= (1271.5):
        var43 = 0.07831886
    else:
        if (input[204]) >= (1414.0):
            if (input[204]) >= (1642.0):
                var43 = -0.03619214
            else:
                var43 = 0.05612392
        else:
            if (input[23]) >= (2192.0):
                var43 = 0.03242747
            else:
                var43 = -0.086064406
    if (input[146]) >= (1537.5):
        if (input[156]) >= (2323.5):
            if (input[256]) >= (23.5):
                var44 = 0.06366872
            else:
                var44 = -0.07792961
        else:
            if (input[2]) >= (2087.5):
                var44 = 0.096307695
            else:
                var44 = -0.0009996531
    else:
        if (input[233]) >= (1940.5):
            var44 = 0.04356626
        else:
            var44 = -0.087648965
    if (input[34]) >= (2019.5):
        if (input[50]) >= (1770.5):
            if (input[44]) >= (1598.0):
                var45 = -0.027228305
            else:
                var45 = 0.07981303
        else:
            if (input[80]) >= (1264.0):
                var45 = 0.09547692
            else:
                var45 = -0.010292556
    else:
        if (input[55]) >= (1445.5):
            var45 = -0.09372314
        else:
            if (input[112]) >= (1967.0):
                var45 = 0.052853882
            else:
                var45 = -0.05952039
    var46 = (((((((((((((((((((((((((((((((((((((((((((((var0) + (var1)) + (var2)) + (var3)) + (var4)) + (var5)) + (var6)) + (var7)) + (var8)) + (var9)) + (var10)) + (var11)) + (var12)) + (var13)) + (var14)) + (var15)) + (var16)) + (var17)) + (var18)) + (var19)) + (var20)) + (var21)) + (var22)) + (var23)) + (var24)) + (var25)) + (var26)) + (var27)) + (var28)) + (var29)) + (var30)) + (var31)) + (var32)) + (var33)) + (var34)) + (var35)) + (var36)) + (var37)) + (var38)) + (var39)) + (var40)) + (var41)) + (var42)) + (var43)) + (var44)) + (var45)
    if (input[220]) >= (1844.5):
        if (input[132]) >= (2437.5):
            var47 = 0.08144367
        else:
            var47 = 0.010756711
    else:
        if (input[23]) >= (2178.0):
            if (input[256]) >= (11.5):
                var47 = -0.035272136
            else:
                var47 = 0.10006153
        else:
            if (input[55]) >= (1545.0):
                var47 = -0.0953783
            else:
                var47 = 0.0034013446
    if (input[199]) >= (1301.5):
        if (input[198]) >= (2443.5):
            if (input[124]) >= (2436.5):
                var48 = 0.0504297
            else:
                var48 = -0.081092
        else:
            if (input[79]) >= (1218.5):
                var48 = 0.0053467457
            else:
                var48 = 0.078180276
    else:
        if (input[256]) >= (28.5):
            var48 = -0.00024801077
        else:
            var48 = -0.08271323
    if (input[208]) >= (1271.5):
        var49 = 0.07249373
    else:
        if (input[23]) >= (2192.0):
            if (input[256]) >= (11.5):
                var49 = -0.030498803
            else:
                var49 = 0.096502
        else:
            if (input[204]) >= (1402.5):
                var49 = 0.0055444418
            else:
                var49 = -0.08143571
    if (input[11]) >= (1258.0):
        if (input[51]) >= (1088.5):
            if (input[86]) >= (1955.5):
                var50 = 0.0376525
            else:
                var50 = -0.044157464
        else:
            if (input[55]) >= (1327.5):
                var50 = -0.089395046
            else:
                var50 = 0.033598308
    else:
        var50 = 0.076095365
    if (input[220]) >= (1844.5):
        if (input[81]) >= (1749.0):
            var51 = 0.077675834
        else:
            var51 = 0.015699344
    else:
        if (input[156]) >= (2333.0):
            if (input[256]) >= (23.5):
                var51 = 0.043010224
            else:
                var51 = -0.09390285
        else:
            if (input[2]) >= (2157.0):
                var51 = 0.08693719
            else:
                var51 = -0.013506265
    if (input[199]) >= (1301.5):
        if (input[55]) >= (1328.5):
            if (input[51]) >= (1088.5):
                var52 = 0.022436557
            else:
                var52 = -0.080540314
        else:
            if (input[71]) >= (1210.5):
                var52 = 0.013048905
            else:
                var52 = 0.08606381
    else:
        if (input[60]) >= (1963.5):
            var52 = -0.07788272
        else:
            var52 = -0.0027058662
    if (input[220]) >= (1844.5):
        if (input[80]) >= (1274.5):
            var53 = 0.07538105
        else:
            var53 = 0.017398894
    else:
        if (input[11]) >= (1258.0):
            if (input[15]) >= (1235.5):
                var53 = 0.0012699192
            else:
                var53 = -0.07360069
        else:
            var53 = 0.07019853
    if (input[44]) >= (1598.5):
        if (input[23]) >= (2178.0):
            if (input[256]) >= (11.5):
                var54 = -0.0339436
            else:
                var54 = 0.093061976
        else:
            if (input[162]) >= (1586.5):
                var54 = -0.0039619724
            else:
                var54 = -0.08709585
    else:
        if (input[29]) >= (1326.5):
            if (input[123]) >= (1733.5):
                var54 = 0.07092941
            else:
                var54 = -0.06992556
        else:
            var54 = 0.084939405
    if (input[220]) >= (1844.5):
        if (input[100]) >= (1674.5):
            var55 = 0.07320192
        else:
            var55 = 0.019159919
    else:
        if (input[156]) >= (2333.0):
            if (input[256]) >= (23.5):
                var55 = 0.042316433
            else:
                var55 = -0.08993038
        else:
            if (input[2]) >= (2157.0):
                var55 = 0.08373468
            else:
                var55 = -0.011056618
    if (input[249]) >= (1229.5):
        if (input[206]) >= (1258.0):
            var56 = -0.037480317
        else:
            var56 = 0.076676674
    else:
        if (input[114]) >= (2006.0):
            if (input[116]) >= (2235.0):
                var56 = -0.021493923
            else:
                var56 = 0.046585277
        else:
            if (input[60]) >= (1681.5):
                var56 = -0.088753626
            else:
                var56 = 0.012101969
    if (input[80]) >= (1266.5):
        if (input[124]) >= (2174.0):
            if (input[156]) >= (2333.5):
                var57 = -0.025819868
            else:
                var57 = 0.09212088
        else:
            if (input[20]) >= (1606.5):
                var57 = -0.062349338
            else:
                var57 = 0.06839491
    else:
        if (input[145]) >= (1351.5):
            if (input[139]) >= (1799.5):
                var57 = -0.09533368
            else:
                var57 = -0.026438043
        else:
            if (input[114]) >= (1999.0):
                var57 = 0.04343478
            else:
                var57 = -0.06689145
    if (input[220]) >= (1844.5):
        var58 = 0.0623597
    else:
        if (input[156]) >= (2323.5):
            if (input[256]) >= (23.5):
                var58 = 0.04392147
            else:
                var58 = -0.08666944
        else:
            if (input[204]) >= (1455.0):
                var58 = 0.04215555
            else:
                var58 = -0.025382403
    if (input[244]) >= (1182.5):
        if (input[87]) >= (1441.5):
            if (input[18]) >= (2435.5):
                var59 = 0.0057105394
            else:
                var59 = -0.08561271
        else:
            if (input[162]) >= (1629.0):
                var59 = 0.069001935
            else:
                var59 = -0.0016684094
    else:
        if (input[28]) >= (2441.5):
            if (input[60]) >= (1484.0):
                var59 = -0.070099466
            else:
                var59 = 0.056522936
        else:
            if (input[152]) >= (1606.0):
                var59 = -0.027752683
            else:
                var59 = 0.057389647
    if (input[80]) >= (1266.5):
        if (input[1]) >= (1293.5):
            if (input[167]) >= (2091.0):
                var60 = -0.043350127
            else:
                var60 = 0.08630721
        else:
            if (input[141]) >= (1963.5):
                var60 = 0.067226
            else:
                var60 = -0.057400625
    else:
        if (input[145]) >= (1351.5):
            var60 = -0.082402155
        else:
            if (input[114]) >= (1999.0):
                var60 = 0.04026751
            else:
                var60 = -0.06331897
    if (input[11]) >= (1258.0):
        if (input[115]) >= (1023.0):
            if (input[86]) >= (1955.5):
                var61 = 0.0287403
            else:
                var61 = -0.04020871
        else:
            var61 = -0.074768476
    else:
        var61 = 0.06596723
    if (input[80]) >= (1266.5):
        if (input[1]) >= (1293.5):
            if (input[167]) >= (2091.0):
                var62 = -0.040959753
            else:
                var62 = 0.083953865
        else:
            if (input[141]) >= (1963.5):
                var62 = 0.06396673
            else:
                var62 = -0.053564318
    else:
        if (input[33]) >= (2107.5):
            var62 = -0.078533694
        else:
            if (input[114]) >= (1999.0):
                var62 = 0.03245807
            else:
                var62 = -0.057513874
    if (input[44]) >= (1598.5):
        if (input[23]) >= (2178.0):
            if (input[256]) >= (11.5):
                var63 = -0.02990335
            else:
                var63 = 0.08409185
        else:
            if (input[11]) >= (1361.5):
                var63 = -0.06415498
            else:
                var63 = 0.017325884
    else:
        if (input[20]) >= (1876.0):
            if (input[83]) >= (1096.5):
                var63 = 0.06368192
            else:
                var63 = -0.044370547
        else:
            var63 = 0.08421992
    if (input[220]) >= (1844.5):
        var64 = 0.058627557
    else:
        if (input[11]) >= (1258.0):
            if (input[15]) >= (1235.5):
                var64 = 0.00080727536
            else:
                var64 = -0.06366595
        else:
            var64 = 0.059725013
    if (input[80]) >= (1264.0):
        if (input[84]) >= (2436.5):
            if (input[55]) >= (1328.0):
                var65 = -0.03571792
            else:
                var65 = 0.0715202
        else:
            if (input[68]) >= (2439.5):
                var65 = 0.02396361
            else:
                var65 = 0.08140033
    else:
        if (input[145]) >= (1351.5):
            var65 = -0.07617601
        else:
            if (input[256]) >= (23.5):
                var65 = 0.06454322
            else:
                var65 = -0.026923466
    if (input[160]) >= (1235.5):
        if (input[168]) >= (1461.5):
            if (input[256]) >= (17.5):
                var66 = 0.03488965
            else:
                var66 = -0.07539462
        else:
            if (input[67]) >= (1149.5):
                var66 = 0.042788275
            else:
                var66 = -0.050468314
    else:
        if (input[23]) >= (2203.5):
            if (input[19]) >= (1118.0):
                var66 = 0.06003921
            else:
                var66 = -0.03243009
        else:
            if (input[11]) >= (1355.5):
                var66 = -0.07987674
            else:
                var66 = 0.016227478
    if (input[205]) >= (1211.5):
        if (input[168]) >= (1459.5):
            if (input[256]) >= (18.5):
                var67 = 0.04269373
            else:
                var67 = -0.07745268
        else:
            if (input[17]) >= (1345.5):
                var67 = -0.0075593726
            else:
                var67 = 0.05765258
    else:
        var67 = -0.06476796
    if (input[44]) >= (1598.5):
        if (input[23]) >= (2178.0):
            if (input[256]) >= (11.5):
                var68 = -0.02820148
            else:
                var68 = 0.07968681
        else:
            if (input[162]) >= (1586.5):
                var68 = -0.0015589931
            else:
                var68 = -0.076244086
    else:
        if (input[20]) >= (1876.0):
            if (input[15]) >= (1235.5):
                var68 = 0.03985968
            else:
                var68 = -0.055473633
        else:
            var68 = 0.07920712
    if (input[80]) >= (1266.5):
        if (input[84]) >= (2436.5):
            if (input[55]) >= (1328.0):
                var69 = -0.03285027
            else:
                var69 = 0.06637337
        else:
            if (input[68]) >= (2439.5):
                var69 = 0.022234967
            else:
                var69 = 0.07855012
    else:
        if (input[151]) >= (2200.0):
            if (input[47]) >= (2437.5):
                var69 = 0.06890082
            else:
                var69 = -0.01836213
        else:
            var69 = -0.06979405
    if (input[249]) >= (1229.5):
        if (input[96]) >= (1363.0):
            var70 = 0.069419615
        else:
            var70 = -0.0053426535
    else:
        if (input[114]) >= (2006.0):
            if (input[163]) >= (1082.5):
                var70 = 0.035650875
            else:
                var70 = -0.02321913
        else:
            if (input[251]) >= (1226.5):
                var70 = -0.07970139
            else:
                var70 = 0.009847601
    if (input[44]) >= (1598.5):
        if (input[23]) >= (2178.0):
            if (input[256]) >= (11.5):
                var71 = -0.024645923
            else:
                var71 = 0.075699024
        else:
            if (input[220]) >= (1844.5):
                var71 = 0.03856192
            else:
                var71 = -0.049005162
    else:
        if (input[112]) >= (1983.5):
            if (input[17]) >= (1579.0):
                var71 = -0.0005249818
            else:
                var71 = 0.07606602
        else:
            if (input[124]) >= (2192.5):
                var71 = -0.0016479911
            else:
                var71 = -0.04490843
    if (input[160]) >= (1235.5):
        if (input[156]) >= (2333.5):
            if (input[256]) >= (22.5):
                var72 = 0.037510585
            else:
                var72 = -0.05786526
        else:
            if (input[256]) >= (29.5):
                var72 = -0.057648428
            else:
                var72 = 0.043883547
    else:
        if (input[256]) >= (27.5):
            var72 = 0.035918478
        else:
            if (input[184]) >= (1215.5):
                var72 = 0.023846874
            else:
                var72 = -0.077929206
    if (input[204]) >= (1455.0):
        if (input[204]) >= (1642.0):
            if (input[141]) >= (1452.5):
                var73 = -0.06077779
            else:
                var73 = 0.030267123
        else:
            if (input[220]) >= (1299.0):
                var73 = 0.009382414
            else:
                var73 = 0.07761994
    else:
        if (input[187]) >= (1274.5):
            if (input[18]) >= (1978.5):
                var73 = 0.0591557
            else:
                var73 = -0.043146472
        else:
            if (input[256]) >= (24.5):
                var73 = 0.022545658
            else:
                var73 = -0.0805814
    if (input[208]) >= (1271.5):
        var74 = 0.056557167
    else:
        if (input[107]) >= (2119.0):
            if (input[13]) >= (1329.5):
                var74 = 0.007126598
            else:
                var74 = 0.060060944
        else:
            if (input[34]) >= (2019.5):
                var74 = 0.0028359452
            else:
                var74 = -0.057294495
    if (input[249]) >= (1229.5):
        if (input[96]) >= (1363.0):
            var75 = 0.06498616
        else:
            var75 = -0.004219177
    else:
        if (input[114]) >= (2006.0):
            if (input[223]) >= (1228.5):
                var75 = 0.035625078
            else:
                var75 = -0.018558435
        else:
            if (input[60]) >= (1815.0):
                var75 = -0.07454685
            else:
                var75 = 0.0034990206
    if (input[208]) >= (1271.5):
        var76 = 0.054733988
    else:
        if (input[107]) >= (2119.0):
            if (input[163]) >= (1085.5):
                var76 = 0.008089031
            else:
                var76 = 0.056921877
        else:
            if (input[34]) >= (2019.5):
                var76 = 0.0025098205
            else:
                var76 = -0.053944886
    if (input[44]) >= (1598.5):
        if (input[23]) >= (1983.5):
            if (input[185]) >= (1212.5):
                var77 = 0.050296772
            else:
                var77 = -0.03463367
        else:
            if (input[217]) >= (1227.5):
                var77 = -0.0014997404
            else:
                var77 = -0.06973677
    else:
        if (input[29]) >= (1326.5):
            if (input[123]) >= (1733.5):
                var77 = 0.052854616
            else:
                var77 = -0.053848412
        else:
            var77 = 0.0667407
    if (input[168]) >= (1459.5):
        if (input[256]) >= (19.5):
            var78 = 0.040308755
        else:
            var78 = -0.07273176
    else:
        if (input[2]) >= (2087.5):
            var78 = 0.06684841
        else:
            if (input[119]) >= (1296.5):
                var78 = -0.028455898
            else:
                var78 = 0.030319823
    if (input[249]) >= (1229.5):
        if (input[161]) >= (1576.5):
            var79 = 0.059842654
        else:
            var79 = 0.00035106888
    else:
        if (input[114]) >= (2006.0):
            if (input[96]) >= (1895.5):
                var79 = -0.055520624
            else:
                var79 = 0.018982248
        else:
            if (input[60]) >= (1828.5):
                var79 = -0.07123413
            else:
                var79 = 0.0036209826
    if (input[80]) >= (1264.0):
        if (input[124]) >= (2436.5):
            if (input[217]) >= (1219.0):
                var80 = 0.07157766
            else:
                var80 = 0.009786328
        else:
            if (input[141]) >= (1963.5):
                var80 = 0.051154383
            else:
                var80 = -0.033065494
    else:
        if (input[145]) >= (1351.5):
            var80 = -0.063129544
        else:
            if (input[256]) >= (23.5):
                var80 = 0.0679002
            else:
                var80 = -0.031701263
    if (input[168]) >= (1459.5):
        if (input[256]) >= (18.5):
            var81 = 0.03470086
        else:
            var81 = -0.07056972
    else:
        if (input[2]) >= (2087.5):
            var81 = 0.064118356
        else:
            if (input[187]) >= (1261.5):
                var81 = 0.028584177
            else:
                var81 = -0.027052104
    if (input[11]) >= (1258.0):
        if (input[51]) >= (1088.5):
            if (input[80]) >= (1266.5):
                var82 = 0.040731955
            else:
                var82 = -0.012300523
        else:
            if (input[1]) >= (1331.5):
                var82 = 0.0041815094
            else:
                var82 = -0.06577006
    else:
        var82 = 0.052807935
    if (input[168]) >= (1459.5):
        if (input[256]) >= (18.5):
            var83 = 0.03324267
        else:
            var83 = -0.06805106
    else:
        if (input[204]) >= (1455.0):
            if (input[256]) >= (28.5):
                var83 = -0.041171327
            else:
                var83 = 0.05807319
        else:
            if (input[187]) >= (1274.5):
                var83 = 0.028292406
            else:
                var83 = -0.041740645
    if (input[11]) >= (1258.0):
        if (input[51]) >= (1088.5):
            if (input[8]) >= (1386.5):
                var84 = -0.008911738
            else:
                var84 = 0.0435316
        else:
            if (input[1]) >= (1331.5):
                var84 = 0.0029036663
            else:
                var84 = -0.06406786
    else:
        var84 = 0.05075049
    if (input[243]) >= (1204.5):
        if (input[244]) >= (1182.5):
            if (input[256]) >= (21.5):
                var85 = 0.015743913
            else:
                var85 = -0.05992179
        else:
            if (input[17]) >= (1345.5):
                var85 = -0.016514203
            else:
                var85 = 0.042685017
    else:
        if (input[163]) >= (1133.5):
            var85 = 0.0041612987
        else:
            var85 = 0.051946204
    if (input[199]) >= (1302.5):
        if (input[109]) >= (2041.5):
            if (input[146]) >= (1619.0):
                var86 = 0.06206147
            else:
                var86 = 0.013449452
        else:
            if (input[256]) >= (13.5):
                var86 = 0.023646142
            else:
                var86 = -0.027203703
    else:
        if (input[91]) >= (2234.5):
            var86 = -0.05648626
        else:
            var86 = 0.0013318359
    if (input[146]) >= (1537.5):
        if (input[187]) >= (1273.5):
            if (input[86]) >= (1997.0):
                var87 = 0.06640397
            else:
                var87 = 0.008461718
        else:
            if (input[86]) >= (2128.5):
                var87 = -0.04197932
            else:
                var87 = 0.011813086
    else:
        var87 = -0.038276795
    if (input[156]) >= (2437.5):
        var88 = -0.048029937
    else:
        if (input[55]) >= (1384.5):
            if (input[22]) >= (1702.5):
                var88 = 0.014917056
            else:
                var88 = -0.050030272
        else:
            if (input[29]) >= (1296.0):
                var88 = 0.005254747
            else:
                var88 = 0.06284059
    if (input[11]) >= (1258.0):
        if (input[51]) >= (1088.5):
            if (input[8]) >= (1363.5):
                var89 = -0.007967728
            else:
                var89 = 0.045055132
        else:
            if (input[1]) >= (1269.5):
                var89 = -0.0014122223
            else:
                var89 = -0.061676037
    else:
        var89 = 0.047364313
    if (input[199]) >= (1302.5):
        if (input[109]) >= (2041.5):
            var90 = 0.048984718
        else:
            if (input[141]) >= (1577.0):
                var90 = -0.049967352
            else:
                var90 = 0.009690791
    else:
        if (input[59]) >= (2172.5):
            var90 = -0.053177238
        else:
            var90 = 0.000009937285
    if (input[44]) >= (1598.5):
        if (input[86]) >= (1955.5):
            if (input[50]) >= (2359.0):
                var91 = -0.01657065
            else:
                var91 = 0.05355225
        else:
            if (input[12]) >= (1422.5):
                var91 = -0.06654667
            else:
                var91 = 0.011436603
    else:
        if (input[112]) >= (1983.5):
            if (input[17]) >= (1579.0):
                var91 = 0.0016403955
            else:
                var91 = 0.06521101
        else:
            var91 = -0.026798204
    if (input[168]) >= (1459.5):
        if (input[256]) >= (16.5):
            var92 = 0.028353214
        else:
            var92 = -0.06468124
    else:
        if (input[2]) >= (2087.5):
            var92 = 0.057489093
        else:
            if (input[55]) >= (1327.0):
                var92 = -0.016376898
            else:
                var92 = 0.047953974
    if (input[146]) >= (1537.5):
        if (input[187]) >= (1273.5):
            if (input[86]) >= (1997.0):
                var93 = 0.06362526
            else:
                var93 = 0.009093158
        else:
            if (input[204]) >= (1455.0):
                var93 = 0.014428898
            else:
                var93 = -0.034267392
    else:
        var93 = -0.036091868
    if (input[168]) >= (1459.5):
        if (input[256]) >= (16.5):
            var94 = 0.02644066
        else:
            var94 = -0.0628692
    else:
        if (input[2]) >= (2087.5):
            var94 = 0.05521774
        else:
            if (input[55]) >= (1327.0):
                var94 = -0.014765208
            else:
                var94 = 0.0465719
    if (input[244]) >= (1182.5):
        if (input[12]) >= (1409.0):
            var95 = -0.056147307
        else:
            var95 = 0.02119379
    else:
        if (input[17]) >= (1345.5):
            if (input[83]) >= (1094.5):
                var95 = 0.03522484
            else:
                var95 = -0.037681077
        else:
            if (input[114]) >= (1999.0):
                var95 = 0.06304009
            else:
                var95 = -0.015873216
    if (input[156]) >= (2333.5):
        if (input[256]) >= (21.5):
            var96 = 0.02630037
        else:
            if (input[104]) >= (1449.0):
                var96 = -0.06483165
            else:
                var96 = -0.011714533
    else:
        if (input[2]) >= (2087.5):
            var96 = 0.05854235
        else:
            if (input[55]) >= (1328.0):
                var96 = -0.012867923
            else:
                var96 = 0.0450996
    if (input[244]) >= (1182.5):
        if (input[12]) >= (1409.0):
            var97 = -0.053769775
        else:
            var97 = 0.01972856
    else:
        if (input[101]) >= (1206.5):
            if (input[251]) >= (1231.5):
                var97 = 0.05695771
            else:
                var97 = -0.004296491
        else:
            if (input[256]) >= (14.0):
                var97 = -0.072728924
            else:
                var97 = 0.031104574
    if (input[34]) >= (2024.5):
        if (input[119]) >= (2351.5):
            if (input[58]) >= (1294.5):
                var98 = -0.026212692
            else:
                var98 = 0.020324675
        else:
            if (input[1]) >= (1247.0):
                var98 = 0.0734384
            else:
                var98 = -0.014100078
    else:
        if (input[55]) >= (1445.5):
            var98 = -0.058387812
        else:
            var98 = 0.013648637
    if (input[156]) >= (2379.5):
        var99 = -0.031993106
    else:
        if (input[34]) >= (2024.5):
            if (input[219]) >= (1237.5):
                var99 = 0.05795842
            else:
                var99 = 0.0017530306
        else:
            if (input[55]) >= (1445.5):
                var99 = -0.05529051
            else:
                var99 = 0.014678019
    if (input[156]) >= (2323.5):
        if (input[256]) >= (12.5):
            var100 = 0.017344559
        else:
            var100 = -0.06104378
    else:
        if (input[2]) >= (2087.5):
            var100 = 0.054380685
        else:
            if (input[55]) >= (1353.5):
                var100 = -0.011709201
            else:
                var100 = 0.04201263
    var101 = (1.0) / ((1.0) + (math.exp((0.0) - (((((((((((((((((((((((((((((((((((((((((((((((((((((((var46) + (var47)) + (var48)) + (var49)) + (var50)) + (var51)) + (var52)) + (var53)) + (var54)) + (var55)) + (var56)) + (var57)) + (var58)) + (var59)) + (var60)) + (var61)) + (var62)) + (var63)) + (var64)) + (var65)) + (var66)) + (var67)) + (var68)) + (var69)) + (var70)) + (var71)) + (var72)) + (var73)) + (var74)) + (var75)) + (var76)) + (var77)) + (var78)) + (var79)) + (var80)) + (var81)) + (var82)) + (var83)) + (var84)) + (var85)) + (var86)) + (var87)) + (var88)) + (var89)) + (var90)) + (var91)) + (var92)) + (var93)) + (var94)) + (var95)) + (var96)) + (var97)) + (var98)) + (var99)) + (var100)))))
    return [(1.0) - (var101), var101]

def score_solo_itchy_2(input):
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var0 = -0.120000005
        else:
            var0 = 0.19139785
    else:
        if (input[41]) >= (1215.0):
            var0 = -0.19827214
        else:
            var0 = 0.1
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var1 = -0.11305224
        else:
            var1 = 0.17465846
    else:
        if (input[214]) >= (2110.5):
            var1 = 0.064563416
        else:
            var1 = -0.18042336
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var2 = -0.10694325
        else:
            var2 = 0.1618269
    else:
        if (input[231]) >= (1703.0):
            var2 = 0.063967824
        else:
            var2 = -0.16700684
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var3 = -0.10152151
        else:
            var3 = 0.151682
    else:
        if (input[232]) >= (1956.5):
            var3 = 0.06333425
        else:
            var3 = -0.15654372
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var4 = -0.09666838
        else:
            var4 = 0.14346248
    else:
        if (input[232]) >= (1956.5):
            var4 = 0.05997708
        else:
            var4 = -0.14814967
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var5 = 0.1381163
        else:
            var5 = -0.10096022
    else:
        if (input[131]) >= (1093.5):
            var5 = -0.14153622
        else:
            var5 = -0.01401705
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var6 = -0.08654644
        else:
            var6 = 0.13104844
    else:
        if (input[231]) >= (1703.0):
            var6 = 0.055626865
        else:
            var6 = -0.13573067
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var7 = 0.12748727
        else:
            var7 = -0.09170043
    else:
        if (input[185]) >= (1817.0):
            var7 = -0.015696991
        else:
            var7 = -0.1310643
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var8 = 0.12312194
        else:
            var8 = -0.08829061
    else:
        if (input[163]) >= (1024.0):
            var8 = -0.12710005
        else:
            var8 = -0.015107855
    if (input[180]) >= (1784.0):
        if (input[60]) >= (2121.5):
            var9 = -0.075299345
        else:
            var9 = 0.118444875
    else:
        if (input[214]) >= (2110.5):
            var9 = 0.049068626
        else:
            var9 = -0.12353698
    if (input[172]) >= (2109.5):
        if (input[12]) >= (1782.0):
            var10 = -0.08616622
        else:
            var10 = 0.116578475
    else:
        var10 = -0.12007024
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var11 = 0.11318054
        else:
            var11 = -0.07726354
    else:
        if (input[41]) >= (1218.0):
            var11 = -0.118026845
        else:
            var11 = -0.016400237
    if (input[230]) >= (2093.0):
        if (input[124]) >= (2325.0):
            var12 = 0.1103624
        else:
            var12 = -0.0727926
    else:
        if (input[75]) >= (2443.5):
            var12 = -0.011582259
        else:
            var12 = -0.11574892
    if (input[172]) >= (2109.5):
        if (input[12]) >= (1782.0):
            var13 = -0.07596073
        else:
            var13 = 0.10851802
    else:
        var13 = -0.113057815
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var14 = 0.10583122
        else:
            var14 = -0.06785003
    else:
        if (input[151]) >= (2437.5):
            var14 = -0.018833203
        else:
            var14 = -0.11184224
    if (input[230]) >= (2093.0):
        if (input[124]) >= (2325.0):
            var15 = 0.10359301
        else:
            var15 = -0.06376305
    else:
        if (input[231]) >= (1558.0):
            var15 = -0.018174272
        else:
            var15 = -0.11024292
    if (input[172]) >= (2109.5):
        if (input[12]) >= (1782.0):
            var16 = -0.06742989
        else:
            var16 = 0.102230705
    else:
        var16 = -0.10803317
    if (input[246]) >= (1227.5):
        if (input[200]) >= (1818.0):
            var17 = 0.09992211
        else:
            var17 = -0.059620857
    else:
        if (input[195]) >= (1120.5):
            var17 = -0.10739664
        else:
            var17 = -0.022645084
    if (input[230]) >= (2093.0):
        if (input[139]) >= (2217.5):
            var18 = 0.09787669
        else:
            var18 = -0.049283784
    else:
        if (input[99]) >= (988.5):
            var18 = -0.1061567
        else:
            var18 = -0.020611143
    if (input[172]) >= (2109.5):
        if (input[12]) >= (1782.0):
            var19 = -0.06005934
        else:
            var19 = 0.096926086
    else:
        var19 = -0.104171194
    if (input[246]) >= (1227.5):
        if (input[200]) >= (2435.0):
            var20 = 0.09455485
        else:
            var20 = -0.041394494
    else:
        if (input[235]) >= (1443.0):
            var20 = -0.025011718
        else:
            var20 = -0.10387315
    if (input[172]) >= (2109.5):
        if (input[12]) >= (1782.0):
            var21 = -0.055705912
        else:
            var21 = 0.09363958
    else:
        var21 = -0.10193726
    if (input[230]) >= (2093.0):
        if (input[172]) >= (2123.5):
            var22 = 0.09063398
        else:
            var22 = -0.02663819
    else:
        if (input[216]) >= (1276.0):
            var22 = -0.024933482
        else:
            var22 = -0.10189495
    if (input[246]) >= (1227.5):
        if (input[133]) >= (1212.5):
            var23 = -0.021942537
        else:
            var23 = 0.089354545
    else:
        if (input[237]) >= (1323.0):
            var23 = -0.027586216
        else:
            var23 = -0.10095393
    if (input[172]) >= (2109.5):
        if (input[228]) >= (1235.0):
            var24 = 0.08838724
        else:
            var24 = -0.03483703
    else:
        var24 = -0.098892346
    if (input[230]) >= (2093.0):
        if (input[246]) >= (1228.5):
            var25 = 0.085475825
        else:
            var25 = -0.013356859
    else:
        if (input[232]) >= (1268.0):
            var25 = -0.026345799
        else:
            var25 = -0.09917763
    if (input[246]) >= (1227.5):
        if (input[230]) >= (2107.0):
            var26 = 0.083823405
        else:
            var26 = -0.010530761
    else:
        if (input[125]) >= (2111.5):
            var26 = -0.028542131
        else:
            var26 = -0.098327115
    if (input[172]) >= (2109.5):
        if (input[77]) >= (1915.5):
            var27 = -0.020000478
        else:
            var27 = 0.083886355
    else:
        var27 = -0.09610965
    if (input[230]) >= (2093.0):
        if (input[139]) >= (2230.0):
            var28 = 0.08073909
        else:
            var28 = -0.0032269116
    else:
        if (input[217]) >= (1382.0):
            var28 = -0.026820103
        else:
            var28 = -0.096575715
    if (input[246]) >= (1227.5):
        if (input[92]) >= (2442.5):
            var29 = 0.07942212
        else:
            var29 = -0.001748072
    else:
        var29 = -0.09319683
    if (input[172]) >= (2109.5):
        if (input[77]) >= (1913.5):
            var30 = -0.008960852
        else:
            var30 = 0.07906536
    else:
        var30 = -0.093294114
    if (input[172]) >= (2078.0):
        if (input[60]) >= (1977.5):
            var31 = -0.025198827
        else:
            var31 = 0.079604015
    else:
        var31 = -0.094128676
    if (input[230]) >= (2093.0):
        if (input[54]) >= (2047.5):
            var32 = 0.009284082
        else:
            var32 = 0.073225535
    else:
        var32 = -0.09001553
    if (input[172]) >= (2078.0):
        if (input[195]) >= (1129.5):
            var33 = -0.016707113
        else:
            var33 = 0.075651094
    else:
        var33 = -0.09229126
    if (input[246]) >= (1227.5):
        if (input[232]) >= (1241.5):
            var34 = 0.070050664
        else:
            var34 = 0.012284551
    else:
        var34 = -0.088135034
    if (input[172]) >= (2078.0):
        if (input[60]) >= (1969.5):
            var35 = -0.01234811
        else:
            var35 = 0.073183306
    else:
        var35 = -0.09034918
    if (input[195]) >= (1130.5):
        if (input[217]) >= (1339.5):
            var36 = -0.02282034
        else:
            var36 = -0.08888229
    else:
        var36 = 0.060817033
    if (input[246]) >= (1224.5):
        if (input[238]) >= (1205.5):
            var37 = 0.067158304
        else:
            var37 = 0.0048892605
    else:
        var37 = -0.086523585
    if (input[172]) >= (2078.0):
        if (input[60]) >= (1962.5):
            var38 = -0.0041113794
        else:
            var38 = 0.06791698
    else:
        var38 = -0.08728275
    if (input[200]) >= (2383.5):
        if (input[87]) >= (1481.5):
            var39 = -0.0021292854
        else:
            var39 = 0.06614226
    else:
        var39 = -0.08629832
    if (input[230]) >= (2093.0):
        var40 = 0.054317266
    else:
        var40 = -0.081121095
    if (input[246]) >= (1227.5):
        var41 = 0.052972604
    else:
        var41 = -0.08004812
    if (input[200]) >= (2383.5):
        if (input[214]) >= (2125.5):
            var42 = 0.060595293
        else:
            var42 = 0.0047702505
    else:
        var42 = -0.082860716
    if (input[172]) >= (2078.0):
        if (input[60]) >= (1934.0):
            var43 = 0.007455627
        else:
            var43 = 0.05862507
    else:
        var43 = -0.081569426
    if (input[200]) >= (2383.5):
        if (input[32]) >= (1226.5):
            var44 = 0.0068611787
        else:
            var44 = 0.057196166
    else:
        var44 = -0.08030993
    if (input[172]) >= (2121.0):
        var45 = 0.047749486
    else:
        var45 = -0.0762911
    var46 = (((((((((((((((((((((((((((((((((((((((((((((var0) + (var1)) + (var2)) + (var3)) + (var4)) + (var5)) + (var6)) + (var7)) + (var8)) + (var9)) + (var10)) + (var11)) + (var12)) + (var13)) + (var14)) + (var15)) + (var16)) + (var17)) + (var18)) + (var19)) + (var20)) + (var21)) + (var22)) + (var23)) + (var24)) + (var25)) + (var26)) + (var27)) + (var28)) + (var29)) + (var30)) + (var31)) + (var32)) + (var33)) + (var34)) + (var35)) + (var36)) + (var37)) + (var38)) + (var39)) + (var40)) + (var41)) + (var42)) + (var43)) + (var44)) + (var45)
    if (input[230]) >= (2093.0):
        var47 = 0.04964872
    else:
        var47 = -0.07349872
    if (input[246]) >= (1224.5):
        var48 = 0.04561107
    else:
        var48 = -0.07427739
    if (input[200]) >= (2383.5):
        var49 = 0.041495528
    else:
        var49 = -0.07523593
    if (input[172]) >= (2078.0):
        var50 = 0.040556647
    else:
        var50 = -0.07384016
    if (input[195]) >= (1130.5):
        var51 = -0.06644714
    else:
        var51 = 0.048931457
    if (input[246]) >= (1227.5):
        var52 = 0.045564737
    else:
        var52 = -0.067069985
    if (input[200]) >= (2383.5):
        var53 = 0.038622107
    else:
        var53 = -0.06992387
    if (input[230]) >= (2093.0):
        var54 = 0.043943193
    else:
        var54 = -0.06402414
    if (input[172]) >= (2078.0):
        var55 = 0.037660893
    else:
        var55 = -0.06727566
    if (input[195]) >= (1135.5):
        var56 = -0.062271066
    else:
        var56 = 0.041707184
    if (input[246]) >= (1227.5):
        var57 = 0.041991785
    else:
        var57 = -0.060546547
    if (input[200]) >= (2383.5):
        var58 = 0.035529647
    else:
        var58 = -0.06335229
    if (input[172]) >= (2078.0):
        var59 = 0.03498673
    else:
        var59 = -0.062081374
    if (input[246]) >= (1227.5):
        var60 = 0.039296005
    else:
        var60 = -0.05654285
    if (input[230]) >= (2093.0):
        var61 = 0.03910386
    else:
        var61 = -0.055410326
    if (input[195]) >= (1135.5):
        var62 = -0.054922838
    else:
        var62 = 0.03787532
    if (input[172]) >= (2078.0):
        var63 = 0.03280197
    else:
        var63 = -0.057074916
    if (input[233]) >= (1374.5):
        var64 = 0.03253872
    else:
        var64 = -0.055705328
    if (input[246]) >= (1224.5):
        var65 = 0.033985507
    else:
        var65 = -0.052598465
    if (input[200]) >= (2383.5):
        var66 = 0.03124266
    else:
        var66 = -0.053842515
    if (input[233]) >= (1374.5):
        var67 = 0.03027588
    else:
        var67 = -0.05220111
    if (input[172]) >= (2078.0):
        var68 = 0.029556474
    else:
        var68 = -0.05149556
    if (input[200]) >= (2383.5):
        var69 = 0.028763419
    else:
        var69 = -0.05046553
    var70 = (1.0) / ((1.0) + (math.exp((0.0) - (((((((((((((((((((((((((((((((((((((((((((((((((((((((var46) + (var47)) + (var48)) + (var49)) + (var50)) + (var51)) + (var52)) + (var53)) + (var54)) + (var55)) + (var56)) + (var57)) + (var58)) + (var59)) + (var60)) + (var61)) + (var62)) + (var63)) + (var64)) + (var65)) + (var66)) + (var67)) + (var68)) + (var69)) + (-0.013564666)) + (-0.012687325)) + (-0.011864829)) + (-0.011094003)) + (-0.010371834)) + (-0.0096956575)) + (-0.009062658)) + (-0.008470341)) + (-0.007915982)) + (-0.007397496)) + (-0.006912514)) + (-0.006458977)) + (-0.0060349265)) + (-0.005638463)) + (-0.0052679717)) + (-0.004921654)) + (-0.0045979177)) + (-0.0042953305)) + (-0.0040127165)) + (-0.0037485359)) + (-0.0035017133)) + (-0.0032710817)) + (-0.0030555928)) + (-0.00285424)) + (-0.0026661546)) + (-0.0024904688)) + (-0.002326281)) + (-0.002172989)) + (-0.0020297626)) + (-0.001895951)) + (-0.0017709552)))))
    return [(1.0) - (var70), var70]

def score_solo_itchy_4(input):
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var0 = 0.080000006
            else:
                var0 = -0.18064515
        else:
            if (input[212]) >= (2367.0):
                var0 = -0.15555556
            else:
                var0 = 0.16906078
    else:
        if (input[110]) >= (2016.0):
            if (input[56]) >= (1377.0):
                var0 = -0.1
            else:
                var0 = 0.16666667
        else:
            if (input[88]) >= (1898.5):
                var0 = 0.15555556
            else:
                var0 = -0.18753247
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var1 = 0.075274736
            else:
                var1 = -0.16504468
        else:
            if (input[212]) >= (2367.0):
                var1 = -0.14415668
            else:
                var1 = 0.15363602
    else:
        if (input[110]) >= (2016.0):
            if (input[56]) >= (1377.0):
                var1 = -0.09267972
            else:
                var1 = 0.15369518
        else:
            if (input[88]) >= (1898.5):
                var1 = 0.14415668
            else:
                var1 = -0.17050312
    if (input[32]) >= (1257.0):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var2 = 0.07095779
            else:
                var2 = -0.15281181
        else:
            if (input[212]) >= (2367.0):
                var2 = -0.13473612
            else:
                var2 = 0.13849951
    else:
        if (input[110]) >= (2016.0):
            if (input[19]) >= (1151.5):
                var2 = 0.12533544
            else:
                var2 = -0.12127339
        else:
            if (input[88]) >= (1898.5):
                var2 = 0.13473612
            else:
                var2 = -0.15834267
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var3 = 0.06699361
            else:
                var3 = -0.14292781
        else:
            if (input[212]) >= (2367.0):
                var3 = -0.12679774
            else:
                var3 = 0.13133773
    else:
        if (input[61]) >= (1875.5):
            if (input[206]) >= (1309.0):
                var3 = 0.0729473
            else:
                var3 = -0.15802847
        else:
            if (input[108]) >= (1810.0):
                var3 = 0.14483434
            else:
                var3 = -0.10332097
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var4 = 0.063336715
            else:
                var4 = -0.13474178
        else:
            if (input[212]) >= (2367.0):
                var4 = -0.119994245
            else:
                var4 = 0.12269956
    else:
        if (input[61]) >= (1875.5):
            if (input[206]) >= (1309.0):
                var4 = 0.06715654
            else:
                var4 = -0.14929157
        else:
            if (input[80]) >= (1230.5):
                var4 = 0.13850597
            else:
                var4 = -0.093183614
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[73]) >= (1685.0):
                var5 = 0.07436745
            else:
                var5 = -0.12606013
        else:
            if (input[3]) >= (1095.5):
                var5 = 0.11083998
            else:
                var5 = -0.18478523
    else:
        if (input[83]) >= (1120.5):
            if (input[123]) >= (1910.5):
                var5 = -0.13125381
            else:
                var5 = 0.08686315
        else:
            if (input[9]) >= (1998.5):
                var5 = 0.08321634
            else:
                var5 = -0.13685665
    if (input[32]) >= (1260.5):
        if (input[148]) >= (2437.5):
            if (input[88]) >= (1602.0):
                var6 = 0.06145675
            else:
                var6 = -0.122284226
        else:
            if (input[212]) >= (2367.0):
                var6 = -0.11952579
            else:
                var6 = 0.10962997
    else:
        if (input[61]) >= (1875.5):
            if (input[178]) >= (1313.5):
                var6 = 0.121838726
            else:
                var6 = -0.13191728
        else:
            if (input[212]) >= (1177.5):
                var6 = -0.09163168
            else:
                var6 = 0.121338904
    if (input[32]) >= (1257.0):
        if (input[148]) >= (2437.5):
            if (input[105]) >= (1826.5):
                var7 = 0.07426534
            else:
                var7 = -0.115144305
        else:
            if (input[127]) >= (2440.5):
                var7 = -0.17291322
            else:
                var7 = 0.09972342
    else:
        if (input[110]) >= (2016.0):
            if (input[56]) >= (1377.0):
                var7 = -0.07959541
            else:
                var7 = 0.12234533
        else:
            if (input[61]) >= (1875.5):
                var7 = -0.13168491
            else:
                var7 = 0.020513007
    if (input[32]) >= (1251.5):
        if (input[148]) >= (2436.5):
            if (input[73]) >= (1700.5):
                var8 = 0.10867312
            else:
                var8 = -0.11761949
        else:
            if (input[11]) >= (2442.5):
                var8 = -0.120724835
            else:
                var8 = 0.09828595
    else:
        if (input[88]) >= (1898.5):
            var8 = 0.10608766
        else:
            if (input[110]) >= (1977.5):
                var8 = 0.040993735
            else:
                var8 = -0.12179333
    if (input[32]) >= (1257.0):
        if (input[198]) >= (2443.5):
            var9 = -0.12843536
        else:
            if (input[141]) >= (1770.0):
                var9 = -0.14634086
            else:
                var9 = 0.08705377
    else:
        if (input[83]) >= (1120.5):
            if (input[123]) >= (1910.5):
                var9 = -0.111558154
            else:
                var9 = 0.07240648
        else:
            if (input[9]) >= (1998.5):
                var9 = 0.07866505
            else:
                var9 = -0.1182753
    if (input[0]) >= (1226.5):
        if (input[198]) >= (2443.5):
            if (input[1]) >= (1330.5):
                var10 = -0.116907395
            else:
                var10 = -0.008271894
        else:
            if (input[141]) >= (1803.0):
                var10 = -0.13907464
            else:
                var10 = 0.10402286
    else:
        if (input[155]) >= (1491.0):
            if (input[110]) >= (1982.0):
                var10 = 0.0369
            else:
                var10 = -0.12348546
        else:
            if (input[153]) >= (1328.0):
                var10 = 0.063073084
            else:
                var10 = -0.106199205
    if (input[121]) >= (1288.5):
        if (input[206]) >= (1309.0):
            if (input[105]) >= (1695.0):
                var11 = 0.12303559
            else:
                var11 = -0.04116711
        else:
            if (input[199]) >= (2449.5):
                var11 = 0.06892044
            else:
                var11 = -0.1238109
    else:
        if (input[48]) >= (1225.5):
            if (input[163]) >= (1081.0):
                var11 = 0.09288695
            else:
                var11 = -0.09025938
        else:
            if (input[201]) >= (1251.5):
                var11 = 0.036101587
            else:
                var11 = -0.10888004
    if (input[121]) >= (1290.5):
        if (input[206]) >= (1309.0):
            if (input[105]) >= (1695.0):
                var12 = 0.11878192
            else:
                var12 = -0.037663445
        else:
            if (input[203]) >= (2448.5):
                var12 = 0.06476208
            else:
                var12 = -0.12129736
    else:
        if (input[13]) >= (1947.5):
            if (input[4]) >= (1803.0):
                var12 = -0.11397045
            else:
                var12 = 0.07475795
        else:
            if (input[153]) >= (1576.0):
                var12 = -0.081447035
            else:
                var12 = 0.092762254
    if (input[121]) >= (1290.5):
        if (input[206]) >= (1309.0):
            if (input[56]) >= (1377.0):
                var13 = -0.04060179
            else:
                var13 = 0.11242523
        else:
            if (input[203]) >= (2448.5):
                var13 = 0.06205206
            else:
                var13 = -0.11857162
    else:
        if (input[13]) >= (1947.5):
            if (input[4]) >= (1803.0):
                var13 = -0.110754445
            else:
                var13 = 0.072304115
        else:
            if (input[148]) >= (2437.5):
                var13 = -0.07537206
            else:
                var13 = 0.08872033
    if (input[32]) >= (1257.0):
        if (input[148]) >= (2438.5):
            if (input[88]) >= (1602.0):
                var14 = 0.052805252
            else:
                var14 = -0.10667854
        else:
            if (input[115]) >= (1066.5):
                var14 = 0.097098134
            else:
                var14 = -0.036327787
    else:
        if (input[99]) >= (1083.5):
            if (input[202]) >= (1244.0):
                var14 = 0.017940661
            else:
                var14 = -0.113201104
        else:
            if (input[83]) >= (1111.5):
                var14 = 0.05365203
            else:
                var14 = -0.09773525
    if (input[32]) >= (1251.5):
        if (input[198]) >= (2443.5):
            var15 = -0.10802783
        else:
            if (input[163]) >= (1088.0):
                var15 = 0.067750774
            else:
                var15 = -0.11544331
    else:
        if (input[99]) >= (1083.5):
            if (input[202]) >= (1220.0):
                var15 = -0.022765962
            else:
                var15 = -0.11086867
        else:
            if (input[83]) >= (1098.0):
                var15 = 0.04154528
            else:
                var15 = -0.10101452
    if (input[127]) >= (2429.0):
        var16 = -0.11170477
    else:
        if (input[148]) >= (2436.5):
            if (input[172]) >= (2064.5):
                var16 = 0.06767918
            else:
                var16 = -0.10159198
        else:
            if (input[58]) >= (1326.5):
                var16 = -0.031712707
            else:
                var16 = 0.08578676
    if (input[121]) >= (1288.5):
        if (input[206]) >= (1391.5):
            if (input[198]) >= (2442.5):
                var17 = -0.04836301
            else:
                var17 = 0.10922215
        else:
            if (input[18]) >= (2438.5):
                var17 = 0.041060057
            else:
                var17 = -0.102203466
    else:
        if (input[48]) >= (1225.5):
            if (input[143]) >= (1225.5):
                var17 = 0.0776588
            else:
                var17 = -0.08344591
        else:
            if (input[201]) >= (1251.5):
                var17 = 0.030625371
            else:
                var17 = -0.09826701
    if (input[127]) >= (2429.0):
        var18 = -0.108275466
    else:
        if (input[83]) >= (1104.5):
            if (input[16]) >= (1215.5):
                var18 = 0.09367672
            else:
                var18 = -0.011981532
        else:
            if (input[57]) >= (1331.5):
                var18 = -0.09843854
            else:
                var18 = 0.08553728
    if (input[127]) >= (2429.0):
        var19 = -0.1062531
    else:
        if (input[148]) >= (2436.5):
            if (input[172]) >= (2064.5):
                var19 = 0.065062866
            else:
                var19 = -0.09498838
        else:
            if (input[58]) >= (1326.5):
                var19 = -0.029845709
            else:
                var19 = 0.07832829
    if (input[127]) >= (2429.0):
        var20 = -0.10428468
    else:
        if (input[83]) >= (1104.5):
            if (input[16]) >= (1215.5):
                var20 = 0.088503346
            else:
                var20 = -0.012309096
        else:
            if (input[51]) >= (1128.5):
                var20 = 0.04530441
            else:
                var20 = -0.10756507
    if (input[127]) >= (2429.0):
        var21 = -0.1023528
    else:
        if (input[148]) >= (2436.5):
            if (input[205]) >= (2218.0):
                var21 = 0.0799781
            else:
                var21 = -0.08743182
        else:
            if (input[58]) >= (1326.5):
                var21 = -0.027557192
            else:
                var21 = 0.07246687
    if (input[204]) >= (1346.0):
        if (input[141]) >= (1761.5):
            var22 = -0.09691262
        else:
            if (input[157]) >= (1506.5):
                var22 = 0.08178567
            else:
                var22 = -0.034950253
    else:
        if (input[88]) >= (1898.5):
            var22 = 0.08429575
        else:
            if (input[208]) >= (1257.0):
                var22 = 0.07664435
            else:
                var22 = -0.10773956
    if (input[127]) >= (2429.0):
        var23 = -0.098971404
    else:
        if (input[252]) >= (1853.5):
            if (input[48]) >= (1222.5):
                var23 = 0.07466526
            else:
                var23 = -0.06667344
        else:
            if (input[55]) >= (1351.5):
                var23 = -0.08908682
            else:
                var23 = 0.04916843
    if (input[204]) >= (1346.0):
        if (input[141]) >= (1761.5):
            var24 = -0.09336657
        else:
            if (input[198]) >= (2443.5):
                var24 = -0.0714161
            else:
                var24 = 0.05893792
    else:
        if (input[121]) >= (1273.0):
            if (input[104]) >= (1628.5):
                var24 = -0.026894955
            else:
                var24 = -0.107483625
        else:
            if (input[113]) >= (1446.5):
                var24 = 0.0750995
            else:
                var24 = -0.0742255
    if (input[208]) >= (1272.5):
        var25 = 0.089817576
    else:
        if (input[160]) >= (1252.5):
            if (input[38]) >= (2308.5):
                var25 = -0.00772112
            else:
                var25 = -0.11138221
        else:
            if (input[99]) >= (1092.5):
                var25 = -0.060386468
            else:
                var25 = 0.039768044
    if (input[204]) >= (1346.0):
        if (input[122]) >= (1412.5):
            if (input[256]) >= (25.0):
                var26 = 0.036158625
            else:
                var26 = -0.09832116
        else:
            if (input[169]) >= (1682.5):
                var26 = -0.069373034
            else:
                var26 = 0.066774346
    else:
        if (input[88]) >= (1898.5):
            var26 = 0.076593265
        else:
            if (input[208]) >= (1257.0):
                var26 = 0.06879925
            else:
                var26 = -0.10174395
    if (input[127]) >= (2429.0):
        var27 = -0.09402277
    else:
        if (input[95]) >= (1580.5):
            if (input[48]) >= (1214.5):
                var27 = 0.08542269
            else:
                var27 = -0.07967162
        else:
            if (input[208]) >= (1272.5):
                var27 = 0.08464881
            else:
                var27 = -0.058458496
    if (input[127]) >= (2429.0):
        var28 = -0.0921444
    else:
        if (input[83]) >= (1097.5):
            if (input[188]) >= (1664.5):
                var28 = -0.10797148
            else:
                var28 = 0.043228768
        else:
            if (input[90]) >= (1279.5):
                var28 = 0.080786996
            else:
                var28 = -0.09003204
    if (input[204]) >= (1346.0):
        if (input[122]) >= (1412.5):
            if (input[256]) >= (25.0):
                var29 = 0.035198905
            else:
                var29 = -0.09588837
        else:
            if (input[76]) >= (1940.0):
                var29 = -0.07187187
            else:
                var29 = 0.06291383
    else:
        if (input[88]) >= (1898.5):
            var29 = 0.072100945
        else:
            if (input[208]) >= (1257.0):
                var29 = 0.06378373
            else:
                var29 = -0.09833183
    if (input[127]) >= (2429.0):
        var30 = -0.08938793
    else:
        if (input[148]) >= (2438.5):
            if (input[172]) >= (2069.0):
                var30 = 0.07074407
            else:
                var30 = -0.091503695
        else:
            if (input[153]) >= (1300.0):
                var30 = 0.04431989
            else:
                var30 = -0.053694315
    if (input[38]) >= (2242.5):
        if (input[0]) >= (1225.5):
            var31 = 0.091192126
        else:
            if (input[57]) >= (1331.5):
                var31 = -0.08377852
            else:
                var31 = 0.07111762
    else:
        if (input[155]) >= (1387.0):
            if (input[203]) >= (2042.0):
                var31 = 0.020496579
            else:
                var31 = -0.0854377
        else:
            if (input[156]) >= (2101.0):
                var31 = 0.08516018
            else:
                var31 = -0.05732059
    if (input[204]) >= (1321.5):
        if (input[24]) >= (1613.5):
            var32 = 0.09235033
        else:
            if (input[55]) >= (1380.0):
                var32 = -0.052378833
            else:
                var32 = 0.04758678
    else:
        if (input[88]) >= (1898.5):
            var32 = 0.066679046
        else:
            if (input[208]) >= (1257.0):
                var32 = 0.059339423
            else:
                var32 = -0.09888595
    if (input[208]) >= (1272.5):
        var33 = 0.080818504
    else:
        if (input[160]) >= (1252.5):
            if (input[38]) >= (2274.5):
                var33 = -0.016830225
            else:
                var33 = -0.10335167
        else:
            if (input[99]) >= (1092.5):
                var33 = -0.04879863
            else:
                var33 = 0.039309323
    if (input[76]) >= (1940.0):
        if (input[109]) >= (2214.5):
            var34 = 0.01698116
        else:
            var34 = -0.0996728
    else:
        if (input[172]) >= (2046.5):
            if (input[198]) >= (1718.5):
                var34 = 0.013599833
            else:
                var34 = 0.09762686
        else:
            if (input[83]) >= (1106.5):
                var34 = 0.012527381
            else:
                var34 = -0.07504713
    if (input[38]) >= (2242.5):
        if (input[0]) >= (1225.5):
            var35 = 0.087303326
        else:
            if (input[57]) >= (1331.5):
                var35 = -0.07781856
            else:
                var35 = 0.06642601
    else:
        if (input[155]) >= (1387.0):
            if (input[203]) >= (2042.0):
                var35 = 0.021905763
            else:
                var35 = -0.0784994
        else:
            if (input[153]) >= (1328.0):
                var35 = 0.08266515
            else:
                var35 = -0.045065895
    if (input[127]) >= (2429.0):
        var36 = -0.082029894
    else:
        if (input[95]) >= (1580.5):
            if (input[198]) >= (1215.5):
                var36 = 0.09140409
            else:
                var36 = -0.03414718
        else:
            if (input[93]) >= (1958.5):
                var36 = -0.078437984
            else:
                var36 = 0.027010633
    if (input[204]) >= (1321.5):
        if (input[141]) >= (1761.5):
            var37 = -0.07884002
        else:
            if (input[198]) >= (2443.5):
                var37 = -0.057936687
            else:
                var37 = 0.04740919
    else:
        if (input[88]) >= (1898.5):
            var37 = 0.061010975
        else:
            if (input[208]) >= (1257.0):
                var37 = 0.052438945
            else:
                var37 = -0.09299649
    if (input[76]) >= (1940.0):
        if (input[109]) >= (2210.5):
            var38 = 0.018316338
        else:
            var38 = -0.09541544
    else:
        if (input[51]) >= (1068.5):
            if (input[198]) >= (2443.5):
                var38 = -0.07575637
            else:
                var38 = 0.039064933
        else:
            if (input[37]) >= (1210.5):
                var38 = -0.084753
            else:
                var38 = -0.007870396
    if (input[208]) >= (1272.5):
        var39 = 0.07520169
    else:
        if (input[160]) >= (1252.5):
            if (input[38]) >= (2220.0):
                var39 = -0.021750798
            else:
                var39 = -0.09912824
        else:
            if (input[108]) >= (1787.5):
                var39 = 0.054677065
            else:
                var39 = -0.028694903
    if (input[204]) >= (1321.5):
        if (input[122]) >= (1412.5):
            if (input[256]) >= (25.0):
                var40 = 0.040338006
            else:
                var40 = -0.08918347
        else:
            if (input[169]) >= (1682.5):
                var40 = -0.054842062
            else:
                var40 = 0.057595234
    else:
        if (input[88]) >= (1898.5):
            var40 = 0.05712835
        else:
            if (input[89]) >= (1420.5):
                var40 = -0.09059387
            else:
                var40 = 0.03685018
    if (input[127]) >= (2417.5):
        var41 = -0.07625313
    else:
        if (input[95]) >= (1580.5):
            if (input[48]) >= (1214.5):
                var41 = 0.07607617
            else:
                var41 = -0.06408309
        else:
            if (input[93]) >= (1958.5):
                var41 = -0.07212951
            else:
                var41 = 0.025332082
    if (input[76]) >= (1940.0):
        if (input[109]) >= (2170.5):
            var42 = 0.008309065
        else:
            var42 = -0.09016579
    else:
        if (input[220]) >= (1852.0):
            if (input[198]) >= (2441.5):
                var42 = -0.018248275
            else:
                var42 = 0.0924443
        else:
            if (input[191]) >= (1229.5):
                var42 = 0.012320801
            else:
                var42 = -0.07054923
    if (input[141]) >= (1761.5):
        var43 = -0.080074735
    else:
        if (input[204]) >= (1321.5):
            if (input[188]) >= (1664.5):
                var43 = -0.07726674
            else:
                var43 = 0.038612496
        else:
            if (input[75]) >= (1235.5):
                var43 = -0.08586708
            else:
                var43 = 0.010833944
    if (input[208]) >= (1272.5):
        var44 = 0.07105582
    else:
        if (input[160]) >= (1252.5):
            if (input[38]) >= (2172.0):
                var44 = -0.02281147
            else:
                var44 = -0.09403874
        else:
            if (input[108]) >= (1787.5):
                var44 = 0.051705875
            else:
                var44 = -0.025715802
    if (input[127]) >= (2403.5):
        var45 = -0.07149931
    else:
        if (input[83]) >= (1097.5):
            if (input[188]) >= (1664.5):
                var45 = -0.07545229
            else:
                var45 = 0.0393396
        else:
            if (input[90]) >= (1279.5):
                var45 = 0.06094118
            else:
                var45 = -0.076333515
    var46 = (((((((((((((((((((((((((((((((((((((((((((((var0) + (var1)) + (var2)) + (var3)) + (var4)) + (var5)) + (var6)) + (var7)) + (var8)) + (var9)) + (var10)) + (var11)) + (var12)) + (var13)) + (var14)) + (var15)) + (var16)) + (var17)) + (var18)) + (var19)) + (var20)) + (var21)) + (var22)) + (var23)) + (var24)) + (var25)) + (var26)) + (var27)) + (var28)) + (var29)) + (var30)) + (var31)) + (var32)) + (var33)) + (var34)) + (var35)) + (var36)) + (var37)) + (var38)) + (var39)) + (var40)) + (var41)) + (var42)) + (var43)) + (var44)) + (var45)
    if (input[114]) >= (2403.0):
        if (input[129]) >= (1556.5):
            var47 = 0.009117897
        else:
            var47 = 0.07421271
    else:
        if (input[161]) >= (1313.5):
            if (input[143]) >= (1730.0):
                var47 = 0.040499624
            else:
                var47 = -0.079290695
        else:
            if (input[122]) >= (1681.5):
                var47 = -0.073126204
            else:
                var47 = 0.027588462
    if (input[38]) >= (2242.5):
        if (input[0]) >= (1225.5):
            var48 = 0.077751644
        else:
            if (input[57]) >= (1331.5):
                var48 = -0.06708883
            else:
                var48 = 0.05254499
    else:
        if (input[145]) >= (1296.5):
            if (input[18]) >= (2274.5):
                var48 = 0.00018353197
            else:
                var48 = -0.08666744
        else:
            if (input[203]) >= (1981.0):
                var48 = 0.06741565
            else:
                var48 = -0.021145593
    if (input[127]) >= (2429.0):
        var49 = -0.070383325
    else:
        if (input[51]) >= (1069.5):
            if (input[163]) >= (1084.5):
                var49 = 0.040971372
            else:
                var49 = -0.050099492
        else:
            if (input[134]) >= (2441.5):
                var49 = 0.016758379
            else:
                var49 = -0.07126587
    if (input[178]) >= (1316.0):
        if (input[198]) >= (2381.5):
            var50 = -0.029924843
        else:
            var50 = 0.076825105
    else:
        if (input[11]) >= (2436.0):
            if (input[256]) >= (25.5):
                var50 = -0.019524913
            else:
                var50 = -0.08914384
        else:
            if (input[95]) >= (1580.5):
                var50 = 0.049154773
            else:
                var50 = -0.03780026
    if (input[208]) >= (1272.5):
        var51 = 0.06656482
    else:
        if (input[160]) >= (1252.5):
            var51 = -0.07984579
        else:
            if (input[108]) >= (1787.5):
                var51 = 0.047187213
            else:
                var51 = -0.021082575
    if (input[220]) >= (1852.0):
        if (input[112]) >= (1218.0):
            if (input[198]) >= (2114.0):
                var52 = 0.015027547
            else:
                var52 = 0.08456163
        else:
            var52 = -0.06523781
    else:
        if (input[173]) >= (1251.0):
            if (input[75]) >= (1243.5):
                var52 = -0.07626512
            else:
                var52 = 0.003979908
        else:
            if (input[31]) >= (2408.5):
                var52 = -0.06319544
            else:
                var52 = 0.041579638
    if (input[208]) >= (1272.5):
        var53 = 0.064164385
    else:
        if (input[160]) >= (1253.5):
            var53 = -0.07625249
        else:
            if (input[108]) >= (1787.5):
                var53 = 0.043912347
            else:
                var53 = -0.020441761
    if (input[204]) >= (1346.0):
        if (input[122]) >= (1395.0):
            if (input[256]) >= (26.5):
                var54 = 0.055173248
            else:
                var54 = -0.08040275
        else:
            if (input[35]) >= (1063.5):
                var54 = -0.024040712
            else:
                var54 = 0.07015107
    else:
        if (input[121]) >= (1279.5):
            var54 = -0.07852223
        else:
            if (input[256]) >= (20.5):
                var54 = -0.05383253
            else:
                var54 = 0.045227803
    if (input[114]) >= (2403.0):
        var55 = 0.054308977
    else:
        if (input[155]) >= (1392.5):
            if (input[153]) >= (2420.5):
                var55 = 0.056065608
            else:
                var55 = -0.043305933
        else:
            if (input[153]) >= (1331.0):
                var55 = 0.072293766
            else:
                var55 = -0.026376322
    if (input[141]) >= (1761.5):
        var56 = -0.06749611
    else:
        if (input[204]) >= (1344.0):
            if (input[122]) >= (1395.0):
                var56 = -0.031031922
            else:
                var56 = 0.047304433
        else:
            if (input[89]) >= (1502.5):
                var56 = -0.051195234
            else:
                var56 = 0.034547206
    if (input[76]) >= (1940.0):
        if (input[12]) >= (1773.5):
            var57 = -0.07226188
        else:
            var57 = -0.009693878
    else:
        if (input[172]) >= (2046.5):
            var57 = 0.068416305
        else:
            if (input[55]) >= (1455.5):
                var57 = -0.05614167
            else:
                var57 = 0.015083845
    if (input[76]) >= (1940.0):
        if (input[223]) >= (1231.5):
            var58 = -0.00913073
        else:
            var58 = -0.07039006
    else:
        if (input[51]) >= (1057.5):
            if (input[83]) >= (1097.5):
                var58 = 0.04020469
            else:
                var58 = -0.034058865
        else:
            var58 = -0.065819964
    if (input[38]) >= (2242.5):
        if (input[118]) >= (2440.5):
            var59 = -0.023739966
        else:
            if (input[150]) >= (2438.5):
                var59 = 0.01528634
            else:
                var59 = 0.070873134
    else:
        if (input[145]) >= (1296.5):
            if (input[216]) >= (1277.5):
                var59 = -0.008814533
            else:
                var59 = -0.07511378
        else:
            if (input[203]) >= (1981.0):
                var59 = 0.05991515
            else:
                var59 = -0.016883267
    if (input[141]) >= (1761.5):
        var60 = -0.064413406
    else:
        if (input[204]) >= (1321.5):
            if (input[188]) >= (1664.5):
                var60 = -0.060908437
            else:
                var60 = 0.03443374
        else:
            if (input[88]) >= (1869.0):
                var60 = 0.031377546
            else:
                var60 = -0.052370615
    if (input[75]) >= (1236.5):
        if (input[256]) >= (27.5):
            if (input[157]) >= (2396.5):
                var61 = 0.08333459
            else:
                var61 = -0.0009321924
        else:
            if (input[122]) >= (1347.0):
                var61 = -0.09946596
            else:
                var61 = 0.0011621778
    else:
        if (input[57]) >= (1335.5):
            if (input[127]) >= (2061.0):
                var61 = 0.035101872
            else:
                var61 = -0.053369183
        else:
            var61 = 0.07028284
    if (input[38]) >= (2242.5):
        if (input[0]) >= (1225.5):
            var62 = 0.06700289
        else:
            if (input[57]) >= (1353.5):
                var62 = -0.05276659
            else:
                var62 = 0.035563968
    else:
        if (input[145]) >= (1296.5):
            if (input[216]) >= (1276.0):
                var62 = -0.011818178
            else:
                var62 = -0.0716325
        else:
            if (input[203]) >= (1981.0):
                var62 = 0.056343883
            else:
                var62 = -0.014578183
    if (input[127]) >= (2417.5):
        var63 = -0.057302635
    else:
        if (input[198]) >= (1904.0):
            if (input[191]) >= (1231.5):
                var63 = 0.048026722
            else:
                var63 = -0.06095919
        else:
            if (input[18]) >= (1238.5):
                var63 = 0.04209737
            else:
                var63 = -0.040661503
    if (input[51]) >= (1068.5):
        if (input[76]) >= (1941.0):
            var64 = -0.06066637
        else:
            if (input[198]) >= (2443.5):
                var64 = -0.05397573
            else:
                var64 = 0.033461243
    else:
        if (input[37]) >= (1210.5):
            var64 = -0.06893212
        else:
            var64 = 0.006744195
    if (input[220]) >= (1852.0):
        if (input[5]) >= (1222.5):
            var65 = -0.037249655
        else:
            var65 = 0.073202975
    else:
        if (input[191]) >= (1229.5):
            if (input[11]) >= (2437.5):
                var65 = -0.06089145
            else:
                var65 = 0.025280794
        else:
            if (input[60]) >= (1700.5):
                var65 = -0.07353711
            else:
                var65 = -0.011506353
    if (input[178]) >= (1316.0):
        if (input[64]) >= (1211.0):
            var66 = -0.009266419
        else:
            var66 = 0.06457874
    else:
        if (input[11]) >= (2436.0):
            var66 = -0.067797475
        else:
            if (input[95]) >= (1580.5):
                var66 = 0.03958357
            else:
                var66 = -0.029524958
    if (input[220]) >= (1852.0):
        if (input[5]) >= (1222.5):
            var67 = -0.033238422
        else:
            var67 = 0.07061361
    else:
        if (input[173]) >= (1251.0):
            if (input[75]) >= (1243.5):
                var67 = -0.062386364
            else:
                var67 = 0.0029814672
        else:
            if (input[31]) >= (2369.5):
                var67 = -0.047392476
            else:
                var67 = 0.03256398
    if (input[51]) >= (1068.5):
        if (input[76]) >= (1941.0):
            var68 = -0.054862466
        else:
            if (input[125]) >= (1519.0):
                var68 = 0.050690006
            else:
                var68 = -0.007994352
    else:
        if (input[37]) >= (1210.5):
            var68 = -0.066192634
        else:
            var68 = 0.0045857215
    if (input[208]) >= (1272.5):
        var69 = 0.0525267
    else:
        if (input[160]) >= (1253.5):
            var69 = -0.06230929
        else:
            if (input[108]) >= (1787.5):
                var69 = 0.03861591
            else:
                var69 = -0.017285228
    if (input[208]) >= (1272.5):
        var70 = 0.051098436
    else:
        if (input[160]) >= (1253.5):
            var70 = -0.05948804
        else:
            if (input[123]) >= (1602.5):
                var70 = 0.0146735525
            else:
                var70 = -0.04857036
    if (input[32]) >= (1257.0):
        if (input[75]) >= (1243.5):
            if (input[256]) >= (22.5):
                var71 = 0.04062713
            else:
                var71 = -0.045840472
        else:
            if (input[148]) >= (2434.5):
                var71 = 0.011467418
            else:
                var71 = 0.06767043
    else:
        if (input[178]) >= (1313.5):
            var71 = 0.042041685
        else:
            if (input[256]) >= (28.5):
                var71 = 0.027158344
            else:
                var71 = -0.056685705
    if (input[148]) >= (2438.5):
        if (input[172]) >= (1979.0):
            var72 = 0.017096251
        else:
            var72 = -0.06640398
    else:
        if (input[58]) >= (1319.0):
            if (input[256]) >= (27.5):
                var72 = 0.039293144
            else:
                var72 = -0.041258402
        else:
            if (input[72]) >= (1268.0):
                var72 = -0.022645794
            else:
                var72 = 0.060046393
    if (input[155]) >= (1392.5):
        if (input[199]) >= (1626.5):
            if (input[122]) >= (1350.0):
                var73 = -0.030743888
            else:
                var73 = 0.05313459
        else:
            if (input[11]) >= (1491.5):
                var73 = -0.06835937
            else:
                var73 = 0.031119809
    else:
        if (input[140]) >= (2415.0):
            var73 = 0.059730995
        else:
            var73 = -0.0064521576
    if (input[141]) >= (1761.5):
        var74 = -0.053370245
    else:
        if (input[48]) >= (1224.5):
            if (input[161]) >= (1313.5):
                var74 = -0.012869184
            else:
                var74 = 0.05610616
        else:
            if (input[178]) >= (1256.0):
                var74 = 0.037167583
            else:
                var74 = -0.053991515
    if (input[256]) >= (27.5):
        if (input[202]) >= (1220.5):
            var75 = 0.07626769
        else:
            var75 = -0.022860227
    else:
        if (input[74]) >= (1210.5):
            if (input[141]) >= (1436.5):
                var75 = -0.095757455
            else:
                var75 = -0.0124839
        else:
            if (input[191]) >= (1230.5):
                var75 = 0.044977844
            else:
                var75 = -0.01879555
    if (input[220]) >= (1852.0):
        if (input[5]) >= (1222.5):
            var76 = -0.028153304
        else:
            var76 = 0.06508037
    else:
        if (input[148]) >= (2435.5):
            if (input[38]) >= (2358.0):
                var76 = -0.006017548
            else:
                var76 = -0.06737708
        else:
            if (input[81]) >= (1422.0):
                var76 = 0.05533707
            else:
                var76 = -0.017130828
    if (input[256]) >= (27.5):
        if (input[202]) >= (1220.5):
            var77 = 0.07365665
        else:
            var77 = -0.021031564
    else:
        if (input[74]) >= (1210.5):
            if (input[141]) >= (1483.0):
                var77 = -0.091289416
            else:
                var77 = -0.012978327
        else:
            if (input[35]) >= (1059.5):
                var77 = -0.032366376
            else:
                var77 = 0.030733583
    if (input[105]) >= (1695.0):
        var78 = 0.042449947
    else:
        if (input[121]) >= (1283.5):
            if (input[113]) >= (1263.5):
                var78 = -0.0670743
            else:
                var78 = 0.010383245
        else:
            if (input[220]) >= (1216.5):
                var78 = 0.05952667
            else:
                var78 = -0.010976114
    if (input[256]) >= (27.5):
        if (input[202]) >= (1220.5):
            var79 = 0.07156729
        else:
            var79 = -0.019804962
    else:
        if (input[138]) >= (1288.5):
            var79 = -0.071358345
        else:
            if (input[252]) >= (1844.0):
                var79 = 0.03627787
            else:
                var79 = -0.023430165
    if (input[204]) >= (1346.0):
        if (input[122]) >= (1395.0):
            if (input[256]) >= (23.5):
                var80 = 0.02689355
            else:
                var80 = -0.059545565
        else:
            if (input[169]) >= (1682.5):
                var80 = -0.025363205
            else:
                var80 = 0.054078735
    else:
        if (input[1]) >= (1313.5):
            var80 = 0.01510412
        else:
            var80 = -0.051775526
    if (input[59]) >= (2251.5):
        if (input[203]) >= (2034.0):
            var81 = 0.024256842
        else:
            var81 = -0.059837814
    else:
        if (input[55]) >= (1391.5):
            if (input[198]) >= (1900.5):
                var81 = -0.046532314
            else:
                var81 = 0.014251264
        else:
            if (input[91]) >= (2278.0):
                var81 = 0.05802988
            else:
                var81 = 0.014156193
    if (input[220]) >= (1852.0):
        if (input[169]) >= (1741.5):
            var82 = -0.021700585
        else:
            var82 = 0.062150538
    else:
        if (input[191]) >= (1229.5):
            if (input[11]) >= (2437.5):
                var82 = -0.049561314
            else:
                var82 = 0.022242082
        else:
            var82 = -0.053026944
    if (input[256]) >= (27.5):
        if (input[202]) >= (1220.5):
            var83 = 0.067081176
        else:
            var83 = -0.01855294
    else:
        if (input[74]) >= (1210.5):
            if (input[134]) >= (2442.5):
                var83 = -0.08268747
            else:
                var83 = -0.015147758
        else:
            if (input[191]) >= (1230.5):
                var83 = 0.038732227
            else:
                var83 = -0.016389301
    if (input[220]) >= (1852.0):
        if (input[169]) >= (1741.5):
            var84 = -0.019835487
        else:
            var84 = 0.06078012
    else:
        if (input[148]) >= (2435.5):
            if (input[38]) >= (2216.5):
                var84 = -0.0126011195
            else:
                var84 = -0.058960408
        else:
            if (input[81]) >= (1422.0):
                var84 = 0.049673725
            else:
                var84 = -0.015991
    if (input[59]) >= (2251.5):
        if (input[203]) >= (2034.0):
            var85 = 0.022308175
        else:
            var85 = -0.056836363
    else:
        if (input[220]) >= (1215.5):
            if (input[198]) >= (2371.5):
                var85 = -0.02794148
            else:
                var85 = 0.06435677
        else:
            if (input[230]) >= (1211.5):
                var85 = -0.041186135
            else:
                var85 = 0.0213426
    if (input[256]) >= (27.5):
        if (input[138]) >= (1236.0):
            var86 = 0.06250026
        else:
            var86 = -0.014328338
    else:
        if (input[74]) >= (1210.5):
            var86 = -0.06282481
        else:
            if (input[35]) >= (1059.5):
                var86 = -0.029025778
            else:
                var86 = 0.027429242
    if (input[55]) >= (1376.5):
        if (input[199]) >= (1627.0):
            if (input[122]) >= (1350.0):
                var87 = -0.019910162
            else:
                var87 = 0.039925527
        else:
            if (input[202]) >= (1208.5):
                var87 = 0.0005956716
            else:
                var87 = -0.065423794
    else:
        if (input[61]) >= (2390.5):
            var87 = 0.057721462
        else:
            var87 = -0.018278366
    if (input[256]) >= (27.5):
        var88 = 0.031076605
    else:
        if (input[138]) >= (1288.5):
            var88 = -0.06318667
        else:
            if (input[252]) >= (1844.0):
                var88 = 0.03233203
            else:
                var88 = -0.021655796
    if (input[55]) >= (1376.5):
        if (input[199]) >= (1627.0):
            if (input[192]) >= (1241.5):
                var89 = -0.028078139
            else:
                var89 = 0.03176675
        else:
            if (input[202]) >= (1208.5):
                var89 = -0.00036894364
            else:
                var89 = -0.06335201
    else:
        if (input[61]) >= (2390.5):
            var89 = 0.05584923
        else:
            var89 = -0.016849844
    if (input[114]) >= (2403.0):
        var90 = 0.038881246
    else:
        if (input[156]) >= (2103.0):
            if (input[159]) >= (1533.5):
                var90 = -0.022130966
            else:
                var90 = 0.038102876
        else:
            var90 = -0.049167354
    if (input[256]) >= (27.5):
        var91 = 0.030108342
    else:
        if (input[74]) >= (1210.5):
            var91 = -0.057652444
        else:
            if (input[35]) >= (1059.5):
                var91 = -0.026711887
            else:
                var91 = 0.025124257
    if (input[204]) >= (1346.0):
        if (input[159]) >= (1757.5):
            var92 = -0.03360907
        else:
            if (input[56]) >= (1377.0):
                var92 = -0.0042542424
            else:
                var92 = 0.050950628
    else:
        if (input[1]) >= (1313.5):
            var92 = 0.011976983
        else:
            var92 = -0.045025412
    if (input[59]) >= (2251.5):
        if (input[203]) >= (2034.0):
            var93 = 0.019150559
        else:
            var93 = -0.05378933
    else:
        if (input[220]) >= (1215.5):
            if (input[198]) >= (1906.0):
                var93 = -0.016056526
            else:
                var93 = 0.06223557
        else:
            if (input[156]) >= (2101.0):
                var93 = 0.012513152
            else:
                var93 = -0.049094416
    if (input[148]) >= (2436.5):
        if (input[198]) >= (1794.0):
            var94 = -0.048483036
        else:
            var94 = 0.0045458376
    else:
        if (input[11]) >= (1566.5):
            if (input[256]) >= (27.5):
                var94 = 0.036190256
            else:
                var94 = -0.026046593
        else:
            var94 = 0.04674243
    if (input[148]) >= (2438.5):
        var95 = -0.03103797
    else:
        if (input[133]) >= (1208.5):
            if (input[125]) >= (1527.5):
                var95 = 0.04855949
            else:
                var95 = 0.002831283
        else:
            if (input[256]) >= (26.5):
                var95 = 0.036887214
            else:
                var95 = -0.035817903
    if (input[59]) >= (2251.5):
        if (input[203]) >= (2034.0):
            var96 = 0.018484531
        else:
            var96 = -0.051487017
    else:
        if (input[220]) >= (1215.5):
            if (input[198]) >= (1906.0):
                var96 = -0.014595012
            else:
                var96 = 0.05997175
        else:
            if (input[156]) >= (2101.0):
                var96 = 0.012744113
            else:
                var96 = -0.04753786
    if (input[148]) >= (2436.5):
        if (input[198]) >= (1794.0):
            var97 = -0.04623792
        else:
            var97 = 0.0049772966
    else:
        if (input[48]) >= (1225.5):
            if (input[75]) >= (1243.5):
                var97 = -0.0008738718
            else:
                var97 = 0.049358416
        else:
            if (input[22]) >= (1501.5):
                var97 = -0.04394522
            else:
                var97 = 0.010191636
    if (input[51]) >= (1068.5):
        if (input[129]) >= (1253.5):
            if (input[256]) >= (23.5):
                var98 = 0.031064093
            else:
                var98 = -0.03291733
        else:
            if (input[48]) >= (1223.5):
                var98 = 0.05034236
            else:
                var98 = -0.0068361657
    else:
        var98 = -0.03001879
    if (input[204]) >= (1346.0):
        if (input[122]) >= (1395.0):
            if (input[85]) >= (1207.5):
                var99 = -0.037245575
            else:
                var99 = 0.0070103738
        else:
            if (input[169]) >= (1680.0):
                var99 = -0.015762307
            else:
                var99 = 0.04614975
    else:
        if (input[48]) >= (1334.0):
            var99 = 0.008353619
        else:
            var99 = -0.043323804
    if (input[220]) >= (1852.0):
        var100 = 0.026853422
    else:
        if (input[148]) >= (2435.5):
            var100 = -0.043416332
        else:
            if (input[256]) >= (20.5):
                var100 = -0.019037705
            else:
                var100 = 0.034694683
    var101 = (1.0) / ((1.0) + (math.exp((0.0) - (((((((((((((((((((((((((((((((((((((((((((((((((((((((var46) + (var47)) + (var48)) + (var49)) + (var50)) + (var51)) + (var52)) + (var53)) + (var54)) + (var55)) + (var56)) + (var57)) + (var58)) + (var59)) + (var60)) + (var61)) + (var62)) + (var63)) + (var64)) + (var65)) + (var66)) + (var67)) + (var68)) + (var69)) + (var70)) + (var71)) + (var72)) + (var73)) + (var74)) + (var75)) + (var76)) + (var77)) + (var78)) + (var79)) + (var80)) + (var81)) + (var82)) + (var83)) + (var84)) + (var85)) + (var86)) + (var87)) + (var88)) + (var89)) + (var90)) + (var91)) + (var92)) + (var93)) + (var94)) + (var95)) + (var96)) + (var97)) + (var98)) + (var99)) + (var100)))))
    return [(1.0) - (var101), var101]

def score_solo_itchy_5(input):
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1237.5):
            if (input[156]) >= (2061.5):
                var0 = 0.19111112
            else:
                var0 = -0.06666667
        else:
            if (input[143]) >= (1356.5):
                var0 = -0.15744682
            else:
                var0 = 0.0278481
    else:
        if (input[41]) >= (1222.5):
            var0 = -0.1974026
        else:
            var0 = 0.15555556
    if (input[112]) >= (2434.5):
        if (input[22]) >= (1553.0):
            if (input[24]) >= (1452.0):
                var1 = 0.059185088
            else:
                var1 = 0.18127201
        else:
            if (input[171]) >= (1911.0):
                var1 = -0.15364039
            else:
                var1 = 0.085381486
    else:
        if (input[105]) >= (1977.5):
            var1 = 0.17228661
        else:
            if (input[247]) >= (1254.0):
                var1 = 0.1010608
            else:
                var1 = -0.16477688
    if (input[112]) >= (2434.5):
        if (input[22]) >= (1553.0):
            if (input[25]) >= (1750.0):
                var2 = 0.051158518
            else:
                var2 = 0.16740881
        else:
            if (input[171]) >= (1911.0):
                var2 = -0.14272468
            else:
                var2 = 0.078203306
    else:
        if (input[105]) >= (1977.5):
            var2 = 0.15956116
        else:
            if (input[115]) >= (1008.5):
                var2 = -0.15848012
            else:
                var2 = 0.042109188
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[156]) >= (2061.5):
                var3 = 0.15720096
            else:
                var3 = -0.053025838
        else:
            if (input[54]) >= (2435.5):
                var3 = 0.06644291
            else:
                var3 = -0.11806752
    else:
        if (input[41]) >= (1222.5):
            var3 = -0.15733577
        else:
            var3 = 0.12297874
    if (input[196]) >= (1303.5):
        if (input[93]) >= (1649.5):
            if (input[125]) >= (2082.5):
                var4 = 0.124467745
            else:
                var4 = -0.06829684
        else:
            if (input[194]) >= (2190.5):
                var4 = -0.13308625
            else:
                var4 = 0.14303231
    else:
        if (input[41]) >= (1222.5):
            var4 = -0.14869222
        else:
            var4 = 0.116682254
    if (input[112]) >= (2434.5):
        if (input[194]) >= (2190.5):
            var5 = -0.12481838
        else:
            if (input[120]) >= (2107.5):
                var5 = -0.102300525
            else:
                var5 = 0.13540348
    else:
        if (input[105]) >= (1960.5):
            if (input[224]) >= (1209.5):
                var5 = 0.007861193
            else:
                var5 = 0.13942032
        else:
            if (input[115]) >= (1011.5):
                var5 = -0.13709308
            else:
                var5 = 0.028551186
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[156]) >= (2061.5):
                var6 = 0.13836384
            else:
                var6 = -0.04300749
        else:
            if (input[54]) >= (2436.5):
                var6 = 0.08102759
            else:
                var6 = -0.093440734
    else:
        if (input[41]) >= (1222.5):
            var6 = -0.13609861
        else:
            var6 = 0.10524183
    if (input[112]) >= (2434.5):
        if (input[194]) >= (2190.5):
            var7 = -0.116593674
        else:
            if (input[120]) >= (2107.5):
                var7 = -0.094039954
            else:
                var7 = 0.12474944
    else:
        if (input[105]) >= (1977.5):
            var7 = 0.12680826
        else:
            if (input[115]) >= (1015.5):
                var7 = -0.12815292
            else:
                var7 = 0.0120276855
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[156]) >= (2061.5):
                var8 = 0.12956226
            else:
                var8 = -0.036082506
        else:
            if (input[54]) >= (2436.5):
                var8 = 0.070257455
            else:
                var8 = -0.08447596
    else:
        if (input[41]) >= (1222.5):
            var8 = -0.12714456
        else:
            var8 = 0.096152715
    if (input[196]) >= (1303.5):
        if (input[93]) >= (1649.5):
            if (input[54]) >= (2282.0):
                var9 = 0.07964262
            else:
                var9 = -0.06256657
        else:
            if (input[194]) >= (2190.5):
                var9 = -0.10979052
            else:
                var9 = 0.11972586
    else:
        if (input[41]) >= (1222.5):
            var9 = -0.123519816
        else:
            var9 = 0.092646934
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[156]) >= (2061.5):
                var10 = 0.12266477
            else:
                var10 = -0.032411948
        else:
            if (input[199]) >= (1990.5):
                var10 = -0.11744435
            else:
                var10 = 0.0065505663
    else:
        if (input[41]) >= (1222.5):
            var10 = -0.12037692
        else:
            var10 = 0.089402646
    if (input[112]) >= (2434.5):
        if (input[22]) >= (1553.0):
            if (input[25]) >= (1739.5):
                var11 = 0.027650854
            else:
                var11 = 0.12377226
        else:
            if (input[25]) >= (1376.5):
                var11 = 0.08818222
            else:
                var11 = -0.0813276
    else:
        if (input[105]) >= (1977.5):
            var11 = 0.114350915
        else:
            if (input[115]) >= (1015.5):
                var11 = -0.11482568
            else:
                var11 = 0.013739456
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[156]) >= (2061.5):
                var12 = 0.117184415
            else:
                var12 = -0.02723786
        else:
            if (input[204]) >= (1537.5):
                var12 = -0.11442467
            else:
                var12 = 0.00398915
    else:
        if (input[41]) >= (1222.5):
            var12 = -0.115326576
        else:
            var12 = 0.08234348
    if (input[144]) >= (1265.0):
        if (input[38]) >= (2018.5):
            if (input[65]) >= (2348.5):
                var13 = -0.100733094
            else:
                var13 = 0.09816921
        else:
            if (input[105]) >= (1984.0):
                var13 = 0.10324903
            else:
                var13 = -0.06904105
    else:
        if (input[185]) >= (1703.5):
            var13 = 0.10444384
        else:
            var13 = -0.11621106
    if (input[112]) >= (2434.5):
        if (input[194]) >= (2190.5):
            var14 = -0.10155671
        else:
            if (input[120]) >= (2107.5):
                var14 = -0.07309043
            else:
                var14 = 0.10310596
    else:
        if (input[63]) >= (2062.5):
            var14 = -0.11489596
        else:
            if (input[155]) >= (1971.0):
                var14 = 0.06469022
            else:
                var14 = -0.06808144
    if (input[88]) >= (1396.0):
        if (input[56]) >= (1999.0):
            var15 = 0.009954675
        else:
            var15 = -0.112816624
    else:
        if (input[93]) >= (1649.5):
            if (input[11]) >= (1704.5):
                var15 = -0.108137466
            else:
                var15 = 0.010963003
        else:
            if (input[194]) >= (2190.5):
                var15 = -0.097094886
            else:
                var15 = 0.10947217
    if (input[196]) >= (1303.5):
        if (input[185]) >= (1232.5):
            if (input[65]) >= (1319.0):
                var16 = -0.0086950455
            else:
                var16 = 0.1220876
        else:
            if (input[199]) >= (1990.5):
                var16 = -0.103276394
            else:
                var16 = 0.0016566542
    else:
        if (input[41]) >= (1222.5):
            var16 = -0.10788175
        else:
            var16 = 0.07148123
    if (input[144]) >= (1265.0):
        if (input[121]) >= (1331.0):
            if (input[249]) >= (1229.5):
                var17 = 0.08349343
            else:
                var17 = -0.04509772
        else:
            var17 = 0.1110987
    else:
        if (input[185]) >= (1703.5):
            var17 = 0.09401615
        else:
            var17 = -0.109554365
    if (input[144]) >= (1265.0):
        if (input[121]) >= (1331.0):
            if (input[249]) >= (1229.5):
                var18 = 0.07903021
            else:
                var18 = -0.041277092
        else:
            if (input[88]) >= (1389.5):
                var18 = 0.035391923
            else:
                var18 = 0.112855665
    else:
        if (input[185]) >= (1703.5):
            var18 = 0.09155745
        else:
            var18 = -0.10804331
    if (input[144]) >= (1265.0):
        if (input[121]) >= (1331.0):
            if (input[63]) >= (2062.5):
                var19 = -0.1077533
            else:
                var19 = 0.014253834
        else:
            if (input[88]) >= (1389.5):
                var19 = 0.033793714
            else:
                var19 = 0.11006036
    else:
        if (input[185]) >= (1703.5):
            var19 = 0.08920368
        else:
            var19 = -0.106639825
    if (input[88]) >= (1396.0):
        if (input[56]) >= (1999.0):
            var20 = 0.008346413
        else:
            var20 = -0.10572795
    else:
        if (input[38]) >= (2146.0):
            if (input[256]) >= (25.5):
                var20 = -0.028069908
            else:
                var20 = 0.10208347
        else:
            if (input[63]) >= (2062.5):
                var20 = -0.10608562
            else:
                var20 = 0.018540893
    if (input[88]) >= (1396.0):
        if (input[56]) >= (1999.0):
            var21 = 0.007779711
        else:
            var21 = -0.104296386
    else:
        if (input[147]) >= (1182.5):
            var21 = -0.095697604
        else:
            if (input[251]) >= (1235.5):
                var21 = 0.07501885
            else:
                var21 = -0.018686755
    if (input[196]) >= (1303.5):
        if (input[83]) >= (1100.5):
            if (input[21]) >= (1208.5):
                var22 = 0.107398145
            else:
                var22 = -0.055589754
        else:
            if (input[204]) >= (1376.5):
                var22 = -0.08135364
            else:
                var22 = 0.025831625
    else:
        if (input[41]) >= (1222.5):
            var22 = -0.100286305
        else:
            var22 = 0.05676044
    if (input[88]) >= (1396.0):
        if (input[56]) >= (1999.0):
            var23 = 0.0054985
        else:
            var23 = -0.10200713
    else:
        if (input[246]) >= (1223.5):
            if (input[73]) >= (1409.5):
                var23 = -0.07083155
            else:
                var23 = 0.09413889
        else:
            if (input[105]) >= (1977.5):
                var23 = 0.09636357
            else:
                var23 = -0.038380276
    if (input[196]) >= (1303.5):
        if (input[61]) >= (2435.5):
            if (input[199]) >= (2446.5):
                var24 = -0.07783308
            else:
                var24 = 0.08396715
        else:
            if (input[230]) >= (1352.0):
                var24 = -0.090631664
            else:
                var24 = 0.009436092
    else:
        if (input[12]) >= (1460.5):
            var24 = -0.098303825
        else:
            var24 = 0.049471505
    if (input[88]) >= (1396.0):
        if (input[56]) >= (1999.0):
            var25 = 0.0044851503
        else:
            var25 = -0.100016356
    else:
        if (input[185]) >= (1219.5):
            if (input[60]) >= (2181.5):
                var25 = -0.02453408
            else:
                var25 = 0.08817996
        else:
            if (input[121]) >= (1273.0):
                var25 = -0.10024065
            else:
                var25 = 0.052026458
    if (input[144]) >= (1265.0):
        if (input[121]) >= (1331.0):
            if (input[249]) >= (1229.5):
                var26 = 0.06950859
            else:
                var26 = -0.033537783
        else:
            var26 = 0.09539303
    else:
        if (input[185]) >= (1703.5):
            var26 = 0.077597365
        else:
            var26 = -0.09986482
    if (input[144]) >= (1265.0):
        if (input[65]) >= (2297.0):
            var27 = -0.10512691
        else:
            if (input[38]) >= (1909.5):
                var27 = 0.06268152
            else:
                var27 = -0.012485745
    else:
        if (input[185]) >= (1703.5):
            var27 = 0.07564478
        else:
            var27 = -0.09876674
    if (input[105]) >= (1977.5):
        var28 = 0.0928799
    else:
        if (input[112]) >= (2434.5):
            if (input[19]) >= (1172.5):
                var28 = -0.02333573
            else:
                var28 = 0.09503622
        else:
            if (input[127]) >= (1377.5):
                var28 = -0.09318766
            else:
                var28 = 0.009437374
    if (input[88]) >= (1396.0):
        if (input[118]) >= (2443.5):
            var29 = 0.0085484
        else:
            var29 = -0.09383576
    else:
        if (input[155]) >= (1708.0):
            if (input[127]) >= (1377.5):
                var29 = -0.01811372
            else:
                var29 = 0.08224719
        else:
            if (input[121]) >= (1273.0):
                var29 = -0.075089544
            else:
                var29 = 0.06989875
    if (input[105]) >= (1977.5):
        var30 = 0.09038668
    else:
        if (input[112]) >= (2434.5):
            if (input[226]) >= (1234.5):
                var30 = -0.07058279
            else:
                var30 = 0.065288864
        else:
            if (input[115]) >= (1015.5):
                var30 = -0.08793529
            else:
                var30 = 0.013355873
    if (input[61]) >= (2432.5):
        if (input[178]) >= (1229.5):
            if (input[66]) >= (1907.5):
                var31 = -0.0774206
            else:
                var31 = 0.08687052
        else:
            if (input[125]) >= (2082.5):
                var31 = 0.057598215
            else:
                var31 = -0.049430262
    else:
        if (input[125]) >= (1315.5):
            var31 = -0.09788394
        else:
            var31 = 0.06921952
    if (input[147]) >= (1173.5):
        if (input[167]) >= (1834.5):
            var32 = 0.06458412
        else:
            if (input[190]) >= (1186.5):
                var32 = -0.09610354
            else:
                var32 = 0.022064082
    else:
        if (input[185]) >= (1219.5):
            if (input[60]) >= (2181.5):
                var32 = -0.016972486
            else:
                var32 = 0.07477177
        else:
            if (input[248]) >= (1739.5):
                var32 = 0.034847215
            else:
                var32 = -0.08526074
    if (input[105]) >= (1977.5):
        var33 = 0.087717615
    else:
        if (input[144]) >= (2438.5):
            if (input[92]) >= (2324.0):
                var33 = 0.10991629
            else:
                var33 = -0.018189719
        else:
            if (input[183]) >= (2303.0):
                var33 = 0.050264474
            else:
                var33 = -0.04995873
    if (input[144]) >= (1265.0):
        if (input[196]) >= (2442.5):
            if (input[41]) >= (1607.0):
                var34 = 0.041269805
            else:
                var34 = -0.09581652
        else:
            if (input[224]) >= (1209.5):
                var34 = -0.057446
            else:
                var34 = 0.05336938
    else:
        if (input[185]) >= (1703.5):
            var34 = 0.06486371
        else:
            var34 = -0.093390346
    if (input[61]) >= (2432.5):
        if (input[185]) >= (1232.5):
            if (input[67]) >= (1150.5):
                var35 = 0.09287427
            else:
                var35 = -0.009619988
        else:
            if (input[228]) >= (1167.5):
                var35 = -0.04826858
            else:
                var35 = 0.08771011
    else:
        if (input[125]) >= (1315.5):
            var35 = -0.09399127
        else:
            var35 = 0.06403353
    if (input[105]) >= (1977.5):
        var36 = 0.08368852
    else:
        if (input[144]) >= (2438.5):
            if (input[92]) >= (2379.5):
                var36 = 0.1022694
            else:
                var36 = -0.009800109
        else:
            if (input[167]) >= (1761.0):
                var36 = 0.025427416
            else:
                var36 = -0.050194155
    if (input[144]) >= (1265.0):
        if (input[65]) >= (2297.0):
            var37 = -0.0872378
        else:
            if (input[4]) >= (1223.5):
                var37 = 0.047144584
            else:
                var37 = -0.013199406
    else:
        if (input[185]) >= (1703.5):
            var37 = 0.0598854
        else:
            var37 = -0.09087558
    if (input[185]) >= (1219.5):
        if (input[60]) >= (2181.5):
            if (input[112]) >= (1806.0):
                var38 = -0.08151397
            else:
                var38 = 0.019089717
        else:
            if (input[256]) >= (24.5):
                var38 = -0.083122276
            else:
                var38 = 0.11013841
    else:
        if (input[121]) >= (1272.5):
            if (input[256]) >= (21.5):
                var38 = -0.016672047
            else:
                var38 = -0.095793806
        else:
            var38 = 0.024221139
    if (input[61]) >= (2432.5):
        if (input[185]) >= (1232.5):
            if (input[224]) >= (1209.5):
                var39 = -0.039068457
            else:
                var39 = 0.07321047
        else:
            if (input[228]) >= (1167.5):
                var39 = -0.04124644
            else:
                var39 = 0.08006601
    else:
        if (input[125]) >= (1315.5):
            var39 = -0.09048159
        else:
            var39 = 0.058335524
    if (input[147]) >= (1173.5):
        if (input[256]) >= (27.5):
            var40 = 0.059913732
        else:
            if (input[167]) >= (1834.5):
                var40 = 0.053498425
            else:
                var40 = -0.08566694
    else:
        if (input[185]) >= (1219.5):
            if (input[256]) >= (24.5):
                var40 = -0.043691207
            else:
                var40 = 0.057573713
        else:
            if (input[55]) >= (1451.5):
                var40 = 0.01540103
            else:
                var40 = -0.08649266
    if (input[61]) >= (2432.5):
        if (input[18]) >= (1997.5):
            if (input[23]) >= (1909.0):
                var41 = 0.009351937
            else:
                var41 = 0.08949333
        else:
            if (input[63]) >= (2062.5):
                var41 = -0.079443924
            else:
                var41 = 0.014257311
    else:
        if (input[125]) >= (1315.5):
            var41 = -0.088309005
        else:
            var41 = 0.05526481
    if (input[12]) >= (1813.5):
        if (input[122]) >= (1808.0):
            var42 = 0.019457866
        else:
            var42 = -0.08469477
    else:
        if (input[185]) >= (1232.5):
            if (input[224]) >= (1209.5):
                var42 = -0.04951274
            else:
                var42 = 0.073529564
        else:
            if (input[256]) >= (25.5):
                var42 = -0.100770056
            else:
                var42 = -0.0015729625
    if (input[105]) >= (1977.5):
        var43 = 0.07684205
    else:
        if (input[147]) >= (1173.5):
            if (input[256]) >= (27.5):
                var43 = 0.054288704
            else:
                var43 = -0.08193592
        else:
            if (input[23]) >= (1240.5):
                var43 = 0.023178408
            else:
                var43 = -0.06309184
    if (input[88]) >= (1354.5):
        if (input[256]) >= (19.5):
            if (input[81]) >= (2422.5):
                var44 = 0.09638315
            else:
                var44 = -0.06588332
        else:
            if (input[60]) >= (2140.5):
                var44 = -0.10617425
            else:
                var44 = -0.020042762
    else:
        if (input[224]) >= (1209.5):
            if (input[64]) >= (2150.5):
                var44 = -0.08770244
            else:
                var44 = 0.027285744
        else:
            if (input[199]) >= (2444.5):
                var44 = -0.059582677
            else:
                var44 = 0.03973947
    if (input[185]) >= (1219.5):
        if (input[60]) >= (2181.5):
            if (input[256]) >= (19.5):
                var45 = 0.036054395
            else:
                var45 = -0.05900395
        else:
            if (input[256]) >= (24.5):
                var45 = -0.07815515
            else:
                var45 = 0.10240688
    else:
        if (input[121]) >= (1272.5):
            if (input[256]) >= (19.5):
                var45 = -0.021113276
            else:
                var45 = -0.08821452
        else:
            var45 = 0.024883362
    var46 = (((((((((((((((((((((((((((((((((((((((((((((var0) + (var1)) + (var2)) + (var3)) + (var4)) + (var5)) + (var6)) + (var7)) + (var8)) + (var9)) + (var10)) + (var11)) + (var12)) + (var13)) + (var14)) + (var15)) + (var16)) + (var17)) + (var18)) + (var19)) + (var20)) + (var21)) + (var22)) + (var23)) + (var24)) + (var25)) + (var26)) + (var27)) + (var28)) + (var29)) + (var30)) + (var31)) + (var32)) + (var33)) + (var34)) + (var35)) + (var36)) + (var37)) + (var38)) + (var39)) + (var40)) + (var41)) + (var42)) + (var43)) + (var44)) + (var45)
    if (input[61]) >= (2432.5):
        if (input[18]) >= (1997.5):
            if (input[193]) >= (1258.5):
                var47 = 0.083783805
            else:
                var47 = 0.014754851
        else:
            if (input[63]) >= (2062.5):
                var47 = -0.074955694
            else:
                var47 = 0.01226858
    else:
        if (input[157]) >= (1321.5):
            var47 = -0.08354937
        else:
            var47 = 0.044438068
    if (input[105]) >= (1977.5):
        var48 = 0.074353255
    else:
        if (input[144]) >= (2438.5):
            if (input[178]) >= (1235.5):
                var48 = 0.0029724918
            else:
                var48 = 0.08147377
        else:
            if (input[167]) >= (1750.5):
                var48 = 0.02468778
            else:
                var48 = -0.040932503
    if (input[155]) >= (1708.5):
        if (input[60]) >= (2181.5):
            if (input[112]) >= (1806.0):
                var49 = -0.07739695
            else:
                var49 = 0.032586597
        else:
            if (input[256]) >= (24.5):
                var49 = -0.04127082
            else:
                var49 = 0.09456017
    else:
        if (input[0]) >= (1303.5):
            var49 = 0.059117675
        else:
            if (input[85]) >= (1221.5):
                var49 = 0.037736207
            else:
                var49 = -0.08201067
    if (input[61]) >= (2432.5):
        if (input[83]) >= (1098.5):
            if (input[99]) >= (1058.5):
                var50 = 0.08369753
            else:
                var50 = -0.026948417
        else:
            if (input[256]) >= (9.5):
                var50 = 0.016107257
            else:
                var50 = -0.070796184
    else:
        if (input[125]) >= (1324.0):
            var50 = -0.08086547
        else:
            var50 = 0.034059644
    if (input[105]) >= (1977.5):
        var51 = 0.07115955
    else:
        if (input[124]) >= (1919.5):
            if (input[112]) >= (2419.0):
                var51 = 0.04786795
            else:
                var51 = -0.07858309
        else:
            if (input[256]) >= (8.5):
                var51 = 0.042878397
            else:
                var51 = -0.06426897
    if (input[125]) >= (2140.0):
        var52 = 0.066221505
    else:
        if (input[193]) >= (1273.5):
            if (input[196]) >= (1958.0):
                var52 = -0.028355638
            else:
                var52 = 0.041186374
        else:
            if (input[180]) >= (1448.0):
                var52 = 0.018551074
            else:
                var52 = -0.08036266
    if (input[125]) >= (2140.0):
        var53 = 0.06394281
    else:
        if (input[193]) >= (1273.5):
            if (input[196]) >= (2442.0):
                var53 = -0.047025204
            else:
                var53 = 0.02422418
        else:
            if (input[180]) >= (1448.0):
                var53 = 0.017626228
            else:
                var53 = -0.07834836
    if (input[88]) >= (1354.5):
        if (input[256]) >= (19.5):
            if (input[81]) >= (2422.5):
                var54 = 0.084462695
            else:
                var54 = -0.05554403
        else:
            var54 = -0.08861577
    else:
        if (input[224]) >= (1209.5):
            if (input[64]) >= (2150.5):
                var54 = -0.080401026
            else:
                var54 = 0.024522325
        else:
            if (input[196]) >= (2442.5):
                var54 = -0.027051467
            else:
                var54 = 0.044451132
    if (input[147]) >= (1173.5):
        if (input[256]) >= (27.5):
            var55 = 0.059227973
        else:
            if (input[32]) >= (1294.0):
                var55 = 0.032127414
            else:
                var55 = -0.08433364
    else:
        if (input[169]) >= (1725.0):
            if (input[115]) >= (1015.5):
                var55 = -0.0062138042
            else:
                var55 = 0.096726894
        else:
            if (input[182]) >= (1225.5):
                var55 = 0.02174233
            else:
                var55 = -0.065927915
    if (input[105]) >= (1977.5):
        var56 = 0.06607841
    else:
        if (input[144]) >= (2438.5):
            if (input[6]) >= (1230.5):
                var56 = 0.013262376
            else:
                var56 = 0.068942085
        else:
            if (input[121]) >= (1272.5):
                var56 = -0.02823623
            else:
                var56 = 0.042291287
    if (input[61]) >= (2432.5):
        if (input[178]) >= (1229.5):
            if (input[138]) >= (1208.5):
                var57 = 0.08187141
            else:
                var57 = -0.017927276
        else:
            if (input[125]) >= (2151.5):
                var57 = 0.0604015
            else:
                var57 = -0.02280639
    else:
        if (input[246]) >= (1223.5):
            var57 = 0.021867288
        else:
            var57 = -0.07623563
    if (input[125]) >= (2140.0):
        var58 = 0.060588617
    else:
        if (input[193]) >= (1273.5):
            if (input[196]) >= (1958.0):
                var58 = -0.023753636
            else:
                var58 = 0.035229724
        else:
            if (input[180]) >= (1415.0):
                var58 = 0.011880933
            else:
                var58 = -0.07301926
    if (input[88]) >= (1354.5):
        if (input[256]) >= (19.5):
            if (input[81]) >= (2422.5):
                var59 = 0.08069099
            else:
                var59 = -0.05135413
        else:
            var59 = -0.085847914
    else:
        if (input[67]) >= (1150.5):
            if (input[256]) >= (24.5):
                var59 = -0.04753777
            else:
                var59 = 0.058675885
        else:
            if (input[256]) >= (27.5):
                var59 = 0.10618436
            else:
                var59 = -0.0707833
    if (input[61]) >= (2432.5):
        if (input[4]) >= (1223.5):
            if (input[23]) >= (1240.5):
                var60 = 0.05527101
            else:
                var60 = -0.048871562
        else:
            if (input[256]) >= (9.5):
                var60 = 0.006398309
            else:
                var60 = -0.08137803
    else:
        if (input[246]) >= (1223.5):
            var60 = 0.01912379
        else:
            var60 = -0.07359051
    if (input[147]) >= (1173.5):
        if (input[256]) >= (27.5):
            var61 = 0.052531432
        else:
            if (input[83]) >= (1098.0):
                var61 = 0.010322356
            else:
                var61 = -0.08872002
    else:
        if (input[256]) >= (24.5):
            if (input[170]) >= (1207.5):
                var61 = 0.0720863
            else:
                var61 = -0.10317329
        else:
            if (input[256]) >= (8.5):
                var61 = 0.06254542
            else:
                var61 = -0.024046952
    if (input[63]) >= (2062.5):
        if (input[112]) >= (2435.5):
            var62 = 0.04975156
        else:
            var62 = -0.078003734
    else:
        if (input[201]) >= (2056.0):
            var62 = 0.08541146
        else:
            if (input[256]) >= (8.5):
                var62 = 0.018559733
            else:
                var62 = -0.0555842
    if (input[63]) >= (2062.5):
        if (input[112]) >= (2434.5):
            var63 = 0.0440216
        else:
            var63 = -0.0786746
    else:
        if (input[201]) >= (2056.0):
            var63 = 0.0832138
        else:
            if (input[256]) >= (8.5):
                var63 = 0.01684553
            else:
                var63 = -0.051720977
    if (input[144]) >= (2438.5):
        var64 = 0.053023946
    else:
        if (input[125]) >= (2140.0):
            var64 = 0.055826288
        else:
            if (input[196]) >= (1958.0):
                var64 = -0.04540392
            else:
                var64 = 0.0028320558
    if (input[61]) >= (2432.5):
        if (input[239]) >= (1218.5):
            if (input[33]) >= (1204.5):
                var65 = 0.0069226674
            else:
                var65 = -0.058837604
        else:
            if (input[155]) >= (1742.0):
                var65 = 0.087744124
            else:
                var65 = -0.027668744
    else:
        if (input[89]) >= (1479.5):
            var65 = -0.06938859
        else:
            var65 = 0.012227778
    if (input[36]) >= (2438.5):
        if (input[112]) >= (2436.5):
            var66 = -0.0059144986
        else:
            var66 = -0.060048718
    else:
        if (input[147]) >= (1173.5):
            if (input[256]) >= (27.5):
                var66 = 0.055824757
            else:
                var66 = -0.05866165
        else:
            if (input[256]) >= (24.5):
                var66 = -0.0270672
            else:
                var66 = 0.040416382
    if (input[61]) >= (2432.5):
        if (input[18]) >= (1997.5):
            var67 = 0.06276476
        else:
            if (input[63]) >= (2062.5):
                var67 = -0.0605309
            else:
                var67 = 0.009134392
    else:
        if (input[89]) >= (1508.5):
            var67 = -0.06714771
        else:
            var67 = 0.009961122
    if (input[125]) >= (2140.0):
        var68 = 0.05431767
    else:
        if (input[81]) >= (2437.5):
            if (input[83]) >= (1095.5):
                var68 = 0.055602636
            else:
                var68 = -0.010995056
        else:
            if (input[198]) >= (2445.5):
                var68 = 0.022869982
            else:
                var68 = -0.07235746
    if (input[185]) >= (1219.5):
        if (input[89]) >= (1821.0):
            if (input[194]) >= (1638.0):
                var69 = 0.052692752
            else:
                var69 = -0.019075826
        else:
            if (input[137]) >= (1332.5):
                var69 = 0.073003136
            else:
                var69 = 0.012073641
    else:
        if (input[54]) >= (2436.5):
            var69 = 0.009737799
        else:
            var69 = -0.067579806
    if (input[36]) >= (2438.5):
        if (input[112]) >= (2436.5):
            var70 = -0.005996913
        else:
            var70 = -0.056248542
    else:
        if (input[147]) >= (1173.5):
            if (input[256]) >= (27.5):
                var70 = 0.05612464
            else:
                var70 = -0.05609342
        else:
            if (input[256]) >= (24.5):
                var70 = -0.026044244
            else:
                var70 = 0.037452877
    if (input[125]) >= (2140.0):
        var71 = 0.053093906
    else:
        if (input[59]) >= (2380.0):
            var71 = -0.060047437
        else:
            if (input[105]) >= (1765.5):
                var71 = 0.043556433
            else:
                var71 = -0.014629232
    if (input[88]) >= (1396.0):
        if (input[256]) >= (19.5):
            var72 = 0.032976918
        else:
            var72 = -0.08741433
    else:
        if (input[224]) >= (1211.5):
            if (input[7]) >= (1212.0):
                var72 = 0.00078146526
            else:
                var72 = -0.06154063
        else:
            if (input[199]) >= (2444.5):
                var72 = -0.044952217
            else:
                var72 = 0.028185314
    if (input[61]) >= (2432.5):
        if (input[18]) >= (1997.5):
            var73 = 0.059304602
        else:
            if (input[112]) >= (1818.5):
                var73 = -0.027352942
            else:
                var73 = 0.02012819
    else:
        if (input[89]) >= (1647.0):
            var73 = -0.06169774
        else:
            var73 = 0.0028734065
    if (input[185]) >= (1219.5):
        if (input[89]) >= (1821.0):
            if (input[194]) >= (1711.0):
                var74 = 0.052755266
            else:
                var74 = -0.017399639
        else:
            if (input[201]) >= (1287.0):
                var74 = 0.069008134
            else:
                var74 = 0.014809931
    else:
        if (input[54]) >= (2436.5):
            var74 = 0.007813885
        else:
            var74 = -0.06431807
    if (input[105]) >= (1977.5):
        var75 = 0.05345125
    else:
        if (input[142]) >= (1425.5):
            var75 = -0.05731687
        else:
            if (input[256]) >= (8.5):
                var75 = 0.020384856
            else:
                var75 = -0.039636433
    if (input[125]) >= (2140.0):
        var76 = 0.0494208
    else:
        if (input[227]) >= (1206.5):
            if (input[182]) >= (1215.5):
                var76 = -0.0033711332
            else:
                var76 = 0.06700673
        else:
            if (input[127]) >= (1397.0):
                var76 = -0.050590407
            else:
                var76 = 0.0010196252
    if (input[144]) >= (1262.5):
        if (input[196]) >= (1958.0):
            if (input[256]) >= (22.5):
                var77 = -0.08446706
            else:
                var77 = 0.023120046
        else:
            if (input[256]) >= (19.5):
                var77 = 0.09344873
            else:
                var77 = -0.014585703
    else:
        if (input[56]) >= (1442.5):
            var77 = -0.05214722
        else:
            var77 = -0.01086052
    if (input[147]) >= (1173.5):
        if (input[256]) >= (27.5):
            var78 = 0.047695544
        else:
            if (input[83]) >= (1098.0):
                var78 = 0.013092411
            else:
                var78 = -0.08212554
    else:
        if (input[256]) >= (24.5):
            if (input[171]) >= (1808.0):
                var78 = 0.059081424
            else:
                var78 = -0.09942515
        else:
            if (input[121]) >= (1373.5):
                var78 = -0.005300244
            else:
                var78 = 0.08201562
    if (input[88]) >= (1354.5):
        if (input[256]) >= (15.5):
            var79 = 0.019266011
        else:
            var79 = -0.07677281
    else:
        if (input[87]) >= (1604.5):
            var79 = 0.05741882
        else:
            if (input[83]) >= (1089.5):
                var79 = 0.023312211
            else:
                var79 = -0.0228725
    if (input[185]) >= (1219.5):
        if (input[89]) >= (1821.0):
            if (input[115]) >= (1017.5):
                var80 = -0.044938013
            else:
                var80 = 0.011493546
        else:
            if (input[137]) >= (1393.5):
                var80 = 0.06478197
            else:
                var80 = 0.014306716
    else:
        if (input[54]) >= (2436.5):
            var80 = 0.0069486434
        else:
            var80 = -0.061909586
    if (input[61]) >= (2432.5):
        if (input[4]) >= (1223.5):
            if (input[224]) >= (1222.0):
                var81 = -0.03555651
            else:
                var81 = 0.04902343
        else:
            if (input[256]) >= (9.5):
                var81 = 0.008632079
            else:
                var81 = -0.069469735
    else:
        if (input[89]) >= (1671.5):
            var81 = -0.05552691
        else:
            var81 = -0.0036231417
    if (input[185]) >= (1219.5):
        if (input[89]) >= (1821.0):
            if (input[115]) >= (1017.5):
                var82 = -0.042646877
            else:
                var82 = 0.0103129605
        else:
            if (input[137]) >= (1395.5):
                var82 = 0.061568778
            else:
                var82 = 0.014722702
    else:
        if (input[55]) >= (1451.5):
            var82 = -0.0010551548
        else:
            var82 = -0.056248486
    if (input[155]) >= (1713.5):
        if (input[239]) >= (1218.5):
            if (input[256]) >= (28.5):
                var83 = 0.070482776
            else:
                var83 = -0.018599015
        else:
            if (input[201]) >= (1582.0):
                var83 = 0.066297725
            else:
                var83 = 0.012312733
    else:
        if (input[112]) >= (2436.5):
            if (input[256]) >= (24.5):
                var83 = -0.040147603
            else:
                var83 = 0.03558388
        else:
            var83 = -0.06668969
    if (input[144]) >= (1262.5):
        if (input[196]) >= (1958.0):
            if (input[256]) >= (19.5):
                var84 = -0.07262934
            else:
                var84 = 0.024008146
        else:
            if (input[256]) >= (19.5):
                var84 = 0.08704685
            else:
                var84 = -0.013985137
    else:
        var84 = -0.04134176
    if (input[227]) >= (1206.5):
        if (input[203]) >= (1345.5):
            var85 = 0.055939198
        else:
            var85 = -0.004140624
    else:
        if (input[127]) >= (1397.0):
            if (input[143]) >= (1649.5):
                var85 = 0.016008252
            else:
                var85 = -0.060282644
        else:
            if (input[256]) >= (8.5):
                var85 = 0.023428524
            else:
                var85 = -0.031743806
    if (input[0]) >= (1223.5):
        if (input[54]) >= (2210.0):
            var86 = 0.065432124
        else:
            if (input[60]) >= (2028.0):
                var86 = -0.047206562
            else:
                var86 = 0.03278176
    else:
        if (input[256]) >= (8.5):
            if (input[127]) >= (1391.5):
                var86 = -0.057618827
            else:
                var86 = 0.029246805
        else:
            if (input[201]) >= (1332.0):
                var86 = 0.0047136145
            else:
                var86 = -0.08036975
    if (input[155]) >= (1713.5):
        if (input[239]) >= (1218.5):
            if (input[256]) >= (28.5):
                var87 = 0.06305721
            else:
                var87 = -0.01740223
        else:
            if (input[201]) >= (1582.0):
                var87 = 0.06315793
            else:
                var87 = 0.012393404
    else:
        if (input[112]) >= (2436.5):
            if (input[256]) >= (24.5):
                var87 = -0.038042154
            else:
                var87 = 0.032590963
        else:
            var87 = -0.06372634
    if (input[83]) >= (1098.5):
        if (input[88]) >= (1289.5):
            var88 = -0.024178239
        else:
            var88 = 0.054251432
    else:
        if (input[256]) >= (9.5):
            if (input[124]) >= (1917.0):
                var88 = -0.06035758
            else:
                var88 = 0.029248072
        else:
            if (input[20]) >= (2155.0):
                var88 = 0.009507048
            else:
                var88 = -0.080707215
    if (input[227]) >= (1206.5):
        if (input[171]) >= (1903.0):
            var89 = 0.00035755496
        else:
            var89 = 0.052305967
    else:
        if (input[182]) >= (1225.5):
            if (input[89]) >= (1802.0):
                var89 = -0.0076382286
            else:
                var89 = 0.041725855
        else:
            if (input[52]) >= (2436.5):
                var89 = -0.0012467431
            else:
                var89 = -0.058485925
    if (input[155]) >= (1713.5):
        if (input[239]) >= (1218.5):
            if (input[256]) >= (28.5):
                var90 = 0.060026318
            else:
                var90 = -0.015683668
        else:
            if (input[171]) >= (2090.5):
                var90 = 0.010592562
            else:
                var90 = 0.0602121
    else:
        if (input[112]) >= (2436.5):
            if (input[256]) >= (24.5):
                var90 = -0.037371393
            else:
                var90 = 0.032067418
        else:
            var90 = -0.06124093
    if (input[196]) >= (2442.5):
        if (input[43]) >= (2371.0):
            var91 = 0.008241043
        else:
            var91 = -0.061033916
    else:
        if (input[224]) >= (1201.5):
            if (input[256]) >= (19.5):
                var91 = 0.04105499
            else:
                var91 = -0.052623153
        else:
            if (input[256]) >= (24.5):
                var91 = -0.038348746
            else:
                var91 = 0.0773436
    if (input[0]) >= (1223.5):
        if (input[54]) >= (2210.0):
            var92 = 0.0580932
        else:
            if (input[61]) >= (2435.5):
                var92 = 0.023252778
            else:
                var92 = -0.04846048
    else:
        if (input[127]) >= (1391.5):
            var92 = -0.054671038
        else:
            if (input[256]) >= (8.5):
                var92 = 0.025149936
            else:
                var92 = -0.049248382
    if (input[155]) >= (1713.5):
        if (input[4]) >= (1248.0):
            if (input[68]) >= (2435.5):
                var93 = -0.014997477
            else:
                var93 = 0.056901813
        else:
            if (input[256]) >= (27.5):
                var93 = 0.04767841
            else:
                var93 = -0.024626212
    else:
        if (input[112]) >= (2436.5):
            if (input[256]) >= (24.5):
                var93 = -0.036777034
            else:
                var93 = 0.030881971
        else:
            var93 = -0.05874302
    if (input[196]) >= (2442.5):
        if (input[256]) >= (19.5):
            var94 = -0.062111646
        else:
            if (input[43]) >= (2290.0):
                var94 = 0.058173236
            else:
                var94 = -0.05152131
    else:
        if (input[124]) >= (1919.5):
            if (input[207]) >= (1303.5):
                var94 = 0.036321595
            else:
                var94 = -0.048589613
        else:
            if (input[256]) >= (14.5):
                var94 = 0.05786125
            else:
                var94 = -0.009995572
    if (input[83]) >= (1098.5):
        if (input[88]) >= (1289.5):
            var95 = -0.020971216
        else:
            var95 = 0.050219398
    else:
        if (input[256]) >= (9.5):
            if (input[124]) >= (1917.0):
                var95 = -0.055744898
            else:
                var95 = 0.023702636
        else:
            if (input[115]) >= (1001.0):
                var95 = 0.0041916207
            else:
                var95 = -0.07193157
    if (input[0]) >= (1223.5):
        if (input[54]) >= (2210.0):
            var96 = 0.052750256
        else:
            if (input[61]) >= (2435.5):
                var96 = 0.0223465
            else:
                var96 = -0.04481735
    else:
        if (input[127]) >= (1391.5):
            var96 = -0.05002713
        else:
            if (input[256]) >= (8.5):
                var96 = 0.01978322
            else:
                var96 = -0.044920128
    if (input[201]) >= (1597.0):
        if (input[46]) >= (1203.5):
            if (input[256]) >= (12.5):
                var97 = 0.01303972
            else:
                var97 = 0.06045681
        else:
            var97 = -0.016960459
    else:
        if (input[256]) >= (9.5):
            if (input[163]) >= (1077.0):
                var97 = -0.019702412
            else:
                var97 = 0.046804152
        else:
            if (input[86]) >= (2310.0):
                var97 = -0.07202715
            else:
                var97 = 0.007132272
    if (input[227]) >= (1206.5):
        var98 = 0.03204416
    else:
        if (input[125]) >= (2118.5):
            var98 = 0.037703663
        else:
            if (input[182]) >= (1225.5):
                var98 = -0.0042763627
            else:
                var98 = -0.045271378
    if (input[201]) >= (1597.0):
        if (input[4]) >= (1248.5):
            var99 = 0.052218925
        else:
            if (input[103]) >= (1340.5):
                var99 = 0.017170226
            else:
                var99 = -0.03509091
    else:
        if (input[256]) >= (9.5):
            if (input[256]) >= (25.5):
                var99 = -0.030858401
            else:
                var99 = 0.030245213
        else:
            if (input[86]) >= (2310.0):
                var99 = -0.06978947
            else:
                var99 = 0.006882009
    if (input[125]) >= (2082.5):
        if (input[256]) >= (13.5):
            var100 = 0.06225452
        else:
            var100 = -0.026551848
    else:
        if (input[256]) >= (18.5):
            if (input[41]) >= (1226.5):
                var100 = -0.08076056
            else:
                var100 = 0.07608283
        else:
            if (input[101]) >= (1228.5):
                var100 = -0.07222319
            else:
                var100 = 0.051647294
    var101 = (1.0) / ((1.0) + (math.exp((0.0) - (((((((((((((((((((((((((((((((((((((((((((((((((((((((var46) + (var47)) + (var48)) + (var49)) + (var50)) + (var51)) + (var52)) + (var53)) + (var54)) + (var55)) + (var56)) + (var57)) + (var58)) + (var59)) + (var60)) + (var61)) + (var62)) + (var63)) + (var64)) + (var65)) + (var66)) + (var67)) + (var68)) + (var69)) + (var70)) + (var71)) + (var72)) + (var73)) + (var74)) + (var75)) + (var76)) + (var77)) + (var78)) + (var79)) + (var80)) + (var81)) + (var82)) + (var83)) + (var84)) + (var85)) + (var86)) + (var87)) + (var88)) + (var89)) + (var90)) + (var91)) + (var92)) + (var93)) + (var94)) + (var95)) + (var96)) + (var97)) + (var98)) + (var99)) + (var100)))))
    return [(1.0) - (var101), var101]

def score_solo_itchy_6(input):
    if (input[175]) >= (1221.5):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (24.5):
                var0 = -0.12727273
            else:
                var0 = 0.04864865
        else:
            var0 = -0.1978892
    else:
        if (input[151]) >= (1638.0):
            if (input[168]) >= (1544.0):
                var0 = -0.02857143
            else:
                var0 = 0.16564417
        else:
            if (input[104]) >= (1396.0):
                var0 = 0.16666667
            else:
                var0 = -0.10857143
    if (input[175]) >= (1221.5):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (24.5):
                var1 = -0.11949158
            else:
                var1 = 0.04433396
        else:
            var1 = -0.18010609
    else:
        if (input[60]) >= (2253.5):
            if (input[104]) >= (1403.5):
                var1 = 0.12305967
            else:
                var1 = -0.11495463
        else:
            if (input[196]) >= (2443.5):
                var1 = -0.066890836
            else:
                var1 = 0.17989115
    if (input[175]) >= (1221.5):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (24.5):
                var2 = -0.112729825
            else:
                var2 = 0.040439412
        else:
            var2 = -0.16668117
    else:
        if (input[60]) >= (2253.5):
            if (input[104]) >= (1403.5):
                var2 = 0.11275041
            else:
                var2 = -0.10485808
        else:
            if (input[196]) >= (2443.5):
                var2 = -0.06322119
            else:
                var2 = 0.16606826
    if (input[175]) >= (1221.5):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (8.5):
                var3 = -0.029932244
            else:
                var3 = 0.1191312
        else:
            var3 = -0.15621004
    else:
        if (input[155]) >= (1741.5):
            if (input[25]) >= (2118.5):
                var3 = -0.035201546
            else:
                var3 = 0.14493684
        else:
            if (input[68]) >= (2058.5):
                var3 = 0.081542864
            else:
                var3 = -0.14316054
    if (input[175]) >= (1221.5):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (24.5):
                var4 = -0.10527668
            else:
                var4 = 0.036809083
        else:
            var4 = -0.1478359
    else:
        if (input[155]) >= (1741.5):
            if (input[25]) >= (2118.5):
                var4 = -0.03214064
            else:
                var4 = 0.13549158
        else:
            if (input[93]) >= (1643.5):
                var4 = -0.10825459
            else:
                var4 = 0.11954029
    if (input[182]) >= (2434.5):
        if (input[8]) >= (1904.5):
            var5 = -0.12690607
        else:
            if (input[158]) >= (2317.0):
                var5 = -0.00014564818
            else:
                var5 = 0.12482878
    else:
        if (input[201]) >= (2419.0):
            if (input[12]) >= (1220.0):
                var5 = -0.029448807
            else:
                var5 = 0.12553218
        else:
            if (input[151]) >= (1233.5):
                var5 = -0.14041303
            else:
                var5 = 0.02041518
    if (input[175]) >= (1220.0):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (8.5):
                var6 = -0.033445995
            else:
                var6 = 0.11786441
        else:
            var6 = -0.13543843
    else:
        if (input[135]) >= (2316.0):
            if (input[168]) >= (1544.0):
                var6 = -0.038922988
            else:
                var6 = 0.11702688
        else:
            if (input[167]) >= (1229.0):
                var6 = -0.13319813
            else:
                var6 = 0.057269454
    if (input[182]) >= (2434.5):
        if (input[244]) >= (1173.5):
            if (input[158]) >= (2317.0):
                var7 = -0.0056352145
            else:
                var7 = 0.12396576
        else:
            if (input[256]) >= (24.0):
                var7 = 0.10010713
            else:
                var7 = -0.13786392
    else:
        if (input[201]) >= (2419.0):
            if (input[12]) >= (1220.0):
                var7 = -0.026631659
            else:
                var7 = 0.11843661
        else:
            if (input[151]) >= (1233.5):
                var7 = -0.12994531
            else:
                var7 = 0.017351864
    if (input[175]) >= (1220.0):
        if (input[201]) >= (2419.0):
            if (input[256]) >= (8.5):
                var8 = -0.030489212
            else:
                var8 = 0.112854555
        else:
            var8 = -0.12676112
    else:
        if (input[155]) >= (1741.5):
            if (input[40]) >= (1919.0):
                var8 = -0.040714424
            else:
                var8 = 0.1169247
        else:
            if (input[93]) >= (1643.5):
                var8 = -0.09440132
            else:
                var8 = 0.09732104
    if (input[111]) >= (1229.5):
        if (input[33]) >= (1202.5):
            var9 = -0.12367999
        else:
            var9 = 0.0041156625
    else:
        if (input[241]) >= (1210.5):
            if (input[256]) >= (23.5):
                var9 = -0.010279416
            else:
                var9 = 0.116906844
        else:
            if (input[155]) >= (1767.0):
                var9 = 0.021457184
            else:
                var9 = -0.1228796
    if (input[175]) >= (1224.5):
        if (input[146]) >= (2439.5):
            if (input[256]) >= (20.5):
                var10 = -0.06727734
            else:
                var10 = 0.056873154
        else:
            if (input[38]) >= (1210.0):
                var10 = -0.12030387
            else:
                var10 = -0.035193782
    else:
        if (input[60]) >= (2179.0):
            if (input[246]) >= (1220.5):
                var10 = 0.06051994
            else:
                var10 = -0.084643625
        else:
            if (input[251]) >= (1227.0):
                var10 = 0.12215085
            else:
                var10 = -0.04330411
    if (input[111]) >= (1231.5):
        var11 = -0.117948785
    else:
        if (input[155]) >= (1741.5):
            if (input[105]) >= (1252.0):
                var11 = 0.10892613
            else:
                var11 = -0.00734178
        else:
            if (input[71]) >= (1564.5):
                var11 = 0.038141847
            else:
                var11 = -0.1179719
    if (input[111]) >= (1231.5):
        var12 = -0.11555711
    else:
        if (input[155]) >= (1737.5):
            if (input[85]) >= (1209.5):
                var12 = -0.011563788
            else:
                var12 = 0.09912386
        else:
            if (input[68]) >= (2094.5):
                var12 = 0.083342165
            else:
                var12 = -0.08764387
    if (input[111]) >= (1231.5):
        var13 = -0.113429
    else:
        if (input[241]) >= (1210.5):
            if (input[256]) >= (23.5):
                var13 = -0.021503592
            else:
                var13 = 0.10389622
        else:
            if (input[21]) >= (1210.5):
                var13 = -0.088966936
            else:
                var13 = 0.02901738
    if (input[111]) >= (1231.5):
        var14 = -0.11152027
    else:
        if (input[37]) >= (1220.5):
            if (input[241]) >= (1210.5):
                var14 = 0.0249949
            else:
                var14 = -0.1089203
        else:
            if (input[110]) >= (1209.5):
                var14 = 0.08654564
            else:
                var14 = -0.00861021
    if (input[111]) >= (1231.5):
        var15 = -0.10979464
    else:
        if (input[155]) >= (1741.5):
            if (input[105]) >= (1252.0):
                var15 = 0.09741064
            else:
                var15 = -0.006610884
        else:
            if (input[68]) >= (2086.5):
                var15 = 0.07995441
            else:
                var15 = -0.085586995
    if (input[111]) >= (1231.5):
        var16 = -0.108221926
    else:
        if (input[21]) >= (1210.5):
            if (input[104]) >= (1403.5):
                var16 = 0.056845304
            else:
                var16 = -0.0750405
        else:
            if (input[18]) >= (1711.5):
                var16 = -0.010425739
            else:
                var16 = 0.07872117
    if (input[111]) >= (1231.5):
        var17 = -0.10677668
    else:
        if (input[155]) >= (1741.5):
            if (input[105]) >= (1252.0):
                var17 = 0.09141972
            else:
                var17 = -0.0049966504
        else:
            if (input[71]) >= (1564.5):
                var17 = 0.027332304
            else:
                var17 = -0.107176445
    if (input[111]) >= (1231.5):
        var18 = -0.10543721
    else:
        if (input[60]) >= (2253.5):
            if (input[105]) >= (1749.5):
                var18 = 0.09523039
            else:
                var18 = -0.035400297
        else:
            if (input[219]) >= (1227.5):
                var18 = 0.09601327
            else:
                var18 = -0.09195893
    if (input[111]) >= (1231.5):
        var19 = -0.10418488
    else:
        if (input[37]) >= (1220.5):
            if (input[251]) >= (1256.5):
                var19 = 0.0501298
            else:
                var19 = -0.08568488
        else:
            if (input[63]) >= (2188.5):
                var19 = -0.047940437
            else:
                var19 = 0.053900253
    if (input[111]) >= (1231.5):
        var20 = -0.103003494
    else:
        if (input[60]) >= (2179.0):
            if (input[68]) >= (2064.5):
                var20 = 0.016017927
            else:
                var20 = -0.07288425
        else:
            if (input[219]) >= (1227.5):
                var20 = 0.10208551
            else:
                var20 = -0.08263831
    if (input[111]) >= (1231.5):
        var21 = -0.101878844
    else:
        if (input[60]) >= (2179.0):
            if (input[105]) >= (1749.5):
                var21 = 0.0911675
            else:
                var21 = -0.026158487
        else:
            if (input[219]) >= (1227.5):
                var21 = 0.09913885
            else:
                var21 = -0.08042324
    if (input[111]) >= (1231.5):
        var22 = -0.10079839
    else:
        if (input[155]) >= (1737.5):
            if (input[105]) >= (1252.0):
                var22 = 0.08041908
            else:
                var22 = -0.0058737188
        else:
            if (input[71]) >= (1564.5):
                var22 = 0.016731266
            else:
                var22 = -0.099290185
    if (input[111]) >= (1231.5):
        var23 = -0.09975097
    else:
        if (input[60]) >= (2142.0):
            if (input[105]) >= (1749.5):
                var23 = 0.086907335
            else:
                var23 = -0.022579422
        else:
            if (input[219]) >= (1227.5):
                var23 = 0.10135694
            else:
                var23 = -0.0760863
    if (input[111]) >= (1231.5):
        var24 = -0.09872659
    else:
        if (input[37]) >= (1220.5):
            if (input[198]) >= (1267.5):
                var24 = -0.0791424
            else:
                var24 = 0.042005345
        else:
            if (input[63]) >= (2188.5):
                var24 = -0.03886265
            else:
                var24 = 0.045233306
    if (input[111]) >= (1231.5):
        var25 = -0.0977163
    else:
        if (input[155]) >= (1737.5):
            if (input[105]) >= (1252.0):
                var25 = 0.0751219
            else:
                var25 = -0.004494805
        else:
            if (input[156]) >= (1727.5):
                var25 = -0.07580828
            else:
                var25 = 0.047108594
    if (input[63]) >= (2344.0):
        if (input[256]) >= (3.5):
            var26 = -0.1019513
        else:
            var26 = -0.031297263
    else:
        if (input[135]) >= (2438.5):
            if (input[256]) >= (21.5):
                var26 = -0.034693204
            else:
                var26 = 0.0804381
        else:
            if (input[72]) >= (1395.5):
                var26 = 0.012024677
            else:
                var26 = -0.08465617
    if (input[111]) >= (1231.5):
        var27 = -0.095835194
    else:
        if (input[60]) >= (2253.5):
            if (input[113]) >= (1777.5):
                var27 = 0.0035097373
            else:
                var27 = -0.088876896
        else:
            if (input[219]) >= (1227.5):
                var27 = 0.07937308
            else:
                var27 = -0.07732832
    if (input[63]) >= (2344.0):
        if (input[256]) >= (3.5):
            var28 = -0.09967605
        else:
            var28 = -0.026772717
    else:
        if (input[60]) >= (2142.0):
            if (input[256]) >= (17.5):
                var28 = -0.0440697
            else:
                var28 = 0.018418293
        else:
            if (input[251]) >= (1227.5):
                var28 = 0.096651055
            else:
                var28 = -0.06286765
    if (input[111]) >= (1231.5):
        var29 = -0.093975194
    else:
        if (input[37]) >= (1220.5):
            if (input[198]) >= (1267.5):
                var29 = -0.07426488
            else:
                var29 = 0.040744524
        else:
            if (input[60]) >= (2142.0):
                var29 = 0.004249797
            else:
                var29 = 0.07231206
    if (input[63]) >= (2344.0):
        if (input[256]) >= (3.5):
            var30 = -0.09790651
        else:
            var30 = -0.022747565
    else:
        if (input[135]) >= (2438.5):
            if (input[256]) >= (21.5):
                var30 = -0.03836995
            else:
                var30 = 0.07488587
        else:
            if (input[72]) >= (1395.5):
                var30 = 0.010272676
            else:
                var30 = -0.07972061
    if (input[111]) >= (1231.5):
        var31 = -0.09206023
    else:
        if (input[105]) >= (1742.5):
            var31 = 0.0850307
        else:
            if (input[44]) >= (2041.5):
                var31 = -0.04310078
            else:
                var31 = 0.022519356
    if (input[63]) >= (2344.0):
        if (input[256]) >= (3.5):
            var32 = -0.0960924
        else:
            var32 = -0.019152125
    else:
        if (input[60]) >= (2142.0):
            if (input[246]) >= (1220.5):
                var32 = 0.01910594
            else:
                var32 = -0.037657533
        else:
            if (input[251]) >= (1227.5):
                var32 = 0.09310895
            else:
                var32 = -0.058637865
    if (input[111]) >= (1231.5):
        var33 = -0.09005111
    else:
        if (input[105]) >= (1742.5):
            var33 = 0.082442716
        else:
            if (input[136]) >= (1620.5):
                var33 = -0.07264705
            else:
                var33 = 0.009895582
    if (input[63]) >= (2344.0):
        if (input[256]) >= (4.5):
            var34 = -0.093910836
        else:
            var34 = -0.02318755
    else:
        if (input[37]) >= (1220.5):
            if (input[198]) >= (1267.5):
                var34 = -0.06876653
            else:
                var34 = 0.043544747
        else:
            if (input[256]) >= (17.5):
                var34 = -0.008618019
            else:
                var34 = 0.050177243
    if (input[111]) >= (1231.5):
        var35 = -0.0880987
    else:
        if (input[60]) >= (2179.0):
            if (input[68]) >= (2064.5):
                var35 = 0.008937156
            else:
                var35 = -0.055286594
        else:
            if (input[219]) >= (1227.5):
                var35 = 0.08338133
            else:
                var35 = -0.06228447
    if (input[47]) >= (1328.5):
        if (input[146]) >= (2439.5):
            var36 = 0.0069497772
        else:
            var36 = -0.09059538
    else:
        if (input[60]) >= (2193.0):
            if (input[113]) >= (2291.0):
                var36 = 0.07363253
            else:
                var36 = -0.016934242
        else:
            if (input[133]) >= (1215.5):
                var36 = -0.013731027
            else:
                var36 = 0.08958777
    if (input[111]) >= (1231.5):
        var37 = -0.08581027
    else:
        if (input[155]) >= (1741.5):
            if (input[99]) >= (1038.5):
                var37 = -0.00045484336
            else:
                var37 = 0.09297748
        else:
            if (input[256]) >= (14.5):
                var37 = -0.09173644
            else:
                var37 = 0.038772907
    if (input[111]) >= (1231.5):
        var38 = -0.08454279
    else:
        if (input[60]) >= (2142.0):
            if (input[48]) >= (1220.5):
                var38 = 0.0018111306
            else:
                var38 = -0.08255956
        else:
            if (input[219]) >= (1227.5):
                var38 = 0.087741725
            else:
                var38 = -0.058856905
    if (input[63]) >= (2344.0):
        if (input[256]) >= (5.5):
            var39 = -0.088811204
        else:
            var39 = -0.01715208
    else:
        if (input[248]) >= (1557.5):
            if (input[82]) >= (1650.0):
                var39 = -0.030839458
            else:
                var39 = 0.08753981
        else:
            if (input[155]) >= (1741.5):
                var39 = 0.010047071
            else:
                var39 = -0.049098693
    if (input[47]) >= (1328.5):
        if (input[146]) >= (2439.5):
            var40 = 0.0047086473
        else:
            var40 = -0.08689904
    else:
        if (input[60]) >= (2193.0):
            if (input[48]) >= (1220.5):
                var40 = 0.0018209767
            else:
                var40 = -0.07920704
        else:
            if (input[126]) >= (1210.5):
                var40 = 0.08600402
            else:
                var40 = -0.00874249
    if (input[175]) >= (1236.5):
        if (input[256]) >= (8.5):
            if (input[95]) >= (1376.5):
                var41 = -0.11334949
            else:
                var41 = 0.023071026
        else:
            if (input[201]) >= (2152.0):
                var41 = 0.10102623
            else:
                var41 = -0.069855236
    else:
        if (input[93]) >= (1378.5):
            if (input[201]) >= (1251.0):
                var41 = 0.014118405
            else:
                var41 = -0.063264936
        else:
            var41 = 0.078311525
    if (input[111]) >= (1231.5):
        var42 = -0.07973059
    else:
        if (input[105]) >= (1742.5):
            var42 = 0.07480463
        else:
            if (input[135]) >= (2438.5):
                var42 = 0.016235914
            else:
                var42 = -0.034524452
    if (input[47]) >= (1230.5):
        if (input[201]) >= (2204.0):
            var43 = 0.008601773
        else:
            var43 = -0.084321484
    else:
        if (input[60]) >= (2193.0):
            if (input[113]) >= (2291.0):
                var43 = 0.06761544
            else:
                var43 = -0.0133450525
        else:
            if (input[256]) >= (7.5):
                var43 = 0.081650496
            else:
                var43 = 0.008536008
    if (input[63]) >= (2295.5):
        if (input[256]) >= (7.5):
            var44 = -0.09476872
        else:
            var44 = 0.029645039
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var44 = 0.06969798
            else:
                var44 = -0.12116813
        else:
            if (input[205]) >= (1964.5):
                var44 = 0.08500899
            else:
                var44 = 0.004751303
    if (input[47]) >= (1328.5):
        if (input[146]) >= (2439.5):
            var45 = 0.0026239536
        else:
            var45 = -0.08126428
    else:
        if (input[60]) >= (2193.0):
            if (input[48]) >= (1220.5):
                var45 = 0.002330584
            else:
                var45 = -0.073986106
        else:
            if (input[126]) >= (1214.0):
                var45 = 0.08060428
            else:
                var45 = 0.0009296369
    var46 = (((((((((((((((((((((((((((((((((((((((((((((var0) + (var1)) + (var2)) + (var3)) + (var4)) + (var5)) + (var6)) + (var7)) + (var8)) + (var9)) + (var10)) + (var11)) + (var12)) + (var13)) + (var14)) + (var15)) + (var16)) + (var17)) + (var18)) + (var19)) + (var20)) + (var21)) + (var22)) + (var23)) + (var24)) + (var25)) + (var26)) + (var27)) + (var28)) + (var29)) + (var30)) + (var31)) + (var32)) + (var33)) + (var34)) + (var35)) + (var36)) + (var37)) + (var38)) + (var39)) + (var40)) + (var41)) + (var42)) + (var43)) + (var44)) + (var45)
    if (input[111]) >= (1231.5):
        var47 = -0.07478496
    else:
        if (input[105]) >= (1742.5):
            var47 = 0.070833564
        else:
            if (input[136]) >= (1620.5):
                var47 = -0.060772367
            else:
                var47 = 0.0062910914
    if (input[175]) >= (1231.5):
        if (input[256]) >= (9.5):
            if (input[60]) >= (1960.5):
                var48 = -0.11399209
            else:
                var48 = 0.018091729
        else:
            if (input[199]) >= (2356.0):
                var48 = 0.08993942
            else:
                var48 = -0.06552894
    else:
        if (input[93]) >= (1378.5):
            if (input[201]) >= (1251.0):
                var48 = 0.012722294
            else:
                var48 = -0.057649333
        else:
            var48 = 0.07404467
    if (input[155]) >= (1737.5):
        if (input[99]) >= (1038.5):
            if (input[145]) >= (1394.0):
                var49 = -0.017658282
            else:
                var49 = 0.07037222
        else:
            var49 = 0.07781334
    else:
        if (input[256]) >= (13.5):
            if (input[89]) >= (1590.5):
                var49 = -0.12611857
            else:
                var49 = 0.02638799
        else:
            if (input[1]) >= (1407.5):
                var49 = 0.09777298
            else:
                var49 = -0.06656002
    if (input[111]) >= (1231.5):
        var50 = -0.07109354
    else:
        if (input[60]) >= (2142.0):
            if (input[105]) >= (1749.5):
                var50 = 0.062498875
            else:
                var50 = -0.0116297705
        else:
            if (input[235]) >= (1226.5):
                var50 = 0.07830231
            else:
                var50 = -0.030157432
    if (input[155]) >= (1737.5):
        if (input[99]) >= (1038.5):
            if (input[145]) >= (1394.0):
                var51 = -0.015364014
            else:
                var51 = 0.06791133
        else:
            var51 = 0.0748715
    else:
        if (input[256]) >= (13.5):
            if (input[120]) >= (2050.5):
                var51 = -0.12111741
            else:
                var51 = 0.021625703
        else:
            if (input[1]) >= (1407.5):
                var51 = 0.094434686
            else:
                var51 = -0.06398213
    if (input[42]) >= (1210.5):
        if (input[163]) >= (1034.0):
            if (input[108]) >= (2053.0):
                var52 = 0.037264775
            else:
                var52 = -0.07052191
        else:
            var52 = 0.054625567
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var52 = 0.06702653
            else:
                var52 = -0.117602386
        else:
            if (input[54]) >= (2157.5):
                var52 = 0.053615995
            else:
                var52 = -0.001017334
    if (input[63]) >= (2403.0):
        var53 = -0.06897278
    else:
        if (input[60]) >= (2142.0):
            if (input[256]) >= (17.5):
                var53 = -0.025976634
            else:
                var53 = 0.014253846
        else:
            if (input[251]) >= (1228.5):
                var53 = 0.07557185
            else:
                var53 = -0.02260244
    if (input[0]) >= (1222.5):
        if (input[1]) >= (1446.5):
            if (input[256]) >= (12.5):
                var54 = 0.11472847
            else:
                var54 = -0.09877108
        else:
            if (input[256]) >= (23.5):
                var54 = -0.10463744
            else:
                var54 = 0.030914197
    else:
        if (input[241]) >= (1210.5):
            var54 = 0.018844757
        else:
            if (input[246]) >= (1212.5):
                var54 = -0.080529556
            else:
                var54 = -0.0009794565
    if (input[175]) >= (1236.5):
        if (input[256]) >= (8.5):
            if (input[93]) >= (2125.5):
                var55 = -0.10628612
            else:
                var55 = 0.01480937
        else:
            if (input[201]) >= (2152.0):
                var55 = 0.09117584
            else:
                var55 = -0.05470304
    else:
        if (input[256]) >= (5.5):
            if (input[9]) >= (1895.5):
                var55 = 0.095286876
            else:
                var55 = 0.0034357652
        else:
            if (input[196]) >= (1394.5):
                var55 = -0.14229365
            else:
                var55 = 0.05904047
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[107]) >= (1732.0):
                var56 = -0.053649005
            else:
                var56 = 0.010035385
        else:
            var56 = 0.07308545
    else:
        if (input[256]) >= (14.5):
            if (input[121]) >= (1337.0):
                var56 = -0.11389555
            else:
                var56 = 0.0057670875
        else:
            if (input[1]) >= (1407.5):
                var56 = 0.089452356
            else:
                var56 = -0.059063204
    if (input[112]) >= (2431.5):
        if (input[256]) >= (19.5):
            var57 = 0.073074415
        else:
            var57 = -0.0065229423
    else:
        if (input[17]) >= (1711.0):
            if (input[256]) >= (16.5):
                var57 = 0.12153254
            else:
                var57 = -0.042725574
        else:
            if (input[256]) >= (17.5):
                var57 = -0.06824051
            else:
                var57 = 0.021418778
    if (input[175]) >= (1236.5):
        if (input[256]) >= (8.5):
            if (input[156]) >= (2007.5):
                var58 = -0.10174414
            else:
                var58 = 0.010718842
        else:
            if (input[201]) >= (2152.0):
                var58 = 0.08668082
            else:
                var58 = -0.052721452
    else:
        if (input[256]) >= (5.5):
            if (input[9]) >= (1895.5):
                var58 = 0.09375103
            else:
                var58 = 0.0038613535
        else:
            if (input[196]) >= (1394.5):
                var58 = -0.13155793
            else:
                var58 = 0.05554331
    if (input[112]) >= (2431.5):
        if (input[256]) >= (19.5):
            var59 = 0.0698434
        else:
            var59 = -0.004604498
    else:
        if (input[17]) >= (1711.0):
            if (input[256]) >= (16.5):
                var59 = 0.11554773
            else:
                var59 = -0.040768873
        else:
            if (input[256]) >= (17.5):
                var59 = -0.06405542
            else:
                var59 = 0.020526404
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[60]) >= (2131.0):
                var60 = -0.011727623
            else:
                var60 = 0.05890518
        else:
            var60 = 0.06953576
    else:
        if (input[256]) >= (14.5):
            if (input[41]) >= (1532.5):
                var60 = -0.10432761
            else:
                var60 = -0.002044433
        else:
            if (input[1]) >= (1407.5):
                var60 = 0.084495
            else:
                var60 = -0.057638355
    if (input[111]) >= (1231.5):
        var61 = -0.061535932
    else:
        if (input[37]) >= (1220.5):
            if (input[251]) >= (1238.5):
                var61 = 0.0073836194
            else:
                var61 = -0.06551977
        else:
            if (input[256]) >= (17.5):
                var61 = -0.008072268
            else:
                var61 = 0.034497675
    if (input[63]) >= (2344.0):
        var62 = -0.055236574
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var62 = 0.06421002
            else:
                var62 = -0.102699734
        else:
            if (input[256]) >= (17.5):
                var62 = -0.012911602
            else:
                var62 = 0.035862558
    if (input[112]) >= (2431.5):
        if (input[256]) >= (19.5):
            var63 = 0.06751727
        else:
            var63 = -0.004366755
    else:
        if (input[175]) >= (1236.5):
            if (input[256]) >= (8.5):
                var63 = -0.09723768
            else:
                var63 = 0.03780369
        else:
            if (input[155]) >= (1741.5):
                var63 = 0.014573114
            else:
                var63 = -0.03148122
    if (input[42]) >= (1210.5):
        if (input[218]) >= (1260.5):
            var64 = 0.031881403
        else:
            if (input[17]) >= (1713.5):
                var64 = 0.010682183
            else:
                var64 = -0.066727154
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var64 = 0.061700888
            else:
                var64 = -0.099360205
        else:
            if (input[112]) >= (2306.5):
                var64 = 0.07169979
            else:
                var64 = 0.0070387805
    if (input[42]) >= (1210.5):
        if (input[251]) >= (1256.5):
            var65 = 0.022699859
        else:
            if (input[205]) >= (1464.5):
                var65 = 0.011290459
            else:
                var65 = -0.07193752
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var65 = 0.05903061
            else:
                var65 = -0.0957854
        else:
            if (input[112]) >= (2306.5):
                var65 = 0.069533914
            else:
                var65 = 0.006381673
    if (input[63]) >= (2295.5):
        if (input[256]) >= (10.5):
            var66 = -0.088355914
        else:
            var66 = 0.028876973
    else:
        if (input[37]) >= (1220.5):
            if (input[198]) >= (1267.5):
                var66 = -0.043418035
            else:
                var66 = 0.035068054
        else:
            if (input[220]) >= (1713.0):
                var66 = 0.064082436
            else:
                var66 = 0.008307836
    if (input[112]) >= (2431.5):
        if (input[256]) >= (21.5):
            var67 = 0.061326593
        else:
            var67 = 0.0029102145
    else:
        if (input[175]) >= (1236.5):
            if (input[256]) >= (8.5):
                var67 = -0.093368106
            else:
                var67 = 0.03813922
        else:
            if (input[155]) >= (1741.5):
                var67 = 0.013291585
            else:
                var67 = -0.02841111
    if (input[42]) >= (1210.5):
        if (input[88]) >= (1396.5):
            if (input[17]) >= (1713.5):
                var68 = 0.010544184
            else:
                var68 = -0.08271101
        else:
            if (input[239]) >= (1218.5):
                var68 = -0.030725194
            else:
                var68 = 0.049767584
    else:
        if (input[169]) >= (1682.5):
            if (input[256]) >= (19.5):
                var68 = 0.057745058
            else:
                var68 = -0.09118254
        else:
            if (input[112]) >= (2306.5):
                var68 = 0.06664991
            else:
                var68 = 0.0060044522
    if (input[85]) >= (1211.5):
        if (input[129]) >= (1457.0):
            var69 = -0.07288076
        else:
            var69 = 0.026951764
    else:
        if (input[112]) >= (2431.5):
            var69 = 0.05166958
        else:
            if (input[201]) >= (1251.0):
                var69 = 0.006893724
            else:
                var69 = -0.051095277
    if (input[155]) >= (1742.5):
        if (input[129]) >= (1442.5):
            if (input[256]) >= (10.5):
                var70 = 0.015641442
            else:
                var70 = -0.04009248
        else:
            if (input[26]) >= (1212.5):
                var70 = 0.017494041
            else:
                var70 = 0.06760224
    else:
        if (input[256]) >= (14.5):
            if (input[73]) >= (1528.0):
                var70 = -0.09748832
            else:
                var70 = -0.017147971
        else:
            if (input[71]) >= (1681.5):
                var70 = 0.079075895
            else:
                var70 = -0.03980956
    if (input[85]) >= (1211.5):
        if (input[129]) >= (1457.0):
            var71 = -0.07052647
        else:
            var71 = 0.024762368
    else:
        if (input[112]) >= (2431.5):
            var71 = 0.049612593
        else:
            if (input[201]) >= (1251.0):
                var71 = 0.0063332925
            else:
                var71 = -0.048412476
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[145]) >= (1394.0):
                var72 = -0.010258044
            else:
                var72 = 0.05602583
        else:
            var72 = 0.064162515
    else:
        if (input[256]) >= (14.5):
            if (input[235]) >= (1245.5):
                var72 = -0.09339478
            else:
                var72 = -0.01797566
        else:
            if (input[71]) >= (1692.5):
                var72 = 0.075661846
            else:
                var72 = -0.034112643
    if (input[85]) >= (1211.5):
        if (input[129]) >= (1457.0):
            var73 = -0.06803667
        else:
            var73 = 0.022858473
    else:
        if (input[112]) >= (2439.5):
            var73 = 0.05563983
        else:
            if (input[201]) >= (1251.0):
                var73 = 0.0066424804
            else:
                var73 = -0.046574783
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[145]) >= (1394.0):
                var74 = -0.009398389
            else:
                var74 = 0.0542079
        else:
            var74 = 0.062426854
    else:
        if (input[256]) >= (14.5):
            if (input[216]) >= (1263.0):
                var74 = -0.08970971
            else:
                var74 = -0.019172097
        else:
            if (input[71]) >= (1705.5):
                var74 = 0.07196494
            else:
                var74 = -0.027424002
    if (input[112]) >= (2431.5):
        var75 = 0.039329622
    else:
        if (input[9]) >= (1279.5):
            if (input[105]) >= (1714.5):
                var75 = 0.046291653
            else:
                var75 = -0.0026331663
        else:
            if (input[256]) >= (11.5):
                var75 = -0.092041165
            else:
                var75 = 0.021947918
    if (input[42]) >= (1213.5):
        var76 = -0.04192665
    else:
        if (input[141]) >= (1419.5):
            if (input[85]) >= (1211.5):
                var76 = -0.061051954
            else:
                var76 = 0.005369289
        else:
            if (input[256]) >= (14.5):
                var76 = -0.01516218
            else:
                var76 = 0.06592836
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[256]) >= (23.5):
                var77 = 0.0296109
            else:
                var77 = -0.01449501
        else:
            var77 = 0.06030294
    else:
        if (input[256]) >= (14.5):
            if (input[137]) >= (1658.0):
                var77 = -0.08344581
            else:
                var77 = -0.022799935
        else:
            if (input[71]) >= (1705.5):
                var77 = 0.06909957
            else:
                var77 = -0.026960999
    if (input[112]) >= (2440.5):
        var78 = 0.044163607
    else:
        if (input[175]) >= (1236.5):
            if (input[256]) >= (8.5):
                var78 = -0.08862156
            else:
                var78 = 0.04254359
        else:
            if (input[256]) >= (5.5):
                var78 = 0.013468114
            else:
                var78 = -0.046151068
    if (input[155]) >= (1742.5):
        if (input[129]) >= (1442.5):
            if (input[256]) >= (10.5):
                var79 = 0.015912667
            else:
                var79 = -0.036234085
        else:
            var79 = 0.053091813
    else:
        if (input[256]) >= (14.5):
            var79 = -0.07079979
        else:
            if (input[71]) >= (1705.5):
                var79 = 0.06660278
            else:
                var79 = -0.025320519
    if (input[85]) >= (1211.5):
        if (input[129]) >= (1457.0):
            var80 = -0.06319418
        else:
            var80 = 0.019748425
    else:
        if (input[112]) >= (2439.5):
            var80 = 0.052672274
        else:
            if (input[201]) >= (1251.0):
                var80 = 0.006063831
            else:
                var80 = -0.043464463
    if (input[112]) >= (2431.5):
        var81 = 0.036465563
    else:
        if (input[79]) >= (1208.5):
            if (input[256]) >= (17.5):
                var81 = -0.05564865
            else:
                var81 = 0.02068293
        else:
            if (input[256]) >= (24.5):
                var81 = 0.06925275
            else:
                var81 = -0.020841368
    if (input[135]) >= (2438.5):
        if (input[256]) >= (17.5):
            if (input[71]) >= (1715.5):
                var82 = -0.09777852
            else:
                var82 = 0.043797
        else:
            if (input[109]) >= (1601.5):
                var82 = -0.044092815
            else:
                var82 = 0.09140645
    else:
        if (input[256]) >= (21.5):
            if (input[25]) >= (2134.0):
                var82 = 0.11940829
            else:
                var82 = -0.02202093
        else:
            if (input[99]) >= (1034.5):
                var82 = -0.09828492
            else:
                var82 = 0.024240075
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[145]) >= (1394.0):
                var83 = -0.00833398
            else:
                var83 = 0.051089346
        else:
            var83 = 0.05824038
    else:
        if (input[256]) >= (14.5):
            var83 = -0.06508016
        else:
            if (input[228]) >= (1349.0):
                var83 = 0.058473956
            else:
                var83 = -0.015823778
    if (input[112]) >= (2439.5):
        var84 = 0.0412112
    else:
        if (input[175]) >= (1236.5):
            if (input[256]) >= (8.5):
                var84 = -0.084266156
            else:
                var84 = 0.04151399
        else:
            if (input[256]) >= (8.5):
                var84 = 0.016131353
            else:
                var84 = -0.03245064
    if (input[85]) >= (1211.5):
        if (input[141]) >= (1422.5):
            var85 = -0.058870196
        else:
            var85 = 0.016555332
    else:
        if (input[60]) >= (2130.5):
            if (input[201]) >= (1251.0):
                var85 = 0.004249558
            else:
                var85 = -0.03578732
        else:
            var85 = 0.042452857
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[60]) >= (2131.0):
                var86 = -0.0073892483
            else:
                var86 = 0.04457265
        else:
            var86 = 0.056642503
    else:
        if (input[256]) >= (14.5):
            var86 = -0.06359478
        else:
            if (input[228]) >= (1344.5):
                var86 = 0.058014225
            else:
                var86 = -0.018001007
    if (input[42]) >= (1213.5):
        var87 = -0.036549736
    else:
        if (input[141]) >= (1419.5):
            if (input[85]) >= (1211.5):
                var87 = -0.053902216
            else:
                var87 = 0.004131373
        else:
            if (input[256]) >= (10.5):
                var87 = -0.006495639
            else:
                var87 = 0.060364213
    if (input[112]) >= (2440.5):
        var88 = 0.039592832
    else:
        if (input[155]) >= (1742.5):
            if (input[99]) >= (1038.5):
                var88 = -0.005146241
            else:
                var88 = 0.055061705
        else:
            if (input[256]) >= (14.5):
                var88 = -0.077350706
            else:
                var88 = 0.0302541
    if (input[48]) >= (1220.5):
        if (input[1]) >= (1446.5):
            if (input[256]) >= (12.5):
                var89 = 0.09669563
            else:
                var89 = -0.07523073
        else:
            if (input[256]) >= (23.5):
                var89 = -0.08039889
            else:
                var89 = 0.023434702
    else:
        var89 = -0.03865453
    if (input[135]) >= (2438.5):
        if (input[256]) >= (17.5):
            if (input[112]) >= (2153.0):
                var90 = 0.047736414
            else:
                var90 = -0.08993297
        else:
            if (input[109]) >= (1587.0):
                var90 = -0.042571392
            else:
                var90 = 0.08590659
    else:
        if (input[256]) >= (21.5):
            if (input[25]) >= (2134.0):
                var90 = 0.10754492
            else:
                var90 = -0.017201943
        else:
            if (input[129]) >= (1428.5):
                var90 = -0.09855657
            else:
                var90 = 0.007265776
    if (input[37]) >= (1220.5):
        if (input[256]) >= (17.5):
            var91 = 0.021441786
        else:
            if (input[145]) >= (1458.0):
                var91 = -0.08054393
            else:
                var91 = 0.0065130675
    else:
        if (input[63]) >= (2295.5):
            if (input[256]) >= (10.5):
                var91 = -0.07333327
            else:
                var91 = 0.03711437
        else:
            if (input[60]) >= (2142.0):
                var91 = 0.006000334
            else:
                var91 = 0.0455168
    if (input[175]) >= (1236.5):
        if (input[256]) >= (8.5):
            var92 = -0.06508025
        else:
            var92 = 0.030993987
    else:
        if (input[256]) >= (8.5):
            if (input[185]) >= (1615.5):
                var92 = 0.08430951
            else:
                var92 = -0.005750203
        else:
            if (input[169]) >= (1604.5):
                var92 = -0.10053817
            else:
                var92 = 0.05369535
    if (input[85]) >= (1211.5):
        if (input[129]) >= (1464.0):
            var93 = -0.05127723
        else:
            var93 = 0.006172081
    else:
        if (input[60]) >= (2130.5):
            if (input[113]) >= (1800.0):
                var93 = 0.0059520965
            else:
                var93 = -0.028036598
        else:
            var93 = 0.03887916
    if (input[37]) >= (1220.5):
        if (input[256]) >= (17.5):
            var94 = 0.0174273
        else:
            if (input[145]) >= (1481.5):
                var94 = -0.074696824
            else:
                var94 = 0.0042584715
    else:
        if (input[256]) >= (17.5):
            if (input[18]) >= (1709.5):
                var94 = -0.09046528
            else:
                var94 = 0.080308326
        else:
            if (input[147]) >= (1146.5):
                var94 = 0.06382073
            else:
                var94 = -0.09919148
    if (input[42]) >= (1213.5):
        var95 = -0.03667277
    else:
        if (input[141]) >= (1419.5):
            if (input[85]) >= (1211.5):
                var95 = -0.05003016
            else:
                var95 = 0.00407907
        else:
            if (input[246]) >= (1223.5):
                var95 = 0.05344795
            else:
                var95 = -0.002556617
    if (input[155]) >= (1742.5):
        if (input[99]) >= (1038.5):
            if (input[60]) >= (2179.0):
                var96 = -0.007408994
            else:
                var96 = 0.03498019
        else:
            var96 = 0.050955158
    else:
        if (input[256]) >= (14.5):
            var96 = -0.058836855
        else:
            var96 = 0.019208264
    if (input[175]) >= (1236.5):
        if (input[256]) >= (8.5):
            var97 = -0.06322418
        else:
            var97 = 0.02868378
    else:
        if (input[256]) >= (8.5):
            if (input[185]) >= (1629.0):
                var97 = 0.08053087
            else:
                var97 = -0.0045360676
        else:
            if (input[169]) >= (1604.5):
                var97 = -0.09251313
            else:
                var97 = 0.048666228
    if (input[205]) >= (1291.5):
        if (input[155]) >= (1742.5):
            if (input[256]) >= (12.5):
                var98 = 0.027077878
            else:
                var98 = -0.012055945
        else:
            if (input[256]) >= (14.5):
                var98 = -0.06353464
            else:
                var98 = 0.032391082
    else:
        if (input[192]) >= (1215.5):
            var98 = -0.055622783
        else:
            var98 = 0.009883361
    if (input[205]) >= (1291.5):
        if (input[53]) >= (1233.0):
            var99 = -0.031111497
        else:
            if (input[155]) >= (1742.5):
                var99 = 0.015016905
            else:
                var99 = -0.017853267
    else:
        if (input[192]) >= (1215.5):
            var99 = -0.054046553
        else:
            var99 = 0.009400173
    if (input[37]) >= (1221.5):
        if (input[241]) >= (1211.5):
            var100 = 0.0016229013
        else:
            var100 = -0.04917949
    else:
        if (input[63]) >= (2299.0):
            if (input[118]) >= (2443.5):
                var100 = -0.0032304872
            else:
                var100 = -0.03322151
        else:
            if (input[60]) >= (2142.0):
                var100 = 0.0041234875
            else:
                var100 = 0.039998543
    var101 = (1.0) / ((1.0) + (math.exp((0.0) - (((((((((((((((((((((((((((((((((((((((((((((((((((((((var46) + (var47)) + (var48)) + (var49)) + (var50)) + (var51)) + (var52)) + (var53)) + (var54)) + (var55)) + (var56)) + (var57)) + (var58)) + (var59)) + (var60)) + (var61)) + (var62)) + (var63)) + (var64)) + (var65)) + (var66)) + (var67)) + (var68)) + (var69)) + (var70)) + (var71)) + (var72)) + (var73)) + (var74)) + (var75)) + (var76)) + (var77)) + (var78)) + (var79)) + (var80)) + (var81)) + (var82)) + (var83)) + (var84)) + (var85)) + (var86)) + (var87)) + (var88)) + (var89)) + (var90)) + (var91)) + (var92)) + (var93)) + (var94)) + (var95)) + (var96)) + (var97)) + (var98)) + (var99)) + (var100)))))
    return [(1.0) - (var101), var101]



port = input("[INPUT] Enter port num:(1440,etc) :")
port = "/dev/cu.usbserial-" + port 
baud = 115200

ser = serial.Serial(port, baud)

label = []
start = False
sequence = 0

bad = 0
seq = []
plot_seq = 0

while True:
    line=str(ser.readline().decode('latin-1'))
    if line[0] != "-" and not start:  continue
    elif line[0] == "-" and len(label) == 0 and not start: 
        print("[INIT]")
        start = True
    elif line[0] == "-" and len(label) == 256: 
        sum_s = sum(label)
        print(sum_s)
        if sum_s > THRES:
            sequence = sequence + 1
            label.append(int(sequence))
            # print(sum(label))
            score_1 = score_solo_itchy_1(label)[1]
            score_2 = score_solo_itchy_2(label)[1]
            # score_3 = score_solo_itchy_3(label)[1]
            score_4 = score_solo_itchy_4(label)[1]
            score_5 = score_solo_itchy_5(label)[1]
            score_6 = score_solo_itchy_6(label)[1]
            
            # print(score_6)
            print(score_1)
            print(score_2)
            # print(score_3)
            print(score_4)
            print(score_5)
            print(score_6)
            print("\\\\\\----\\\\")
            all_score = [score_1,score_2,score_4,score_5,score_6]


            # for i in range(3,4):
            #     if all_score[i] > 0.85: all_score[i] = (all_score[i]-0.85)*10
            #     else: all_score[i] = 0

            # if(sum(all_score[2:3])) > 1.6: 
            #     all_score[2] = 0
            #     all_score[3] = 0


            # print(all_score)
            print(sum(all_score)*500)
            # print(sum(all_score) >1)
            # print()
            # print(test_2)
            # max_value = max(test_2) 
            # max_index = test_2.index(max_value) 
            # print(int(max_index!=0))

            # print(int(test_2[0]<0.05))
            # test_2 = score_all_nopad(label)
            # test_1 = score1(label)
            # fn = []
            # fn.append((test_1[0] + test_2[0])/2)
            # fn.append((test_1[1] + test_2[1])/2)
            
            # print(test_2)
            # print(fn)
            # if fn[0] >0.47 and fn[0] <0.55:
            #     print(int(round(random.random()*2)>1))
            # else:
           
           
            # print(int(fn[0]<0.475))

            # if(int(fn[0]<0.475)):
            #     print("BAD_POSTURE", score_w(label))


            # print(test_1>0.9)
            # sgd = score(label)/ 100
            # xgb = score1(label)[0]
            # log = score2(label)/10
            # ada = loaded_model.predict([label])[0]
            # print(ada)


            # sgd = score(label)
            # xgb = score1(label)[0]
            # log = score2(label)
            # ada = loaded_model.predict([label])[0]

            # print(sgd, log,  xgb, ada)

            # sgd = int(sgd > 20)
            # xgb = int(xgb < 0.65)
            # log = int(log > 2)

            # print(sgd, log,  xgb, ada)

            # data['y1'][plot_seq] = sum(all_score)
            # PLOTTING 

            
            data['y1'].append(sum(all_score)*500)
            data['y1'] = data['y1'][1: 101]

            # data['y1'] =  new_y1
            
            # PLOTTING 
            # print(data['y1'])

            # if plot_seq < 99: plot_seq += 1
            # else: plot_seq = 0

            with open('data.csv', 'w') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for i in range(0,100):
                    info = {
                        "x_val": data['x_val'][i],
                        "y1": data['y1'][i]
                    }
                    csv_writer.writerow(info)


            # VOTING !!!!


            # if (sum([sgd, xgb, log, ada])) > 2: 
            #     # print('1')
            #     seq.append(1)
            # else: 
            #     # print("0")
            #     seq.append(0)

            # if(len(seq) > 50):
            #     print("PREDICTED:")
            #     if (sum(seq) > (0.6 * 50)):
            #         print("BAD POSTURE")
            #     else:
            #         print("GOOD POSTURE")
            #     print("CALCULATING...............")
            #     seq = []


            # TORCH


            # print(score(label))
            # print(score1(label))
            # result = loaded_model.predict([label])
            
            # print(result)

            # print(score(label)[1] > 0.06)
            
            # if score(label) > 50:
            #   print("1")
            #   bad += 1
            #   if bad > 10: 
            #     print("VIBRATING!!!!!")
            #     bad = 0
            # else: 
            #     print("Good")
            #     bad = 0
            # print("[COLLECTED] ",label)
            # label = preProcess(label)
            # label = torch.from_numpy(np.asarray([label]))

            # with torch.no_grad():
            #     out = model(label.float())
            # print(out)
            # pred = out > 0.5
            # print("predicted label:", pred)   
            label = []
  
        elif sum_s < THRES: 
            print("[DETECT NO HUMAN]")
            sequence = 0
            label = []
            
    # 没有采集到一行，继续采集
    else:
        thearr = line.split(",")
        # 如果有16个
        if len(thearr) == 17:
            for i in thearr:
                try:  label.append(int(i))
                except: pass
        # 如果没有 清空
        else: 
            print("[RESET]")
            label = []
            start = False