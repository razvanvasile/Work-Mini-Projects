function write_pvs_to_file(filename)
% Function to write unique pv names in sorted order to file

pv_names = get_all_pv_names();
pv_names = sort(pv_names);

fid = fopen(filename, 'w');
sri21_pv_length = length(pv_names);
for i = 1:sri21_pv_length(1)
    fprintf(fid, '%s\n', pv_names(i,:));
end
end
