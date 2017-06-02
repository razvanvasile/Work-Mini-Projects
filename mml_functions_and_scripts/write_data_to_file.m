function write_data_to_file(file_name, data)
%WRITE_DATA_TO_FILE Summary of this function goes here
%   Detailed explanation goes here
fid=fopen(file_name, 'w');
[nrows,ncol] = size(data);
for row = 1:nrows
    fprintf(fid, '%s\n', data(row,:));
end
fclose(fid);
end
