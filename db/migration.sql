CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 537980e0b839

DROP TABLE air_quality_nyc;

INSERT INTO alembic_version (version_num) VALUES ('537980e0b839');

-- Running upgrade 537980e0b839 -> 8202909f63ae

UPDATE alembic_version SET version_num='8202909f63ae' WHERE alembic_version.version_num = '537980e0b839';

