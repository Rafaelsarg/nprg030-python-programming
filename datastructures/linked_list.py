class Node:
    def __init__(self, val, next = None) :
        self.val = val 
        self.next = next

class LinkedList:
    def __init__(self,ls):
        self.head = None
        for i in reversed(ls):
            self.head = Node(i, self.head)

        
    def to_list(self):
        temp = self.head
        list_ = []
        while temp: 
            list_.append(temp.val)
            temp = temp.next

        return list_    

    def len(self):
        temp = self.head
        count = 0
        while temp: 
            count += 1
            temp = temp.next

        return count    

    def get(self,n):  
        temp = self.head
        count = 0
        while temp:
            if(count == n):
                return temp.val

            temp = temp.next
            count += 1    

    def has(self, x):
        temp = self.head
        while temp:
            if(temp.val == x):
                return True 

            temp = temp.next    

        return False        
    
    def delete(self, x):
        temp = self.head
        if self.head == None:
            return 
        if(temp.val == x):
            self.head = self.head.next  

        while temp.next:
            if(temp.next.val == x):
                temp.next = temp.next.next
                return
            temp = temp.next    



    def rotate(self):
        temp = self.head
        prev = None

        while not temp or not temp.next:
            return

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None

        temp.next = self.head
        self.head = temp    

        


    def starts_with(self,m):
        temp = self.head
        a = m.head

        if(LinkedList.len(m) > LinkedList.len(self)):
            return False

        for i in range(0,LinkedList.len(m)):
            if(temp.val != a.val):
                return False

            temp = temp.next
            a = a.next

        return True        

    def contains(self,m):
        temp = self.head
        a = m.head

        if(m.head == None):
            return True
        difference = LinkedList.len(self) - LinkedList.len(m)
            
        if(difference < 0):
            return False

        for i in range(0,difference + 1):
            contains_ = True
            if(temp.val == a.val):
                temp_test = temp
                a_test = a
                for j in range(0,LinkedList.len(m)):
                    if(temp_test.val != a_test.val):
                        contains_ = False
                        
                    temp_test = temp_test.next
                    a_test = a_test.next    
                if(contains_ == True):
                    return True

            temp = temp.next    
           

        return False

    def ends_with(self,m):
        temp = self.head
        a = m.head

        if(self.head == None and m.head != None):
            return False
        len_ = LinkedList.len(self) - LinkedList.len(m)

        if(len_ < 0):
            return False

        for i in range(0,len_):
            temp = temp.next

        for i in range(len_,LinkedList.len(self)):
            if(temp.val != a.val):
                return False

        return True       



