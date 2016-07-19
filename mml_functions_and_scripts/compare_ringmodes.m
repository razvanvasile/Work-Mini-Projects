function compare_ringmodes
% Compare PVs in ringmodes 'SRI21' and 'VMX'

% sri21_channels = get_pv_channels();

sri21_channels = get_pv_channels();
vmx_channels = get_pv_channels();


sri21_vmx = setdiff(sri21_channels, vmx_channels);
vmx_sri21 = setdiff(sri21_channels, vmx_channels);

% TODO: Find a way to print the contents of a char array row wise
fprintf('Here are the results, sri21-vmx, %d\n', sri21_vmx);

end

function channel_names = get_pv_channels()
    middlelayer mode
    
    data = getfamilydata();
    family_names = fieldnames(data);

for i = 1:numel(family_names)% should this have a different name?
    family_data = data.(family_names{i});
    if isfield(family_data, 'Monitor') == 1
        % Assume if Monitor exists then a channel name exists
        fetched_names = family_data.Monitor.ChannelNames();
        fetched_names = unique(fetched_names, 'rows');
        fprintf('fetched_names = %d\n', size(fetched_names));
        fprintf('channel_names = %d\n', size(channel_names));
        
        % Check wether the size of the two arrays match
        fetched_size = size(fetched_names);
        channel_size = size(channel_size);

        % TODO: Find a way to resize these arrays?
        if fetched_size > channel_size
            resize_arrays(fetched_size, channel_size);
        elseif channel_size > fetched_size
            resize_arrays(channel_size, fetched_size);
        end

        % Add data together, collumn wise
        channel_names = [fetched_names; channel_names];
    elseif isfield(family_data, 'Setpoint')
        fetched_names = family_data.Setpoint.ChannelNames();
        fetched_names = unique(fetched_names, 'rows');

        channel_names = [fetched_names; channel_names];
    else
        fprintf('Could not find a setpoint or monitor field for %s\n', family_data.FamName);
    end
end
end

function result = resize_arrays(target, source)
    

end
