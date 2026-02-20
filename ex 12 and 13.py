class dnode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class dlinked_list:
    def __init__(self):
        self.head = None

    def Infirst(self, x):
        n = dnode(x)
        if self.head is not None:
            n.next = self.head
            self.head.prev = n
        self.head = n

    def Inlast(self, x):
        if self.head is None:
            self.In_first(x)
            return
        t = self.head
        while t.next:
            t = t.next
        n = dnode(x)
        t.next = n
        n.prev = t

    def Inafter(self, x, y):
        if self.head is None:
            print("no list")
            return
        t = self.head
        while t:
            if t.data == x:
                if t.next is None:
                    self.In_last(y)
                    return
                n = dnode(y)
                n.next = t.next
                n.prev = t
                t.next.prev = n
                t.next = n
                return
            t = t.next
        print("none")

    def Inbefore(self, x, y):
        if self.head is None:
            print("no list")
            return
        t = self.head
        while t:
            if t.data == x:
                if t.prev is None:
                    self.In_first(y)
                    return
                n = dnode(y)
                n.next = t
                n.prev = t.prev
                t.prev.next = n
                t.prev = n
                return
            t = t.next
        print("none")

    def delfirst(self):
        if self.head is None:
            print("no list")
            return
        t = self.head
        self.head = t.next
        if self.head:
            self.head.prev = None
        del t

    def dellast(self):
        if self.head is None:
            print("error")
            return
        t = self.head
        while t.next:
            t = t.next
        if t.prev is None:
            self.del_first()
            return
        t.prev.next = None
        del t

    def delbefore(self, x):
        if self.head is None:
            print("no list")
            return
        if self.head.data == x:
            print("error")
            return
        t = self.head.next
        while t:
            if t.data == x:
                n = t.prev
                if n.prev:
                    n.prev.next = t
                    t.prev = n.prev
                else:
                    self.head = t
                    t.prev = None
                del n
                return
            t = t.next
        print("not found")

    def del_after(self , x):
        if self.head is None:
            print("no list")
            return
        t= self.head
        while t:
            if t.data == x:
                if t.next :
                    n = t.next
                    t.next = n.next
                    if n.next:
                        n.next.prev = t
                    del n
                    return
                print("error")
                return
            t = t.next
            print("none")

    def del_x(self , x):
        if self.head is None:
            print("no list")
            return
        t = self.head
        while t:
            if t.data == x:
                if t.next is None:
                    self.del_last()
                    return
                t.prev.next = t.next
                t.next.prev = t.prev
                del t
                return
            t = t.next
            print("none")




