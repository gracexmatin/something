import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
from scipy import interpolate
from pylab import mpl
from function1 import reverse
from function2 import (problemdata_humidity, problemdata_temperature,
                       problemdata_pressure, problemdata_ac_load_power)
from function3 import repeating
from function4 import getvalue
from function5 import check
from function6 import getvalue2
from function7 import KNN,KNN2


def split_livingroom(df):
    a = df.values[:,:]
    a10 = []
    a1 = np.array(a10)
    a20 = []
    a2 = np.array(a20)
    a30 = []
    a3 = np.array(a30)
    a40 = []
    a4 = np.array(a40)
    a50 = []
    a5 = np.array(a50)
    a60 = []
    a6 = np.array(a60)
    b10 = []
    b1 = np.array(b10)
    b20 = []
    b2 = np.array(b20)
    b30 = []
    b3 = np.array(b30)
    b40 = []
    b4 = np.array(b40)
    b50 = []
    b5 = np.array(b50)
    b60 = []
    b6 = np.array(b60)
    c10 = []
    c1 = np.array(c10)
    c20 = []
    c2 = np.array(c20)
    c30 = []
    c3 = np.array(c30)
    c40 = []
    c4 = np.array(c40)
    c50 = []
    c5 = np.array(c50)
    c60 = []
    c6 = np.array(c60)
    for i in range (len(a)):
        if a[i,3] == 'humidity_value':
            a1 = np.append(a1,a[i,0])
            a2 = np.append(a2, a[i,1])
            a3 = np.append(a3, a[i,2])
            a4 = np.append(a4, a[i,3])
            a5 = np.append(a5, a[i,4])
            a6 = np.append(a6, a[i,5])
        if a[i,3] == 'temperature_value':
            b1 = np.append(b1, a[i,0])
            b2 = np.append(b2, a[i,1])
            b3 = np.append(b3, a[i,2])
            b4 = np.append(b4, a[i,3])
            b5 = np.append(b5, a[i,4])
            b6 = np.append(b6, a[i,5])
        if a[i,3] == 'pressure_value':
            c1 = np.append(c1, a[i,0])
            c2 = np.append(c2, a[i,1])
            c3 = np.append(c3, a[i,2])
            c4 = np.append(c4, a[i,3])
            c5 = np.append(c5, a[i,4])
            c6 = np.append(c6, a[i,5])
    df_a1 = pd.DataFrame(a1)
    df_a2 = pd.DataFrame(a2)
    df_a3 = pd.DataFrame(a3)
    df_a4 = pd.DataFrame(a4)
    df_a5 = pd.DataFrame(a5)
    df_a6 = pd.DataFrame(a6)
    df_b1 = pd.DataFrame(b1)
    df_b2 = pd.DataFrame(b2)
    df_b3 = pd.DataFrame(b3)
    df_b4 = pd.DataFrame(b4)
    df_b5 = pd.DataFrame(b5)
    df_b6 = pd.DataFrame(b6)
    df_c1 = pd.DataFrame(c1)
    df_c2 = pd.DataFrame(c2)
    df_c3 = pd.DataFrame(c3)
    df_c4 = pd.DataFrame(c4)
    df_c5 = pd.DataFrame(c5)
    df_c6 = pd.DataFrame(c6)
    columns_all = ['id', 'datatime_recv','datatime_send','attr','value','static_id']
    dfa = pd.concat([df_a1, df_a2,df_a3,df_a4,df_a5,df_a6], axis=1)
    dfa.columns = columns_all
    dfa.to_excel('humidity_after.xlsx',index=False)
    dfb = pd.concat([df_b1, df_b2, df_b3, df_b4, df_b5, df_b6], axis=1)
    dfb.columns = columns_all
    dfb.to_excel('temperature_after.xlsx',index=False)
    dfc = pd.concat([df_c1, df_c2, df_c3, df_c4, df_c5, df_c6], axis=1)
    dfc.columns = columns_all
    dfc.to_excel('pressure_after.xlsx',index=False)
    return 0


