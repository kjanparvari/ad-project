class Node:

    def __init__(self, _id: int):
        self._id: int = _id
        self._neighbours: list = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def neighbours(self) -> list:
        return self._neighbours

    def add_neighbour(self, neighbour: int) -> None:
        self._neighbours.append(neighbour)

    def out_degree(self) -> int:
        return len(self._neighbours)

    def in_degree(self) -> int:
        pass

    def degree(self) -> int:
        return self.in_degree() + self.out_degree()

    def __str__(self) -> str:
        return str(self._id) + " : " + str(self._neighbours)


class Graph:

    def __init__(self):
        self._nodes: dict = {}

    @property
    def nodes(self) -> dict:
        return self._nodes

    def get_node(self, _id: int) -> Node or None:
        if _id not in self._nodes.keys():
            return None
        return self._nodes[_id]

    def add(self, src_id: int, dst_id: int) -> None:
        if src_id not in self._nodes.keys():
            self._nodes[src_id] = Node(src_id)
        self._nodes[src_id].add_neighbour(dst_id)

    def add_multiple(self, edges: list) -> None:
        for (src_id, dst_id) in edges:
            self.add(src_id, dst_id)

    def get_score(self, src_id: int, dst_id: int) -> float:
        pass

    @staticmethod
    def get_graph_from_file(file_address: str):
        edges: list
        with open(file_address, "r", encoding='utf-8') as file:
            edges = [tuple([int(node) for node in line.split()]) for line in file.readlines()]
            file.close()
        _graph = Graph()
        _graph.add_multiple(edges)
        return _graph

    def __str__(self) -> str:
        _str = ""
        for _id, node in self._nodes.items():
            _str += str(node) + "\n"
        return _str
