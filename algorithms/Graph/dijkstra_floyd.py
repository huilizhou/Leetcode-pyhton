inf = float('inf')
matrix_distance = [[0,1,12,inf,inf,inf],
                   [inf,0,9,3,inf,inf],
                   [inf,inf,0,inf,5,inf],
                   [inf,inf,4,0,13,15],
                   [inf,inf,inf,inf,0,4],
                   [inf,inf,inf,inf,inf,0]]

def dijkstra(matrix_distance, source_node):
    inf = float('inf')
    # init the source node distance to others
    dis = matrix_distance[source_node]
    node_nums = len(dis)
    
    flag = [0 for i in range(node_nums)]
    flag[source_node] = 1
    
    for i in range(node_nums-1):
        min = inf
        #find the min node from the source node
        for j in range(node_nums):
            if flag[j] == 0 and dis[j] < min:
                min = dis[j]
                u = j
        flag[u] = 1
        #update the dis 
        for v in range(node_nums):
            if flag[v] == 0 and matrix_distance[u][v] < inf:
                if dis[v] > dis[u] + matrix_distance[u][v]:
                    dis[v] = dis[u] + matrix_distance[u][v]                    
    
    return dis

print(dijkstra(matrix_distance, 0))


def Floyd(dis):
    #min (Dis(i,j) , Dis(i,k) + Dis(k,j) )
    nums_vertex = len(dis[0])
    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis
print(Floyd(matrix_distance))