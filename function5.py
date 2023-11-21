import numpy
import math

def check(time):
    min = time[1]-time[0]
    max = time[1]-time[0]
    if (time[2]-time[1])<min:
        min = time[2]-time[1]
    if (time[3]-time[2])<min:
        min = time[3] - time[2]
    if (time[2] - time[1]) >max:
        max = time[2] - time[1]
    if (time[3] - time[2]) > max:
        max = time[3] - time[2]
    if max >=3*min:
        return 1
    else:
        return 0