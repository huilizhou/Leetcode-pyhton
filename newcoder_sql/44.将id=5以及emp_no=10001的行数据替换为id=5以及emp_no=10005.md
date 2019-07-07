```
运用REPLACE(X,Y,Z)函数。其中X是要处理的字符串，Y是X中将要被替换的字符串，Z是用来替换Y的字符串，最终返回替换后的字符串
```
```
UPDATE titles_test SET emp_no=REPLACE(emp_no,10001,10005) WHERE id=5
```