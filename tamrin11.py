
class node :
    def __init__(self , d):
        self.data = d
        self.next = None

class linked_list :
    def __init__(self):
        self.head = None

    def insert_frist(self , x):
        if self.head == None:
            self.head = node(x)
        else:
            a = node(x)
            a.next = self.head
            self.head = a

    def insert_last(self , x):
        if self.head is None:
            self.head = node(x)
        else:
            a = node(x)
            t = self.head
            while t.next:
                t = t.next
            t.next = a

    def insert_after(self , x, y):
        if self.head is None:
            print("list is empty")
        else:
            t= self.head
            while t:
                if t.data == x:
                    t= node(y)
                    a.next = t.next
                    t.next = a
                t = t.next
            print("none")

    def insert_before(self , x, y):
        if self.head is None:
            print("list is empty")
            return
        if self.head.Data == x:
            self.insert_frist(y)
            return
        while t.next:
            if t.next.data == x:
                a = node(y)
                a.next = t.next
                t.next = a
                return
            t= t.next
        print("none")
                                                                                                                                              
