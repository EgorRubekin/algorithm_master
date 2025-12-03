def test_find_connected_components():
    # Пустой граф
    graph = {}
    assert find_connected_components(graph) == []

    # Одна вершина
    graph = {1: []}
    assert sorted(map(sorted, find_connected_components(graph))) == [[1]]

    # Изолированные вершины 
    graph = {1: [], 2: [], 3: []}
    assert sorted(map(sorted, find_connected_components(graph))) == [[1], [2], [3]]

    # Простой связный граф
    graph = {1: [2], 2: [1, 3], 3: [2]}
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2, 3]]

    # Несколько компонент
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: [],
    }
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2], [3, 4], [5]]

    # Компонента-цикл
    graph = {1: [2], 2: [3], 3: [1]}
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2, 3]]

    # Несимметричный ввод
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: [],
    }
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2], [3, 4]]

    # Большая компонента + одиночные 
    graph = {
        1: [2, 3],
        2: [1],
        3: [1, 4],
        4: [3],
        10: [],
        11: [],
    }
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2, 3, 4], [10], [11]]

    # Строковые вершины 
    graph = {
        "a": ["b"],
        "b": ["a", "c"],
        "c": ["b"],
        "x": [],
    }
    assert sorted(map(sorted, find_connected_components(graph))) == [["a", "b", "c"], ["x"]]

    # Дубликаты рёбер 
    graph = {
        1: [2, 2, 2],
        2: [1, 1],
        3: [],
    }
    assert sorted(map(sorted, find_connected_components(graph))) == [[1, 2], [3]]

    print("Все тесты пройдены")



test_find_connected_components()