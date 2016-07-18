% Simple script to return the pv value off a component
middlelayer

pv='LI-RF-MOSC-01:FREQ_SET';
fprintf('Value of %s is %d.\n', pv, getpv(pv))

try
    % Should fail because it is being called from outside the gateway
    setpv(pv, 4)
catch
    fprintf('Failed to setpv.\n')
end
