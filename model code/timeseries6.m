%% load data
clear all 
clc
T = 240;
interval = 60;
data = textread('movie_series2.txt');
cascade_list = data/(3600*24);
cascade_list = cascade_list-cascade_list(:,1);
[cas_num,~] = size(cascade_list);

output = zeros(cas_num,interval);
for num = 1:739
    num
    test_cascade = cascade_list(num,:);
    test_index = find(test_cascade<T & test_cascade>=0);
    
    [~,num2] = size(test_index);
    if num2>=10
        test_cascade_list = test_cascade(test_index);
        options = optimoptions('fmincon','Display','off');
        [para,~] = fmincon(@(para) likelihood_6(test_cascade_list,para),[rand(1)*2;rand(1)*1;rand(1)*1;rand(1)*1;20],[],[],[],[],[0.1;0.1;2;0.1;0],[1.5;1;100;2;50],[],options);
        % µÃµ½n*
        alpha = 2.016;
        nStar = para(1)*(alpha-1)/((alpha-1-para(2))*para(4)*para(3)^para(4));
          for i=1:interval
              test_index2 = test_cascade_list(find(test_cascade_list<T/interval*i)) ;
              output(num,i) = length(test_index2)+para(5)/para(2)*exp(-para(2)*T);
              for j=1:length(test_index2)
                  output(num,i) = output(num,i) + para(1)/(para(4)*(T+para(3)-test_index2(j))^para(4));
              end
   
          end
    end
end

for i = 1:739
    output(i,interval+1) = length(find(cascade_list(i,:)>0));
end