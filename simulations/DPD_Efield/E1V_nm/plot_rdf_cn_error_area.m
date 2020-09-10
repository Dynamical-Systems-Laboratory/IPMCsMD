function plot_rdf_cn_error_area(x,y, rdf_title, ymax, i, clr, ylab, figname)
    dy = std(y)';
    y = mean(y)';
    x = x';
    
    % Create figure
    figure1 = openfig(figname);
    hold on
        
    fill([x;flipud(x)],[y-dy;flipud(y+dy)],[.7 .7 .7],'linestyle','none');
    line(x,y, 'LineWidth',2,...
        'Color', clr)
    
       disp(ylab)
    disp(rdf_title)
    [pks,locs] = findpeaks(y);
    if length(locs) > 0
        disp(x(locs(1:2)))
    end   
end