def split_bedroom(df):
    a = df.values[:,:]
    a10 = []
    a1 = np.array(a10)
    a20 = []
    a2 = np.array(a20)
    a30 = []
    a3 = np.array(a30)
    a40 = []
    a4 = np.array(a40)
    a50 = []
    a5 = np.array(a50)
    a60 = []
    a6 = np.array(a60)
    b10 = []
    b1 = np.array(b10)
    b20 = []
    b2 = np.array(b20)
    b30 = []
    b3 = np.array(b30)
    b40 = []
    b4 = np.array(b40)
    b50 = []
    b5 = np.array(b50)
    b60 = []
    b6 = np.array(b60)
    for i in range (len(a)):
        if a[i,3] == 'humidity_value':
            a1 = np.append(a1,a[i,0])
            a2 = np.append(a2, a[i,1])
            a3 = np.append(a3, a[i,2])
            a4 = np.append(a4, a[i,3])
            a5 = np.append(a5, a[i,4])
            a6 = np.append(a6, a[i,5])
        if a[i,3] == 'temperature_value':
            b1 = np.append(b1, a[i,0])
            b2 = np.append(b2, a[i,1])
            b3 = np.append(b3, a[i,2])
            b4 = np.append(b4, a[i,3])
            b5 = np.append(b5, a[i,4])
            b6 = np.append(b6, a[i,5])
    df_a1 = pd.DataFrame(a1)
    df_a2 = pd.DataFrame(a2)
    df_a3 = pd.DataFrame(a3)
    df_a4 = pd.DataFrame(a4)
    df_a5 = pd.DataFrame(a5)
    df_a6 = pd.DataFrame(a6)
    df_b1 = pd.DataFrame(b1)
    df_b2 = pd.DataFrame(b2)
    df_b3 = pd.DataFrame(b3)
    df_b4 = pd.DataFrame(b4)
    df_b5 = pd.DataFrame(b5)
    df_b6 = pd.DataFrame(b6)
    columns_all = ['id', 'datatime_recv','datatime_send','attr','value','static_id']
    dfa = pd.concat([df_a1, df_a2,df_a3,df_a4,df_a5,df_a6], axis=1)
    dfa.columns = columns_all
    dfa.to_excel('humidity_after.xlsx',index=False)
    dfb = pd.concat([df_b1, df_b2, df_b3, df_b4, df_b5, df_b6], axis=1)
    dfb.columns = columns_all
    dfb.to_excel('temperature_after.xlsx',index=False)
    return 0

def split_companion(df):
    a = df.values[:,:]
    a30 = []
    a3 = np.array(a30)
    a50 = []
    a5 = np.array(a50)
    b10 = []
    b1 = np.array(b10)
    b20 = []
    b2 = np.array(b20)
    b30 = []
    b3 = np.array(b30)
    b40 = []
    b4 = np.array(b40)
    b50 = []
    b5 = np.array(b50)
    b60 = []
    b6 = np.array(b60)
    for i in range (len(a)):
        if a[i,3] == 'ac_state':
            a3 = np.append(a3, a[i,2])
            a5 = np.append(a5, a[i,4])
        if a[i,3] == 'ac_load_power':
            b1 = np.append(b1, a[i,0])
            b2 = np.append(b2, a[i,1])
            b3 = np.append(b3, a[i,2])
            b4 = np.append(b4, a[i,3])
            b5 = np.append(b5, a[i,4])
            b6 = np.append(b6, a[i,5])
    df_a3 = pd.DataFrame(a3)
    df_a5 = pd.DataFrame(a5)
    df_b1 = pd.DataFrame(b1)
    df_b2 = pd.DataFrame(b2)
    df_b3 = pd.DataFrame(b3)
    df_b4 = pd.DataFrame(b4)
    df_b5 = pd.DataFrame(b5)
    df_b6 = pd.DataFrame(b6)
    columns_all = ['id', 'datatime_recv','datatime_send','attr','value','static_id']
    columns_this = ['datatime_send','value']
    dfa = pd.concat([df_a3,df_a5], axis=1)
    dfa.columns = columns_this
    dfa.to_excel('AC_STATES_OF_COMPANION.xlsx',index=False)
    dfb = pd.concat([df_b1, df_b2, df_b3, df_b4, df_b5, df_b6], axis=1)
    dfb.columns = columns_all
    dfb.to_excel('ac_load_power_after.xlsx',index=False)
    return 0


