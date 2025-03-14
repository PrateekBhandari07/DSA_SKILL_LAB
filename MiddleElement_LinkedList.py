class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def getMiddle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    return slow_ptr.data

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))

if __name__ == "__main__":
    main()
