class Queue:
    def __init__(self ,k= 10):
        self.list=[]* k
        self.front = -1
        self.rear = -1

    def insert(self,x):
        if self.rear >= len(self.list) -1 :
            print("full")
            return

        elif self.front == -1 :
            self.front=0
            self.rear=0
            self.list[self.rear] = x
            return
        else:
         self.rear+= 1
         self.list[self.rear] = x

    def delete(self):
        if self.front == -1 :
            print("empty")
            return

        elif  self.front == self.rear :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        else:
         k = self.list[self.front]
         self.front+= 1
         return k

    def display(self):
        if self.front == -1 :
            print("empty")
            return
        else:
            print(self.Queue)


x=Queue()
x.insert(1)
x.insert(2)
x.delete()
x.display()






class Cqueue:
    def __init__(self, k):
        self.list = [] * k
        self.front = -1
        self.rear = -1

    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("full")
            return

        elif  self.front == -1:
            self.front = 0
            self.rear = 0
            self.list[0] = x
            return
        else:
         self.rear=(self.rear +1) % len(self.list)
         self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("empty")
            return
        elif self.front == self.rear:
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        else:
         k = self.list[self.front]
         self.front = (self.front +1) % len (self.list)
         return k

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear +1) % len (self.list) == self.front
    
    def display(self):
        if self.front == -1 :
            print("empty")
            return
        else:
            print(self.Cqueue)

y=Cqueue()
y.insert(1)
y.insert(2)
y.insert(3)
y.delete()
y.is_empty()
y.display()

