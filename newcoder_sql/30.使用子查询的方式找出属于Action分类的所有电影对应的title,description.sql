```
SELECT f.title,f.description
FROM (film f
JOIN film_category fc
ON f.film_id=fc.film_id)
JOIN category c
ON fc.category_id=c.category_id
WHERE c.name='Action'
```