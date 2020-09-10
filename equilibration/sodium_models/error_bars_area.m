% Template for area like error-bars
% https://www.mathworks.com/matlabcentral/answers/39540-continuous-error-bars

x = linspace(0,1,20)';
y = sin(x);
dy = .1*(1+rand(size(y))).*y;  % made-up error values
fill([x;flipud(x)],[y-dy;flipud(y+dy)],[.9 .9 .9],'linestyle','none');
line(x,y)