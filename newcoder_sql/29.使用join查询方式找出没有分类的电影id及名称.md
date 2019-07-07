```
SELECT f.film_id,f.title 
FROM film f 
LEFT JOIN film_category fc
ON f.film_id=fc.film_id
WHERE fc.category_id IS NULL
```