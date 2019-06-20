class StackSimpleArray(object):

    def __init__(self, limit=99):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def size(self):
        return len(self.stk)

    def push(self, item):

        if len(self.stk) >= self.limit:
            print(' Stack Overflow !')
        else:
            self.stk.append(item)

    def pop(self):
        if len(self.stk) <= 0:
            print(' Stack Underflow !')
            return 0
        else:
            return self.stk.pop(0)

    def peek(self):
        if len(self.stk) < 0:
            print(' Stack Underflow !')
            return 0
        else:
            return self.stk[-1]

    def find(self):
        print(self.stk)

    def Sort(self):
        return self.stk.sort()

    def SortReverse(self):
        return self.stk.sort(reverse=True)


q = StackSimpleArray(10)
q.find()