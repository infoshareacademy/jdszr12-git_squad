---------------Tabela airlinewise
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow
select * into temp airlinewise_t from airlinewise a 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0

select * from airlinewise_t

---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow
-----airlinewise_p
select * into airlinewise_p from airlinewise a 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0

select * from airlinewise_t

---------------Tabela citypairwise 
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow
select * into temp citypairwise_t from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" >0 and "PASSENGERS FROM CITY2 TO CITY1" >0

select * from citypairwise_t


---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow
-----citypairwise_p
select * into citypairwise_p from citypairwise c 
where "PASSENGERS FROM CITY1 TO CITY2" >0 and "PASSENGERS FROM CITY2 TO CITY1" >0

select * from citypairwise_p

---------------Tabela countrwise
---------Utworzenie tabeli tymczasowej bez zer w kolumnach pasarzerow
select * into temp countrywise_t from countrywise c 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0

select * from countrywise_t

---------Utworzenie NOWEJ TABELI bez zer w kolumnach pasarzerow
-----countrywise_p
select * into countrywise_p from countrywise c 
where "PASSENGERS TO INDIA" >0 and "PASSENGERS FROM INDIA" >0

select * from countrywise_p





















