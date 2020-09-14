%% Average and plot RDFs and CNs for all 3 voltages 

clear
close all

load('E5V_nm_rdf_data')

plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_so, 'Sulfur - oxygen in water', 5, 1, [0.04,0.36,0.56], 'RDF', 'so_rdf', 0)
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_ss, 'Sulfur - sulfur', 1.7, 2, [0.04,0.36,0.56], 'RDF', 'ss_rdf', 0)
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_sna, 'Sulfur - $\mathrm{Na^+}$', 12.0, 3, [0.04,0.36,0.56], 'RDF', 'sna_rdf', 0)
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_oo, 'Oxygen in water - oxygen in water', 8, 4, [0.04,0.36,0.56], 'RDF', 'oo_rdf', 0)

plot_rdf_cn_error_area(bin_pos(1,:), all_cn_so, 'Sulfur - oxygen in water', 60.0, 5, [0.72,0.24,0.04], 'CN', 'so_cn', 1)
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_ss, 'Sulfur - sulfur', 3.0, 6, [0.72,0.24,0.04], 'CN', 'ss_cn', 1)
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_sna, 'Sulfur - $\mathrm{Na^+}$', 5.0, 7, [0.72,0.24,0.04], 'CN', 'sna_cn', 1)
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_oo, 'Oxygen in water - oxygen in water', 80.0, 8, [0.72,0.24,0.04], 'CN', 'oo_cn', 1)

clear
close all
load('../E1V_nm/E1V_nm_rdf_data')

add_rdf_cn_error_area(bin_pos(1,:), all_rdf_so, 'Sulfur - oxygen in water', 5, 1, [0.04,0.36,0.56], 'RDF', 'so_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_ss, 'Sulfur - sulfur', 1.7, 2, [0.04,0.36,0.56], 'RDF', 'ss_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_sna, 'Sulfur - $\mathrm{Na^+}$', 12.0, 3, [0.04,0.36,0.56], 'RDF', 'sna_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_oo, 'Oxygen in water - oxygen in water', 8, 4, [0.04,0.36,0.56], 'RDF', 'oo_rdf', 0)

add_rdf_cn_error_area(bin_pos(1,:), all_cn_so, 'Sulfur - oxygen in water', 60.0, 5, [0.72,0.24,0.04], 'CN', 'so_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_ss, 'Sulfur - sulfur', 3.0, 6, [0.72,0.24,0.04], 'CN', 'ss_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_sna, 'Sulfur - $\mathrm{Na^+}$', 5.0, 7, [0.72,0.24,0.04], 'CN', 'sna_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_oo, 'Oxygen in water - oxygen in water', 80.0, 8, [0.72,0.24,0.04], 'CN', 'oo_cn', 1)

clear
close all
load('../../../equilibration/sodium_models/eq_rdf_data')

add_rdf_cn_error_area(bin_pos(1,:), all_rdf_so, 'Sulfur - oxygen in water', 5, 1, [0.04,0.6,0.56]*1.1, 'RDF', 'so_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_ss, 'Sulfur - sulfur', 1.7, 2, [0.04,0.6,0.56]*1.1, 'RDF', 'ss_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_sna, 'Sulfur - $\mathrm{Na^+}$', 12.0, 3, [0.04,0.6,0.56]*1.1, 'RDF', 'sna_rdf', 0)
add_rdf_cn_error_area(bin_pos(1,:), all_rdf_oo, 'Oxygen in water - oxygen in water', 8, 4, [0.04,0.6,0.56]*1.1, 'RDF', 'oo_rdf', 0)

add_rdf_cn_error_area(bin_pos(1,:), all_cn_so, 'Sulfur - oxygen in water', 60.0, 5, [0.2,0.4,0.04]*1.1, 'CN', 'so_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_ss, 'Sulfur - sulfur', 3.0, 6, [0.2,0.4,0.04]*1.1, 'CN', 'ss_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_sna, 'Sulfur - $\mathrm{Na^+}$', 5.0, 7, [0.2,0.4,0.04]*1.1, 'CN', 'sna_cn', 1)
add_rdf_cn_error_area(bin_pos(1,:), all_cn_oo, 'Oxygen in water - oxygen in water', 80.0, 8, [0.2,0.4,0.04]*1.1, 'CN', 'oo_cn', 1)

function plot_rdf_cn_error_area(x,y, rdf_title, ymax, i, clr, ylab, figname, cn_plot)

    close all

    dy = std(y)';
    y = mean(y)';
    x = x';
    
    % Create figure
    figure1 = figure(i);

    % Create axes
    axes1 = axes('Parent',figure1);
    
    fill([x;flipud(x)],[y-dy;flipud(y+dy)],[.7 .7 .7],'linestyle','none');
    line(x,y, 'LineWidth',2,...
        'Color', clr)
    
    % For double checking
%     hold on 
%     errorbar(x,y,dy,'b');
    
    % Create ylabel
    ylabel(ylab,'Interpreter','latex');

    % Create xlabel
    xlabel('Radial distance, $\AA$','Interpreter','latex');

    % Create title
    title(rdf_title,'Interpreter','latex');

    % Uncomment the following line to preserve the Y-limits of the axes
    % ylim(axes1,[0 5]);
    box(axes1,'on');
    % Set the remaining axes properties
    set(axes1,'FontSize',20,'TickLabelInterpreter','latex','XGrid','on','YGrid',...
        'on');
    
    % ylim
    ylim([0.0,ymax]);
    
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



