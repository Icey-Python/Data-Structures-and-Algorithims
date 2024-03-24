def reverseList(head):
  if not head or not head.next:
      return head

  new_head = reverseList(head.next)
  head.next.next = head
  head.next = None

  return new_head