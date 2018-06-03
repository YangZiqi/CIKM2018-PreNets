function y = likelihood_2(X,para)
% para: alpha, beta
T = 5;
% 将第一个点的时间设为观察起点，时间单位为分钟
% X = (X-X(1))/60 ;
[~,N] = size(X) ;
temp = 0;
for i=1:N
    temp =temp + log(max(para(1)*length(X(i))*exp(-para(2)*(X(i))),0.00001));
end
y = -para(1)/para(2)*N+N*para(1)/para(2)*exp(-para(2)*(T))+temp;
y = -y;
end