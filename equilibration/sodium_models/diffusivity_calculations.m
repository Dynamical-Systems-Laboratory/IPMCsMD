% Script for collecting the MSD data

clear
close all

% Number of data points
npoints = 6000;

collect_msd('nafion.ion_diff','eq_nafion_ion_diff', 'seed_*', npoints);
collect_msd('nafion.water_diff','eq_nafion_water_diff', 'seed_*', npoints);

% All data
function collect_msd(fin, fout, dirname, npoints)
    % Collects msd data from fin, for each directory that has a common name
    % dirname. The data needs to have npoints. Collected data is saved as
    % a mat file.

    % Directories to consider
    dir_names = dir(dirname);
    dir_names = {dir_names.name};
    ndirs = length(dir_names);
    
    % MSD
    msd_tot_all = zeros(ndirs,npoints);
    msd_x_all = zeros(ndirs,npoints);
    msd_y_all = zeros(ndirs,npoints);
    msd_z_all = zeros(ndirs,npoints);
    % Time 
    time_all = zeros(ndirs, npoints);

    for i=1:ndirs
       fname = dir_names(i);
       path = sprintf('%s',fname{:});
       fprintf("Processing %s\n", path)
       % Move to path and execute the python script for averaging
       cd(path);
       % Load data 
       data = load(fin);
       % Store
       time_all(i,:) = data(:,1);
       msd_x_all(i,:) = data(:,2);
       msd_y_all(i,:) = data(:,3);
       msd_z_all(i,:) = data(:,4);
       msd_tot_all(i,:) = data(:,5);
       cd '../'
    end
    
    % If not 0.0 (i.e. bins not equal), use interpolation to have all
    % datasets on the same time grid
    err=max(abs((std(time_all(:,1:end)))))
    % Save data
    save(fout);

end
