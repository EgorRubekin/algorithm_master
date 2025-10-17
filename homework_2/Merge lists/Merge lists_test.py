def test_merge_lists():
 

    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([1, 3, 4])
    result = merge_two_lists(list1, list2)
    assert linkedlist_to_list(result) == [1, 1, 2, 3, 4, 4]
    print("Тест 1 пройден")
    

    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([1, 3, 4])
    result = merge_two_lists(list1, list2)
    assert linkedlist_to_list(result) == [1, 3, 4]
    print("Тест 2 пройден")
    

    list1 = list_to_linkedlist([1, 2, 4])
    list2 = list_to_linkedlist([])
    result = merge_two_lists(list1, list2)
    assert linkedlist_to_list(result) == [1, 2, 4]
    print("Тест 3 пройден")
    

    list1 = list_to_linkedlist([])
    list2 = list_to_linkedlist([])
    result = merge_two_lists(list1, list2)
    assert linkedlist_to_list(result) == []
    print("Тест 4 пройден")



test_merge_lists()

