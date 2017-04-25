/*-----------------------------------------------------------------------------------
Name:			ITMI Nautilus Freeze-Thaw Package
Description:	Package containing procedures for use with the ITMI Nautilus application.
Last Updated:	November 29, 2016
See https://github.com/ITMI/nautilus-lims for development updates
-----------------------------------------------------------------------------------*/

CREATE OR REPLACE PACKAGE itmi_ntls_frz_thw AS
	PROCEDURE update_u_freeze_thaw_cnt (aliquot_id_in IN NUMBER);

END itmi_ntls_frz_thw;

/

GRANT EXECUTE ON itmi_ntls_frz_thw TO lims_sys;
GRANT EXECUTE ON itmi_ntls_frz_thw to lims_user;

/

CREATE OR REPLACE PACKAGE BODY itmi_ntls_frz_thw AS 

/* ------------------------------------------------------------
Name:           update_u_freeze_thaw_cnt
Description:    A procedure that increments aliquot_user.u_freeze_thaw_cnt once an aliquot removed from liquid nitrogen.
Dependencies:   
Last Updated:	November 29, 2016
--------------------------------------------------------------- */

PROCEDURE update_u_freeze_thaw_cnt (aliquot_id_in IN NUMBER) IS
    an_aliquot_id               NUMBER;
    a_thaw_count                NUMBER;
    
    CURSOR aliquot_cursor IS
        WITH location_grab AS(
        SELECT 
            ushu.u_sample_history_id
            ,ushu.u_entity_id
            ,REGEXP_REPLACE(REGEXP_REPLACE(SUBSTR(REGEXP_SUBSTR(ushu.u_log, 'was moved from .+ to'), 16), '(.+)( to)', '\1'), '(.+)( on.+)', '\1') from_match
            -- ^ this grabs the name of the location an aliquot was moved FROM
            ,REGEXP_REPLACE(SUBSTR(REGEXP_SUBSTR(ushu.u_log, ' to.+'), 5), '(.+)( on.+)', '\1') to_match
            -- ^ this grabs the name of the location an aliquot was moved TO
        FROM u_sample_history_user ushu
        WHERE
            LOWER(ushu.u_entity_name) = 'aliquot'
        ),

        from_check AS(
        SELECT 
            lo.name location
            ,lg.u_sample_history_id
            ,lg.u_entity_id
            ,lg.to_match
        FROM location lo
            INNER JOIN location_user lu ON lu.location_id = lo.location_id
            INNER JOIN location_grab lg ON lg.from_match = lo.name
        WHERE
            lu.u_storage_condition IN ('F2','FLN')
        ),

        to_check AS(
        SELECT 
            lo.name location
            ,fc.u_sample_history_id
            ,fc.u_entity_id
        FROM location lo
            INNER JOIN location_user lu ON lu.location_id = lo.location_id
            INNER JOIN from_check fc ON fc.to_match = lo.name
        WHERE
            lu.u_storage_condition NOT IN ('F2','FLN')
        )

        SELECT 
            al.aliquot_id
            ,COUNT(ushu.u_sample_history_id) thaw_count
        FROM to_check tc
            INNER JOIN aliquot al ON al.aliquot_id = tc.u_entity_id
            INNER JOIN u_sample_history_user ushu ON ushu.u_sample_history_id = tc.u_sample_history_id
        GROUP BY
            al.aliquot_id
;

BEGIN

    OPEN aliquot_cursor;
    
    LOOP
        FETCH aliquot_cursor INTO an_aliquot_id, a_thaw_count;
        EXIT WHEN aliquot_cursor%NOTFOUND;
        
        UPDATE aliquot_user
        SET
            u_freeze_thaw_cnt = a_thaw_count
        WHERE
            aliquot_id = an_aliquot_id
        ;
        
    END LOOP;

END update_u_freeze_thaw_cnt;

END itmi_ntls_frz_thw;