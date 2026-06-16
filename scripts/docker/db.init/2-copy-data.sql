--- Copy presidential elections data from CSV to tables ---
COPY "2006_presidential" FROM '/tmp/presidential/2006_presidencia.csv' DELIMITER ',' CSV HEADER;
-- COPY "2010_presidential" FROM '/tmp/presidential/2010_presidencia.csv' DELIMITER ',' CSV HEADER;
-- COPY "2014_presidential" FROM '/tmp/presidential/2014_presidencia.csv' DELIMITER ',' CSV HEADER;
-- COPY "2018_presidential" FROM '/tmp/presidential/2018_presidencia.csv' DELIMITER ',' CSV HEADER;

--- Copy senate elections data from CSV to tables ---
-- COPY "2006_senate" FROM '/tmp/senate/2006_senado.csv' DELIMITER ',' CSV HEADER;
-- COPY "2010_senate" FROM '/tmp/senate/2010_senado.csv' DELIMITER ',' CSV HEADER;
-- COPY "2014_senate" FROM '/tmp/senate/2014_senado.csv' DELIMITER ',' CSV HEADER;
-- COPY "2018_senate" FROM '/tmp/senate/2018_senado.csv' DELIMITER ',' CSV HEADER;