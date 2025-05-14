close all;
clc;

roz = fopen('fuz0_0.txt');

b = fscanf(roz, '%g', [2 5]);

fclose(roz);

B=b(1:1,:);

A=b(2:2,:);

plot(A,B,'black.', 'MarkerSize', 10);