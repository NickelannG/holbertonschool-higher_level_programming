-- lists all genres of the show Dexter in the imported hbtn_0d_tvshows database.
SET @dexter_id := 
(SELECT id FROM tv_shows WHERE title = 'Dexter');

SELECT name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = @dexter_id
GROUP BY name
ORDER BY name ASC;