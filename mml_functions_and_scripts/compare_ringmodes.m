function compare_ringmodes
% Compare PVs for sri21 and vmx ring modes
sri21_channels = get_pv_channels();
vmx_channels = get_pv_channels();

sri21_vmx = setdiff(sri21_channels, vmx_channels, 'rows');
vmx_sri21 = setdiff(vmx_channels, sri21_channels, 'rows');

fprintf('Here are the results, sri21 - vmx\n');
print_array(sri21_vmx);
fprintf('Here are the results, vmx - sri21\n');
print_array(vmx_sri21);
end

function channel_names = get_pv_channels()
    middlelayer mode
    
    data = getfamilydata();
    family_names = fieldnames(data);
    channel_names = char([]);

for i = 1:numel(family_names)
    family_data = data.(family_names{i});
    if isfield(family_data, 'Monitor') == 1
        % Assume if Monitor exists then a channel name exists
        fetched_names = family_data.Monitor.ChannelNames();
        fetched_names = unique(fetched_names, 'rows');
        
        % Check wether the size of the two arrays match
        fetched_size = size(fetched_names);
        
        % Add fetched array to channel names array
        for i = 1:fetched_size
            channel_names(end+1, 1:fetched_size(2)) = fetched_names(i,:);
        end
    else
        fprintf(['Could not find a setpoint or monitor field for '
            '%s\n'], family_data.FamName);
    end
end
end

function print_array(array)
    for i=1:length(array)
        fprintf('%s\n', array(i,:));
    end
end