def Draw(data_x, data_y, new_data_x, new_data_y):
    plt.plot(new_data_x, new_data_y, label="拟合曲线", color="black")
    plt.scatter(data_x, data_y, label="离散数据", color="red")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("三次样条函数")
    plt.legend(loc="upper left")
    plt.show()


def humidity_value_adjust(df):
    a=df.values[:,[2,4]]
    m0=[]
    m=np.array(m0)
    n0=[]
    n = np.array(n0)
    t0 = []
    t = np.array(t0)
    fix0 = []
    fix = np.array(fix0)
    num0 = []
    num = np.array(num0)
    print(len(a))
    reverse(a)
    a = repeating(a)
    k = len(a)
    df_a = pd.DataFrame(a)
    df_a.to_excel('checking_humidity.xlsx',index=False)
    s=0
    BUG = 0
    for i in range(k):
        if a[i,1]>100:
            a[i,1]=a[i,1]/100
        problemdata_humidity(i,a)
    for i in range(len(a)-3):
        humidity_value1=a[i,1]
        humidity_value2=a[(i+1),1]
        humidity_value3=a[(i+2),1]
        humidity_value4=a[(i+3),1]
        the_time1=a[i,0]-a[0,0]
        the_time_int1=the_time1.seconds/60 + the_time1.days * 60*24
        the_time2=a[i+1,0]-a[0,0]
        the_time_int2=the_time2.seconds/60 + the_time2.days * 60*24
        the_time3=a[i+2,0]-a[0,0]
        the_time_int3=the_time3.seconds/60 + the_time3.days * 60*24
        the_time4=a[i+3,0]-a[0,0]
        the_time_int4=the_time4.seconds/60 + the_time4.days * 60*24
        the_time = [the_time_int1, the_time_int2, the_time_int3, the_time_int4]
        humidity_value = [humidity_value1, humidity_value2, humidity_value3, humidity_value4]
        if (the_time[3] - the_time[2]) > 2880:
            the_timeget = a[i-1, 0] - a[0, 0]
            the_timeget_int = the_timeget.seconds / 60 + the_timeget.days * 60 * 24
            humidity_valueget = a[i-1, 1]
            time_x = [the_timeget_int,the_time_int1, the_time_int2, the_time_int3]
            humidity_y = [humidity_valueget,humidity_value1, humidity_value2, humidity_value3]
            thing0 = []
            thing = np.array(thing0)
            for j in range(math.ceil(time_x[1]), math.ceil(time_x[3]), 1):
                thing = np.append(thing, j)
            m = np.append(m, thing)
            if (the_time[3]-the_time[2]) < 7200:
                fix = np.append(fix,math.ceil(the_time[2]))
                fix = np.append(fix,math.ceil(the_time[3]))
                num = np.append(num,len(m))
                BUG = BUG +1
            if check(time_x) == 1:
                ychange0 = getvalue2(time_x,humidity_y)
            else:
                tck = interpolate.splrep(time_x,humidity_y,k=3)
                ychange = interpolate.splev(thing, tck)
                ychange0 = np.array(ychange)
            n = np.append(n, ychange0)
            s = s + 1
            print(a[i, 0])
            print(i)
            print(len(m))
            print(len(n))
            print(s)
            continue
        if (the_time[2] - the_time[1]) > 2880:
            continue
        if (the_time[1] - the_time[0]) > 2880:
            continue
        thing0 = []
        thing = np.array(thing0)
        for j in range(math.ceil(the_time[0]), math.ceil(the_time[1]), 1):
            thing = np.append(thing, j)
        m = np.append(m, thing)
        if check(the_time) == 1:
            ychange0 = getvalue(the_time, humidity_value)
        else:
            tck = interpolate.splrep(the_time, humidity_value, k=3)
            ychange = interpolate.splev(thing,tck)
            ychange0 = np.array(ychange)
        n = np.append(n,ychange0)
        print(a[i,0])
        print(i)
        print(len(m))
        print(len(n))
        s = s + 1
        print(s)
    print(s)
    print("BUG",BUG)
    m1 = KNN(m, n, fix, num)
    n1 = KNN2(m,n,fix,num)
    df_m = pd.DataFrame(m1)
    t = pd.to_datetime(df_m,unit='m',origin=pd.Timestamp(a[0,0]))
    print(t)
    df_t=pd.DataFrame(t)
    df_n = pd.DataFrame(n1)
    columns_0 = ['minute_number','humidity']
    df_mn = pd.concat([df_t, df_n], axis = 1)
    df_mn.columns = columns_0
    df_mn.to_excel('humidity_adjust.xlsx')
    Draw(a[:,0], a[:,1], m1, n1)
    return 0


