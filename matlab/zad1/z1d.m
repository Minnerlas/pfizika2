clear
close all
clc

vreme=linspace(0,60,1000);
options=odeset;
%[t,y]=ode45(@LHO,vreme,[y0,v0],options,omega);

figure(1);

for i=2:2
    m=1;
    omega=1;
    x0=10;
    v0=20;
    alpha=[omega, omega/10, 15*omega, 0];

    [t,y]=ode45(@prigusene_oscilacije,vreme,[x0,v0],options,omega,alpha(i));
    
    plot(t,y(:,1));
     Ek=m*y(:,2).^2/2;
    Ep=(m*(omega^2))*y(:,1).^2/2;
    
    plot(t,Ek); hold all
    plot(t,Ep);
    legend('Ek','Ep');
 
    grid on
end
