def test_analyze_dag():
    # Простой ацикличный граф
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    kind, res = analyze_dag(graph)
    assert kind == "toposort"
    assert res == ['A', 'B', 'C']

    #  Граф с циклом 
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    kind, cycle = analyze_dag(graph)
    assert kind == "cycle"
    assert cycle[0] == cycle[-1]  
    assert set(cycle[:-1]) == {'A', 'B', 'C'}

    # Граф с несколькими компонентами, один цикл 
    graph = {
        1: [2],
        2: [3],
        3: [1],  
        4: [5],
        5: []
    }
    kind, cycle = analyze_dag(graph)
    assert kind == "cycle"
    assert set(cycle[:-1]) == {1, 2, 3}

    # Граф без рёбер
    graph = {1: [], 2: [], 3: []}
    kind, res = analyze_dag(graph)
    assert kind == "toposort"
    assert set(res) == {1, 2, 3}

    # Граф из одной вершины 
    graph = {10: []}
    kind, res = analyze_dag(graph)
    assert kind == "toposort"
    assert res == [10]

    # Несимметричный
    graph = {
        "A": ["B"],
        "B": [],
        "C": ["D"],
        "D": ["C"]  
    }
    kind, res = analyze_dag(graph)
    assert kind == "cycle"
    assert set(res[:-1]) == {"C", "D"}


    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["E"],
        "E": []
    }
    kind, topo = analyze_dag(graph)
    assert kind == "toposort"
    # A должен идти до B и C, B и C — до D, D — до E
    assert topo.index("A") < topo.index("B")
    assert topo.index("A") < topo.index("C")
    assert topo.index("B") < topo.index("D")
    assert topo.index("C") < topo.index("D")
    assert topo.index("D") < topo.index("E")

    print("Все тесты пройдены")




test_analyze_dag()
