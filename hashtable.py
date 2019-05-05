class Hashtable:
    def __init__(self, size):
        self.__size = size
        self.__hashtable = [[None]] * self.__size
        self.__start_size = size

    def __str__(self):
        out = "["
        for i in range(0, self.__size):
            if self.__hashtable[i] == [None]:
                out += " None"
            else:
                out += " " + str(self.__hashtable[i][0]) + ": " + str(self.__hashtable[i][1]) + ";"
        return out + "]"

    def __hash_function(self, key):
        return len(str(key)) % self.__start_size

    def add(self, key, value):
        hash_key = self.__hash_function(key)
        if self.__hashtable[hash_key] == [None]:
            self.__hashtable[hash_key] = [key, value]
        else:
            if self.__hashtable[hash_key][0] == key:
                self.__hashtable[hash_key][1] = value
            else:
                while hash_key < self.__size-1:
                    if self.__hashtable[hash_key] != [None]:
                        hash_key += 1
                    else:
                        self.__hashtable[hash_key] = [key, value]
                        return
                else:
                    self.__size += 1
                    self.__hashtable.append([key, value])

    def search(self, key):
        hash_key = self.__hash_function(key)
        if self.__hashtable[hash_key] == [None]:
            raise KeyError
        elif self.__hashtable[hash_key][0] == key:
            return self.__hashtable[hash_key][1]
        else:
            while hash_key < self.__size:
                if self.__hashtable[hash_key] == [None] or self.__hashtable[hash_key][0] != key:
                    hash_key += 1
                elif self.__hashtable[hash_key][0] == key:
                    return self.__hashtable[hash_key][1]
            return

    def remove(self, key):
        hash_key = self.__hash_function(key)
        if self.__hashtable[hash_key] == [None]:
            return
        elif self.__hashtable[hash_key][0] == key:
            self.__hashtable[hash_key] = [None]
            return
        else:
            while hash_key < self.__size:
                if self.__hashtable[hash_key] == [None] or self.__hashtable[hash_key][0] != key:
                    hash_key += 1
                elif self.__hashtable[hash_key][0] == key:
                    self.__hashtable[hash_key] = [None]
            return
