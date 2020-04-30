function dy = prinudne_oscilacije(t,y,alfa,m,F0,Omega,omega0)
dy = zeros(2,1);
dy(1) = y(2);
dy(2) = (F0/m)*sin(t*Omega)-(omega0^2)*y(1)-2*alfa*y(2);