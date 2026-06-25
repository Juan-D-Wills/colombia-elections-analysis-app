--- Automated copy of elections data from CSV ---
DO $$
DECLARE
    election_years TEXT[] := ARRAY['2006', '2010', '2014','2018']; -- '2022'
    election_type TEXT[] := ARRAY['presidential', 'senate'];
    year TEXT;
    type TEXT;
    current_time TIMESTAMP :=NOW();
BEGIN
    FOREACH type IN ARRAY election_type LOOP
        FOREACH year IN ARRAY election_years LOOP
            EXECUTE format('COPY %I FROM %L DELIMITER '','' CSV HEADER', year || '_' || type, '/tmp/data/' || type || '/' || year || '_' || type || '.csv');
        END LOOP;
    END LOOP;
END $$;
