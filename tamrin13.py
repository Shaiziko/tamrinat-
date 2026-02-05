class dnode():
    def __init__(self , x):
        self.Data = x
        self.next = None
        self.prev = None


class dlinked_list :
    def __init__(self):
        self.head = None

    def del_after(self , x):
        if self.head is None:
            print("no list")
            return
        t= self.head
        while t:
            if t.data == x:
                if t.next :
                    a = t.next
                    t.next = a.next
                    if a.next:
                        a.next.prev = t
                    del a
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
            