# backgroud set
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import pandas as pd

# load data
data1 = pd.read_csv('10_minute_twitter.csv',index_col='Unnamed: 0')
data2 = pd.read_csv('1_hour_twitter.csv',index_col='Unnamed: 0')
#data1 = pd.read_csv('10_day_movie.csv',index_col='Unnamed: 0')
#data2 = pd.read_csv('100_day_movie.csv',index_col='Unnamed: 0')

plt.figure(figsize = (6.8, 4))
ax1 = plt.subplot(121)
sns.heatmap(data=data1, annot=True,linewidths=.0,fmt=".4f",vmax=0.31, vmin=0.25,cmap=sns.color_palette('Greys',n_colors=100))

#sns.heatmap(data=data1, annot=True,linewidths=.0,fmt=".2f",cmap="Blues",vmax=0.6, vmin=0.48,ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=10)
ax1.set_yticklabels(ax1.get_yticklabels(), rotation=0)
ax1.set_title('10 Minutes Observation')

ax2 = plt.subplot(122)
sns.heatmap(data=data2, annot=True,linewidths=.0,fmt=".4f",vmax=0.21, vmin=0.15,cmap=sns.color_palette('Greys',n_colors=100))

#sns.heatmap(data=data2, annot=True,linewidths=.0,fmt=".2f",cmap="Blues",vmax=0.52, vmin=0.42,ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=10)
ax2.set_yticklabels(ax2.get_yticklabels(), rotation=0)
ax2.set_title('1 Hour Observation')
plt.tight_layout(pad=2)
plt.show()