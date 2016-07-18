function get_families_count
% Function to print the count for each family in the machine

families = getfamilydata();  % returns a struct
fields = fieldnames(families); % returns a cell array of strings
for i = 1:numel(fields)
    family_name = families.(fields{i}).FamilyName;
    family_count = length(families.(fields{i}).ElementList);
    
    if family_count == 1
      fprintf('There is %d element in %s\n', family_count, family_name)
    else
      fprintf('There are %d elements in %s\n', family_count, family_name)
    end
end
end
