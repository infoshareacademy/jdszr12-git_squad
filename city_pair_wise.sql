--Stworzenie wstepnej tabeli 'city_pairwise' z:
--'citypairwise' (dostępne na kaggle.com International Air Traffic from and to India by Rajanand Ilangovan)
--oraz 'city_country_coordinates' (opracowanie własne)

--create table city_pairwise as (
--select cc.country as country1, c.city1, cc.latitude as latitude1, cc.longitude as longitude1,
--ccc.country as country2, c.city2, ccc.latitude as latitude2, ccc.longitude as longitude2,
--c."YEAR", c.quarter, c."PASSENGERS FROM CITY1 TO CITY2", c."PASSENGERS FROM CITY2 TO CITY1",
--c."FREIGHT FROM CITY1 TO CITY2", c."FREIGHT FROM CITY2 TO CITY1"
--from citypairwise c
--left join city_country_coordinates cc on c.city1 = cc.city_name
--left join city_country_coordinates ccc on c.city2 = ccc.city_name
--);

--Stworzenie finalnej tabeli 'city_pair_wise' z 'city_pairwise',
--po usunieciu danych zerowych i zmianie nazw kolumn

create table city_pair_wise as (
select 
cp.country1 as "Kraj", cp.city1 as "Miasto", cp.latitude1 as "Latitude", cp.longitude1 as "Longitude",
cp.country2 as "Indie", cp.city2 as "Indie_Miasto", cp.latitude2 as "I_latitude", cp.longitude2 as "I_longitude",
cp."YEAR" as "Rok", cp.quarter as "Kwartal",
cp."PASSENGERS FROM CITY1 TO CITY2" as "Pasazerowie_do_Indii", cp."PASSENGERS FROM CITY2 TO CITY1" as "Pasazerowie_z_Indii",
cp."FREIGHT FROM CITY1 TO CITY2" as "Fracht_do_Indii", cp."FREIGHT FROM CITY2 TO CITY1" as "Fracht_z_Indii"
from
(select *, case
when "PASSENGERS FROM CITY1 TO CITY2" = "PASSENGERS FROM CITY2 TO CITY1" and "PASSENGERS FROM CITY2 TO CITY1"=0 and "PASSENGERS FROM CITY1 TO CITY2"=0 and "FREIGHT FROM CITY1 TO CITY2" = "FREIGHT FROM CITY2 TO CITY1" and "FREIGHT FROM CITY2 TO CITY1"=0 and "FREIGHT FROM CITY1 TO CITY2"=0
then 1
else 0 end as q
from city_pairwise) as cp
where cp.q != 1
);
