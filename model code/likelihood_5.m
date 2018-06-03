function y = likelihood_5(X,para)
% para: alpha, beta, v
T = 200;
% 将第一个点的时间设为观察起点，时间单位为分钟
% X = (X-X(1))/60 ;
[~,N] = size(X);
temp = 0;
for i=1:N
    temp =temp + log(max(para(3)*exp(-para(2)*X(i))+para(1)*sum(exp(-para(2)*(X(i)-X(1:i)))),0.00001));
end
y = para(3)/para(2)*(exp(-para(2)*T)-1)-para(1)/para(2)*N+para(1)/para(2)*sum(exp(-para(2)*(T-X)))+temp;
y = -y;
end