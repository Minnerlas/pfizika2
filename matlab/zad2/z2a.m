clear
close all
clc

vreme=linspace(0,60,1000);
options=odeset;
%[t,y]=ode45(@LHO,vreme,[y0,v0],options,omega);



omega0=10;
alfa=omega0/20;
x0=10;
v0=0;
F0=20;
Omega=2;
m=1;

[t,y]=ode45(@prinudne_oscilacije,vreme,[x0,v0],options,alfa,m,F0,Omega,omega0);

figure(1);
plot(t,y(:,1));
grid on

figure(2);
plot(y(:,1),y(:,2));
grid on

figure(3);
plot(y(:,1),y(:,2));
grid on
xlim([-1,1]);
ylim([-5,5]);