%
% Script for computation of average bulk density
%

% Directories to consider
dir_names = dir('seed_*');
dir_names = {dir_names.name};
ndirs = length(dir_names);

% All data
all_densities = zeros(ndirs, 1);

for i=1:ndirs
   fname = dir_names(i);
   path = sprintf('%s',fname{:});
   % Move to path and execute the python script for averaging
   cd(sprintf('%s/post_processing/', path));
   fprintf("Processing %s\n", path)
   
   % Uncomment if not using the bash script
   % Run the python script
   %! /usr/local/bin/python3.6 density_analysis.py
   
   % Load and store data 
   data = load('bulk_density_w_time.txt');
   % Compute average and store in all_densities
   all_densities(i) = mean(data(:,2));
   cd '../../'
end

% Save data
save('E1V_nm_density_data');