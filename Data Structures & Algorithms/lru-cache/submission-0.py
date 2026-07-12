class Node:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left, self.right= Node(0,0), Node(0,0)
        self.left.next, self.right.prev= self.right, self.left
    def remove(self, node):
        p=node.next
        j=node.prev
        j.next=p
        p.prev=j

    def insert(self,node):
        d=self.right.prev
        node.prev=d
        node.next=self.right
        d.next=node
        self.right.prev=node
        

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)

        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
