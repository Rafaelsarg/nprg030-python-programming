class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.ls = [None] * size
        self.head = 0 
        self.tail = -1 
        self.countnum = 0
        self.sum = 0

        

    def enqueue(self, n):

        ls_ = []
        if(self.tail == self.size - 1 and self.ls[0] == None):
            self.tail = 0
            self.ls[self.tail] = n
            self.countnum += 1
            self.sum += n


        else:
            self.tail += 1
            self.ls[self.tail] = n
            self.countnum += 1
            self.sum += n

        if(self.countnum == self.size):
            self.ls += [None] * self.size
            if(self.tail < self.head):
                ls_ = self.ls[self.head:self.size].copy()
                self.ls[self.head:self.size] = [None for i in self.ls[self.head:self.size-1]]
                self.ls[self.size*2 - len(ls_): self.size*2 ] =  ls_
                self.head = self.head + self.size 
            self.size = self.size * 2
            print('Resized to ' + str(self.size) + ' elements')
               
        
         
        

    def dequeue(self):
        self.sum -= self.ls[self.head]
        k = self.ls[self.head]
        self.ls[self.head] = None
        if(self.head+1 == self.size):
            self.head = 0
        else:

            self.head += 1
        self.countnum -= 1
        
        return k

    def count(self):
        return self.countnum
        


    def avg(self):
        return self.sum/self.countnum

