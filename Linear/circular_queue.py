class Queue:

    def __init__(self,size):
        self.size = size
        self.queue = [None]* self.size
        self.rear = -1
        self.front = -1

    def enqueue(self,value):

        ## Overflow Check
        if (self.rear + 1) %  self.size == self.front:
            print("Queue Overflow")
            return

        ## Inset
        else:
            if self.rear == -1 and self.front == -1:
                self.rear = 0
                self.front = 0 
            else:
                self.rear = (self.rear + 1) % self.size

            self.queue[self.rear] = value 
            print("Value Inserted Sucessfully")

    def dequeue(self):

        ## Underflow Check
        if self.rear == -1 and self.front == -1:
            print("Queue is empty")

        ## Delete
        else:
            n = self.queue[self.front]
            print("Sucessfully deleted")
            if self.front == self.rear:
                self.front == -1
                self.rear == -1
            else:
                self.front = (self.front + 1) % self.size

    def print_parameter(self):
        print(f"Rear is at {self.rear}th index")
        print(f"Front is at {self.front}th index")

    def display(self):

        ## Empty queue
        if self.front == -1 and self.rear == -1:
            print('Qeueue is Empty')

        else:
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size


queue = Queue(8)


queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)

queue.display()

queue.print_parameter()

queue.dequeue()
queue.dequeue()

queue.display()
queue.print_parameter()


