def KNN2(m,n,fix,num):
    import numpy as np
    time0 = []
    time = np.array(time0)
    value0 = []
    value = np.array(value0)
    for i in range(len(num)):
        for k in range(int(fix[2 * i]), int(fix[2 * i + 1]), 1):
            valuek = 0
            sum = 0
            length = m[int(num[i]) + 1440+ k-int(fix[2*i])]-m[int(num[i]) - 1440+ k-int(fix[2*i])]
            for j in range((int(num[i]) - 1440 + k-int(fix[2*i])), (int(num[i]) + 1440+ k-int(fix[2*i])), 1):
                sum = abs(k - m[j]) + sum
            for h in range((int(num[i]) - 1440+ k-int(fix[2*i])), (int(num[i]) + 1440+ k-int(fix[2*i])), 1):
                valuek = valuek + (length-abs(k - m[h])) * n[h] / (2879 * length -sum)
            value = np.append(value, valuek)
            time = np.append(time, k)
        m = np.insert(m, int(num[i]), time)
        n = np.insert(n, int(num[i]), value)
    return n

def KNN(m,n,fix,num):
    import numpy as np
    time0=[]
    time=np.array(time0)
    value0=[]
    value=np.array(value0)
    for i in range(len(num)):
        for k in range(int(fix[2*i]),int(fix[2*i+1]),1):
            valuek = 0
            sum = 0
            length = m[int(num[i]) + 1440 + k - int(fix[2 * i])] - m[int(num[i]) - 1440 + k - int(fix[2 * i])]
            for j in range((int(num[i]) - 1440 + k - int(fix[2 * i])), (int(num[i]) + 1440 + k - int(fix[2 * i])), 1):
                sum = abs(k - m[j]) + sum
            for h in range((int(num[i]) - 1440 + k - int(fix[2 * i])), (int(num[i]) + 1440 + k - int(fix[2 * i])), 1):
                valuek = valuek + (length - abs(k - m[h])) * n[h] / (2879 * length -sum)
            value = np.append(value,valuek)
            time = np.append(time,k)
        m = np.insert(m,int(num[i]),time)
        n = np.insert(n,int(num[i]),value)
    return m


