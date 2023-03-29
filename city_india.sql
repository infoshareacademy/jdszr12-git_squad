----------Suma liczby pasazerow i towarow w zstawieniu kwartalnym
------- dla kazdego miasta w Indiach




select distinct  c."YEAR" , c.quarter, city2,
sum("PASSENGERS FROM CITY1 TO CITY2"+"PASSENGERS FROM CITY2 TO CITY1")
      over (partition by c.quarter,c."YEAR", city2) as passengers_sum,
sum("FREIGHT FROM CITY1 TO CITY2" + "FREIGHT FROM CITY2 TO CITY1")
      over (partition by c.quarter, c."YEAR", city2) as freight_sum
from citypairwise c 





