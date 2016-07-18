function related_groups = get_related_groups
% Function to print the related groups in the machine

% These are the indices without the MemborOf property
invalid_indexes = [3, 4, 30, 31, 34, 35, 36];
related_groups = containers.Map;

families = getfamilydata();  % returns a struct
fields = fieldnames(families); % returns a cell array of strings

try
% Iterate over each family
for fam_index = 1:numel(fields)
    if valid_index(fam_index, invalid_indexes)
        target_group = families.(fields{fam_index}).MemberOf;
        family = fields{fam_index};
        
        % Iterate over each group
        for group_index = 1:numel(fields)
            if valid_index(group_index, invalid_indexes)
                union_group = families.(fields{group_index}).MemberOf;
                related_groups(family) = union(target_group, union_group);
            end
        end
    end
end

catch me
    me.stack
    fprintf('Could not access index: %d', group_index)
end

% Print the related groups for each family
map_keys = keys(related_groups);
map_values = values(related_groups);
for fam_index = 1:numel(map_values)
    fprintf('Key: %s, Values: ', map_keys{fam_index})
    for group_index = 1:numel(map_values{fam_index})
        fprintf('%s, ', map_values{fam_index}{group_index})
    end
    fprintf('\x08\x08.\n')
end
end

function valid = valid_index(given_idx, invalid_idx)
% Check if given_idx exists in invalid_idx. If it does then
% the family valid_index doesn't have the MemberOf property.

valid = 1;
for idx = 1:numel(invalid_idx)
    if given_idx == invalid_idx(idx)
        valid = 0;
    end
end
end
