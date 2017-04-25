getBadAliquots.sql Notes

- This query was written for a Jasper Report to pull data from an Oracle database.
- The purpose of the report was to list aliquots that had unacceptable values for turn around time. The particular line of the WHERE clause concerning this is:
	TRUNC((shu1.u_date_time - au.u_collection_date) * 24 * 60,2) > 120
    OR TRUNC((shu1.u_date_time - au.u_collection_date) * 24 * 60,2) < 0)