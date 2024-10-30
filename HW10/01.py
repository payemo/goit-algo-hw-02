class SingleLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def __str__(self):
        s = ""
        curr = self.head
        while curr:
            s += str(curr.data) + (" -> " if curr.next else "")
            curr = curr.next
        return s

    def insert_front(self, data):
        new_node = SingleLinkedList.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = SingleLinkedList.Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

def reverse(head: SingleLinkedList.Node):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    head = prev
    return head

def insertion_sort(head: SingleLinkedList.Node):
    if not head or not head.next:
        return head
    
    sorted_head = SingleLinkedList.Node()
    curr = head

    while curr:
        next = curr.next

        position = sorted_head

        while position.next and position.next.data < curr.data:
            position = position.next

        curr.next = position.next
        position.next = curr

        curr = next

    return sorted_head.next

def merge_sort(head: SingleLinkedList.Node):
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge(left, right)

def merge(left: SingleLinkedList.Node, right: SingleLinkedList.Node):
    dummy = SingleLinkedList.Node()
    tail = dummy

    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next

def main():
    sll = SingleLinkedList()
    sll.insert_front(5)
    sll.insert_front(3)
    sll.insert_front(1)
    sll.insert_front(4)
    sll.insert_front(2)

    print('%s before reverse' % sll)
    sll.head = reverse(sll.head)
    print('%s after reverse' % sll)

    print('%s before insertion sort' % sll)
    sll.head = insertion_sort(sll.head)
    print('%s after insertion sort' % sll)

    sll2 = SingleLinkedList()
    sll2.insert_front(6)
    sll2.insert_front(8)
    sll2.insert_front(1)
    sll2.insert_front(20)
    sll2.insert_front(4)

    print('%s before merge sort' % sll2)
    sll2.head = merge_sort(sll2.head)
    print('%s after merge sort' % sll2)

    sll3 = SingleLinkedList()
    sll3.head = merge(sll.head, sll2.head)
    print('%s after mergin 2 sorted lists' % sll3)


if __name__ == '__main__':
    main()