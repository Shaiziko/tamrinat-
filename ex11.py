
class node :
    def __init__(self , d):
        self.data = d
        self.next = None

class linked_list :
    def __init__(self):
        self.head = None

    def infirst(self , x):
        if self.head == None:
            self.head = node(x)
        else:
            n = node(x)
            n.next = self.head
            self.head = n

    def inlast(self , x):
        if self.head is None:
            self.head = node(x)
        else:
            n = node(x)
            t = self.head
            while t.next:
                t = t.next
            t.next = a

    def inafter(self , x, y):
        if not self.head :
            print("empty")
        else:
            t= self.head
            while t:
                if t.data == x:
                    n= node(y)
                    n.next = t.next
                    t.next = n
                t = t.next
            print("none")

    def inbefore(self , x, y):
        if not self.head :
            print("empty")
            return
        if self.head.Data == x:
            self.insert_frist(y)
            return
        while t.next:
            if t.next.data == x:
                n= node(y)
                n.next = t.next
                t.next = n
                return
            t= t.next
        print("none")
                                                                                                                                              
