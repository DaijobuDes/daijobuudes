CREATE DATABASE `OSU_DB`;

CREATE TABLE IF NOT EXISTS `OSU_USER` (
    USERNAME VARCHAR(32) NOT NULL,
    DISCORD_ID VARCHAR(18) NOT NULL
);


CREATE TABLE IF NOT EXISTS `GETUSER` (
    DATEANDTIME VARCHAR(64) UNIQUE NOT NULL,

    USERNAME VARCHAR(32) NOT NULL,
    OSUID VARCHAR(16) NOT NULL,
    OSUMODE VARCHAR(1) NOT NULL,
    COUNTRY VARCHAR(2) NOT NULL,
    ACCURACY VARCHAR(32) NOT NULL,
    PP VARCHAR(32) NOT NULL,

    GLOBALRANK VARCHAR(16) NOT NULL,
    COUNTRYRANK VARCHAR(16) NOT NULL,
    300S VARCHAR(32) NOT NULL,
    100S VARCHAR(32) NOT NULL,
    50S VARCHAR(32) NOT NULL,
    JOINDATE VARCHAR(32) NOT NULL,
    
    SS VARCHAR(8) NOT NULL,
    SSH VARCHAR(8) NOT NULL,
    S VARCHAR(8) NOT NULL,
    SH VARCHAR(8) NOT NULL,
    A VARCHAR(8) NOT NULL,

    SS_RATE VARCHAR(8) NOT NULL,
    S_RATE VARCHAR(8) NOT NULL,
    A_RATE VARCHAR(8) NOT NULL
);