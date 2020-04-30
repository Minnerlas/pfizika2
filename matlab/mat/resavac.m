clear
close all
clc

vreme=linspace(0,20,1000);
options=odeset;
%[t,y]=ode45(@LHO,vreme,[y0,v0],options,omega);

for i=1:4
    m=1;
    omega=[.5 1 2 4];
    x0=5;
    v0=0;

    [t,y]=ode45(@LHO,vreme,[x0,v0],options,omega(i));
    
%     figure((i-1)*4+1);
%     plot(t,y(:,1));
%     grid on
%     
%     figure((i-1)*4+2);
%     plot(t,y(:,2));
%     grid on
%     
%     figure((i-1)*4+3);
%     plot(y(:,1),y(:,2));
%     grid on

    figure((i-1)*1+1);
    subplot(2,2,1)
    plot(t,y(:,1));
    grid on
    
    subplot(2,2,2)
    plot(t,y(:,2));
    grid on
    
    subplot(2,2,3)
    plot(y(:,1),y(:,2));
    grid on
    
    Ek=m*y(:,2).^2/2;
    Ep=(m*(omega(i)^2))*y(:,1).^2/2;
    subplot(2,2,4);
    plot(t,Ek); hold all
    plot(t,Ep); hold all
    plot(t,Ek+Ep);
    legend('Ek','Ep','Eu');
    grid on
end
