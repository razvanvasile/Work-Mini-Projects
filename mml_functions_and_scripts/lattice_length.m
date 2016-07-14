function lattice_length
% Function to return the total length of the machine
middlelayer
global THERING
lattice_length=0
for i=1:length(THERING)
    lattice_length = lattice_length+THERING{i}.Length
end

% Print the length of the lattice to the screen
fprintf('Length of the lattice is: %d.\n', lattice_length)
end
