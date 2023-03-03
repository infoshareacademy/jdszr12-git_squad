-- Code that creates a new table city_pairwise from tables city_country_coordinates and citypairwise

-- citypairwise.csv from kaggle rajanand international-air-traffic-from-and-to-india

-- city_country_coordinates is a file/table with corrected character encoding and with 2 columns removed (original file placed on different branch: https://github.com/infoshareacademy/jdszr12-git_squad/blob/Ula/CITY_COUNTRY_Coordinates%20.csv)

------------------------------
-- Creating main table city_pairwise

create table city_pairwise as (
select cc.country as country1, c.city1, cc.latitude as latitude1, cc.longitude as longitude1,
ccc.country as country2, c.city2, ccc.latitude as latitude2, ccc.longitude as longitude2,
c."YEAR", c.quarter, c."PASSENGERS FROM CITY1 TO CITY2", c."PASSENGERS FROM CITY2 TO CITY1",
c."FREIGHT FROM CITY1 TO CITY2", c."FREIGHT FROM CITY2 TO CITY1"
from citypairwise c
left join city_country_coordinates cc on c.city1 = cc.city_name
left join city_country_coordinates ccc on c.city2 = ccc.city_name
);

------------------------------
-- city_pairwise definition

-- Drop table
-- DROP TABLE public.city_pairwise;
-- CREATE TABLE public.city_pairwise (
--      country1 varchar(50) NOT NULL,
--      city1 varchar(50) NOT NULL,
--      latitude1 float4 NOT NULL,
--      longitude1 float4 NOT NULL,
--      country2 varchar(50) NOT NULL,
--      city2 varchar(50) NOT NULL,
--      latitude2 float4 NOT NULL,
--      longitude2 float4 NOT NULL,
--      "YEAR" int4 NOT NULL,
--      quarter varchar(50) NOT NULL,
--      "PASSENGERS FROM CITY1 TO CITY2" int4 NOT NULL,
--      "PASSENGERS FROM CITY2 TO CITY1" int4 NOT NULL,
--      "FREIGHT FROM CITY1 TO CITY2" float4 NOT NULL,
--      "FREIGHT FROM CITY2 TO CITY1" float4 NOT NULL
-- );
