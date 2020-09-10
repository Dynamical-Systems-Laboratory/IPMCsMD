%% Post-process MSD averages
clear
% load('nafion_water_diff')
load('nafion_ion_diff')

% Start and end point for looking for a diffusive regime
nt0 = 4000; 
ntF = 5500;

[x,y,dy] = get_mean(time_all, msd_x_all);
msd_fig(x, y, dy,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$')
[Dx_mean, Dx_std] = average_diffusion_coefs(time_all, msd_x_all, nt0, ntF)
hold on
plot(x/1e6, y(1) + 2*Dx_mean*10*(x-x(1)), 'k--')
axis tight
hold off

[x,y,dy] = get_mean(time_all, msd_y_all);
msd_fig(x,y,dy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$')
[Dy_mean, Dy_std] = average_diffusion_coefs(time_all, msd_y_all, nt0, ntF)
hold on
plot(x/1e6, y(1) + 2*Dy_mean*10*(x-x(1)), 'k--')
hold off

[x,y,dy] = get_mean(time_all, msd_z_all);
msd_fig(x,y,dy,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$')
[Dz_mean, Dz_std] = average_diffusion_coefs(time_all, msd_z_all, nt0, ntF)
hold on
plot(x/1e6, y(1) + 2*Dz_mean*10*(x-x(1)), 'k--')
hold off

Dtot = 1./3*(Dx_mean + Dy_mean + Dz_mean)
Dtot_std = std([Dx_std,Dy_std,Dz_std])

function msd_fig(x,y,dy,clrB, clrF, i, ylab)

    x = x/1e6;
    figure1 = figure(i);
    axes1 = axes('Parent',figure1);
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB,'linestyle','none');
    line(x, y, 'LineWidth',2, 'Color', clrF)
            
    % For double checking
%     hold on 
%     errorbar(x,y,dy,'b');
    
    % Create ylabel
    ylabel(ylab,'Interpreter','latex');

    % Create xlabel
    xlabel('Time, [ns]','Interpreter','latex');

    % Create title
    %title(rdf_title,'Interpreter','latex');

    % Uncomment the following line to preserve the Y-limits of the axes
    box(axes1,'on');
    % Set the remaining axes properties
    set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
        'on');
    
    grid on
    
    % ylim
    %ylim([0.0,ymax]);
end

function [p_ave, p_std] = average_diffusion_coefs(x, y, nt0, ntF)
    % Compute diffusion coefficient from the fit that is closest to beta=1,
    % as determined on the inteval nt0 to ntF-1
  
   tvals = [nt0:1:ntF-1];

   all_ind = 1;
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
       if min(err) > 0.05
           continue
       end
       t0 = tvals(ind);
%        disp(i)
%        disp(betas(ind))
%        disp(Ds(ind))
       all_p(all_ind) = Ds(ind);
       all_ind = all_ind + 1;
   end
   p_ave = mean(all_p);
   p_std = std(all_p);
   disp(all_ind-1)
end

function [x,y,dy] = get_mean(xp, yp)
    % Common x-axis
     x_int = [xp(1,1):(xp(1,2)-xp(1,1))/2.0:xp(1,end)];
    
    for i = 1:size(xp,1)
        % First interpolate to a common t value
        y_int(i,:) = pchip(xp(i,:), yp(i,:), x_int);
    end
    dy = std(y_int)';
    y = mean(y_int)';
    x = x_int';
end