from LinkedListSingle.SinglyLinkedList import SinglyLinkedList

if __name__ == '__main__':

    ll = SinglyLinkedList()

    # inserting head
    ll.insert_at_end(5)
    print('current_items: ', [node for node in ll])

    # inserting at end
    ll.insert_at_end(4)
    print('after_insertion: ', [node for node in ll])

    # inserting at front
    ll.insert_at_front(3)
    print('after_insertion: ', [node for node in ll])

    # delete head
    ll.delete_key(3)
    print('after_deletion: ', [node for node in ll])

    # insert at end
    ll.insert_at_end(10)
    print('after_insertion: ', [node for node in ll])

    # delete head
    ll.delete_key(5)
    print('after_deletion: ', [node for node in ll])

    # delete tail
    ll.delete_key(10)
    print('after_deletion: ', [node for node in ll])

    # delete non-existent key
    ll.delete_key(15)
    print('after_deletion: ', [node for node in ll])

    # recursve length
    print('recursive_length: ', ll.recursive_len())

    # insert at end
    ll.insert_at_end(10)
    print('after_insertion: ', [node for node in ll])
    ll.recursive_len()
    print('recursive_length: ', ll.recursive_len())

    # search for given key
    print('searching for 10: ', ll.search(10))
    print('searching for 15: ', ll.search(15))
    print('searching for 10 recursively: ', ll.recursive_search(10))
    print('searching for 15 recursively: ', ll.recursive_search(15))

    # search for nth element
    print('searching for 2nd element: ', ll.get_n(2))
    print('searching for 1st element: ', ll.get_n(1))
    print('searching for 10th element: ', ll.get_n(10))


    # search from end
    ll.insert_at_end(11)
    print('after_insertion: ', [node for node in ll])
    print('1st element from last: ', ll.get_n_end(0))
    print('2nd element from end : ', ll.get_n_end(1))
    print('3rd element from end : ', ll.get_n_end(2))
    print('4th element from end : ', ll.get_n_end(3))

    # test loop detection
    ll_loop = SinglyLinkedList()
    ll_loop.insert_at_end(5)
    ll_loop.insert_at_end(10)
    ll_loop.insert_at_end(15)
    ll_loop.insert_at_end(20)
    print('after insertion in looped list: ', [node for node in ll_loop])
    print('Loop before introducing loop: ', ll_loop.detect_loop())
    ll_loop.tail.next = ll_loop.head
    print('Loop after introducing loop: ', ll_loop.detect_loop())
    ll_loop.tail.next = None

    # test sorted deletion
    ll_sorted = SinglyLinkedList()
    ll_sorted.insert_at_end(1)
    ll_sorted.insert_at_end(2)
    ll_sorted.insert_at_end(3)
    ll_sorted.insert_at_end(4)
    ll_sorted.insert_at_end(4)
    print('after insertion in sorted list: ', [node for node in ll_sorted])
    ll_sorted.delete_sorted_duplicate()
    print('after deletion in sorted list: ', [node for node in ll_sorted])

    # reversing list
    ll_reverse = SinglyLinkedList()
    ll_reverse.insert_at_end(1)
    ll_reverse.insert_at_end(2)
    ll_reverse.insert_at_end(3)
    ll_reverse.insert_at_end(4)
    ll_reverse.insert_at_end(5)
    print('after insertion in list to be reversed: ', [node for node in ll_reverse])
    ll_reverse.reverse()
    print('after reversing the list: ', [node for node in ll_reverse])

    # sorted intersection
    ll_intersect = SinglyLinkedList()
    ll_intersect.insert_at_end(3)
    ll_intersect.insert_at_end(2)
    ll_intersect.insert_at_end(1)
    print('original list: ', [node for node in ll_reverse])
    print('list to be intersected: ', [node for node in ll_intersect])
    intersected_list = ll_reverse.sorted_intersect_decreasing(ll_intersect)
    print('intersected list: ', [node for node in intersected_list])
