%% Post-process RDF averages
clear
load('E1V_nm_stress_conc_data')

% Box and bin dimensions (Seed 1 - last damp without efield
box = [-6.8920100281133756e-01 4.2604373712814919e+01;
-3.9211809832795872e+00 4.5836353693286085e+01;
-5.3723467213784559e-01 4.2452407382139313e+01];

dx=box(1,2)-box(1,1);
L=dx/10;
x=0:L/20:L;
xc=x(2:end)-L/20/2;

% Volume of one bin, m3
V_bin = dx/20*(box(2,2)-box(2,1))*(box(3,2)-box(3,1))*1e-30;
% Temperature, K
T = 300;
% Universal gas constant, atm*m3/(mol K)
R = 8.2057e-5;
% Avogadro's number
N_avg = 6.0221409e+23;
% Charge, C
e_charge = 1.602176634e-19;
% Conversion to V/nm
m2nm = 1e9;
A2m = 1e-10;

n_i = all_c_na - all_c_s;
E_i = (sum(n_i*dx/20*A2m,2)*e_charge/V_bin)/m2nm;
mean(E_i)
std(E_i)


plot_sc_error_area(xc, n_i, 'ni', 1, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Number of atoms')


function plot_sc_error_area(x, y, plot_title, i, clrB, clrF, ylab)
    
    % Create figure
    figure1 = figure(i);

    % Create axes
    axes1 = axes('Parent',figure1);
    
    % Initial
    x = x';
     
    % Final
    dy = std(y)';
    y = mean(y)';
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB*0.8,'linestyle','none');
    hold on
    plot(x,y, '-s', 'LineWidth',2, 'Color', clrF*0.5, 'MarkerSize',  10)

    hold off
    
    % Create ylabel
    ylabel(ylab,'Interpreter','latex');

    % Create xlabel
    xlabel('x direction, [nm]','Interpreter','latex');

    % Create title
    title(plot_title,'Interpreter','latex');

    % Uncomment the following line to preserve the Y-limits of the axes
    % ylim(axes1,[0 5]);
    box(axes1,'on');
    % Set the remaining axes properties
    set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
        'on');
   
end