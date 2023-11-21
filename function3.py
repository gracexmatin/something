import numpy as np
import math
import datetime

def repeating(a):
    k = len(a) - 1
    i = 0
    while i < k:
        if (math.ceil((a[i+1,0]-a[i,0]).seconds/60)==1
            or math.ceil((a[i+1,0]-a[i,0]).seconds/60)==0
            or math.ceil((a[i+1,0]-a[i,0]).seconds/60)==-1):
            a = np.delete(a,i+1,0)
            k = len(a)-1
        else:
            i = i + 1
    return a
