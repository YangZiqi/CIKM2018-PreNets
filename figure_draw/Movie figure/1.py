import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
data1 = pd.read_csv('20_minute.csv')
data2 = pd.read_csv('100_minute.csv')
flatui1 = ['silver','firebrick']
plt.figure(figsize=(9,3.5))
ax1 = plt.subplot(121)
ax1 = sns.barplot(data=data1,x='Unnamed: 2',hue='Unnamed: 1',y='MAPE',palette=sns.color_palette(flatui1))
plt.ylim(0, 0.5)
plt.title('20 Days for Movie')
ax2 = plt.subplot(122)
ax2 = sns.barplot(data=data2,x='Unnamed: 2',hue='Unnamed: 1',y='MAPE',palette=sns.color_palette(flatui1))
plt.ylim(0, 0.5)
plt.title('100 Days for Movie')
plt.tight_layout(pad=1)
plt.show()