def temperature_value_adjust(df):
    a=df.values[:,[2,4]]
    m0=[]
    m=np.array(m0)
    n0=[]
    n = np.array(n0)
    t0 = []
    t = np.array(t0)
    fix0 = []
    fix = np.array(fix0)
    num0 = []
    num = np.array(num0)
    print(len(a))
    reverse(a)
    a = repeating(a)
    k = len(a)
    df_a = pd.DataFrame(a)
    df_a.to_excel('checking_temperature.xlsx',index=False)
    s=0
    BUG = 0
    for i in range(k):
        if a[i,1]>100:
            a[i,1]=a[i,1]/100
        problemdata_temperature(i,a)
    for i in range(len(a)-3):
        temperature_value1=a[i,1]
        temperature_value2=a[(i+1),1]
        temperature_value3=a[(i+2),1]
        temperature_value4=a[(i+3),1]
        the_time1=a[i,0]-a[0,0]
        the_time_int1=the_time1.seconds/60 + the_time1.days * 60*24
        the_time2=a[i+1,0]-a[0,0]
        the_time_int2=the_time2.seconds/60 + the_time2.days * 60*24
        the_time3=a[i+2,0]-a[0,0]
        the_time_int3=the_time3.seconds/60 + the_time3.days * 60*24
        the_time4=a[i+3,0]-a[0,0]
        the_time_int4=the_time4.seconds/60 + the_time4.days * 60*24
        the_time = [the_time_int1, the_time_int2, the_time_int3, the_time_int4]
        temperature_value = [temperature_value1, temperature_value2, temperature_value3, temperature_value4]
        if (the_time[3] - the_time[2]) > 2880:
            the_timeget = a[i-1, 0] - a[0, 0]
            the_timeget_int = the_timeget.seconds / 60 + the_timeget.days * 60 * 24
            temperature_valueget = a[i-1, 1]
            time_x = [the_timeget_int,the_time_int1, the_time_int2, the_time_int3]
            temperature_y = [temperature_valueget,temperature_value1, temperature_value2, temperature_value3]
            thing0 = []
            thing = np.array(thing0)
            for j in range(math.ceil(time_x[1]), math.ceil(time_x[3]), 1):
                thing = np.append(thing, j)
            m = np.append(m, thing)
            if (the_time[3]-the_time[2]) < 7200:
                fix = np.append(fix,math.ceil(the_time[2]))
                fix = np.append(fix,math.ceil(the_time[3]))
                num = np.append(num,len(m))
                BUG = BUG +1
            if check(time_x) == 1:
                ychange0 = getvalue2(time_x,temperature_y)
            else:
                tck = interpolate.splrep(time_x,temperature_y,k=3)
                ychange = interpolate.splev(thing, tck)
                ychange0 = np.array(ychange)
            n = np.append(n, ychange0)
            s = s + 1
            print(a[i, 0])
            print(i)
            print(len(m))
            print(len(n))
            print(s)
            continue
        if (the_time[2] - the_time[1]) > 2880:
            continue
        if (the_time[1] - the_time[0]) > 2880:
            continue
        thing0 = []
        thing = np.array(thing0)
        for j in range(math.ceil(the_time[0]), math.ceil(the_time[1]), 1):
            thing = np.append(thing, j)
        m = np.append(m, thing)
        if check(the_time) == 1:
            ychange0 = getvalue(the_time, temperature_value)
        else:
            tck = interpolate.splrep(the_time, temperature_value, k=3)
            ychange = interpolate.splev(thing,tck)
            ychange0 = np.array(ychange)
        n = np.append(n,ychange0)
        print(a[i,0])
        print(i)
        print(len(m))
        print(len(n))
        s = s + 1
        print(s)
    print(s)
    print("BUG",BUG)
    m1 = KNN(m, n, fix, num)
    n1 = KNN2(m,n,fix,num)
    df_m = pd.DataFrame(m1)
    t = pd.to_datetime(df_m,unit='m',origin=pd.Timestamp(a[0,0]))
    print(t)
    df_t=pd.DataFrame(t)
    df_n = pd.DataFrame(n1)
    columns_0 = ['minute_number','temperature']
    df_mn = pd.concat([df_t, df_n], axis = 1)
    df_mn.columns = columns_0
    df_mn.to_excel('temperature_adjust.xlsx')
    Draw(a[:,0], a[:,1], m1, n1)
    return 0
