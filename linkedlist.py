class LinkedNode:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.head = self

    def insert(self, value):
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = LinkedNode(value)

    def printLinkedList(self):
        curr = self.head
        while(curr != None):
            print(curr.data)
            curr = curr.next

def main():
    ll = LinkedNode(0)
    #ll.printLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(5)
    ll.printLinkedList()

if __name__ == "__main__":
    main()
