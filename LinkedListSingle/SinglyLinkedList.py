from LinkedListSingle.Node import Node


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        length = 0
        if self.head:
            current = self.head
            while current:
                length += 1
                current = current.next
        return length

    def len_rec(self, current):
        if not current:
            return 0
        if current:
            return self.len_rec(current.next) + 1

    def recursive_len(self):
        if self.head:
            return self.len_rec(self.head)
        else:
            return 0

    def insert_at_end(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def insert_at_front(self, data):
        node = Node(data)
        if self.head:
            temp = self.head
            self.head = node
            self.head.next = temp
        else:
            self.head = node
            self.tail = node

    def delete_key(self, key):
        """
        deletes first occurrence of key in list
        :param key: to delete
        :return: None
        """

        # can only delete if head exists
        if self.head:
            # if head is to be deleted
            if self.head.data == key:

                # store current head in temp
                temp = self.head

                # point current head to the next node of head
                self.head = temp.next

                # update the tail
                if self.tail == temp:
                    self.tail = self.head

                # delete the temp
                del temp

            # if some other node is to be deleted
            else:
                # traverse till the prev node of the key to be deleted
                current = self.head
                while current.next:
                    if current.next.data == key:
                        temp = current.next
                        current.next = temp.next

                        # update the tail
                        if self.tail == temp:
                            self.tail = current

                        del temp
                        break
                    current = current.next

    def search(self, key):
        """

        searches for a key
        :param key: to search for
        :return: True if exists, else False
        """
        found = False
        if self.head:
            current = self.head
            while current:
                if current.data == key:
                    found = True
                current = current.next
            return found
        else:
            return 'list empty'

    def recursive_search(self, key):
        """
        searches for a key recursively
        :param key: to search for
        :return: True if exists, else False
        """
        def search_rec(current, key):
            if not current:
                return False
            if current.data == key:
                return True
            return search_rec(current.next, key)
        if self.head:
            return search_rec(self.head, key)

    def get_n(self, n):
        """
        search for nth node in the LL
        :param n: position to search
        :return: element at nth position, -1 if invalid
        """
        found = -1
        if self.head:
            curr_pos = 0
            current = self.head
            while current:
                if curr_pos == n-1:
                    return current.data
                curr_pos += 1
                current = current.next
            return found
        else:
            return found

    def get_n_end(self, n):
        """
        get nth node from end
        :param n: position
        :return: nth element from end, -1 if invalid
        """

        # if LL contains atleast one element
        if self.head:
            fast_node = self.head
            slow_node = self.head
            curr_fast = 0

            # move fast node by n-1 amount
            while curr_fast < n:
                fast_node = fast_node.next

                # if n > len, break
                if fast_node:
                    curr_fast += 1
                else:
                    return -1

            # n was smaller than length. now increment both nodes till end of list by 1
            while fast_node.next:
                fast_node = fast_node.next
                slow_node = slow_node.next

            return slow_node.data

        # if LL is empty
        else:
            return -1

    def detect_loop(self):
        """
        detects a loop using Floyd's Cycle finding algorithm
        Check this link for proof: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
        :return: True if loop exists, else False. Returns loop length also
        """

        if self.head:
            fast_node = self.head
            slow_node = self.head
            loop_length = -1
            while fast_node.next.next:
                fast_node = fast_node.next.next
                slow_node = slow_node.next
                if fast_node == slow_node:
                    fast_node = fast_node.next
                    loop_length = 1
                    while fast_node != slow_node:
                        fast_node = fast_node.next
                        loop_length += 1
                    return True, loop_length
            return False, loop_length
        else:
            return False, -1

    def palindrome(self):
        """
        TODO: checks if list is a palindrome
        :return: True if it is, False otherwise
        """
        if self.head:
            pass
        else:
            return False

    def delete_sorted_duplicate(self):
        """
        deletes all but one occurrences of duplicate elements from sorted list.
        :return: None
        """
        if self.head:
            current = self.head
            while current.next:
                if current.data == current.next.data:
                    temp = current.next
                    current.next = temp.next
                    if self.tail == temp:
                        self.tail = current
                    del temp
                else:
                    current = current.next

    def reverse(self):
        """
        reverse list non-recursively
        :return: None
        """
        if self.head:
            current = self.head
            self.tail = self.head
            prev = None
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            self.head = prev
        else:
            print('list empty')

    def sorted_intersect_decreasing(self, l2):
        """
        given 2 sorted lists in decreasing order, construct another list which intersection of 1st two
        CAUTION: current list has to be a sorted list
        :param l2: 2nd sorted list with which current has to be intersected
        :return: 3rd list which is intersection of 1st two
        """

        if self.head:
            new_L = SinglyLinkedList()
            c1 = self.head
            c2 = l2.head
            while c1 and c2:
                if c1.data == c2.data:
                    new_L.insert_at_end(c1.data)
                    c1 = c1.next
                    c2 = c2.next
                elif c1.data > c2.data: # change sign to '<' if increasingly sorted
                    c1 = c1.next
                elif c2.data > c1.data: # change sign to '<' if increasingly sorted
                    c2 = c2.next
            return new_L
        else:
            print('current list empty')


