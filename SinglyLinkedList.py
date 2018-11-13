from Node import Node


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
        def search_rec(current, key):
            if not current:
                return False
            if current.data == key:
                return True
            return search_rec(current.next, key)
        if self.head:
            return search_rec(self.head, key)
