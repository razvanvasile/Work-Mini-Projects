function pvs_enabled = bpmx_status()
% Returns a list of ones and zeroes which represents
% whether a bpm is enabled (1) or disabled (0)
% Instead of this, use getfamilydata('BPMx', 'Status')
    
% Get the string template to work with
template=getfamilydata('BPMx', 'FR', 'ChannelNames');

% Parse the template
N = length(template);
pvs_enabled=cell(1,N);
for i=1:length(template)
    pvs_enabled{i} = [template(i,1:16), ':CF:ENABLED_S'];
end

% Get BPM status
pvs_enabled = getpv(pvs_enabled);
end
