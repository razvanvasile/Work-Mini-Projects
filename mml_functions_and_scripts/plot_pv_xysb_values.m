function plot_pv_xysb_values
% Plot BPM x/y coordinates against their position in the ring
middlelayer

% Setup the data
bpmx = getfamilydata('BPMx');
bpmy = getfamilydata('BPMy');
bpmx_pvs = getpv('BPMx');
bpmy_pvs = getpv('BPMy');
bpmx_pos = getpv('BPMx', 'Position');
bpmy_pos = getpv('BPMy', 'Position');

% Plot the required values
figure
col = hsv(10);
hold on

xlabel('bpm x(blue)/y(red) coordinates')
plot(bpmx_pos, bpmx_pvs);
ylabel('bpm position')
plot(bpmy_pos, bpmy_pvs, 'color', col(1, :));

hold off

end
