from sort import bubble_sort, insertion_sort, quick_sort, merge_sort
import sys
import threading


def main():
    # sort_command, file_address = input().split()
    sort_command, file_address = "bubble", f"./testCases/test{12}.txt"
    sort_algorithm = bubble_sort
    if sort_command == "bubble":
        sort_algorithm = bubble_sort
    elif sort_command == "insertion":
        sort_algorithm = insertion_sort
    elif sort_command == "quick":
        sort_algorithm = quick_sort
    elif sort_command == "merge":
        sort_algorithm = merge_sort
    else:
        print("unknown sort algorithm")
        exit(-1)

    from graph import Graph
    import time
    import matplotlib.pyplot as plt
    before = time.time()
    _graph = Graph.get_graph_from_file(file_address)
    after = time.time()
    print(f"reading and storing in data structure: {round(after - before, 5)} seconds")
    before = time.time()
    _edges: list = _graph.get_all_edges()
    after = time.time()
    print(f"computing scores for first time: {round(after - before, 5)} seconds")

    sort_times = []
    before = time.time()
    _edges = sort_algorithm(_edges)
    after = time.time()
    sort_times.append(round(after - before, 4))
    # for edge in _edges:
    #     print(edge)
    from graph import Edge
    cnt = 0
    while True:
        # print("sorting")
        before = time.time()
        _edges = sort_algorithm(_edges)
        after = time.time()
        sort_times.append(round(after - before, 6))
        # print("removing edge")
        deleted_edge: Edge = _edges.pop(0)
        print("deleted edge: ", deleted_edge)
        cnt += 1
        _graph.delete_edge(deleted_edge.src, deleted_edge.dst)
        _graph.delete_edge(deleted_edge.dst, deleted_edge.src)
        # print("checking connectivity")
        if not _graph.is_connected():
            break
        # print("updating scores")
        _edge: Edge
        for _edge in _edges:
            if _edge.src == deleted_edge.src or _edge.src == deleted_edge.dst or _edge.dst == deleted_edge.src or _edge.dst == deleted_edge.dst:
                _edge.score = _graph.get_score(_edge.src, _edge.dst)
    for component in _graph.connected_components():
        print(component)
    print(f"number of deleted: {cnt}")
    _graph.write_edges()
    _graph.write_components()
    plt.plot(list(range(1, len(sort_times) + 1)), sort_times)
    plt.show()


if __name__ == '__main__':
    # main()
    sys.setrecursionlimit(10 ** 9)
    threading.stack_size(10 ** 8)
    threading.Thread(target=main).start()
