import numpy as np

def problemdata_humidity(i,a):
    if a[i,1] > 50000:
        a = np.delete(a, i, 0)

def problemdata_temperature(i,a):
    if a[i,1] > 5000:
        a = np.delete(a, i, 0)

def problemdata_pressure(i,a):
    if a[i,1] > 150000 or a[i,1] < 50000:
        a = np.delete(a, i, 0)

def problemdata_ac_load_power(i,a):
    if a[i,1] > 1000:
        a = np.delete(a, i, 0)