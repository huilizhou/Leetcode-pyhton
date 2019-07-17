# Write your MySQL query statement below
select Score,(select count(distinct score) from Scores where Score>=s.Score) as Rank from Scores  as s order by Score desc;