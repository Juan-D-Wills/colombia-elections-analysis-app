-- PRESIDENTIA TABLES --
CREATE TABLE IF NOT EXISTS "colombia_elections_template" (
    id_electoral INT,
    tipo_eleccion VARCHAR(200),
    fecha_elecciones DATE,
    codigo_departamento INT,
    departamento VARCHAR(200),
    codigo_municipio INT,
    municipio VARCHAR(200),
    circunscripcion VARCHAR(200),
    codigo_partido INT,
    codigo_lista INT,
    candidato VARCHAR(200),
    votos INT,
    curules INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Autogenerate tables for each elections year based on the "colombia_elections_template" template --
DO $$
DECLARE
    election_years TEXT[] := ARRAY['2006', '2010', '2014', '2018']; -- '2022'
    election_type TEXT[] := ARRAY['presidential', 'senate'];
    year TEXT;
    type TEXT;
BEGIN
    FOREACH type IN ARRAY election_type LOOP
        FOREACH year IN ARRAY election_years LOOP
            EXECUTE format('CREATE TABLE IF NOT EXISTS %I (LIKE colombia_elections_template INCLUDING ALL)', year || '_' || type);
        END LOOP;
    END LOOP;
END $$;
