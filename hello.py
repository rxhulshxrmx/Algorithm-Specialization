import sys

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

def read_graph_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    n, m = map(int, lines[0].split())
    graph = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v, w = map(int, line.split())
        graph[u-1].append((v-1, w))
    return graph

if __name__ == '__main__':
    filenames = ['graph1.txt', 'graph2.txt', 'graph3.txt']
    for filename in filenames:
        graph = read_graph_file(filename)
        dist = floyd_warshall(graph)
        min_dist = sys.maxsize
        for i in range(len(dist)):
            for j in range(len(dist)):
                if i != j:
                    min_dist = min(min_dist, dist[i][j])
        print(f"Minimum shortest path in {filename}: {min_dist}")
