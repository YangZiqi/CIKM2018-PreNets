import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)
import pandas as pd
import time
sns.set_style("white")
# small time GAN1 GAN2 LARM Hybrid
np.random.seed(int(time.time()))
data1 = np.array([0.3321,0.2921,0.2643,0.2382,0.218,0.201])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data2 = np.array([0.3145,0.288,0.261,0.2474,0.235,0.2186])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data3 = np.array([0.3745,0.3292,0.291,0.272,0.256,0.24])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data4 = np.array([0.3245,0.2922,0.2721,0.2532,0.2306,0.22])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])

flatui1 = ['dimgray']

plt.figure(figsize=(10,2))
upper = 95
lower = 70
ax1 = plt.subplot(143)
sns.tsplot(data=data1,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax1,linewidth=1)
s= data1.mean(axis=0)-np.array([0.03,0.03,0.03,0.03,0.03,0.03])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax1.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['20','40','60','80','100','120']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.9)
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.legend('a')

ax2 = plt.subplot(144)
sns.tsplot(data=data2,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax2,linewidth=1)
s= data2.mean(axis=0)-np.array([0.03,0.03,0.03,0.03,0.03,0.03])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax2.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['20','40','60','80','100','120']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.9)
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.legend('a')

ax3 = plt.subplot(141)
sns.tsplot(data=data3,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax3,linewidth=1)
s= data3.mean(axis=0)-np.array([0.03,0.03,0.03,0.03,0.03,0.03])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax3.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['20','40','60','80','100','120']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.9)
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.legend('a')

ax4 = plt.subplot(142)
sns.tsplot(data=data4,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax4,linewidth=1)
s= data4.mean(axis=0)-np.array([0.03,0.03,0.03,0.03,0.03,0.03])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax4.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['20','40','60','80','100','120']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.9)
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.legend('a')

ax1.set_title("PreNet-MB")
ax3.set_ylabel('MAPE')
ax1.set_xlabel('Time (days)')
ax2.set_title("PreNet-MF")
ax2.set_xlabel('Time (days)')
ax3.set_title("LARM")
ax3.set_xlabel('Time (days)')
ax4.set_title("Hybrid")
ax4.set_xlabel('Time (days)')
plt.tight_layout(pad=1)
plt.show()