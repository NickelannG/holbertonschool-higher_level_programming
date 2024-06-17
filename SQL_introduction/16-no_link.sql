-- Lists all records from table second_table in current db.
-- Except rows without a name value.
-- Results display score and name in descending order.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;