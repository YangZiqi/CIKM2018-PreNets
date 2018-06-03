function y = likelihood_plus_2(X,para)
% para: v,alpha1,alpha2,alpha3 
T = 240;
% 将第一个点的时间设为观察起点，时间单位为分钟
% X = (X-X(1))/60 ;
[~,N] = size(X);
temp = 0;
for i=4:N
    temp = temp+log(max(1/(para(1)+para(2)*(X(i)-X(i-1))+para(3)*(X(i)-X(i-2))+para(4)*(X(i)-X(i-3))),0.001));
end
y = temp;
for i=4:N
    y = y - log(max(1/(para(1)+para(2)*(X(i)-X(i-1))+para(3)*(X(i)-X(i-2))+para(4)*(X(i)-X(i-3))),0.001))/log(2.718281828);
end
y = y - log(max(1/(para(1)+para(2)*(T-X(N-1))+para(3)*(T-X(N-2))+para(4)*(T-X(N-3))),0.001));
y = -y;
end