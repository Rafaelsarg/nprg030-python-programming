import sys

def my_hash(s):
    h = 0
    for c in s:
        h = (h * 1_000_003 + ord(c)) % (2 ** 32)
    return h 


class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class HashMap:
    def __init__(self, numBuckets = 5):
        self.a = numBuckets * [None]
        self.count = 0


    def contains(self, x, ):
        i = my_hash(x) % len(self.a)     
        p = self.a[i]
        while p != None:
            if p.key == x:
                return True
            p = p.next
        return False

    def add(self, x, x_val):
        if not self.contains(x):
            i = my_hash(x) % len(self.a)
            self.a[i] = Node(x,x_val, self.a[i])
            self.count += 1

        else:
            i = my_hash(x) % len(self.a)
            parent=None
            n=self.a[i]
            while n:
                if n.key==x and parent==None:
                    self.a[i].val = x_val
                    return
                elif n.key==x:
                    parent.next.val = x_val
                    return
                parent=n
                n=n.next
            
    def set(self, x, x_val):
        self.add(x, x_val)

        l1 = []
        if(self.count / len(self.a) > 4):
            l1 = self.a.copy()
            self.a += [None] * len(self.a)
            for i in range(0,len(l1)):
                p = l1[i]
                while p != None:
                    self.remove(p.key, True)
                    self.add(p.key, p.val)
                    p = p.next
            print(f'resizing to {len(self.a)} buckets')        


                


    def get(self, x):
        i = my_hash(x) % len(self.a)     
        p = self.a[i]
        while p != None:
            if p.key == x:
                a =  p.val
                self.remove(p.key)
                return a
            p = p.next
        return None

  

    def remove(self,x, resizing = False):
        if(resizing == True):
            i = my_hash(x) % (len(self.a)//2)   
            
        else:
            i = my_hash(x) % len(self.a)  

        p = self.a[i]
        if(p == None):
            return None

        if(p.key == x):
            self.a[i] = p.next
            self.count -= 1
            return 

        if(p.next == None):
            self.a[i] = None
            self.count -= 1
            return
        g = p.next

        while g != None:
            if g.key == x:
                p.next = g.next
                self.count -= 1
                return
            p = g
            g = g.next

    def unique_count(self):
        return self.count

