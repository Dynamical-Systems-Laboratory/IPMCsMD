%
% Script for computation of average RDFs and CNs
%

% Directories to consider
dir_names = dir('seed_*');
dir_names = {dir_names.name};
ndirs = length(dir_names);

% All data
% RDFs
all_rdf_so = zeros(ndirs, 300);
all_rdf_sna = zeros(ndirs, 300);
all_rdf_ss = zeros(ndirs, 300);
all_rdf_oo = zeros(ndirs, 300);
% CNs
all_cn_so = zeros(ndirs, 300);
all_cn_sna = zeros(ndirs, 300);
all_cn_ss = zeros(ndirs, 300);
all_cn_oo = zeros(ndirs, 300);
% Bin positions
bin_pos = zeros(ndirs, 300);
for i=1:ndirs
   fname = dir_names(i);
   path = sprintf('%s',fname{:});
   % Move to path and execute the python script for averaging
   cd(sprintf('%s/post_processing/', path));
   % Run the python script
   ! /usr/local/bin/python3.6 rdf_calculations.py
   % Load data 
   data = load('rdf_cn_averaged.txt');
   % Store
   bin_pos(i,:) = data(:,2);
   all_rdf_so(i,:) = data(:,3);
   all_cn_so(i,:) = data(:,4);
   all_rdf_sna(i,:) = data(:,5);
   all_cn_sna(i,:) = data(:,6);
   all_rdf_ss(i,:) = data(:,7);
   all_cn_ss(i,:) = data(:,8);  
   all_rdf_oo(i,:) = data(:,9);
   all_cn_oo(i,:) = data(:,10);
   cd '../../'
end
% If not 0.0 (i.e. bins not equal), use interpolation
err=max(abs((std(bin_pos(:,1:end)))))
% Save data
save('rdf_data');


