from SinglyLinkedList import SinglyLinkedList

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
