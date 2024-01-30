
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left      
        self.right = right    


def getCount(root_, lo, hi):

    if root_ == None:
            return 0

    if(root_.val == lo and root_.val == hi):
        return 1 

    if(root_.val <= hi and root_.val >= lo):
            return (1 + getCount(root_.left,lo,hi) + getCount(root_.right, lo,hi))

    elif root_.val < lo:
        return getCount(root_.right, lo, hi)


    else:
        return getCount(root_.left, lo, hi)
    pass

class TreeSet:
    def __init__(self):
        self.root = None
        self.size_ = 0
        self.maxValue = 0
        self.minValue = 0

    def replace(self, parent, n, p):
      if parent == None:      # n is the root
          self.root = p
      elif parent.left == n:  # n is the left child
          parent.left = p
      elif parent.right == n: # n is the right child
          parent.right = p
      else:
          assert False, 'not a child'    

    def contains(self, x):
        n = self.root
        while n != None:
            if x == n.val:
                return True
            if x < n.val:
                n = n.left
            else:
                n = n.right
        return False    

    def add(self, x):
      n = self.root
      if n == None:
          self.root = Node(x)
          self.size_ += 1
          return
      
      while True:
          if x == n.val:
              return         
          elif x < n.val:
              if n.left == None:
                  n.left = Node(x)
                  self.size_ += 1 
                  return
              else:
                  n = n.left
          else:   
              if n.right == None:
                  n.right = Node(x)
                  self.size_ += 1
                  return
              else:
                  n = n.right    

    def minVal_Node(self, root_):
        min_Node = root_
        parent_Node = None

        if root_ is None:
            return None
        
        while root_.left != None:
            parent_Node = root_
            min_Node = root_.left
            root_ = root_.left

        return min_Node, parent_Node  


    def remove(self, x):
        n = self.root
        parent = None

        if n is None:
            return n

        while n != None:
            if x < n.val:
                parent = n
                n = n.left

            elif x > n.val:
                parent = n
                n = n.right

            else:
                if(n.left == None and n.right == None):
                    self.replace(parent, n, None)
                    break

                elif(n.left == None):
                    self.replace(parent,n,n.right)
                    break
                elif(n.right == None):
                    self.replace(parent,n,n.left)
                    break
                else:
                    temp, parent_temp = self.minVal_Node(n.right)
                    if(parent_temp == None):
                        parent_temp = n

                    if(temp.right != None):
                        n.val = temp.val
                        self.replace(parent_temp, temp, temp.right)
                        break
                    else:
                        n.val = temp.val
                        self.replace(parent_temp, temp, temp.right)
                        break

        self.size_ -= 1
        


    def min(self):
        n = self.root

        if n is None:
            return None

        if(n.left == None):
            return n.val

        while n.left != None:
            n = n.left
            self.minValue = n.val
            

        return self.minValue

    def max(self):
        n = self.root

        if n is None:
            return None

        if n.right == None:
            return n.val

        while n.right != None:
            n = n.right
            self.maxValue = n.val

        return self.maxValue    

    def size(self):
        return self.size_   
    

    def count(self,lo,hi):
        count_ = getCount(self.root,lo,hi)

        return count_
        
        