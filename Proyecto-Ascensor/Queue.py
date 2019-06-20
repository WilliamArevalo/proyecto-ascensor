class Node(object):

    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    # Method for setting the data
    def setData(self, data):
        self.data = data

    # Method for getting the data
    def getData(self):
        return self.data

    # Method for setting the next
    def setNext(self, next):
        self.next = next

    # Method for getting the next
    def getNext(self):
        return self.next

    # return true if thenode point to another node
    def hasNext(self):
        return self.next != None


class QueueLinkedListsCircular(object):

    def __init__(self):
        self.front = None
        self.lastNode = None
        self.rear = None
        self.size = 0

    def enQueueUP(self, data):
        temp = Node(data)

        if self.front is None:
            self.front = temp
            self.lastNode = self.front

        elif temp.data < self.front.data:
            self.front.prev = temp
            temp.next = self.front
            self.front = temp

        else:
            temp.prev = self.front
            temp.next = self.front.next
            self.front.next.prev = temp
            self.front.next = temp
            for i in range(0, self.size):
                if temp.data > temp.next.data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = temp.next.next
                    temp.next.prev.next = temp
                    temp.prev = temp.next.prev
                    temp.next.prev = temp

        self.size +=1


    def enQueueDown(self, data):
        temp = Node(data)

        if self.front is None:
            self.front = temp
            self.lastNode = self.front

        elif temp.data > self.front.data:
            self.front.prev = temp
            temp.next = self.front
            self.front = temp
        else:
            temp.prev = self.front
            temp.next = self.front.next
            self.front.next.prev = temp
            self.front.next = temp
            for i in range(0, self.size):
                if temp.data > temp.prev.data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    temp.next = temp.next.next
                    temp.next.prev.next = temp
                    temp.prev = temp.next.prev
                    temp.next.prev = temp


        self.size +=1


    def deQueue(self):
        if self.front is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        result = self.front.getData()
        self.front = self.front.next
        self.size -=1
        return result

    def queueRear(self):
        if self.rear is None:
            print('Sorry, the queue is empty..!')
            raise IndexError
        return self.rear.getData()

    def queueFront(self):
        if self.front is None:
            print('Sorry, the queue is empty')
            raise IndexError
        return self.front.getData()

    def size(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True

    def printList(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next


e = QueueLinkedListsCircular()
e.enQueueUP(9)
e.enQueueUP(10)
e.enQueueUP(4)
e.enQueueUP(8)
e.enQueueUP(7)
e.printList()
print(' ')
q = QueueLinkedListsCircular()
q.enQueueDown(9)
q.enQueueDown(5)
q.enQueueDown(4)
q.enQueueDown(7)
q.enQueueDown(8)
q.printList()