clear
close all
clc

vreme=linspace(0,60,1000);
options=odeset;
%[t,y]=ode45(@LHO,vreme,[y0,v0],options,omega);

figure(1);

for i=1:4
    m=1;
    omega=1;
    x0=10;
    v0=20;
    alpha=[omega, omega/10, 15*omega, 0];

    [t,y]=ode45(@prigusene_oscilacije,vreme,[x0,v0],options,omega,alpha(i));
    subplot(2,2,i);
   
    plot(t,y(:,1));
    grid on
end
