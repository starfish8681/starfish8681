from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
  

    def add(self, key):   
        h = MD5.new()
        h.update(key.encode("utf-8"))         
        x = h.hexdigest()
        y = int(x, 16)   
        i = y%self.capacity
        if self.data[i] == None:
            self.data[i] = ListNode(x)
        else:
            while self.data[i] != None:
                self.data[i] = self.data[i].next
            self.data[i] = ListNode(x)
                  
                
    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))         
        x = h.hexdigest()
        y = int(x, 16)   
        i = y%self.capacity
        if self.contains(key) is True:
            if self.data[i].val == x:
                self.data[i] = self.data[i].next
            else:
                pre = self.data[i]
                current = self.data[i].next
                while current:  
                    if current.val == x:
                        pre.next = current.next
                    else:
                        current = current.next
                        pre = pre.next  
                        
  
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))         
        x = h.hexdigest()
        y = int(x, 16)   
        i = y%self.capacity
        current = self.data[i]
        if current is None:
            return False
        else:
            while current != None:
                if current.val == x:
                    return True
                else:
                    current = current.next
            return False
                    

