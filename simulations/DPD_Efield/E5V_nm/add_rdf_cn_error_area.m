function add_rdf_cn_error_area(x,y, rdf_title, ymax, i, clr, clrb, ylab, figname, cn_plot)
    
    close all

    dy = std(y)';
    y = mean(y)';
    x = x';
    
    figure1 = openfig(figname);
    hold on
        
    fill([x;flipud(x)],[y-dy;flipud(y+dy)],clrb,'linestyle','none');
    line(x,y, 'LineWidth',2,...
        'Color', clr)
    
       disp(ylab)
    disp(rdf_title)
    if cn_plot == 0
        % RDF - look at peaks
        disp('RDF peaks')
        [pks,locs] = findpeaks(y);
        if length(locs) > 0
            disp(x(locs(1:2)))
        end
    else
        % CN - value at 10 A
        disp('CN at 10 A')
        xpp = 0:0.001:10; 
        ypp = pchip(x,y,xpp);
        dy_pp = pchip(x,dy,xpp);

        disp(ypp(end))
        disp(dy_pp(end))
    end
    savefig(figname)
end