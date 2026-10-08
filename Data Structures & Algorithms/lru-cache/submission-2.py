class LRUCache:

    def __init__(self, capacity: int):
        self.keyMap = {}
        self.head, self.tail = None, None
        self.maxCap= capacity

    def get(self, key: int) -> int:
        if key in self.keyMap:
            node = self.keyMap[key]
            self.remove(node)
            self.insert(node)
            #self.print()
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            # insert to map and list
            node = Node(key,value,None,None)
            self.insert(node)
            self.keyMap[key] = node

            if len(self.keyMap) > self.maxCap:
                del self.keyMap[self.tail.key]
                self.remove(self.tail)
        #self.print()


    def remove(self, node:Node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.nextNode
            self.head.prevNode = None
        elif node == self.tail:
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
        else:
            node.prevNode.nextNode = node.nextNode
            node.nextNode.prevNode = node.prevNode
        
        # reset pointer
        node.prevNode = None
        node.nextNode = None

    def insert(self, node:Node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prevNode = node
            node.nextNode = self.head
            self.head = node
    
    def print(self):
        curr = self.head
        while curr:
            print(f"{curr.key},{curr.value}")
            curr = curr.nextNode
        print("----")


class Node:
    def __init__(self, key:int, value:int, prevNode:Node, nextNode:Node):
        self.key = key
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode