---------------Tabela airlinewise
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow i freight
select * into temp airlinewise_frtemp from airlinewise a 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0
      and "FREIGHT TO INDIA">0 and "FREIGHT FROM INDIA">0
      
      
select * from airlinewise_frtemp

---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow i freight
-----airlinewise_fr
select * into airlinewise_fr from airlinewise a 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0
      and "FREIGHT TO INDIA">0 and "FREIGHT FROM INDIA">0

select * from airlinewise_fr

---------------Tabela citypairwise 
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow i freight
select * into temp citypairwise_frtemp from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" >0 and "PASSENGERS FROM CITY2 TO CITY1" >0
      and "FREIGHT FROM CITY1 TO CITY2">0 and "FREIGHT FROM CITY2 TO CITY1">0
      
select * from citypairwise_frtemp


---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow i freight
-----citypairwise_fr
select * into citypairwise_fr from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" >0 and "PASSENGERS FROM CITY2 TO CITY1" >0
      and "FREIGHT FROM CITY1 TO CITY2">0 and "FREIGHT FROM CITY2 TO CITY1">0

select * from citypairwise_fr

---------------Tabela countrwise
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow i freight
select * into temp countrywise_frtemp from countrywise c 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0
      and "FREIGHT TO INDIA">0 and "FREIGHT FROM INDIA">0

select * from countrywise_frtemp

---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow i freight 
-----countrywise_fr
select * into countrywise_fr from countrywise c 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0
      and "FREIGHT TO INDIA">0 and "FREIGHT FROM INDIA">0


select * from countrywise_fr
