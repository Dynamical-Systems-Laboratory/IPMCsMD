%% Stress and concentration plots for all voltages
clear
load('../E1V_nm/E1V_nm_stress_conc_data')
% load('stress_conc_data')

% Box and bin dimensions
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

plot_sc_error_area(xc, all_pre_c_h2o, all_c_h2o, 'Oxygen in a water molecule', 1, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Number of atoms', 'water')
plot_sc_error_area(xc, all_pre_c_na, all_c_na, 'Sodium ion', 2, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Number of atoms', 'sodium')
plot_sc_error_area(xc, all_pre_c_s, all_c_s, 'Sulfur', 3, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Number of atoms', 'sulfur')

plot_sc_error_area(xc, all_pre_s_xx, all_s_xx, '$\sigma_{xx}$', 4, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Stress, [atm]', 'sigma_xx')
plot_sc_error_area(xc, all_pre_s_yy, all_s_yy, '$\sigma_{yy}$', 5, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]', 'sigma_yy')
plot_sc_error_area(xc, all_pre_s_zz, all_s_zz, '$\sigma_{zz}$', 6, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]', 'sigma_zz')

plot_sc_error_area(xc, all_pre_s_xy, all_s_xy, '$\sigma_{xy}$', 7, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Stress, [atm]', 'sigma_xy')
plot_sc_error_area(xc, all_pre_s_yz, all_s_yz, '$\sigma_{yz}$', 8, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]', 'sigma_yz')
plot_sc_error_area(xc, all_pre_s_xz, all_s_xz, '$\sigma_{xz}$', 9, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]', 'sigma_xz')

clear
close all 
% load('../E1V_nm/E1V_nm_stress_conc_data')
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

add_sc_error_area(xc, all_c_h2o, 'Oxygen in a water molecule', 1, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Number of atoms', 'water')
add_sc_error_area(xc, all_c_na, 'Sodium ion', 2, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Number of atoms', 'sodium')
add_sc_error_area(xc,all_c_s, 'Sulfur', 3, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Number of atoms', 'sulfur')

add_sc_error_area(xc, all_s_xx, '$\sigma_{xx}$', 4, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Stress, [atm]', 'sigma_xx')
add_sc_error_area(xc, all_s_yy, '$\sigma_{yy}$', 5, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]', 'sigma_yy')
add_sc_error_area(xc, all_s_zz, '$\sigma_{zz}$', 6, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]', 'sigma_zz')

add_sc_error_area(xc, all_s_xy, '$\sigma_{xy}$', 7, [186/255, 149/255, 193/255],[134/255, 5/255, 159/255], 'Stress, [atm]', 'sigma_xy')
add_sc_error_area(xc, all_s_yz, '$\sigma_{yz}$', 8, [180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 'Stress, [atm]', 'sigma_yz')
add_sc_error_area(xc, all_s_xz, '$\sigma_{xz}$', 9, [229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 'Stress, [atm]', 'sigma_xz')

function plot_sc_error_area(x, y0, y, plot_title, i, clrB, clrF, ylab, figname)
    
    close all

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
    plot(x,y0, 'o', 'LineWidth',2, 'Color', clrF, 'MarkerSize', 10)
    
    % Final
    dy = std(y)';
    y = mean(y)';
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB*0.8,'linestyle','none');
    plot(x,y, 's', 'LineWidth',2, 'Color', clrF*0.5, 'MarkerSize',  10)

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
   
    savefig(figname)
    
end

function add_sc_error_area(x, y, plot_title, i, clrB, clrF, ylab, figname)
    
     close all

    figure1 = openfig(figname);
    hold on
        
    x = x';
    dy = std(y)';
    y = mean(y)';
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB*0.8,'linestyle','none');
    plot(x,y, 's', 'LineWidth',2, 'Color', clrF*0.5, 'MarkerSize',  10)

    hold off
    
    savefig(figname)
   
end