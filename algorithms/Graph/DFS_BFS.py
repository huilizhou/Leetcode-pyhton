graph = {
    'a': ['b', 'c'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['c', 'd'],
    'f': ['d']
}

# BFS


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)


BFS(graph, 'a')

# DFS


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


DFS(graph, 'a')


def DFS1(graph, s, queue=[]):
    queue.append(s)
    for i in graph[s]:
        if i not in queue:
            DFS1(graph, i, queue)
    return queue


print(DFS1(graph, 'a'))
