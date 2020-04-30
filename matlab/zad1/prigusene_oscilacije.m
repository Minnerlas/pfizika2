function dy = prigusene_oscilacije(t,y,omega0,alpha)
dy = zeros(2,1);
dy(1) = y(2);
dy(2) = -omega0^2*y(1)-2*alpha*y(2);