class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class List:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__length = 0

    def __str__(self):
        if self.__first is not None:
            elem = self.__first
            out = "[" + str(elem.value)
            while elem.next is not None:
                elem = elem.next
                out += ", " + str(elem.value)
            return out + "]"
        else:
            return "[]"

    def push(self, value):
        self.__length += 1
        if self.__first is None:
            self.__first = self.__last = Node(value)
        else:
            self.__last.next = self.__last = Node(value)

    def add(self, value, place):
        if place > self.__length + 1:
            raise IndexError
        elif place == 0:
            self.__length += 1
            self.__first = Node(value, self.__first)
        elif place == self.__length + 1:
            self.__length += 1
            self.__last.next = self.__last = Node(value)
        else:
            self.__length += 1
            elem = self.__first
            for i in range(1, place):
                elem = elem.next
            elem.next = Node(value, elem.next)

    def remove(self, i):
        if self.__first is None:
            return
        else:
            if i > self.__length:
                raise IndexError
            else:
                self.__length -= 1
                current = self.__first
                for k in range(i-1):
                    current = current.next
                current.next = current.next.next

    def __getitem__(self, item):
        if item > self.__length - 1:
            raise IndexError
        else:
            count = 0
            if self.__first is not None:
                current = self.__first
                while count != item:
                    current = current.next
                    count += 1
                return current.value

    def __setitem__(self, key, value):
        if key > self.__length + 1:
            raise KeyError
        elif key == self.__length + 1:
            self.__last.next = self.__last = Node(value)
        else:
            count = 0
            if self.__first is not None:
                current = self.__first
                while count != key:
                    current = current.next
                    count += 1
                current.value = value

    def clear(self):
        self.__init__()

    def __len__(self):
        return self.__length

    def __add__(self, other):
        if self.__first and other.__first is not None:
            self.__length += other.__length
            self.__last.next = self.__last = other.__first
            self.__last = other.__last
            return self
        elif self.__first is None:
            return other
        elif other.__first is None:
            return self


