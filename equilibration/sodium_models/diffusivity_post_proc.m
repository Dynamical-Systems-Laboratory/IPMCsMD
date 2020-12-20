%% Script for computing the diffusion coefficients from MSD and plotting of
%% MSD in each direction

clear
close all

% When to start figure numbering for each species
wfig = 1;
ifig = 4;

msd_plot_and_save('eq_nafion_water_diff', 'processed_eq_nafion_water_diff', wfig)
msd_plot_and_save('eq_nafion_ion_diff', 'processed_eq_nafion_ion_diff', ifig)

function msd_plot_and_save(post_fin, post_fout, jfig)
    
    load(post_fin)

    % Start and end point for looking for a diffusive regime
    nt0 = 4000; 
    ntF = 5500;

    [xx,yx,dyx] = get_mean(time_all, msd_x_all);
    msd_fig(xx, yx, dyx,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], jfig, '$\mathrm{MSD_{x}}$')
    [Dx_mean, Dx_std] = average_diffusion_coefs(time_all, msd_x_all, nt0, ntF)
    hold on
    plot(xx/1e6, yx(1) + 2*Dx_mean*10*(xx-xx(1)), 'k--')
    axis tight
    hold off

    [xy,yy,dyy] = get_mean(time_all, msd_y_all);
    msd_fig(xy,yy,dyy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], jfig+1, '$\mathrm{MSD_{y}}$')
    [Dy_mean, Dy_std] = average_diffusion_coefs(time_all, msd_y_all, nt0, ntF)
    hold on
    plot(xy/1e6, yy(1) + 2*Dy_mean*10*(xy-xy(1)), 'k--')
    hold off

    [xz,yz,dyz] = get_mean(time_all, msd_z_all);
    msd_fig(xz,yz,dyz,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], jfig+2, '$\mathrm{MSD_{z}}$')
    [Dz_mean, Dz_std] = average_diffusion_coefs(time_all, msd_z_all, nt0, ntF)
    hold on
    plot(xz/1e6, yz(1) + 2*Dz_mean*10*(xz-xz(1)), 'k--')
    hold off

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

function [p_ave, p_std] = average_diffusion_coefs(x, y, nt0, ntF)
    % Compute diffusion coefficient from the fit that is closest to beta=1,
    % as determined on the inteval nt0 to ntF-1
  
   tvals = [nt0:1:ntF-1];

   all_ind = 1;
   fprintf("New set\n")
   for i = 1:size(x,1)
       Ds = [];
       betas = [];
       for j=1:length(tvals)
            p = polyfit(log(x(i,tvals(j):end)-x(i,tvals(j)-1)), log(y(i,tvals(j):end)-y(i,tvals(j)-1)), 1);
            betas(j) = real(p(1));
            Ds(j) = exp(real(p(2)))*0.1/2.0;
       end
       err = abs(betas-1);
       ind = find(err == min(err));
       
       % If still larger than 0.05, skip this value
       if min(err) > 0.05
           continue
       end
       t0 = tvals(ind);
       
       % Comment out if no inspection needed
       fprintf("Ds and beta for set %d: %e, %f\n", i, Ds(ind), betas(ind))

       all_p(all_ind) = Ds(ind);
       all_ind = all_ind + 1;
   end
   p_ave = mean(all_p);
   p_std = std(all_p);
   disp(all_ind-1)
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