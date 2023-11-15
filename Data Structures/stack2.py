class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
   
s= Stack()
s.push ( 3 ) 
s.push ( 5 )
s.push ( 2 )
s.push ( 15 )
s.push ( 42 )
s.pop ()
s.pop ()
s.push (14)
s.push (7)
s.pop()
s.push (9)
s.pop() 
s.pop()
s.push (51)
s.pop ()
s.pop()

print(s.items)