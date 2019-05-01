import itertools
import math
import map1


class Graph:
    def __init__(self, graph, start, end):
        self.__graph = graph
        self.__vertices = len(graph)
        self.__print_table()
        print(self.__dijkstra(start, end))

    def __dijkstra(self, start, end):
        dist = [math.inf] * self.__vertices
        dist[start] = 0
        visited = [False] * self.__vertices
        min_index = start
        for _ in range(self.__vertices):
            min_value = math.inf
            for vertex in range(self.__vertices):
                if dist[vertex] < min_value and visited[vertex] is False:
                    min_value = dist[vertex]
                    min_index = vertex
            visited[min_index] = True
            for vertex in range(self.__vertices):
                if self.__graph[min_index][vertex] > 0 and visited[vertex] is False and dist[vertex] > dist[min_index] + self.__graph[min_index][vertex]:
                    dist[vertex] = dist[min_index] + self.__graph[min_index][vertex]
        return dist[end]

    def __print_table(self):
        for iterator, row in enumerate(itertools.zip_longest(*self.__graph)):
            string_row = self.__vertices * "{:<7}"
            try:
                print(string_row.format(*row))
            except TypeError:
                row = ['' if number is None else number for number in row]
                print(string_row.format(*row))


g = Graph(map1.graph, map1.start, map1.end)
