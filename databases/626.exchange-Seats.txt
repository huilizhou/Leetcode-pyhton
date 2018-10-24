select s.id,s.student from 
(select id -1 as id,student from seat  where id%2=0
union 
select id +1 as id ,student from seat where id%2=1 and id !=(select count(*) form seat)
union
select id,student from seat where id%2=1 and id=(select count(*) from seat)
) s order by id;