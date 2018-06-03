%% load data
% data = textread('data_small.txt');
% index = textread('index_small.txt');
% [cas_num,~] = size(index);
% [tweet_num,~]  =size(data);
clear all 
clc
T = 100;
interval = 60;
data = textread('movie_series2.txt');
cascade_list = data/(3600*24);
cascade_list = cascade_list-cascade_list(:,1);
[cas_num,~] = size(cascade_list);
% %% list cascade
% % get list
% cascade_list = ones(cas_num,max(index(:,3)-index(:,2))+1)*(-1) ;
% follower_list = ones(cas_num,max(index(:,3)-index(:,2))+1)*(-1) ;
% t = 0 ;
% cascade_index = 0 ;
% for i=1:tweet_num
%     if i==1
%         cascade_index = cascade_index + 1 ;
%         t = 1;
%         cascade_list(cascade_index,t) = data(i,1) ;
%         follower_list(cascade_index,t) = data(i,2) ;
%     else
%         if data(i,1)==0 && data(i-1,1)~=0
%             cascade_index = cascade_index + 1 ;
%             t = 1;
%             cascade_list(cascade_index,t) = data(i,1) ;
%             follower_list(cascade_index,t) = data(i,2) ;
%         else
%             t = t+1 ;
%             cascade_list(cascade_index,t) = data(i,1) ;
%             follower_list(cascade_index,t) = data(i,2) ;
%          end
%     end
% end
% cascade_list = cascade_list/60 ;
% cascade_list = cascade_list(:,1:end);
% cascade_list = cascade_list-cascade_list(:,1);
% follower_list = follower_list(:,1:end);
%% alpha cascade_list & feature extraction
alpha_cascade_list = zeros(739,interval);
X_cascade = zeros(739,3);
y_cascade = zeros(739,1);
for i=1:739
    temp = cascade_list(i,:);
    temp = temp(find(temp>=0));
    for j=1:interval
        alpha_cascade_list(i,j) = length(find(temp<=T/interval*j))/length(find(temp<=T));
    end
    y_cascade(i) = length(find(temp<=T))/length(temp);
    temp = temp(find(temp<=T));
    X_cascade(i,1) = length(temp);
    temp = diff(temp);
    X_cascade(i,2) = sum(temp)/length(temp);
    temp = diff(temp);
    X_cascade(i,3) = sum(temp)/length(temp);
end

%% K-means 6 categories 
idx = kmeans(alpha_cascade_list,6);
RT1 = fitrtree(X_cascade(find(idx==1),:),y_cascade(find(idx==1)));
RT2 = fitrtree(X_cascade(find(idx==2),:),y_cascade(find(idx==2)));
RT3 = fitrtree(X_cascade(find(idx==3),:),y_cascade(find(idx==3)));
RT4 = fitrtree(X_cascade(find(idx==4),:),y_cascade(find(idx==4)));
RT5 = fitrtree(X_cascade(find(idx==5),:),y_cascade(find(idx==5)));
RT6 = fitrtree(X_cascade(find(idx==6),:),y_cascade(find(idx==6)));

%% test 
result = zeros(739,2);
for i=1:739
    i
    temp = cascade_list(i,:);
    real = length(temp(find(temp>=0)));
    temp = temp(find(temp<=T & temp>=0));
    result(i,2) = length(temp);
    X(1) = length(temp);
    temp = diff(temp);
    X(2) = sum(temp)/length(temp);
    temp = diff(temp);
    X(3) = sum(temp)/length(temp);
    temp_result(1) = predict(RT1,X);
    temp_result(2) = predict(RT2,X);
    temp_result(3) = predict(RT3,X);
    temp_result(4) = predict(RT4,X);
    temp_result(5) = predict(RT5,X);
    temp_result(6) = predict(RT6,X);
    [~,temp_index] = min(abs(temp_result-real));
    result(i,1) = temp_result(temp_index); 
end


for i =1:739
    result(i,3) = result(i,2)/result(i,1);
end

