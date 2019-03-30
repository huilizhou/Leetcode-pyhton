'''
合并区间
现在需要多名编辑把有病句的句子合并起来送给总编审核。
比如A编辑指出的病句是[1,10],[32,45];B编辑指出的病句是[5,16],[78,94]

那么[1,10]和[5,16]是有交叉的，可以合并成[1,16],[32,45],[78,94]

- 输入描述
编辑数量m，之后每行是每个编辑的标记的下标集合，第一个和最后一个下标用英文逗号分割，
每组下标之间用分号分隔

- 输出描述
合并后的下标集合，第一个和最后一个下标用英文逗号分隔，每组下标之间用分号分隔。
返回结果是从小到大的递增排列。

'''

# 输入处理
m = int(input())

tmp = []
for _ in range(m):
    line = [list(map(int, item.split(","))) for item in input().split(";")]
    tmp.extend(line)  # 将所有的病句存在一起

# 排序，按每段病句[l,r]的第一个位置l排序
tmp = sorted(tmp, key=lambda x: x[0])

ret = [tmp[0]]
for item in tmp[1:]:
    if ret[-1][1] >= item[0]:  # 贪心：对[l1,r1],[l2,r2]，如果r1>l2，则r1=max(r1,r2)
        ret[-1][1] = max(ret[-1][1], item[1])
    else:
        ret.append(item)

# 输出处理
s = ''
for item in ret[:-1]:
    s += str(item[0]) + ',' + str(item[1]) + ';'
s += str(ret[-1][0]) + ',' + str(ret[-1][1])
print(s)
