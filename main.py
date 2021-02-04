def main():
    from graph import Graph
    _graph = Graph.get_graph_from_file(f"./testCases/test{1}.txt")
    print(_graph)


if __name__ == '__main__':
    main()
