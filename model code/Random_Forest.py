##### T ##########
T = 5

## the five point summary function
def fivenum(v):
    """Returns Tukey's five number summary (minimum, lower-hinge, median, upper-hinge, maximum) for the input vector, a list or array of numbers based on 1.5 times the interquartile distance"""
    import numpy as np
    from scipy.stats import scoreatpercentile
    try:
        np.sum(v)
    except TypeError:
        print('Error: you must provide a list or array of only numbers')
    q1 = scoreatpercentile(v,25)
    q3 = scoreatpercentile(v,75)
    iqd = q3-q1
    md = np.median(v)
    whisker = 1.5*iqd
    return np.min(v), md-whisker, md, md+whisker, np.max(v)


from scipy.io import loadmat
import pandas as pd
import numpy as np

# unify ratio and cascade_list
ratio = pd.read_csv('ratio.csv',header=None)
ratio = np.array(ratio.iloc[:10000]).tolist()
temp_ratio = []
for i in ratio:
    if i[0]>10 or i[0]==0:
        continue
    else:
        temp_ratio.append(i[0])
                

data = loadmat('cascade_list.mat')
data2 = loadmat('follower_list.mat')
data = pd.DataFrame(data['cascade_list'])
#print data.head()
data2 = pd.DataFrame(data2['follower_list'])

# feature extraction
friend_list = []
avg_1_wait = []
avg_2_wait = []
five_point_summary_1 = []
five_point_summary_2 = []
five_point_summary_3 = []
five_point_summary_4 = []
five_point_summary_5 = []
total_num = []
for i in range(10000):
	if i%10==0:
		print i
	if ratio[i][0]>10 or ratio[i][0]==0:
		continue
	temp = data.iloc[i].tolist()
	temp_follower = data2.iloc[i].tolist()
	temp_cascade = []
	cas_follower = []
	for j in range(len(temp)):
		if temp[j]>=0 and temp[j]<=T:
			temp_cascade.append(temp[j])
			cas_follower.append(temp_follower[j])
		else:
			break
	if len(temp_cascade)<10:
		friend_list.append(0)
		avg_1_wait.append(0)
		avg_2_wait.append(0)
		five_point_summary_1.append(0)
		five_point_summary_2.append(0)
		five_point_summary_3.append(0)
		five_point_summary_4.append(0)
		five_point_summary_5.append(0)
		total_num.append(0)
	else:
		friend_list.append(float(sum(cas_follower))/len(cas_follower))
		temp_cascade_1 = []
		for i in range(len(temp_cascade)/2):
			temp_cascade_1.append(temp_cascade[i])
		temp_cascade_2 = []
		for i in range(len(temp_cascade)-len(temp_cascade)/2):
			temp_cascade_2.append(temp_cascade[i+len(temp_cascade)/2])	
		diff_cascade = []
		for i in range(len(temp_cascade)-1):
			diff_cascade.append(temp_cascade[i+1]-temp_cascade[i])
		avg_1 = []
		for i in range(len(temp_cascade_1)-1):
			avg_1.append(float(temp_cascade_1[i+1])-float(temp_cascade_1[i]))
		try:
			avg_1 = sum(avg_1)/len(avg_1)
		except:
			avg_1 = 0
		avg_2 = []
		for i in range(len(temp_cascade_2)-1):
			avg_2.append(float(temp_cascade_2[i+1])-float(temp_cascade_2[i]))
		try:
			avg_2 = sum(avg_2)/len(avg_2)
		except:
			avg_2 = 0
		avg_1_wait.append(avg_1)
		avg_2_wait.append(avg_2)
		num1, num2, num3, num4, num5 = fivenum(diff_cascade)
		five_point_summary_1.append(num1)
		five_point_summary_2.append(num2)
		five_point_summary_3.append(num3)
		five_point_summary_4.append(num4)
		five_point_summary_5.append(num5)
		total_num.append(len(temp_cascade))



from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=3, random_state=2)
import numpy as np

# fit a Random Forest
X = [friend_list,avg_1_wait,avg_2_wait,five_point_summary_1,five_point_summary_2,five_point_summary_3,five_point_summary_4,five_point_summary_5,total_num]
X = np.matrix(X).T
y = temp_ratio
regr.fit(X,y)
#print X.shape
#print len(y)
#print regr.predict([[1,1,1,1,1,1,1,1,1]])

#print regr.predict([[1,1,1,1,1,1,1,1,1]])
# feature
friend_list = []
avg_1_wait = []
avg_2_wait = []
five_point_summary_1 = []
five_point_summary_2 = []
five_point_summary_3 = []
five_point_summary_4 = []
five_point_summary_5 = []
total_num = []
for i in range(10000):
	if i%10==0:
		print i
	temp = data.iloc[i].tolist()
	temp_follower = data2.iloc[i].tolist()
	temp_cascade = []
	cas_follower = []
	for j in range(len(temp)):
		if temp[j]>=0 and temp[j]<=T:
			temp_cascade.append(temp[j])
			cas_follower.append(temp_follower[j])
		else:
			break
	if len(temp_cascade)<10:
		friend_list.append(0)
		avg_1_wait.append(0)
		avg_2_wait.append(0)
		five_point_summary_1.append(0)
		five_point_summary_2.append(0)
		five_point_summary_3.append(0)
		five_point_summary_4.append(0)
		five_point_summary_5.append(0)
		total_num.append(0)
	else:
		friend_list.append(float(sum(cas_follower))/len(cas_follower))
		temp_cascade_1 = []
		for i in range(len(temp_cascade)/2):
			temp_cascade_1.append(temp_cascade[i])
		temp_cascade_2 = []
		for i in range(len(temp_cascade)-len(temp_cascade)/2):
			temp_cascade_2.append(temp_cascade[i+len(temp_cascade)/2])	
		diff_cascade = []
		for i in range(len(temp_cascade)-1):
			diff_cascade.append(temp_cascade[i+1]-temp_cascade[i])
		avg_1 = []
		for i in range(len(temp_cascade_1)-1):
			avg_1.append(float(temp_cascade_1[i+1])-float(temp_cascade_1[i]))
		try:
			avg_1 = sum(avg_1)/len(avg_1)
		except:
			avg_1 = 0
		avg_2 = []
		for i in range(len(temp_cascade_2)-1):
			avg_2.append(float(temp_cascade_2[i+1])-float(temp_cascade_2[i]))
		try:
			avg_2 = sum(avg_2)/len(avg_2)
		except:
			avg_2 = 0
		avg_1_wait.append(avg_1)
		avg_2_wait.append(avg_2)
		num1, num2, num3, num4, num5 = fivenum(diff_cascade)
		five_point_summary_1.append(num1)
		five_point_summary_2.append(num2)
		five_point_summary_3.append(num3)
		five_point_summary_4.append(num4)
		five_point_summary_5.append(num5)
		total_num.append(len(temp_cascade))

X = [friend_list,avg_1_wait,avg_2_wait,five_point_summary_1,five_point_summary_2,five_point_summary_3,five_point_summary_4,five_point_summary_5,total_num]
X = np.matrix(X).T
s = regr.predict(X)
s = pd.DataFrame(s)
s.to_csv("cikm2018.csv")
