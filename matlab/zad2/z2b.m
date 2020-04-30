clear
close all
clc

vreme=linspace(0,60,1000);
options=odeset;

omega0=10;
alfa=omega0/20;
x0=10;
v0=0;
F0=20;
m=1;
Omega = linspace(0,2*omega0,200);

aaa=arrayfun(@A,Omega);

figure(1);
plot(Omega,aaa,'--');
grid on


