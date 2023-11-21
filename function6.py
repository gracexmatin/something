import numpy as np
import math
from scipy import interpolate

def getvalue2(time,value):
    length = time[3]-time[0]
    min = time[1] - time[0]
    if (time[2] - time[1]) < min:
        min = time[2] - time[1]
    if (time[3] - time[2]) < min:
        min = time[3] - time[2]
    time_point=[]
    value_point=[]
    num=math.ceil(length/min)
    change = []
    ychange0 = np.array(change)
    for j in range(num+1):
        x=j*min+time[0]
        for k in range(3):
            if x<time[k+1] and x>=time[k]:
                y=(time[k+1]-x)*value[k]/(time[k+1]-time[k])+(x-time[k])*value[k+1]/(time[k+1]-time[k])
        if x > time[3]:
            y = ((x - time[2]) * value[3] - (x - time[3]) * value[2]) / (time[3] - time[2])
        time_point.append(x)
        value_point.append(y)
        if x<time[1] and (x+min)>time[1]:
            time_point.append(time[1])
            value_point.append(value[1])
        if x<time[2] and (x+min)>time[2]:
            time_point.append(time[2])
            value_point.append(value[2])
        if x<time[3] and (x+min)>time[3]:
            time_point.append(time[3])
            value_point.append(value[3])
    for k in range(len(time_point)-3):
        if time_point[k] < time[1]:
            continue
        time_use=[time_point[k],time_point[k+1],time_point[k+2],time_point[k+3]]
        value_use=[value_point[k],value_point[k+1],value_point[k+2],value_point[k+3]]
        datax0=[]
        datax=np.array(datax0)
        if time_point[k+3] == time[3]:
            for i in range(math.ceil(time_use[0]), math.ceil(time_use[3]), 1):
                datax = np.append(datax, i)
        else:
            for i in range(math.ceil(time_use[0]), math.ceil(time_use[1]), 1):
                datax = np.append(datax, i)
        if len(datax)==0:
            break
        tck = interpolate.splrep(time_use, value_use, k=3)
        ychange = interpolate.splev(datax,tck)
        y_change = np.array(ychange)
        ychange0 = np.append(ychange0,y_change)
        if time_point[k + 3] == time[3]:
            break
    return ychange0
