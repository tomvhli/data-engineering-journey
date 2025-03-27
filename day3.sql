-- 1. Count species
SELECT species, COUNT(*) 
FROM iris 
GROUP BY species;

-- 2. Average petal length by species
SELECT species, AVG(petal_length) 
FROM iris 
GROUP BY species;

-- 3. Filter large sepal lengths
SELECT * 
FROM iris 
WHERE sepal_length > 5.0;