-------------------------
---MONTH_INTERNATIONAL ---
-------------------------

--- wielkosc zaladunku (ludzi i towarow) per linia lotnicza w calym okresie

----ANALIZA PASAZEROW DO INDII
select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 2; 


select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 2 desc;

---ANALIZA PASAZEROW Z INDII
select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 3; 


select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 3 desc;

----ANALIZA TOWAROW DO INDII
select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 4; 


select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 4 desc;

---ANALIZA TOWAROW Z INDII
select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 5; 


select "AIRLINE NAME", sum("PASSENGERS TO INDIA"), sum("PASSENGERS FROM INDIA"), sum("FREIGHT TO INDIA"), sum("FREIGHT FROM INDIA") from month_international mi
group by 1 order by 5 desc;

		--WNIOSKI: 
				--- Eva Airways nie przewozila nic:  
				select * from month_international mi where "AIRLINE NAME" ilike 'Eva Airways' ;
				
				--- 6 linii nie przewozi pasazerow, tylko towary
				
				--- 15 linii nie przywozi towarow do Indii, 10 linii nie wywozi towarów z Indii.

			---PASAZEROWIE: 
				----do Indii polecialo: najmniej - 465, najwięcej - 8320544
				--- z Indii wylecialo: najmniej - 237, najwiecej - 8471096		

			---TOWARY:
				----do Indii wlecialo: najmniej - 2.196, najwiecej 181452.44
				--- Z Indii wylecialo: najmniej - 0.1, najwięcej 347591.8



---udzial linii indyjskich w calym ruchu 			
select count( distinct "AIRLINE NAME")  from month_international mi 
where "CARRIER TYPE"  ilike 'DOMESTIC';

			
select count( "AIRLINE NAME")  from month_international mi 
where "CARRIER TYPE"  ilike 'DOMESTIC';


select count( "AIRLINE NAME")  from month_international mi 		
select count(distinct  "AIRLINE NAME")  from month_international mi 

			---WNIOSKI: 5 linii krajowych ( 5%, wszystkich jest 100), które zrealizowały 135 loty (6%, wszystkie loty: 2334) 

----ile wartosci jest poza odchyleniem standardowym dla PASSENGERS TO INDIA

		
select "AIRLINE NAME", "PASSENGERS TO INDIA",  
case
	when abs("PASSENGERS TO INDIA" - avg_value) < odchylenie then 1 else 0 end as in_std 
	
from
	(select *, round(avg("PASSENGERS TO INDIA") over (partition by "AIRLINE NAME"),2) as avg_value,
	round(stddev("PASSENGERS TO INDIA") over (partition by "AIRLINE NAME"),2) as odchylenie
	from month_international mi) as q;

-----WNIOSKI: 200 jest poza odchyleniem na 2334.













----rozklad oblozenia lotow w podziale na lata/kwartaly/miesiace
select "YEAR", 
	sum("PASSENGERS TO INDIA") as P_TO_I, 
	sum("PASSENGERS FROM INDIA") as P_FROM_I, 
	sum("FREIGHT TO INDIA") as F_TO_I, 
	sum("FREIGHT FROM INDIA") as F_FROM_I 
from month_international mi 
group by 1 order by 1;

YEAR|p_to_i  |p_from_i|f_to_i   |f_from_i |
----+--------+--------+---------+---------+
2015|23781640|24858956| 560737.2| 887774.8|
2016|26543689|27122472|570518.56|893202.44|
2017| 6778304| 7424671|154621.08|238545.94|


select "YEAR", 
	case
		when "MONTH" like 'JAN' then '01'
		when "MONTH" like 'FEB' then '02'
		when "MONTH" like 'MAR' then '03'
		when "MONTH" like 'APR' then '04'
		when "MONTH" like 'MAY' then '05'
		when "MONTH" like 'JUN' then '06'
		when "MONTH" like 'JUL' then '07'
		when "MONTH" like 'AUG' then '08'
		when "MONTH" like 'SEP' then '09'
		when "MONTH" like 'OCT' then '10'
		when "MONTH" like 'NOV' then '11'
		else '12'
	end as MSC,
	sum("PASSENGERS TO INDIA") as P_TO_I, 
	sum("PASSENGERS FROM INDIA") as P_FROM_I, 
	ROUND(sum("FREIGHT TO INDIA")::numeric ,2) as F_TO_I, 
	round(sum("FREIGHT FROM INDIA")::numeric ,2) as F_FROM_I 
from month_international mi 
group by 1, 2 order by 1,2;

YEAR|msc|p_to_i |p_from_i|f_to_i  |f_from_i |
----+---+-------+--------+--------+---------+
2015|01 |2079662| 2236061|39561.90| 72763.20|
2015|02 |1764380| 1982268|40590.80| 65478.40|
2015|03 |1868188| 2158036|46228.90| 75520.90|
2015|04 |1779369| 2138120|44996.80| 69767.40|
2015|05 |2032635| 2233776|48352.40| 72994.30|
2015|06 |2064960| 1904483|45391.10| 71952.20|
2015|07 |2178194| 1793448|46769.80| 71087.60|
2015|08 |1815667| 2260718|56823.40| 68385.60|
2015|09 |1717241| 2010317|47047.70| 65945.10|
2015|10 |2042536| 2011537|54270.70| 81603.10|
2015|11 |2096937| 1943196|43958.20| 62025.00|
2015|12 |2341871| 2186996|46745.50|110252.00|
2016|01 |2263352| 2421968|43765.60| 66392.60|
2016|02 |1973688| 2123380|41089.20| 68938.40|
2016|03 |2106490| 2325940|49371.30| 80505.30|
2016|04 |1959340| 2375183|45922.00| 75218.50|
2016|05 |2206612| 2437937|46190.40| 77512.40|
2016|06 |2355296| 1962625|45061.70| 78705.70|
2016|07 |2475137| 2081707|48473.00| 73268.60|
2016|08 |2067689| 2424063|47419.10| 73907.40|
2016|09 |1973033| 2296748|49742.40| 72500.10|
2016|10 |2200089| 2094707|52396.90| 80946.10|
2016|11 |2324759| 2194642|49964.80| 71950.70|
2016|12 |2638204| 2383572|51122.30| 73356.40|
2017|01 |2479129| 2602815|49208.80| 73118.10|
2017|02 |2065487| 2322833|45059.50| 76144.10|
2017|03 |2233688| 2499023|60352.80| 89283.70|




