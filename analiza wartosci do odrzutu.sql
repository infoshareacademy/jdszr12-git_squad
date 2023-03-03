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
-----GRUPOWANIE DLA CITY1 - MIN, MAX, SUM, SREDNIA--------------
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

































