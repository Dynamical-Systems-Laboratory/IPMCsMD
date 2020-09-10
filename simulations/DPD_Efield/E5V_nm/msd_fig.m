function msd_fig(x,y,dy,clrB, clrF, i, ylab, figname)

    figure1 = openfig(figname);
    hold on
    %axes1 = axes('Parent',figure1);
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)], clrB,'linestyle','none');
    line(x,y, 'LineWidth',2, 'Color', clrF)
            
    % For double checking
%     hold on 
%     errorbar(x,y,dy,'b');
    
%     % Create ylabel
%     ylabel(ylab,'Interpreter','latex');
% 
%     % Create xlabel
%     xlabel('Time, [fs]','Interpreter','latex');
% 
%     % Create title
%     %title(rdf_title,'Interpreter','latex');
% 
%     % Uncomment the following line to preserve the Y-limits of the axes
%     box(axes1,'on');
%     % Set the remaining axes properties
%     set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
%         'on');
%     
%     grid on
    
    % ylim
    %ylim([0.0,ymax]);
end