--select count("PASSENGERS TO INDIA") 
--from airlinewise a
--
--select count(*) 
--from airlinewise a

select *, object_id()
case
when "PASSENGERS TO INDIA"::varchar is null then 1
when "PASSENGERS TO INDIA"::varchar like '' then 1
when "PASSENGERS TO INDIA"::varchar like ' ' then 1
else 0
end as cwee
from airlinewise a
order by cwee desc limit 1

--Name                 |Value                   |
-----------------------+------------------------+
--YEAR                 |2016                    |
--MONTH                |NOV                     |
--quarter              |Q4                      |
--AIRLINE NAME         |VIRGIN ATLANTIC AIRLINES|
--CARRIER TYPE         |FOREIGN                 |
--PASSENGERS TO INDIA  |                        |
--PASSENGERS FROM INDIA|6696                    |
--FREIGHT TO INDIA     |203.7                   |
--FREIGHT FROM INDIA   |409.8                   |
--cwee                 |1                       |
