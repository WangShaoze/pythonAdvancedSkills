class DirectedGraph:
    def __init__(self, d):
        if isinstance(d, dict):
            self.__graph = d
        else:
            self.__graph = dict()
            print("Sth Error")
        self.__results = []

    def __generatePath(self, graph, path: list, end, results):
        current = path[-1]
        if current == end:
            results.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.__generatePath(graph, path + [n], end, results)

    def searchPath(self, start, end):
        self.__generatePath(self.__graph, [start], end, self.__results)
        self.__results.sort(key=lambda x: len(x))
        print("the path from {} to {} is:".format(self.__results[0][0], self.__results[0][-1]))
        for path in self.__results:
            print(path)


if __name__ == '__main__':
    # dg = DirectedGraph()
    # dg.searchPath("A", "E")
    pass

