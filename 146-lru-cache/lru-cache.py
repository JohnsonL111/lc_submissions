class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = ListNode(-1, -1) # dummy
        self.tail = ListNode(-1, -1) # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    # adds to end
    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    # removes the node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def get(self, key: int) -> int:
        # add to the dicts back
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    # add to doubly LL. 
    def put(self, key: int, value: int) -> None:
        # remove old one if exists
        if key in self.dict:
            old_node = self.dict[key]
            self.remove(old_node)
        # add to end
        node = ListNode(key, value)
        self.dict[key] = node
        self.add(node)

        # check capacity to evict LRU (head)
        if len(self.dict) > self.capacity:
            node_del = self.head.next
            self.remove(node_del)
            del self.dict[node_del.key]

        

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)