select "YEAR", quarter, 
	sum("PASSENGERS TO INDIA") as P_TO_I, 
	sum("PASSENGERS FROM INDIA") as P_FROM_I, 
	sum("FREIGHT TO INDIA") as F_TO_I, 
	sum("FREIGHT FROM INDIA") as F_FROM_I 
from month_international mi 
group by 1, 2 order by 1, 2;

YEAR|quarter|p_to_i |p_from_i|f_to_i   |f_from_i |
----+-------+-------+--------+---------+---------+
2015|Q1     |5712230| 6376365|126381.53|213762.52|
2015|Q2     |5876964| 6276379|138740.33|214713.92|
2015|Q3     |5711102| 6064483|150640.97|205418.27|
2015|Q4     |6481344| 6141729|144974.52|253880.69|
2016|Q1     |6343530| 6871288|134226.06|215836.25|
2016|Q2     |6521248| 6775745|137174.06|231436.66|
2016|Q3     |6515859| 6802518|145634.56|219676.08|
2016|Q4     |7163052| 6672921|153484.05|226253.25|
2017|Q1     |6778304| 7424671|154621.08|238545.94|


---======================================================================================
---===============   COUNTRY QUARTER    =================================================
---======================================================================================

---- puste przeloty:

select count("COUNTRY NAME")  from country_q cq 
where "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0; 


select count(distinct "COUNTRY NAME")  from country_q cq 
where "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0; 

select distinct "COUNTRY NAME"  from country_q cq 
where "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0; 


---przeloty tylko z ładunkiem (jakimkolwiek)
select count("COUNTRY NAME")  from country_q cq 
where  "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and ("FREIGHT TO INDIA"::numeric  > 0 or  "FREIGHT FROM INDIA" ::numeric > 0);  


select count(distinct "COUNTRY NAME")  from country_q cq 
where "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and ("FREIGHT TO INDIA"::numeric  > 0 or "FREIGHT FROM INDIA" ::numeric > 0); 

select distinct "COUNTRY NAME"  from country_q cq 
where "PASSENGERS TO INDIA"::numeric = 0 AND "PASSENGERS FROM INDIA"::numeric  = 0 and ("FREIGHT TO INDIA"::numeric  > 0 or  "FREIGHT FROM INDIA" ::numeric > 0); 



---przeloty tylko z pasazerami (jakimikolwiek)
select count("COUNTRY NAME")  from country_q cq 
where  "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0 and ("PASSENGERS TO INDIA"::numeric > 0 or "PASSENGERS FROM INDIA"::numeric  > 0); 


select count(distinct "COUNTRY NAME")  from country_q cq 
where "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0 and ("PASSENGERS TO INDIA"::numeric > 0 or "PASSENGERS FROM INDIA"::numeric  > 0);

select distinct "COUNTRY NAME"  from country_q cq 
where "FREIGHT TO INDIA"::numeric  = 0 and "FREIGHT FROM INDIA" ::numeric = 0 and ("PASSENGERS TO INDIA"::numeric > 0 or "PASSENGERS FROM INDIA"::numeric  > 0); 





---LICZBA PASAZEROW DO INDII:

select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 2 ; 


select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 2 desc ; 

select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 3; 


select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 3 desc ; 

select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 4; 


select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 4 desc ; 

select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 5; 


select "COUNTRY NAME", sum("PASSENGERS TO INDIA") as P_TO_I, sum("PASSENGERS FROM INDIA") as P_FROM_I, sum("FREIGHT TO INDIA") as ftoi, sum("FREIGHT FROM INDIA") as F_FROM_I 
from country_q cq 
group by 1 order by 5 desc ; 



---WNIOSKI: 
			---bylo 35 /499 lotow na pusto, z 7 krajow : Belgium, Georgia, Iraq, Jordan, Reunion, South Africa, Vietnam
			--- wszystkie loty ktore mialy ladunek, mialy pasazerow chociaz w jedna strone		
			--- 9 lotow do/z krajow docelowych/startowych gdzie byli pasazerowie, ale nie bylo ladunku (dotyczy to 3 krajow: Azerbaijan, Iraq, Yemen)


			--- WAŻNE!!	jest UAE z *, jest tez United ARAB Emirates bez * - trzeba zweryfikowac czy to to samo, o co chodzi z gwiazdka

			---PASAZEROWIE:
			---do Indii leciało: najmniej 4104 pasażerow, najwięcej 15045602 (to UAE z *, jest tez United ARAB Emirates bez * - trzeba zweryfikowac czy to to samo)
			---z Indii leciało: najmniej 4386 pasażerow, najwięcej 15398512
			
			---TOWARY:
			----do Indii przylecialo: najmniej 2.2 towarow, a najwiecej: 234428.89
			----z Indii przyleciało: najmniej 1.3 towarow, a najwiecej: 496442.0 








