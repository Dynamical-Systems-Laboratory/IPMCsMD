function plot_sc_error_area(x, y0, y, plot_title, i, clrB, clrF, ylab, figname)
    
    % Create figure
    figure1 = openfig(figname);

    % Create axes
%     axes1 = axes('Parent',figure1);
    
    % Initial
    dy0 = std(y0)';
    y0 = mean(y0)';
    x = x';
    
    hold on
    
%     fill([x;flipud(x)],[y0-dy0;flipud(y0+dy0)], clrB,'linestyle','none');
%     plot(x,y0, '-o', 'LineWidth',2, 'Color', clrF, 'MarkerSize', 10)
    
    % Final
    dy = std(y)';
    y = mean(y)';
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB*0.8,'linestyle','none');
    plot(x,y, '-s', 'LineWidth',2, 'Color', clrF*0.5, 'MarkerSize',  10)

    hold off
    
    % Create ylabel
%     ylabel(ylab,'Interpreter','latex');
% 
%     % Create xlabel
%     xlabel('x direction, [nm]','Interpreter','latex');
% 
%     % Create title
%     title(plot_title,'Interpreter','latex');
% 
%     % Uncomment the following line to preserve the Y-limits of the axes
%     % ylim(axes1,[0 5]);
%     box(axes1,'on');
%     % Set the remaining axes properties
%     set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
%         'on');
   
end