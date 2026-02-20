class stack : 
    def __init__(self , k = 10):
        self.stack=[]
        self.k = k

    def push(self , x):
        if len(self.stack) >= self.k:
           print("stack is full")
           return -1
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0 :
            print("stack is empty")
            return -1
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0 :
            print("stack is empty")
            return -1
        return self.stack[-1]

     def display(self):
        print(self.stack)

    def find(self,x):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
           print(i)

    def find1(self,x):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
           print(i)
           return

    def find2(self,x):
    for i in range(len(self.stack)-1,-1,-1) :
        if self.stack[i] == x :
            print(i)
            return

    def replace(self,x,y):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
            self.stack[i]=y
                                


s=stack
s.push(10)
s.push(20)
s.pop()
s.replace(10,30)
s.find(30)
s.display()