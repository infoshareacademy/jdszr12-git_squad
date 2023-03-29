---->>>>>>>> ile jest wszystkich rekordow

select count(*) from citypairwise 


====================================================================================
-----ILE WARTOSCI JEST POZA ODCHYLENIEM--------------
====================================================================================

------------------WNIOSKI: wszystkich rekordow jest 2841


---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla PASSENGERS FROM city 1 to city 2

select count(*) from (

select "city1", "city2", "PASSENGERS FROM CITY1 TO CITY2",  
case
	when abs("PASSENGERS FROM CITY1 TO CITY2" - avg_value) < odchylenie then 1 else 0 end as in_std 
	
from
	(select *, round(avg("PASSENGERS FROM CITY1 TO CITY2") over (partition by "city1", "city2"),2) as avg_value,
	round(stddev("PASSENGERS FROM CITY1 TO CITY2") over (partition by  "city1", "city2"),2) as odchylenie
	from citypairwise c ) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 1007 z 2841;

---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla PASSENGERS FROM city 2 to city 1

select count(*) from (

select "city1", "city2", "PASSENGERS FROM CITY2 TO CITY1",  
case
	when abs("PASSENGERS FROM CITY2 TO CITY1" - avg_value) < odchylenie then 1 else 0 end as in_std 
	
from
	(select *, round(avg("PASSENGERS FROM CITY2 TO CITY1") over (partition by "city1", "city2"),2) as avg_value,
	round(stddev("PASSENGERS FROM CITY2 TO CITY1") over (partition by  "city1", "city2"),2) as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

------- WNIOSKI: Poza odchyleniem jest 998 z 2841


---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla FREIGHT FROM city 1 to city 2

select count(*) from (

select "city1", "city2", "FREIGHT FROM CITY1 TO CITY2",  
case
	when abs("FREIGHT FROM CITY1 TO CITY2" - avg_value) < odchylenie then 1 else 0 end as in_std 
	
from
	(select *, avg("FREIGHT FROM CITY1 TO CITY2") over (partition by "city1", "city2") as avg_value,
	stddev("FREIGHT FROM CITY1 TO CITY2") over (partition by  "city1", "city2") as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 1032 z 2841;

---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla FREIGHT FROM city 2 to city 1

select count(*) from (

select "city1", "city2", "FREIGHT FROM CITY2 TO CITY1",  
case
	when abs("FREIGHT FROM CITY2 TO CITY1" - avg_value) < odchylenie then 1 else 0 end as in_std 
	
from
	(select *, avg("FREIGHT FROM CITY2 TO CITY1") over (partition by "city1", "city2") as avg_value,
	stddev("FREIGHT FROM CITY2 TO CITY1") over (partition by  "city1", "city2") as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 1002 z 2841;

====================================================================================
-----ILE WARTOSCI JEST POZA PODWOJNYM ODCHYLENIEM--------------
====================================================================================


---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla PASSENGERS FROM city 1 to city 2

select count(*) from (

select "city1", "city2", "PASSENGERS FROM CITY1 TO CITY2",  
case
	when abs("PASSENGERS FROM CITY1 TO CITY2" - avg_value) < 2 * odchylenie then 1 else 0 end as in_std 
	
from
	(select *, round(avg("PASSENGERS FROM CITY1 TO CITY2") over (partition by "city1", "city2"),2) as avg_value,
	round(stddev("PASSENGERS FROM CITY1 TO CITY2") over (partition by  "city1", "city2"),2) as odchylenie
	from citypairwise c ) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 268 z 2841;

---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla PASSENGERS FROM city 2 to city 1

select count(*) from (

select "city1", "city2", "PASSENGERS FROM CITY2 TO CITY1",  
case
	when abs("PASSENGERS FROM CITY2 TO CITY1" - avg_value) < 2* odchylenie then 1 else 0 end as in_std 
	
from
	(select *, round(avg("PASSENGERS FROM CITY2 TO CITY1") over (partition by "city1", "city2"),2) as avg_value,
	round(stddev("PASSENGERS FROM CITY2 TO CITY1") over (partition by  "city1", "city2"),2) as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

------- WNIOSKI: Poza odchyleniem jest 279 z 2841


---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla FREIGHT FROM city 1 to city 2

select count(*) from (

select "city1", "city2", "FREIGHT FROM CITY1 TO CITY2",  
case
	when abs("FREIGHT FROM CITY1 TO CITY2" - avg_value) < 2* odchylenie then 1 else 0 end as in_std 
	
from
	(select *, avg("FREIGHT FROM CITY1 TO CITY2") over (partition by "city1", "city2") as avg_value,
	stddev("FREIGHT FROM CITY1 TO CITY2") over (partition by  "city1", "city2") as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 488 z 2841;

---->>>>>>>>ile wartosci jest poza odchyleniem standardowym dla FREIGHT FROM city 2 to city 1

select count(*) from (

select "city1", "city2", "FREIGHT FROM CITY2 TO CITY1",  
case
	when abs("FREIGHT FROM CITY2 TO CITY1" - avg_value) < 2* odchylenie then 1 else 0 end as in_std 
	
from
	(select *, avg("FREIGHT FROM CITY2 TO CITY1") over (partition by "city1", "city2") as avg_value,
	stddev("FREIGHT FROM CITY2 TO CITY1") over (partition by  "city1", "city2") as odchylenie
	from citypairwise) as q) as q2 where in_std = 0 ;

---------WNIOSKI: Poza odchyleniem jest 410 z 2841;


====================================================================================
-----GRUPOWANIE DLA CITY1 I CITY2- MIN, MAX, SUM, SREDNIA--------------
====================================================================================
----->>>> dla CITY1

SELECT city1, 
	min("PASSENGERS FROM CITY1 TO CITY2"),
	max("PASSENGERS FROM CITY1 TO CITY2"),
	sum("PASSENGERS FROM CITY1 TO CITY2"),
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),2) as avg_pass,

	min("PASSENGERS FROM CITY2 TO CITY1"),
	max("PASSENGERS FROM CITY2 TO CITY1"),
	sum("PASSENGERS FROM CITY2 TO CITY1"),
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),2) as avg_pass2,

	min("FREIGHT FROM CITY1 TO CITY2"),
	max("FREIGHT FROM CITY1 TO CITY2"),
	sum("FREIGHT FROM CITY1 TO CITY2"),
	avg("FREIGHT FROM CITY1 TO CITY2") as avg_frei,


	min("FREIGHT FROM CITY2 TO CITY1"),
	max("FREIGHT FROM CITY2 TO CITY1"),
	sum("FREIGHT FROM CITY2 TO CITY1"),
	avg("FREIGHT FROM CITY2 TO CITY1") as avg_frei1


FROM citypairwise c 
group by 1 order by 1;


----->>>> dla CITY2

SELECT city2, 
	min("PASSENGERS FROM CITY1 TO CITY2"),
	max("PASSENGERS FROM CITY1 TO CITY2"),
	sum("PASSENGERS FROM CITY1 TO CITY2"),
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),2) as avg_pass,

	min("PASSENGERS FROM CITY2 TO CITY1"),
	max("PASSENGERS FROM CITY2 TO CITY1"),
	sum("PASSENGERS FROM CITY2 TO CITY1"),
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),2) as avg_pass2,

	min("FREIGHT FROM CITY1 TO CITY2"),
	max("FREIGHT FROM CITY1 TO CITY2"),
	sum("FREIGHT FROM CITY1 TO CITY2"),
	avg("FREIGHT FROM CITY1 TO CITY2") as avg_frei,


	min("FREIGHT FROM CITY2 TO CITY1"),
	max("FREIGHT FROM CITY2 TO CITY1"),
	sum("FREIGHT FROM CITY2 TO CITY1"),
	avg("FREIGHT FROM CITY2 TO CITY1") as avg_frei1


FROM citypairwise c 
group by 1 order by 1;


====================================================================================
-----WYSZUKANIE PUSTYCH PRZELOTOW (calkowicie lub tylko passengers/freight----------
====================================================================================

---->>>> Całkowicie puste przeloty = 185 przelotow

select * from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" = 0 and "PASSENGERS FROM CITY2 TO CITY1" = 0 and "FREIGHT FROM CITY1 TO CITY2" = 0 and "FREIGHT FROM CITY2 TO CITY1" = 0;


---->>>>> przeloty tylko pasazerskie = 299 przelotow (w obie strony sa pasazerowie), 323 przelotow (przynajmniej w jedna strone sa pasazerowie)

select * from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" > 0 AND "PASSENGERS FROM CITY2 TO CITY1" >0 and "FREIGHT FROM CITY1 TO CITY2" = 0 and "FREIGHT FROM CITY2 TO CITY1" = 0;

select * from citypairwise c 
where ("PASSENGERS FROM CITY1 TO CITY2" > 0 OR "PASSENGERS FROM CITY2 TO CITY1" >0) and "FREIGHT FROM CITY1 TO CITY2" = 0 and "FREIGHT FROM CITY2 TO CITY1" = 0;


--->>>> przeloty tylko z ładunkiem = 47 przelotow (w obie strony jest ładunek), 103 przeloty (przynajmniej w jedna strone jest ładunek)

select * from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" = 0 and "PASSENGERS FROM CITY2 TO CITY1" = 0 and "FREIGHT FROM CITY1 TO CITY2" > 0 and "FREIGHT FROM CITY2 TO CITY1" > 0;

select * from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" = 0 and "PASSENGERS FROM CITY2 TO CITY1" = 0 and ("FREIGHT FROM CITY1 TO CITY2" > 0 OR "FREIGHT FROM CITY2 TO CITY1" > 0);


===================================================================================
----- GRUPOWANIE PO ROKU I KWARTALE -----------------------------------------------
===================================================================================

---->>> Grupowanie po roku 

select "YEAR",  
	sum("PASSENGERS FROM CITY1 TO CITY2") as P_TO_I, 
	sum("PASSENGERS FROM CITY2 TO CITY1") as P_FROM_I, 
	round(sum("FREIGHT FROM CITY1 TO CITY2")::numeric, 2) as F_TO_I, 
	round(sum("FREIGHT FROM CITY2 TO CITY1")::numeric,2) as F_FROM_I 
from citypairwise c 
group by 1 order by 1;

YEAR|p_to_i  |p_from_i|f_to_i   |f_from_i |
----+--------+--------+---------+---------+
2015|23781640|24858956|560738.00|887775.00|
2016|26807724|27771398|587550.00|897475.00|
2017| 6521248| 6775745|137174.00|231437.00|


select "YEAR", city1, city2,  
	sum("PASSENGERS FROM CITY1 TO CITY2") as P_TO_I, 
	sum("PASSENGERS FROM CITY2 TO CITY1") as P_FROM_I, 
	round(sum("FREIGHT FROM CITY1 TO CITY2")::numeric, 2) as F_TO_I, 
	round(sum("FREIGHT FROM CITY2 TO CITY1")::numeric,2) as F_FROM_I 
from citypairwise c 
group by 1,2,3 order by 1;

---->>>Grupowanie po kwartale

select "YEAR", quarter,  
	sum("PASSENGERS FROM CITY1 TO CITY2") as P_TO_I, 
	sum("PASSENGERS FROM CITY2 TO CITY1") as P_FROM_I, 
	round(sum("FREIGHT FROM CITY1 TO CITY2")::numeric, 2) as F_TO_I, 
	round(sum("FREIGHT FROM CITY2 TO CITY1")::numeric,2) as F_FROM_I 
from citypairwise c 
group by 1,2 order by 1,2;

YEAR|quarter|p_to_i |p_from_i|f_to_i   |f_from_i |
----+-------+-------+--------+---------+---------+
2015|Q1     |5712230| 6376365|126382.00|213763.00|
2015|Q2     |5876964| 6276379|138741.00|214714.00|
2015|Q3     |5711102| 6064483|150642.00|205418.00|
2015|Q4     |6481344| 6141729|144974.00|253880.00|
2016|Q1     |6343530| 6871288|134226.00|215836.00|
2016|Q2     |6778304| 7424671|154550.00|237738.00|
2016|Q3     |7170031| 6672921|153139.00|224225.00|
2016|Q4     |6515859| 6802518|145634.00|219676.00|
2017|Q1     |6521248| 6775745|137174.00|231437.00|



select "YEAR", quarter, city1, city2,
	sum("PASSENGERS FROM CITY1 TO CITY2") as P_TO_I, 
	sum("PASSENGERS FROM CITY2 TO CITY1") as P_FROM_I, 
	round(sum("FREIGHT FROM CITY1 TO CITY2")::numeric, 2) as F_TO_I, 
	round(sum("FREIGHT FROM CITY2 TO CITY1")::numeric, 2) as F_FROM_I 
from citypairwise c 
group by 1, 2, 3, 4 order by 1, 2;























