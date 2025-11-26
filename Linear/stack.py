"""
Stack in an ordered list that allows insertion and deletion of elements from one end known as 'Top' . It follows LIFO ---Last In First Out--- principle.
It alows 3 opearations Push, Pop, Display.
"""

class Stack:
    def __init__(self,size):
        self.stack = [None]*size
        self.top = -1

    def push_value(self,value):
        
        ## overflow check
        if self.top == len(self.stack)-1:
            print("Stack overflow")
            return
        
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Sucessfully inserted")

    def print_top(self):
        print(self.top)
    
    def pop_value(self):

        # underflow check
        if self.top < 0:
            print("Stack Underflow")
            return

        else:
            del(self.stack[self.top])
            self.top = self.top -1
            print("Sucessfully deleted")


    def display_stack(self):
        for i in range(0,len(self.stack)):
            print(self.stack[i],)


stack1 = Stack(8)

stack1.push_value(5)
stack1.push_value(10)
stack1.push_value(15)
stack1.push_value(20)
stack1.push_value(25)

stack1.print_top()

stack1.display_stack()

stack1.pop_value()

stack1.print_top()

stack1.display_stack()
        

