import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("kc_house_data.csv")
df1 = df[['price', 'bedrooms', 'sqft_living']]
# print(df1)
w0 = 60760
w1 = 20
n = 0
alpha = 0.0000000066
while  n <1500000:
    sigma0 = 0
    sigma1 = 0    
    for i in np.arange(0, 60, 1):
        x = df1.loc[i, 'sqft_living']
        p = df1.loc[i, 'price']
        h = x*w1 + w0
        sigma0 = sigma0 + (p - h)
        sigma1 = sigma1 + (p - h)*x
        # print(h, p, sigma0, sigma1)
    w0 = w0 + alpha*sigma0
    w1 = w1 + alpha*sigma1
    n = n +1
    print(w1, w0)
# plt.scatter(df1['sqft_living'], df1['price'])
# plt.show()