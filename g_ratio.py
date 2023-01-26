# -*- coding: utf-8 -*-
"""G-ratio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BvAcmvVK8f5Bi0wAFlDGQZcJrfwfurJ0

# Calculation of wear depth

This algorithm is used to calculate wear depth measured using Alicona microscope
"""

from tables.table import Column
import pandas as pd
import numpy as np

df = pd.read_csv('/content/23T2/specimen_23_S2_depth4.csv', encoding = 'utf-16', header = 0, sep = '\t')
# data1 = pd.read_csv("data1.csv", encoding="utf-16")

z = np.array(df.iloc[0:,[1]])
a = z.max()
a1 = z[0]
b = z.min()
print(a)
print(a1)


l = np.array(df.iloc[0:,[0]])
c = l.max()
d = l.min()


diff = (c - d)
print('delta l in m:' ,diff)
diff2 = (a - b)
print('delta z in m:' ,diff2)

#difference in micro-meter
diff = (c - d)*10E5
print('delta l in micro meter:' ,diff)
diff2 = (a - b)*10E5
print('delta z in micro meter:' ,diff2)

"""# Calculation of G-ratio

*G-ratio is defined as the volume of material removed divided by the volume of wheel wear*

***G-ratio = V_w/V_s***

V_w = Volume of material wear

V_s = Volume of wheel wear 









"""

from pandas.core.frame import Axes
from pandas._libs.hashtable import value_count
import pandas as pd
import math

#dataframe of all the values in micrometer

data = {'d_s_after_dressing_1':[120,120,120,120],'V_w_resinwheel_S1':[268.562,267.58,311.523,228.4265],'V_s_resinwheel_S1':[70,100,100,60],
                  'd_s_after_dressing_2':[120,120,120,120],'V_w_resinwheel_S2':[211.77,273.88,269.503,151.614],'V_s_resinwheel_S2':[160,100,130,80],
                  'd_s_100%wheel':[120,120,120,120],'V_w_100%wheel_S1':[172.182,264.511,165.8925,203.36],'V_s_100%wheel_S1':[700,400,300,180],
                  'd_s_100%wheel_after_S1':[120,120,120,120],'V_w_100%wheel_S2':[216.36,191.25,179.12,161.88],'V_s_100%wheel_S2':[200,200,150,170]}
df = pd.DataFrame(data = data)
df



#G-ratio of resin wheels at both speeds

#length of the ground surface in micrometer
L_w = 92000

#Diameter of the wheel
d_s = df.iloc[0:,9]
#depth of ground surface     
a_w = df.iloc[0:,10]

#wheel wear 
a_s = df.iloc[0:,11]

G_ratio = (a_w*L_w)/(a_s*math.pi*d_s)
G_ratio