#TODO KNN KNN2 checking


def pressure_value_adjust(df):
    a=df.values[:,[2,4]]
    m0=[]
    m=np.array(m0)
    n0=[]
    n = np.array(n0)
    t0 = []
    t = np.array(t0)
    fix0 = []
    fix = np.array(fix0)
    num0 = []
    num = np.array(num0)
    print(len(a))
    reverse(a)
    a = repeating(a)
    k = len(a)
    df_a = pd.DataFrame(a)
    df_a.to_excel('checking_pressure.xlsx',index=False)
    s=0
    BUG = 0
    for i in range(k):
        problemdata_pressure(i,a)
    for i in range(len(a)-3):
        pressure_value1=a[i,1]
        pressure_value2=a[(i+1),1]
        pressure_value3=a[(i+2),1]
        pressure_value4=a[(i+3),1]
        the_time1=a[i,0]-a[0,0]
        the_time_int1=the_time1.seconds/60 + the_time1.days * 60*24
        the_time2=a[i+1,0]-a[0,0]
        the_time_int2=the_time2.seconds/60 + the_time2.days * 60*24
        the_time3=a[i+2,0]-a[0,0]
        the_time_int3=the_time3.seconds/60 + the_time3.days * 60*24
        the_time4=a[i+3,0]-a[0,0]
        the_time_int4=the_time4.seconds/60 + the_time4.days * 60*24
        the_time = [the_time_int1, the_time_int2, the_time_int3, the_time_int4]
        pressure_value = [pressure_value1, pressure_value2, pressure_value3, pressure_value4]
        if (the_time[3] - the_time[2]) > 2880:
            the_timeget = a[i-1, 0] - a[0, 0]
            the_timeget_int = the_timeget.seconds / 60 + the_timeget.days * 60 * 24
            pressure_valueget = a[i-1, 1]
            time_x = [the_timeget_int,the_time_int1, the_time_int2, the_time_int3]
            pressure_y = [pressure_valueget,pressure_value1, pressure_value2, pressure_value3]
            thing0 = []
            thing = np.array(thing0)
            for j in range(math.ceil(time_x[1]), math.ceil(time_x[3]), 1):
                thing = np.append(thing, j)
            m = np.append(m, thing)
            if (the_time[3]-the_time[2]) < 7200:
                fix = np.append(fix,math.ceil(the_time[2]))
                fix = np.append(fix,math.ceil(the_time[3]))
                num = np.append(num,len(m))
                BUG = BUG +1
            if check(time_x) == 1:
                ychange0 = getvalue2(time_x,pressure_y)
            else:
                tck = interpolate.splrep(time_x,pressure_y,k=3)
                ychange = interpolate.splev(thing, tck)
                ychange0 = np.array(ychange)
            n = np.append(n, ychange0)
            s = s + 1
            print(a[i, 0])
            print(i)
            print(len(m))
            print(len(n))
            print(s)
            continue
        if (the_time[2] - the_time[1]) > 2880:
            continue
        if (the_time[1] - the_time[0]) > 2880:
            continue
        thing0 = []
        thing = np.array(thing0)
        for j in range(math.ceil(the_time[0]), math.ceil(the_time[1]), 1):
            thing = np.append(thing, j)
        m = np.append(m, thing)
        if check(the_time) == 1:
            ychange0 = getvalue(the_time, pressure_value)
        else:
            tck = interpolate.splrep(the_time, pressure_value, k=3)
            ychange = interpolate.splev(thing,tck)
            ychange0 = np.array(ychange)
        n = np.append(n,ychange0)
        print(a[i,0])
        print(i)
        print(len(m))
        print(len(n))
        s = s + 1
        print(s)
    print(s)
    print("BUG",BUG)
    m1 = KNN(m, n, fix, num)
    n1 = KNN2(m,n,fix,num)
    df_m = pd.DataFrame(m1)
    t = pd.to_datetime(df_m,unit='m',origin=pd.Timestamp(a[0,0]))
    print(t)
    df_t=pd.DataFrame(t)
    df_n = pd.DataFrame(n1)
    columns_0 = ['minute_number','pressure']
    df_mn = pd.concat([df_t, df_n], axis = 1)
    df_mn.columns = columns_0
    df_mn.to_excel('pressure_adjust.xlsx')
    Draw(a[:,0], a[:,1], m1, n1)
    return 0
