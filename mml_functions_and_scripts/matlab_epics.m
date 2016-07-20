% Simple script to return the pv value of a component

pv='LI-RF-MOSC-01:FREQ_SET';
fprintf('Value of %s is %d.\n', pv, lcaGet(pv))

try
    % Should fail because it is being called from outside the gateway
    lcaPut(pv, 4)
catch
    fprintf('Failed to set pv.\n')
end
