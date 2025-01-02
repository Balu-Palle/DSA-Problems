def printLinkedList(head):
    node=head
    if head is None :
        print()
    while node is not None :
        print(node.data)
        node=node.next