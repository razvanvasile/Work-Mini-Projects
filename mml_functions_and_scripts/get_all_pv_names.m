function channel_names = get_all_pv_names(mode)
% Method to return a vector of all pv names from a selected machine mode
    storageringinit(mode);
    
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
        for j = 1:fetched_size
            channel_names(end+1, 1:fetched_size(2)) = fetched_names(j,:);
        end
    else
        fprintf(['Could not find a setpoint or monitor field for '
            '%s\n'], family_data.FamName);
    end
end
end