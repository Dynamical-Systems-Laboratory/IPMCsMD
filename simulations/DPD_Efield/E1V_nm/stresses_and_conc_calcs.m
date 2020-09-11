% Collect concentration and stress data

% Directories to consider
dir_names = dir('seed_*');
dir_names = {dir_names.name};
ndirs = length(dir_names);

% All data
% Stresses
all_s_xx = zeros(ndirs, 20);
all_s_yy = zeros(ndirs, 20);
all_s_zz = zeros(ndirs, 20);
all_s_xy = zeros(ndirs, 20);
all_s_yz = zeros(ndirs, 20);
all_s_xz = zeros(ndirs, 20);
% Before efield
all_pre_s_xx = zeros(ndirs, 20);
all_pre_s_yy = zeros(ndirs, 20);
all_pre_s_zz = zeros(ndirs, 20);
all_pre_s_xy = zeros(ndirs, 20);
all_pre_s_yz = zeros(ndirs, 20);
all_pre_s_xz = zeros(ndirs, 20);
% Concentrations
all_c_h2o = zeros(ndirs, 20);
all_c_na = zeros(ndirs, 20);
all_c_s = zeros(ndirs, 20);
all_pre_c_h2o = zeros(ndirs, 20);
all_pre_c_na = zeros(ndirs, 20);
all_pre_c_s = zeros(ndirs, 20);

for i=1:ndirs
   fname = dir_names(i);
   path = sprintf('%s',fname{:});
   % Move to path and execute the python script for averaging
   cd(sprintf('%s/post_processing/', path));

   % Collect the data
   temp = load('stresses_out_xx.txt');
   all_s_xx(i,:) = mean(temp(length(temp)/2:end,:));
   temp = load('stresses_out_yy.txt');
   all_s_yy(i,:) = mean(temp(length(temp)/2:end,:));
   temp = load('stresses_out_zz.txt');
   all_s_zz(i,:) = mean(temp(length(temp)/2:end,:));
   temp = load('stresses_out_xy.txt');
   all_s_xy(i,:) = mean(temp(length(temp)/2:end,:));
   temp = load('stresses_out_yz.txt');
   all_s_yz(i,:) = mean(temp(length(temp)/2:end,:));
   temp = load('stresses_out_xz.txt');
   all_s_xz(i,:) = mean(temp(length(temp)/2:end,:));
   %
   temp = load('pre_stresses_out_xx.txt');
   all_pre_s_xx(i,:) = mean(temp);
   temp = load('pre_stresses_out_yy.txt');
   all_pre_s_yy(i,:) = mean(temp);
   temp = load('pre_stresses_out_zz.txt');
   all_pre_s_zz(i,:) = mean(temp);
   temp = load('pre_stresses_out_xy.txt');
   all_pre_s_xy(i,:) = mean(temp);
   temp = load('pre_stresses_out_yz.txt');
   all_pre_s_yz(i,:) = mean(temp);
   temp = load('pre_stresses_out_xz.txt');
   all_pre_s_xz(i,:) = mean(temp);
   % Concentrations
   temp = load('number_density_h2o.txt');
   all_c_h2o(i,:) = mean(temp(:,length(temp)/2:end),2);
   temp = load('number_density_na.txt');
   all_c_na(i,:) = mean(temp(:,length(temp)/2:end),2);
   temp = load('number_density_s.txt');
   all_c_s(i,:) = mean(temp(:,length(temp)/2:end),2);
   temp = load('pre_number_density_h2o.txt');
   all_pre_c_h2o(i,:) = mean(temp,2);
   temp = load('pre_number_density_na.txt');
   all_pre_c_na(i,:) = mean(temp,2);
   temp = load('pre_number_density_s.txt');
   all_pre_c_s(i,:) = mean(temp,2);
   
   cd '../../'
end

% Save data
save('E1V_nm_stress_conc_data');


