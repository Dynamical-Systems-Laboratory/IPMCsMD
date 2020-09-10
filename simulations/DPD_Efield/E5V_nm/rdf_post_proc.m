%% Post-process RDF averages
clear
load('rdf_data')

plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_so, 'Sulfur - oxygen in water', 4, 1, [0.04,0.36,0.56], 'RDF', 'sow_rdf')
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_ss, 'Sulfur - sulfur', 1.0, 2, [0.04,0.36,0.56], 'RDF', 'ss_rdf')
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_sna, 'Sulfur - $\mathrm{Na^+}$', 8.0, 3, [0.04,0.36,0.56], 'RDF', 'sna_rdf')
plot_rdf_cn_error_area(bin_pos(1,:), all_rdf_oo, 'Oxegen in water - oxygen in water', 6.5, 4, [0.04,0.36,0.56], 'RDF', 'owow_rdf')

plot_rdf_cn_error_area(bin_pos(1,:), all_cn_so, 'Sulfur - oxygen in water', 50.0, 5, [0.72,0.24,0.04], 'CN', 'sow_cn')
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_ss, 'Sulfur - sulfur', 2.5, 6, [0.72,0.24,0.04], 'CN', 'ss_cn')
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_sna, 'Sulfur - $\mathrm{Na^+}$', 4.0, 7, [0.72,0.24,0.04], 'CN', 'sna_cn')
plot_rdf_cn_error_area(bin_pos(1,:), all_cn_oo, 'Oxegen in water - oxygen in water', 60.0, 8, [0.72,0.24,0.04], 'CN', 'ow_ow_cn')

