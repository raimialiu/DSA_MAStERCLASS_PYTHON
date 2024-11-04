from .LinkedNode import LinkedNode


class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__pointer = None

    def push(self, item):
        if self.__head is None and self.__tail is None:
            new_item = LinkedNode(item)
            self.__head = self.__pointer = self.__tail = new_item
        else:
            if self.__head is not None and self.__tail is not None:
                new_node = LinkedNode(item) #0, 2, 3
                tail = self.__tail
                self.__tail = new_node
                tail.next = self.__tail



