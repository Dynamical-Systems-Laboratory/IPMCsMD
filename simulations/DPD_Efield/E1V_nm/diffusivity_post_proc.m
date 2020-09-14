%% Script for computing the diffusion coefficients from MSD and plotting of
%% MSD in each direction

clear
close all

% When to start figure numbering for each species
wfig = 1;
ifig = 4;

msd_plot_and_save('E1V_nm_nafion_water_diff', 'processed_E1V_nm_nafion_water_diff', wfig)
msd_plot_and_save('E1V_nm_nafion_ion_diff', 'processed_E1V_nm_nafion_ion_diff', ifig)

function msd_plot_and_save(post_fin, post_fout, jfig)
    
    load(post_fin)

    % Interval for computing the diffusion coefficients
    nt0 = 1; 
    % Original was 50 but 500 covers the pre-pile up range
    ntF = 250;

    [xx,yx,dyx] = get_mean(time_all, msd_x_all);
    msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], jfig, '$\mathrm{MSD_{x}}$')
    [Dx_mean, Dx_std] = average_diffusion_coefs(time_all, msd_x_all, nt0, ntF)
    
    [xy,yy,dyy] = get_mean(time_all, msd_y_all);
    msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], jfig+1, '$\mathrm{MSD_{y}}$')
    [Dy_mean, Dy_std] = average_diffusion_coefs(time_all, msd_y_all, nt0, ntF)
    

    [xz,yz,dyz] = get_mean(time_all, msd_z_all);
    msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], jfig+2, '$\mathrm{MSD_{z}}$')
    [Dz_mean, Dz_std] = average_diffusion_coefs(time_all, msd_z_all, nt0, ntF)
    
    Dtot = 1./3*(Dx_mean + Dy_mean + Dz_mean)
    Dtot_std = std([Dx_std,Dy_std,Dz_std])

    save(post_fout)
end

function msd_fig(x,y,dy,clrB, clrF, i, ylab)

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
end

function [p_ave, p_std] = average_diffusion_coefs(x, y, t0, tf)
   for i = 1:size(x,1)
       % For the intial (before pile-up) electric field part only
       p = polyfit(x(i,t0:tf),y(i,t0:tf),1);
%        p = polyfit(x(i,:),y(i,:),1);
       all_p(i) = p(1)*0.1/2.0;
   end
   p_ave = mean(all_p);
   p_std = std(all_p);
end

function [x,y,dy] = get_mean(xp, yp)
    % Compute statistics of the msd - average (y) and standard deviation
    % (dy) on a common time axis (x)
    
    % Common x-axis, refined by a factor of 2
     x_int = [xp(1,1):(xp(1,2)-xp(1,1))/2.0:xp(1,end)];
    
    for i = 1:size(xp,1)
        % First interpolate to a common t value
        y_int(i,:) = pchip(xp(i,:), yp(i,:), x_int);
    end
    dy = std(y_int)';
    y = mean(y_int)';
    x = x_int';
end