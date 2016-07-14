function python_epics()
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    pv='LI-RF-MOSC-01:FREQ_SET';
    fprintf('Value of %s is %d.\n', pv, getpv(pv))

    try
        setpv(pv, 4)
    catch
        fprintf('Failed to setpv.\n')
    end
end

