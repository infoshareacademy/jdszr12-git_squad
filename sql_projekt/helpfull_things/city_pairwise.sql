
------------------------------------------------
---- WARUNEK USUWAJACY ZEROWE POLACZENIA
------------------------------------------------

select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0;

--------------------------------------------------------------
----5 NAJWIEKSZYCH LOTNISK (POD WZGLEDEM RUCHU PASAZERSKIEGO)
--------------------------------------------------------------
DELHI, MUMBAI, CHENNAI, KOCHI, BENGALURU

select  country2, city2, sum("PASSENGERS FROM CITY1 TO CITY2"), sum("PASSENGERS FROM CITY2 TO CITY1")  from 

(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0) as q

group by 1, 2   order by 4 DESC;



-----------------
----KWARTALNIE: SREDNIA MIN MAX DLA RUCHU PASAZERSKIEGO TOP5 vs CALOSC
-----------------


-----PRZYLOTY DO INDII:
----- dla TOP5 dla wlatujących dla Indii
select city2, "YEAR" ,quarter, 
	min("PASSENGERS FROM CITY1 TO CITY2") as minimum,
	max("PASSENGERS FROM CITY1 TO CITY2") as maximum,
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2, 3 order by 1, 2 , 3;


---- dla wszystkich dla wlatujacych do Indii
select city2, "YEAR" ,quarter, 
	min("PASSENGERS FROM CITY1 TO CITY2") as minimum,
	max("PASSENGERS FROM CITY1 TO CITY2") as maximum,
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2, 3 order by 1, 2 , 3;



----WYLOTY Z INDII:

----- dla TOP5 dla wylatujacych z Indii
select city2, "YEAR" ,quarter, 
	min("PASSENGERS FROM CITY2 TO CITY1") as minimum,
	max("PASSENGERS FROM CITY2 TO CITY1") as maximum,
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2, 3 order by 1, 2 , 3;


---- dla wszystkich dla wylatujacych z Indii
select city2, "YEAR" ,quarter, 
	min("PASSENGERS FROM CITY2 TO CITY1") as minimum,
	max("PASSENGERS FROM CITY2 TO CITY1") as maximum,
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2, 3 order by 1, 2 , 3;




-----------------
----ROCZNIE: SREDNIA MIN MAX DLA RUCHU PASAZERSKIEGO TOP5 vs CALOSC
-----------------


-----PRZYLOTY DO INDII:
----- dla TOP5 dla wlatujących dla Indii
select city2, "YEAR" , 
	min("PASSENGERS FROM CITY1 TO CITY2") as minimum,
	max("PASSENGERS FROM CITY1 TO CITY2") as maximum,
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2 order by 1, 2 ;


---- dla wszystkich dla wlatujacych do Indii
select city2, "YEAR" , 
	min("PASSENGERS FROM CITY1 TO CITY2") as minimum,
	max("PASSENGERS FROM CITY1 TO CITY2") as maximum,
	round(avg("PASSENGERS FROM CITY1 TO CITY2"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2 order by 1, 2;


----WYLOTY Z INDII:

----- dla TOP5 dla wylatujacych z Indii
select city2, "YEAR",
	min("PASSENGERS FROM CITY2 TO CITY1") as minimum,
	max("PASSENGERS FROM CITY2 TO CITY1") as maximum,
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2 order by 1, 2;


---- dla wszystkich dla wylatujacych z Indii
select city2, "YEAR" , 
	min("PASSENGERS FROM CITY2 TO CITY1") as minimum,
	max("PASSENGERS FROM CITY2 TO CITY1") as maximum,
	round(avg("PASSENGERS FROM CITY2 TO CITY1"),0) as srednia

from
(select * from city_pairwise cp 
where "PASSENGERS FROM CITY1 TO CITY2" != 0 and "PASSENGERS FROM CITY2 TO CITY1" != 0 and "FREIGHT FROM CITY1 TO CITY2" !=0 and "FREIGHT FROM CITY2 TO CITY1" != 0
and city2 like 'DELHI' or city2 like 'MUMBAI' or city2 like 'CHENNAI' or city2 like 'KOCHI' or city2 like 'BENGALURU') as q
group by 1, 2 order by 1, 2 ;



