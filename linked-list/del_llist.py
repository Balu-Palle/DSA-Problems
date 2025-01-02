def deleteNode(llist, position):
    
    if not llist:
        return None
    if position ==0:
        return llist.next
    index=0 # used to track the position of the llist 
    node=llist
    
    
    while node and index < position - 1:
        node=node.next
        index+=1
    if node is None or node.next is None:
        return llist
    node.next=node.next.next
    
    return llist