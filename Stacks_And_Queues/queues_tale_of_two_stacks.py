class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    
    def peek(self):
        self.move_item()
        return self.stack2[len(self.stack2)-1]
        
        
    def pop(self):
        self.move_item()
        return self.stack2.pop()
         
        
        
        
    def put(self, value):
        self.stack1.append(value)
        
    def move_item(self):
        if len(self.stack2) == 0:
            #while len(self.stack1) > 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())            
        return           
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())