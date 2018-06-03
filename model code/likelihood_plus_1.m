function y = likelihood_plus_1(X,para)
% para: mu,alpha
T = 240;
% 将第一个点的时间设为观察起点，时间单位为分钟
% X = (X-X(1))/60 ;
[~,N] = size(X) ;
temp = 0;
for i=1:N
    temp = temp+para(1)*X(i)-(i-1)*para(2);
end
y = temp;
for i=1:N-1
    y = y - exp(para(1)*X(i+1)-i*para(2))/para(1) + exp(para(1)*X(i)-i*para(2))/para(1);
end
y = y-exp(para(1)*X(1))/para(1)+1/para(1)-exp(para(1)*T-N*para(2))/para(1)+exp(para(1)*X(N)-N*para(2))/para(1);
y = -y;
end