#TODO KNN KNN2 checking


def companion_value_adjust(df):
    a=df.values[:,[2,4]]
    m0=[]
    m=np.array(m0)
    n0=[]
    n = np.array(n0)
    t0 = []
    t = np.array(t0)
    fix0 = []
    fix = np.array(fix0)
    num0 = []
    num = np.array(num0)
    reverse(a)
    a = repeating(a)
    k = len(a)
    print(k)
    df_a = pd.DataFrame(a)
    df_a.to_excel('checking_ac_load_power.xlsx',index=False)
    s=0
    BUG = 0
    for i in range(k):
        problemdata_ac_load_power(i,a)
    for i in range(len(a)-3):
        ac_load_power_value1=a[i,1]
        ac_load_power_value2=a[(i+1),1]
        ac_load_power_value3=a[(i+2),1]
        ac_load_power_value4=a[(i+3),1]
        the_time1=a[i,0]-a[0,0]
        the_time_int1=the_time1.seconds/60 + the_time1.days * 60*24
        the_time2=a[i+1,0]-a[0,0]
        the_time_int2=the_time2.seconds/60 + the_time2.days * 60*24
        the_time3=a[i+2,0]-a[0,0]
        the_time_int3=the_time3.seconds/60 + the_time3.days * 60*24
        the_time4=a[i+3,0]-a[0,0]
        the_time_int4=the_time4.seconds/60 + the_time4.days * 60*24
        the_time = [the_time_int1, the_time_int2, the_time_int3, the_time_int4]
        ac_load_power_value = [ac_load_power_value1, ac_load_power_value2, ac_load_power_value3, ac_load_power_value4]
        if (the_time[3] - the_time[2]) > 2880:
            the_timeget = a[i-1, 0] - a[0, 0]
            the_timeget_int = the_timeget.seconds / 60 + the_timeget.days * 60 * 24
            ac_load_power_valueget = a[i-1, 1]
            time_x = [the_timeget_int,the_time_int1, the_time_int2, the_time_int3]
            ac_load_power_y = [ac_load_power_valueget,ac_load_power_value1, ac_load_power_value2, ac_load_power_value3]
            thing0 = []
            thing = np.array(thing0)
            for j in range(math.ceil(time_x[1]), math.ceil(time_x[3]), 1):
                thing = np.append(thing, j)
            m = np.append(m, thing)
            if (the_time[3]-the_time[2]) < 7200:
                fix = np.append(fix,math.ceil(the_time[2]))
                fix = np.append(fix,math.ceil(the_time[3]))
                num = np.append(num,len(m))
                BUG = BUG +1
            if check(time_x) == 1:
                ychange0 = getvalue2(time_x,ac_load_power_y)
            else:
                tck = interpolate.splrep(time_x,ac_load_power_y,k=3)
                ychange = interpolate.splev(thing, tck)
                ychange0 = np.array(ychange)
            n = np.append(n, ychange0)
            s = s + 1
            print(a[i, 0])
            print(i)
            print(len(m))
            print(len(n))
            print(s)
            continue
        if (the_time[2] - the_time[1]) > 2880:
            continue
        if (the_time[1] - the_time[0]) > 2880:
            continue
        thing0 = []
        thing = np.array(thing0)
        for j in range(math.ceil(the_time[0]), math.ceil(the_time[1]), 1):
            thing = np.append(thing, j)
        m = np.append(m, thing)
        if check(the_time) == 1:
            ychange0 = getvalue(the_time, ac_load_power_value)
        else:
            tck = interpolate.splrep(the_time, ac_load_power_value, k=3)
            ychange = interpolate.splev(thing,tck)
            ychange0 = np.array(ychange)
        n = np.append(n,ychange0)
        print(a[i,0])
        print(i)
        print(len(m))
        print(len(n))
        s = s + 1
        print(s)
    print(s)
    print("BUG",BUG)
    m1 = KNN(m, n, fix, num)
    n1 = KNN2(m,n,fix,num)
    df_m = pd.DataFrame(m1)
    t = pd.to_datetime(df_m,unit='m',origin=pd.Timestamp(a[0,0]))
    print(t)
    df_t=pd.DataFrame(t)
    df_n = pd.DataFrame(n1)
    columns_0 = ['minute_number','ac_load_power']
    df_mn = pd.concat([df_t, df_n], axis = 1)
    df_mn.columns = columns_0
    df_mn.to_excel('ac_load_power_adjust.xlsx')
    Draw(a[:,0], a[:,1], m1, n1)
    return 0


