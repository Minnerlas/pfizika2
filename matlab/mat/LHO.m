function dy = LHO(t,y,omega0)
dy = zeros(2,1);
dy(1) = y(2);
dy(2) = -omega0^2*y(1);