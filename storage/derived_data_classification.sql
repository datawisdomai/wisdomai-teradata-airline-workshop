-- Row-level derived column on WORKSHOP_SYNTHETIC_service_notes.
-- Name: workshop_data_classification
CASE WHEN synthetic_flag = 1
     THEN 'Synthetic workshop data'
     ELSE 'Review source classification'
END
