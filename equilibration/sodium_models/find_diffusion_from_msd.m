%% Inspect the diffusive regime
% This is just a visualization support
% Actual search is done in a more robust way in diffusivity_post_proc
% Need to plot the linear fit manually

clear
load('eq_nafion_ion_diff')

Ds = [];
betas = [];

tvals = [4000:1:5999];
for i=1:length(tvals)
    p = polyfit(log(time_all(1,tvals(i):end)-time_all(1,tvals(i)-1)), log(msd_x_all(1,tvals(i):end)-msd_x_all(1,tvals(i)-1)), 1);
    betas(i) = real(p(1));
    Ds(i) = exp(real(p(2)))*0.1/2.0;
end

err = abs(betas-1);
ind = find(err == min(err));

t0 = tvals(ind)
betas(ind)
Ds(ind)

plot(log(time_all(1,t0:end)-time_all(1,t0-1)), log(msd_x_all(1,t0:end)-msd_x_all(1,t0-1)));
