SELECT
  REGEXP_REPLACE(st.name, 'Study (\d+)', '\1 ') "Study"
  ,s.name "Collection Name"
  ,a.name "Aliquot"
  ,a.MATRIX_TYPE "Aliquot Type"
  ,TO_CHAR(au.u_collection_date,'mm-dd-yyyy hh24:mi:ss') "Collection Date Time"
  ,TO_CHAR(shu1.u_date_time,'mm-dd-yyyy hh24:mi:ss') "Storage Date Time"
  ,TRUNC((shu1.u_date_time - au.u_collection_date) * 24 * 60,2) "Turn Around Time"
  ,op.name "Received By"
  ,shu1.u_log "Log Entry"
FROM lims_sys.u_sample_history_user shu1
  INNER JOIN lims_sys.aliquot_user AU ON shu1.u_entity_id = au.aliquot_id
  INNER JOIN lims_sys.aliquot A ON shu1.u_entity_id = a.aliquot_id
  INNER JOIN lims_sys.sample S ON a.sample_id = s.sample_id
  INNER JOIN lims_sys.study st ON st.study_id = s.study_id
  INNER JOIN lims_sys.operator op ON op.operator_id = s.received_by
WHERE
  shu1.u_sample_history_id IN(
    SELECT
      MIN(sh.u_sample_history_id) "First Transaction"
    FROM lims_sys.u_sample_history sh
    INNER JOIN lims_sys.u_sample_history_user shu
      ON sh.u_sample_history_id = shu.u_sample_history_id
    WHERE shu.u_entity_id IN(
      SELECT
        al.aliquot_id
      FROM lims_sys.aliquot al
      INNER JOIN lims_sys.lims_group lg
        ON al.group_id = lg.group_id
      WHERE
        al.container_type_id IN (23,106,107)
        -- these are the aliquots that are supposed to fall within the 90 minute window
        AND al.status NOT LIKE 'X'
        AND lg.name = 'ITMI Lab'
        )
    AND (
    U_LOG LIKE '%was moved FROM ITMI Lab to%'
    OR
    U_LOG LIKE '%was moved FROM ITMI Processing Area%'
        )
    GROUP BY
      shu.u_entity_id
        )
  AND(
    TRUNC((shu1.u_date_time - au.u_collection_date) * 24 * 60,2) > 120
    -- this was changed FROM > 90 to > 120 after speaking with QC Supervisor
    OR TRUNC((shu1.u_date_time - au.u_collection_date) * 24 * 60,2) < 0)
ORDER BY
  au.u_collection_date DESC
  ,a.matrix_type ASC