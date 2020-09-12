%% Density statistics over all realizations

clear
close all

load('E5V_nm_density_data');

fprintf("Average density: %f g/cm3\n", mean(all_densities))
fprintf("Standard deviation of density: %f g/cm3\n", std(all_densities))