def companion_value_adjust_new(df):
    a=df.values[:,[2,4]]
    m0=[]
    m=np.array(m0)
    n0=[]
    n = np.array(n0)
    t0 = []
    t = np.array(t0)
    fix0 = []
    fix = np.array(fix0)
    num0 = []
    num = np.array(num0)
    reverse(a)
    a = repeating(a)
    k = len(a)
    print(k)
    df_a = pd.DataFrame(a)
    df_a.to_excel('checking_ac_load_power.xlsx',index=False)
    s=0
    BUG = 0
    for i in range(k):
        problemdata_ac_load_power(i,a)
    for i in range(len(a)-3):
        ac_load_power_value1=a[i,1]
        ac_load_power_value2=a[(i+1),1]
        the_time1=a[i,0]-a[0,0]
        the_time_int1=the_time1.seconds/60 + the_time1.days * 60*24
        the_time2=a[i+1,0]-a[0,0]
        the_time_int2=the_time2.seconds/60 + the_time2.days * 60*24
        if (the_time_int2 - the_time_int1) > 2880:
            if (the_time_int2-the_time_int1) < 7200:
                fix = np.append(fix,math.ceil(the_time_int1))
                fix = np.append(fix,math.ceil(the_time_int2))
                num = np.append(num,len(m))
                BUG = BUG +1
            continue
        thing0 = []
        thing = np.array(thing0)
        for j in range(math.ceil(the_time_int1), math.ceil(the_time_int2), 1):
            thing = np.append(thing, j)
        m = np.append(m, thing)
        the_time=[the_time_int1,the_time_int2]
        ac_load_power_value=[ac_load_power_value1,ac_load_power_value2]
        tck = interpolate.splrep(the_time, ac_load_power_value, k=1)
        ychange = interpolate.splev(thing,tck)
        ychange0 = np.array(ychange)
        n = np.append(n,ychange0)
        print(a[i,0])
        print(i)
        print(len(m))
        print(len(n))
        s = s + 1
        print(s)
    print(s)
    print("BUG",BUG)
    m1 = KNN(m, n, fix, num)
    n1 = KNN2(m,n,fix,num)
    df_m = pd.DataFrame(m1)
    t = pd.to_datetime(df_m,unit='m',origin=pd.Timestamp(a[0,0]))
    print(t)
    df_t=pd.DataFrame(t)
    df_n = pd.DataFrame(n1)
    columns_0 = ['minute_number','ac_load_power']
    df_mn = pd.concat([df_t, df_n], axis = 1)
    df_mn.columns = columns_0
    df_mn.to_excel('ac_load_power_adjust.xlsx')
    Draw(a[:,0], a[:,1], m1, n1)
    return 0