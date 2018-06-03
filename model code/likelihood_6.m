function y = likelihood_6(X1,para)
T =240;
% para: kapa, beta, c, theta, v
% X1: retweeting list


% get the length of X
[~,N] = size(X1);
% 第一项+第二项
y = 0;
for i=2:N
    temp = 0;
    for j=1:i-1
        temp = temp + para(1)/((X1(i)-X1(j)+para(3))^(para(4)+1));
    end
    y = y + log(max(0.0001,temp+para(5)*exp(-para(2)*X1(i))));
end
%第三项
for i=1:N
    y = y - para(1)*(1/(para(4)*para(3)^para(4))-(T+para(3)-X1(i))^(-para(4))/para(4));
end
% v这一项
y = y-para(5)/para(2)+para(5)/para(2)*exp(-para(2)*T);
y = -y;
end