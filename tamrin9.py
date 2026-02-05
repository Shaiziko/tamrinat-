class Queue:
    def __init__(self ,k= 100):
        self.list=[None]* k
        self.front = -1
        self.rear = -1
    def insert(self,x):
        if self.rear >= len(self.list) -1 :
            print("Queue is Full")
            return

        elif self.front == -1 :
            self.front=0
            self.rear=0
            self.list[self.rear] = x
            return
        else:
         self.rear+= 1
         self.list[self.rear] = x

    def Del(self):
        if self.front == -1 :
            print("Queue is empty")
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
    


q = Queue(3)
q.insert(5)
q.insert(32)
q.insert(4)
q.insert(9)
q.Del()
q.insert(39)





class C_Queue:
    def __init__(self, k):
        self.list = [] * k
        self.front = -1
        self.rear = -1

    def  insert(self , x):
        if (self.rear +1) % len(self.list) == self.front:
            print("Queue is full")
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
            print("Queue is empty")
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
    
    

