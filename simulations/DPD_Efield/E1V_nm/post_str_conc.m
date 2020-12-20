%% Post-process RDF averages
clear
load('stress_conc_data')

% Box and bin dimensions
box = [-2.0000000000000000e+00 4.5000000000000000e+01
-1.6497992171793179e+00 4.4727718147189719e+01
-1.6497992171793179e+00 4.4727718147189719e+01];
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

plot_sc_error_area(xc, all_pre_c_h2o, all_c_h2o, 'Water', 1, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Number of atoms')
plot_sc_error_area(xc, all_pre_c_na, all_c_na, 'Sodium', 2, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Number of atoms')
plot_sc_error_area(xc, all_pre_c_s, all_c_s, 'Sulfonate', 3, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Number of atoms')

plot_sc_error_area(xc, all_pre_s_xx, all_s_xx, 'xx component', 4, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Stress, [atm]')
plot_sc_error_area(xc, all_pre_s_yy, all_s_yy, 'yy component', 5, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]')
plot_sc_error_area(xc, all_pre_s_zz, all_s_zz, 'zz component', 6, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]')

plot_sc_error_area(xc, all_pre_s_xy, all_s_xy, 'xy component', 7, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Stress, [atm]')
plot_sc_error_area(xc, all_pre_s_yz, all_s_yz, 'yz component', 8, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]')
plot_sc_error_area(xc, all_pre_s_xz, all_s_xz, 'xz component', 9, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]')

% % Concentrations, mol/m3
% % Sodium
% pre_c_na = all_pre_c_na/N_avg/V_bin;
% c_na = all_c_na/N_avg/V_bin;
% % Sulfur
% pre_c_s = all_pre_c_s/N_avg/V_bin;
% c_s = all_c_s/N_avg/V_bin;
% % Water
% pre_c_h2o = all_pre_c_h2o/N_avg/V_bin;
% c_h2o = all_c_h2o/N_avg/V_bin;
% 
% plot_sc_error_area(xc, pre_c_na, c_na, 'Sodium', 1, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Concentration, $\mathrm{[mol/m^3]}$')
% plot_sc_error_area(xc, pre_c_s, c_s, 'Sulfur', 2, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Concentration, $\mathrm{[mol/m^3]}$')
% plot_sc_error_area(xc, pre_c_h2o, c_h2o, 'Water', 3, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Concentration, $\mathrm{[mol/m^3]}$')
% 
% % Stresses, atm
% pre_sigma_ion = -R*T/N_avg/V_bin*(all_pre_c_na);
% sigma_ion = -R*T/N_avg/V_bin*(all_c_na);
% plot_sc_error_area(xc, pre_sigma_ion, sigma_ion, '$\sigma_{ion,xx}$', 4, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Stress, [atm]')
% plot_sc_error_area(xc, all_pre_s_xx-pre_sigma_ion, all_s_xx-sigma_ion, '$\sigma_{pol,xx}$', 5, [174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 'Stress, [atm]')

function plot_sc_error_area(x, y0, y, plot_title, i, clrB, clrF, ylab)
    
    % Create figure
    figure1 = figure(i);

    % Create axes
    axes1 = axes('Parent',figure1);
    
    % Initial
    dy0 = std(y0)';
    y0 = mean(y0)';
    x = x';
    
    hold on
    
    fill([x;flipud(x)],[y0-dy0;flipud(y0+dy0)], clrB,'linestyle','none');
    plot(x,y0, '-o', 'LineWidth',2, 'Color', clrF, 'MarkerSize', 10)
    
    % Final
    dy = std(y)';
    y = mean(y)';
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB*0.8,'linestyle','none');
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