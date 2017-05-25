Freeze-Thaw Stored Procedure Notes:

This procedure corrects system data for specimen samples (aliquots) that were received years before their entry into the Laboratory Information Management System AND insures that new data is homogeneous. This provided the laboratory with insights into aliquot condition, allowed them to work more efficiently, and helped insure data quality.

The anonymous procedure, anon_itmi_ntls_frz_thw.sql, looks at existing log entries of aliquot thawing events and uses those strings to calculate a value and assign it to the user-defined field 'u_freeze_thaw_cnt'. 

The stored procedure was configured along with Nautilus client-side workflows to re-populate the u_freeze_thaw_cnt field when aliquots were moved to storage locations with different temperatures.