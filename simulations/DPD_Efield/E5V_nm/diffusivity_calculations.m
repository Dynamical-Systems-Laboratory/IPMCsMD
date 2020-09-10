%
% Script for computation of average diffusivities and plots of MSD
%

%%% Specify the file name in two places

clear

% Directories to consider
dir_names = dir('seed_*');
dir_names = {dir_names.name};
ndirs = length(dir_names);

% Number of data points
npoints = 6000; 

% All data
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
   % Move to path and execute the python script for averaging
   cd(path);
   % Load data 
   data = load('with_efield_nafion.water_diff');
%    data = load('nafion.water_diff');
   % Store
   time_all(i,:) = data(:,1);
   msd_x_all(i,:) = data(:,2);
   msd_y_all(i,:) = data(:,3);
   msd_z_all(i,:) = data(:,4);
   msd_tot_all(i,:) = data(:,5);
   cd '../'
end
% If not 0.0 (i.e. bins not equal), use interpolation
err=max(abs((std(time_all(:,1:end)))))
% Save data
save('nafion_water_diff');

