-- lists all cities of Calfornia that can be found in database hbtn_0d_usa
SET @desired_id :=
(SELECT id FROM states
WHERE name = 'California');
SELECT id, name FROM cities
WHERE state_id = @desired_id
ORDER BY id ASC;