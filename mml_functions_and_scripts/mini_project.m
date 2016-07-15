function mini_project

% Setup
middlelayer

% First task:
BPMy = getlist('BPMy');
fprintf('The number of BPMy elements in the lattice: %d.\n', length(BPMy))

% Second task: 
bpm_channels=family2channel('BPMx');
pvs=getpv('BPMx');
disp('List of pv names and associated value for all BPMS.\n')
for i=1:length(pvs)
    % TODO: find specific channel name for each channel
    fprintf('BPMx channel name: %s\n', bpm_channels(i,:))
    fprintf('PV value: %s\n', pvs(i))
end

% Third task
sp_values=getpv('QUAD_', 'Setpoint');
rb_values=getpv('QUAD_');
for i=1:length(sp_values)
    fprintf('Readback value: %d\n', rb_values(i))
    fprintf('Setpoint value: %d\n', sp_values(i))
end
