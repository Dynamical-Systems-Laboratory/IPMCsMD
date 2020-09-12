%% Script for computing the diffusion coefficients from MSD and plotting of
%% MSD in each direction

clear
close all
load('processed_E5V_nm_nafion_ion_diff')

msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$', 'msd_ion_x')
msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$', 'msd_ion_y')
msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$', 'msd_ion_z')

clear
close all 
load('../E1V_nm/processed_E1V_nm_nafion_ion_diff')

add_msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$', 'msd_ion_x')
add_msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$', 'msd_ion_y')
add_msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$', 'msd_ion_z')

clear
close all
load('processed_E5V_nm_nafion_water_diff')

msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$', 'msd_water_x')
msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$', 'msd_water_y')
msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$', 'msd_water_z')

clear
close all 
load('../E1V_nm/processed_E1V_nm_nafion_water_diff')

add_msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$', 'msd_water_x')
add_msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$', 'msd_water_y')
add_msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$', 'msd_water_z')


function msd_fig(x,y,dy,clrB, clrF, i, ylab, figname)

    close all

    % Convert from fs to ns
    fs2ns = 1e6;
    x = x/fs2ns;
    
    figure1 = figure(i);
    axes1 = axes('Parent',figure1);
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB,'linestyle','none');
    line(x, y, 'LineWidth',2, 'Color', clrF)
            
    % For errorbars
%     hold on 
%     errorbar(x,y,dy,'b');
    
    % Create ylabel
    ylabel(ylab,'Interpreter','latex');

    % Create xlabel
    xlabel('Time, [ns]','Interpreter','latex');

    % Uncomment the following line to preserve the Y-limits of the axes
    box(axes1,'on');
    % Set the remaining axes properties
    set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
        'on');
    
    grid on
    
    % Uncomment for custom limits
    %ylim([0.0,ymax]);
    
    savefig(figname)
end

function add_msd_fig(x,y,dy,clrB, clrF, i, ylab, figname)

    close all

    % Convert from fs to ns
    fs2ns = 1e6;
    x = x/fs2ns;
    
    figure1 = openfig(figname);
    hold on
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB,'linestyle','none');
    line(x, y, 'LineWidth',2, 'Color', clrF)
            
    % For errorbars
%     hold on 
%     errorbar(x,y,dy,'b');
    
    savefig(figname)
end

