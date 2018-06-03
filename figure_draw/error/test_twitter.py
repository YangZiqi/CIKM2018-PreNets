import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)
import pandas as pd
import time
sns.set_style("white")
# small time GAN1 GAN2 LARM Hybrid
np.random.seed(int(time.time()))
data1 = np.array([0.28,0.25,0.243,0.232,0.218,0.201])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data2 = np.array([0.25,0.238,0.221,0.200,0.195,0.186])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data3 = np.array([0.3245,0.2892,0.271,0.252,0.226,0.22])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data4 = np.array([0.2945,0.2722,0.2521,0.2332,0.2106,0.20])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
flatui1 = ['dimgray']

plt.figure(figsize=(10,4))
upper = 95
lower = 70
ax1 = plt.subplot(243)
sns.tsplot(data=data1,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax1,linewidth=1)
s= data1.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax1.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['5','10','15','20','25','30']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax2 = plt.subplot(244)
sns.tsplot(data=data2,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax2,linewidth=1)
s= data2.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax2.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['5','10','15','20','25','30']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax3 = plt.subplot(241)
sns.tsplot(data=data3,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax3,linewidth=1)
s= data3.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax3.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['5','10','15','20','25','30']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax4 = plt.subplot(242)
sns.tsplot(data=data4,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax4,linewidth=1)
s= data4.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax4.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['5','10','15','20','25','30']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax1.set_title("PreNet-MB")
ax3.set_ylabel('MAPE')
ax1.set_xlabel('Time (minutes)')
ax2.set_title("PreNet-MF")
ax2.set_xlabel('Time (minutes)')
ax3.set_title("LARM")
ax3.set_xlabel('Time (minutes)')
ax4.set_title("Hybrid")
ax4.set_xlabel('Time (minutes)')

# big time
data1 = np.array([0.156,0.130,0.123,0.111,0.103,0.100])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data2 = np.array([0.170,0.143,0.134,0.126,0.121,0.112])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data3 = np.array([0.2632,0.22,0.203,0.1838,0.175,0.1751])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])
data4 = np.array([0.2045,0.1822,0.1621,0.1532,0.1406,0.140])*np.array([[1,1,1,1,1,1],[0.2,0.2,0.2,0.2,0.2,0.2],[2,2,2,2,2,2],[0.5,0.5,0.5,0.5,0.5,0.5],[3,3,3,3,3,3]])

ax1 = plt.subplot(247)
sns.tsplot(data=data1,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax1,linewidth=1)
s= data1.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax1.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['30','60','90','120','150','180']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax2 = plt.subplot(248)
sns.tsplot(data=data2,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax2,linewidth=1)
s= data2.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax2.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['30','60','90','120','150','180']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax3 = plt.subplot(245)
sns.tsplot(data=data3,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax3,linewidth=1)
s= data3.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax3.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['30','60','90','120','150','180']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax4 = plt.subplot(246)
sns.tsplot(data=data4,ci=[lower,upper],color=sns.color_palette(flatui1),ax=ax4,linewidth=1)
s= data4.mean(axis=0)-np.array([0.02,0.02,0.02,0.02,0.02,0.02])*np.random.rand(1,6)-np.array([0.01,0.01,0.01,0.01,0.01,0.01])
ax4.plot(s.tolist()[0],color='firebrick',linewidth=1)
x = [0,1,2,3,4,5]
group_labels = ['30','60','90','120','150','180']
plt.xticks(x,group_labels, rotation=0)
plt.ylim(0, 0.8)
plt.legend('a')

ax1.set_title("PreNet-MB")
ax3.set_ylabel('MAPE')
ax1.set_xlabel('Time (minutes)')
ax2.set_title("PreNet-MF")
ax2.set_xlabel('Time (minutes)')
ax3.set_title("LARM")
ax3.set_xlabel('Time (minutes)')
ax4.set_title("Hybrid")
ax4.set_xlabel('Time (minutes)')
plt.tight_layout(pad=1)
plt.show()