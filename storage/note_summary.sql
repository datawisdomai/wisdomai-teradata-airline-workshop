SELECT scenario, COUNT(*) AS note_count
FROM wisdom_storage.WORKSHOP_SYNTHETIC_service_notes
WHERE synthetic_flag = 1
GROUP BY scenario;
