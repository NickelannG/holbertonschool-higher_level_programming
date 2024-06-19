-- Lists number of records with same score in second_table
SELECT score, COUNT(*) AS result FROM second_table GROUP BY score ORDER BY score DESC;