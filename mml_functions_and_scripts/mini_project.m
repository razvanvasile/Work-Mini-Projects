function mini_project

% Setup
middlelayer

% First task: to print the number of BPMs in the lattice
%             which equals to the number of BPMy elements.
BPMy = getlist('BPMy');
fprintf('The number of BPMy elements in the lattice: %d.\n', length(BPMy))

% Second task: 
bpm_channels=family2channel('BPMx');
pvs=getpv('BPMx');
disp('List of pv names and associated value for all BPMS.\n')
for i=1:length(pvs)
    fprintf('BPMx channel name: %s\n', bpm_channels(i,:))
    fprintf('PV value: %s\n', pvs(i))
end

% Third task
quads=getlist('QUAD_')
sp=getsp('QUAD_')
for i=1:length(sp)
    fprintf('Readback value: %d\n', sp(i))
    fprintf('Setpoint value: %d\n', sp(i))
end