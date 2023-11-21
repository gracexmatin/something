import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
from scipy import interpolate
from pylab import mpl
from solution import (split_livingroom,split_companion,
                      split_bedroom,humidity_value_adjust,
                      temperature_value_adjust,pressure_value_adjust,
                      companion_value_adjust,companion_value_adjust_new)

#df = pd.read_excel('livingroom2022.xlsx',sheet_name=0)
#ff = pd.read_excel('bedroom2022.xlsx',sheet_name=0)
#fd = pd.read_excel('bedroom2021.xlsx',sheet_name=0)
dd = pd.read_excel('companion2022.xlsx',sheet_name=0)

#split_livingroom(df)
#split_bedroom(ff)
split_companion(dd)
#split_bedroom(fd)

#df1 = pd.read_excel('humidity_after.xlsx',sheet_name=0)
#df2 = pd.read_excel('temperature_after.xlsx',sheet_name=0)
#df3 = pd.read_excel('pressure_after.xlsx',sheet_name=0)
df4 = pd.read_excel('ac_load_power_after.xlsx',sheet_name=0)

#humidity_value_adjust(df1)
#temperature_value_adjust(df2)
#pressure_value_adjust(df3)
#companion_value_adjust(df4)
companion_value_adjust_new(df4)
#humidity_value_adjust(df1)
#temperature_value_adjust(df2)