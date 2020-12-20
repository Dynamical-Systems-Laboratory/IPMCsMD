%% Script for computing the diffusion coefficients from MSD and plotting of
%% MSD in each direction

clear
close all
load('../E1V_nm/processed_E1V_nm_nafion_ion_diff')

msd_fig(xx, yx, dyx,[213/255, 242/255, 218/255],[61/255, 201/255, 61/255], 1, '$\mathrm{MSD}\left(x\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_x')
msd_fig(xy,yy,dyy,[209/255, 228/255, 237/255],[69/255, 162/255, 208/255], 2, '$\mathrm{MSD}\left(y\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_y')
msd_fig(xz,yz,dyz,[242/255, 208/255, 213/255],[208/255, 106/255, 120/255], 3, '$\mathrm{MSD}\left(z\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_z')

clear
close all 
load('processed_E5V_nm_nafion_ion_diff')

add_msd_fig(xx, yx, dyx,[125/255, 186/255, 135/255],[27/255, 133/255, 27/255], 1, '$\mathrm{MSD}\left(x\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_x')
add_msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[13/255, 93/255, 133/255], 2, '$\mathrm{MSD}\left(y\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_y')
add_msd_fig(xz,yz,dyz,[232/255, 144/255, 156/255],[156/255, 19/255, 37/255], 3, '$\mathrm{MSD}\left(z\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_ion_z')

clear
close all
load('../E1V_nm/processed_E1V_nm_nafion_water_diff')

msd_fig(xx, yx, dyx,[213/255, 242/255, 218/255],[61/255, 201/255, 61/255], 1, '$\mathrm{MSD}\left(x\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_x')
msd_fig(xy,yy,dyy,[209/255, 228/255, 237/255],[69/255, 162/255, 208/255], 2, '$\mathrm{MSD}\left(y\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_y')
msd_fig(xz,yz,dyz,[242/255, 208/255, 213/255],[208/255, 106/255, 120/255], 3, '$\mathrm{MSD}\left(z\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_z')

clear
close all 
load('processed_E5V_nm_nafion_water_diff')

add_msd_fig(xx, yx, dyx,[125/255, 186/255, 135/255],[27/255, 133/255, 27/255], 1, '$\mathrm{MSD}\left(x\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_x')
add_msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[13/255, 93/255, 133/255], 2, '$\mathrm{MSD}\left(y\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_y')
add_msd_fig(xz,yz,dyz,[232/255, 144/255, 156/255],[156/255, 19/255, 37/255], 3, '$\mathrm{MSD}\left(z\right)$, $\left[\mathrm{\AA^2}\right]$', 'msd_water_z')


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
    set(axes1,'FontSize',28,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
        'on');
    
    grid on
    
    % Uncomment for custom limits
    %ylim([0.0,ymax]);
    
    xlim([8.6, 11.6])
    xticks([8.6, 9.6, 10.6, 11.6])
    
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

