class stack : 
    def __init__(self , limit = 100):
        self.stack=[]
        self.limit = limit
    def push(self , x):
        if len(self.stack) >= self.limit:
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


s= stack(10)
s.push(5)
s.push(121)
s.push(-1)
p=test.peek()




#ایندکس(x) های درون پشته را برگرداند.
def find(self,x):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
           print(i)


#اولین ایندکس شامل  (x) را برگرداند
def find1(self,x):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
           print(i)
           return


# چاپ اخرین ایندکس شامل x
def find2(self,x):
    for i in range(len(self.stack)-1,-1,-1) :
        if self.stack[i] == x :
            print(i)
            return
def find2_n(self,x):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
            p=i
    print(p)                


def find2_n(self,x):
    list=[]
    for i in range(len(self.st)):
        if self.stack[i] == x :
            list.append(i)
    print(list[2])


def replace(self,x,y):
    for i in range(len(self.stack)):
        if self.stack[i] == x :
            self.stack[i]=y
                                
