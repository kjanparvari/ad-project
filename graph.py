class Node:

    def __init__(self, _id: int):
        self._id: int = _id
        self._neighbours: list = []
        # self._in_degree: int = 0

    @property
    def id(self) -> int:
        return self._id

    @property
    def neighbours(self) -> list:
        return self._neighbours

    # @property
    # def in_degree(self):
    #     return self._in_degree

    # @property
    # def out_degree(self) -> int:
    #     return len(self._neighbours)

    @property
    def degree(self) -> int:
        # return self.in_degree + self.out_degree
        return len(self._neighbours)

    def contains_neighbour(self, neighbour_id: int) -> bool:
        return True if neighbour_id in self._neighbours else False

    # def increase_in_degree(self) -> int:
    #     self._in_degree += 1
    #     return self._in_degree

    def add_neighbour(self, neighbour_id: int) -> None:
        self._neighbours.append(neighbour_id)

    def __str__(self) -> str:
        return str(self._id) + " : " + str(self._neighbours)


class Edge:

    def __init__(self, _src_id: int, _dst_id: int, _score: float):
        self.src = _src_id
        self.dst = _dst_id
        self.score = _score

    def copy(self):
        return Edge(self.src, self.dst, self.score)

    def __str__(self) -> str:
        return f"({self.src}, {self.dst}) -> {self.score}"

    def __repr__(self) -> str:
        return self.__str__()


class Graph:

    def __init__(self):
        self._nodes: dict = {}

    @property
    def nodes(self) -> dict:
        return self._nodes

    def get_node(self, _id: int) -> Node or None:
        if _id not in self._nodes:
            return None
        return self._nodes[_id]

    def add_edge(self, src_id: int, dst_id: int) -> None:
        if src_id not in self._nodes:
            self._nodes[src_id] = Node(src_id)
        if dst_id not in self._nodes:
            self._nodes[dst_id] = Node(dst_id)
        # self._nodes[dst_id].increase_in_degree()
        self._nodes[src_id].add_neighbour(dst_id)

    def add_multiple_edge(self, edges: list) -> None:
        for (src_id, dst_id) in edges:
            self.add_edge(src_id, dst_id)

    def delete_edge(self, src_id: int, dst_id: int):
        if dst_id in self._nodes[src_id].neighbours:
            self._nodes[src_id].neighbours.remove(dst_id)

    def directed_cycles_number(self, src_id: int, dst_id: int) -> int:
        result: int = 0
        if src_id in self._nodes[dst_id].neighbours:
            for node_id in self._nodes[src_id].neighbours:
                if dst_id in self._nodes[node_id].neighbours:
                    result += 1
            return result
        else:
            return 0

    def cycles_number(self, node_id1: int, node_id2: int) -> int:
        return self.directed_cycles_number(node_id1, node_id2)  # + self.directed_cycles_number(node_id2, node_id1)

    def get_score(self, src_id: int, dst_id: int) -> float:
        if self._nodes[src_id].degree == 1 or self._nodes[dst_id].degree == 1:
            return float("inf")
        _cycles_number = self.cycles_number(src_id, dst_id) + 1
        # if src_id == 4 and dst_id == 91:
        #     print("degree", self._nodes[src_id].degree, self._nodes[dst_id].degree)
        return _cycles_number / (min(self._nodes[src_id].degree, self._nodes[dst_id].degree) - 1)

    def get_all_edges(self) -> list:
        _result: list = []
        _dict: dict = {}
        for _node_id in self._nodes:
            for _neighbour_id in self._nodes[_node_id].neighbours:
                if not ((_node_id, _neighbour_id) in _dict or (_neighbour_id, _node_id) in _dict):
                    _dict[(_node_id, _neighbour_id)] = True
                    _score = self.get_score(_node_id, _neighbour_id)
                    _result.append(Edge(_node_id, _neighbour_id, _score))
        return _result

    def is_connected(self) -> bool:
        return True if len(self.connected_components()) == 1 else False

    def DFSUtil(self, temp: list, node_id: int, visited: dict) -> list:
        visited[node_id] = True
        temp.append(node_id)
        for neighbour_id in self._nodes[node_id].neighbours:
            if not visited[neighbour_id]:
                temp = self.DFSUtil(temp, neighbour_id, visited)
        return temp

    # Method to retrieve connected components
    # in an undirected graph
    def connected_components(self) -> list:
        visited = {}
        cc = []
        for node_id in self._nodes:
            visited[node_id] = False
        for node_id in self._nodes:
            if not visited[node_id]:
                temp = []
                cc.append(self.DFSUtil(temp, node_id, visited))
        return cc

    def write_edges(self):
        lines = []
        with open("./dist/edges.txt", "w") as file:
            for _node_id in self._nodes:
                for _neighbour_id in self._nodes[_node_id].neighbours:
                    lines.append(f"{_node_id}, {_neighbour_id}\n")
            file.writelines(lines)
            # print(lines)
            file.close()

    def write_components(self):
        lines = []
        [class_a, class_b] = self.connected_components()
        for _node_id in class_a:
            lines.append(f"{_node_id} -> A\n")
        for _node_id in class_b:
            lines.append(f"{_node_id} -> B\n")
        with open("./dist/components.txt", "w") as file:
            file.writelines(lines)
            # print(lines)
            file.close()

    @staticmethod
    def get_graph_from_file(file_address: str):
        edges: list
        with open(file_address, "r", encoding='utf-8') as file:
            edges = [tuple([int(node) for node in line.split()]) for line in file.readlines()]
            file.close()
        _graph = Graph()
        _graph.add_multiple_edge(edges)
        return _graph

    def __str__(self) -> str:
        _str = ""
        for _id, node in self._nodes.items():
            _str += str(node) + "\n"
        return _str
