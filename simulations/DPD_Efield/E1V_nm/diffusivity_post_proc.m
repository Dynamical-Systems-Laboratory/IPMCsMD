%% Post-process MSD averages
clear
%load('nafion_water_diff')
% load('all_nafion_water_diff')
load('all_nafion_ion_diff')

[x,y,dy] = get_mean(time_all, msd_x_all);
msd_fig(x,y,dy,[174/255, 229/255, 183/255],[40/255, 182/255, 40/255], 1, '$\mathrm{MSD_{x}}$')
[Dx_mean, Dx_std] = average_diffusion_coefs(time_all, msd_x_all)

[x,y,dy] = get_mean(time_all, msd_y_all);
msd_fig(x,y,dy,[180/255, 209/255, 223/255],[17/255, 122/255, 175/255], 2, '$\mathrm{MSD_{y}}$')
[Dy_mean, Dy_std] = average_diffusion_coefs(time_all, msd_y_all)

[x,y,dy] = get_mean(time_all, msd_z_all);
msd_fig(x,y,dy,[229/255, 163/255, 172/255],[201/255, 31/255, 54/255], 3, '$\mathrm{MSD_{z}}$')
[Dz_mean, Dz_std] = average_diffusion_coefs(time_all, msd_z_all)

Dtot = 1./3*(Dx_mean + Dy_mean + Dz_mean)
Dtot_std = 1./3*(Dx_std + Dy_std + Dz_std)

function msd_fig(x,y,dy,clrB, clrF, i, ylab)

    figure1 = figure(i);
    axes1 = axes('Parent',figure1);
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB,'linestyle','none');
    line(x,y, 'LineWidth',2, 'Color', clrF)
            
    % For double checking
%     hold on 
%     errorbar(x,y,dy,'b');
    
    % Create ylabel
    ylabel(ylab,'Interpreter','latex');

    % Create xlabel
    xlabel('Time, [fs]','Interpreter','latex');

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

function [p_ave, p_std] = average_diffusion_coefs(x, y)
   for i = 1:size(x,1)
       % Currently for electric field
       p = polyfit(x(i,1:50),y(i,1:50),1);
%        p = polyfit(x(i,:),y(i,:),1);
       all_p(i) = p(1)*0.1/2.0;
   end
   p_ave = mean(all_p);
   p_std = std(all_p);
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