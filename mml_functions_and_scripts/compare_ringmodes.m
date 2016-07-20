function compare_ringmodes
% Compare PVs for sri21 and vmx ring modes
sri21_channels = get_all_pv_names();
vmx_channels = get_all_pv_names();

sri21_vmx = setdiff(sri21_channels, vmx_channels, 'rows');
vmx_sri21 = setdiff(vmx_channels, sri21_channels, 'rows');
 
fprintf('Here are the results, sri21 - vmx:\n');
print_array(sri21_vmx);
fprintf('Here are the results, vmx - sri21:\n');
print_array(vmx_sri21);

% Part 2: Compare above results with pvs read from files
added_magnets_path = '../data/added_magnets.txt';
removed_magnets_path = '../data/removed_magnets.txt';

added_magnets = read_file(added_magnets_path);
removed_magnets = read_file(removed_magnets_path);

added_sri21 = intersect(sri21_channels, added_magnets, 'rows');
removed_vmx = intersect(vmx_channels, removed_magnets, 'rows');

fprintf('Results for added_magnets union sri21_channels:\n');
print_array(added_sri21);
fprintf('Results for removed_magnets union removed_magnets:\n');
print_array(removed_vmx);

end

function print_array(array)
    for i=1:length(array)
        fprintf('%s\n', array(i,:));
    end
end

function result = read_file(path)
    fid = fopen(path, 'r');
    result = char([]);

    tline = fgets(fid);
    while(ischar(tline))
        line_size = size(tline);
        result(end+1, 1:line_size(2)) = tline;
        tline = fgets(fid);
    end
end
