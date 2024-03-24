def detectCycle(head):
  if not head or not head.next:
      return None

  slow = head
  fast = head

  # Find the meeting point
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          break

  # If there is no cycle
  if not fast or not fast.next:
      return None

  # Move slow to the head
  slow = head

  # Move slow and fast one step at a time until they meet
  while slow != fast:
      slow = slow.next
      fast = fast.next

  # Return the meeting point
  return slow