def test_dijkstra():
    # Простейший граф
    graph = {
        'A': {'B': 1},
        'B': {},
    }
    assert dijkstra(graph, 'A') == {'A': 0, 'B': 1}

    # Граф с несколькими путями 
    graph = {
        'A': {'B': 5, 'C': 1},
        'B': {'C': 2, 'D': 1},
        'C': {'B': 1, 'D': 4},
        'D': {}
    }
    res = dijkstra(graph, 'A')
    assert res['A'] == 0
    assert res['C'] == 1                
    assert res['B'] == 2                
    assert res['D'] == 3 


    graph = {
        1: {2: 3},
        2: {},
        3: {4: 2},
        4: {}
    }
    res = dijkstra(graph, 1)
    assert res[1] == 0
    assert res[2] == 3
    assert res[3] == float('inf')
    assert res[4] == float('inf')

    # Одновершинный граф
    graph = {10: {}}
    assert dijkstra(graph, 10) == {10: 0}

    # Случай с циклом
    graph = {
        'A': {'B': 2},
        'B': {'C': 2},
        'C': {'A': 2}
    }
    res = dijkstra(graph, 'A')
    assert res == {'A': 0, 'B': 2, 'C': 4}

    # Рёбра с разными весами
    graph = {
        'S': {'A': 10, 'B': 1},
        'A': {'C': 2},
        'B': {'A': 3},
        'C': {}
    }
    res = dijkstra(graph, 'S')
    assert res['S'] == 0
    assert res['B'] == 1                     
    assert res['A'] == 4                     
    assert res['C'] == 6 

    print("Все тесты пройдены")





test_dijkstra()
