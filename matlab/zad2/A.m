function dy = A(ulaz)
omega0=10;
alfa=omega0/20;
F0=20;
m=1;
dy=(F0/m)/(sqrt((omega0^2-ulaz^2)^2+(2*alfa*ulaz)^2));