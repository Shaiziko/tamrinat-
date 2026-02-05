class dnode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None


class dlinked_list:
    def __init__(self):
        self.head = None

    def In_first(self, x):
        a = dnode(x)
        if self.head is not None:
            a.next = self.head
            self.head.prev = a
        self.head = a

    def In_last(self, x):
        if self.head is None:
            self.In_first(x)
            return
        t = self.head
        while t.next:
            t = t.next
        a = dnode(x)
        t.next = a
        a.prev = t

    def In_after(self, x, y):
        if self.head is None:
            print("error")
            return
        t = self.head
        while t:
            if t.data == x:
                if t.next is None:
                    self.In_last(y)
                    return
                a = dnode(y)
                a.next = t.next
                a.prev = t
                t.next.prev = a
                t.next = a
                return
            t = t.next
        print("none")

    def In_before(self, x, y):
        if self.head is None:
            print("no list")
            return
        t = self.head
        while t:
            if t.data == x:
                if t.prev is None:
                    self.In_first(y)
                    return
                a = dnode(y)
                a.next = t
                a.prev = t.prev
                t.prev.next = a
                t.prev = a
                return
            t = t.next
        print("none")

    def del_first(self):
        if self.head is None:
            print("no list")
            return
        t = self.head
        self.head = t.next
        if self.head:
            self.head.prev = None
        del t

    def del_last(self):
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

    def del_before(self, x):
        if self.head is None:
            print("no list")
            return
        if self.head.data == x:
            print("error")
            return
        t = self.head.next
        while t:
            if t.data == x:
                a = t.prev
                if a.prev:
                    a.prev.next = t
                    t.prev = a.prev
                else:
                    self.head = t
                    t.prev = None
                del a
                return
            t = t.next
        print("x not found")

                                                   




