class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None
        # double linked list

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head =  LinkedListNode(-1,-1)
        self.tail =  LinkedListNode(-1,-1)
        
        # head connects tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
        # move the list node to most recent used place
        # return the node value 

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            oldnode = self.dict[key]
            self.remove(oldnode)
        
        newnode = LinkedListNode(key, value)
        self.add(newnode)
        self.dict[key] = newnode

        # if existed : remove value
        # insert the new value
        if len(self.dict)>self.capacity:
            # remove head node
            headnode = self.head.next
            self.remove(headnode)
            del self.dict[headnode.key]
            # delete the least used listnode 
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        # add to tail
        prev_node = self.tail.prev
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)