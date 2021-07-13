-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT s.title, g.id
FROM hbtn_0d_tvshows.tv_shows s
LEFT JOIN hbtn_0d_tvshows.tv_show_genres sg ON sg.show_id = s.id
LEFT JOIN hbtn_0d_tvshows.tv_genres g ON sg.genre_id = g.id
WHERE g.id IS NULL
ORDER BY s.title ASC, g.id ASC;
