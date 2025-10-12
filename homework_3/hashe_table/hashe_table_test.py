def test_hash_table():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ХЕШ-ТАБЛИЦЫ")
    print("=" * 60)

    print("\nТест 1: Базовая функциональность")
    table = HashTable()
    table.put("name", "Alice")
    table.put("age", 25)
    table.put("city", "Moscow")
    assert table.get("name") == "Alice"
    assert table.get("age") == 25
    assert table.get("city") == "Moscow"
    assert table.get("country") is None
    assert len(table) == 3
    print("Тест 1 пройден")

    print("\nТест 2: Обновление значений")
    table.put("age", 26)
    assert table.get("age") == 26
    assert len(table) == 3
    print("Тест 2 пройден")

    print("\nТест 3: Удаление элементов")
    assert table.delete("city") == True
    assert table.get("city") is None
    assert len(table) == 2
    assert table.delete("nonexistent") == False
    print("Тест 3 пройден")

    print("\nТест 4: Проверка наличия ключей")
    assert "name" in table
    assert "city" not in table
    assert table.contains("age") == True
    assert table.contains("country") == False
    print("Тест 4 пройден")

    print("\nТест 5: Коллизии")
    small_table = HashTable(initial_size=2)
    small_table.put("a", 1)
    small_table.put("b", 2)
    small_table.put("c", 3)
    assert small_table.get("a") == 1
    assert small_table.get("b") == 2
    assert small_table.get("c") == 3
    assert len(small_table) == 3
    print("Тест 5 пройден")

    print("\nТест 6: Динамическое расширение")
    expanding_table = HashTable(initial_size=4, load_factor=0.75)
    initial_size = expanding_table.size
    expanding_table.put("k1", "v1")
    expanding_table.put("k2", "v2")
    expanding_table.put("k3", "v3")
    assert expanding_table.size == initial_size
    expanding_table.put("k4", "v4")
    assert expanding_table.size > initial_size
    assert expanding_table.get("k1") == "v1"
    assert expanding_table.get("k2") == "v2"
    assert expanding_table.get("k3") == "v3"
    assert expanding_table.get("k4") == "v4"
    print(f"Тест 6 пройден: {initial_size} -> {expanding_table.size}")

    print("\nТест 7: Разные типы ключей")
    table_mixed = HashTable()
    table_mixed.put(1, "integer")
    table_mixed.put(3.14, "float")
    table_mixed.put((1, 2), "tuple")
    table_mixed.put("string", "text")
    assert table_mixed.get(1) == "integer"
    assert table_mixed.get(3.14) == "float"
    assert table_mixed.get((1, 2)) == "tuple"
    assert table_mixed.get("string") == "text"
    print("Тест 7 пройден")

    print("\nТест 8: Методы keys, values, items")
    table_kvi = HashTable()
    table_kvi.put("x", 10)
    table_kvi.put("y", 20)
    table_kvi.put("z", 30)
    keys = table_kvi.keys()
    values = table_kvi.values()
    items = table_kvi.items()
    assert set(keys) == {"x", "y", "z"}
    assert set(values) == {10, 20, 30}
    assert set(items) == {("x", 10), ("y", 20), ("z", 30)}
    print("Тест 8 пройден")

    print("\nТест 9: Строковое представление")
    table_str = HashTable()
    table_str.put("a", 1)
    table_str.put("b", 2)
    result_str = str(table_str)
    assert "a: 1" in result_str
    assert "b: 2" in result_str
    print("Тест 9 пройден")

    print("\nТест 10: Большое количество элементов")
    large_table = HashTable()
    for i in range(1000):
        large_table.put(f"key_{i}", f"value_{i}")
    for i in range(1000):
        assert large_table.get(f"key_{i}") == f"value_{i}"
    assert len(large_table) == 1000
    print("Тест 10 пройден")

    print("\nТест 11: None значения")
    table_none = HashTable()
    table_none.put("test", None)
    assert table_none.get("test") is None
    assert "test" in table_none
    table_none.put("key1", None)
    table_none.put("key2", "not None")
    table_none.put("key3", None)
    assert "key1" in table_none
    assert "key2" in table_none
    assert "key3" in table_none
    assert "key4" not in table_none
    assert table_none.get("key1") is None
    assert table_none.get("key2") == "not None"
    assert table_none.get("key3") is None
    assert table_none.get("key4") is None
    print("Тест 11 пройден")

test_hash_table()