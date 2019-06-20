class Node:
    def __init__(self, data):
        self.Data = data
        self.next = None
        self.prev = None

    def getNode(self):
        return self.Data

class List:
    def __init__(self):
        self.__first = None
        self.__last = None

    def isEmpty(self):
        if self.__first == None:
            return True

    def insert(self, data):
        temp = Node(data)
        if self.isEmpty() == True:
            self.__first = temp
            self.__last = temp
        else:
            self.__last.next = temp
            temp.prev = self.__last
            self.__last = temp

    def show(self):
        node = self.__first
        while (node != None):
            print(node.Data, end=" ")
            node = node.next
        print("\n")

