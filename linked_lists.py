## Part 1: Extend the Linked List

class Node:
    """A single node in a linked list."""

    def __init__(self, value):
        self.value = value   # The data this node holds
        self.next = None     # Reference to the next node (None if this is the last)

    def __repr__(self):
        return f"Node({self.value})"

class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None  # The list starts empty

    def insert_at_beginning(self, value):
        """Add a new node at the front of the list. O(1) time."""
        new_node = Node(value)
        new_node.next = self.head  # New node points to the old head
        self.head = new_node       # New node becomes the new head

    def insert_at_end(self, value):
        """Add a new node at the end of the list. O(n) time — must traverse to the end."""
        new_node = Node(value)
        if self.head is None:      # List is empty
            self.head = new_node
            return
        current = self.head
        while current.next:        # Walk to the last node
            current = current.next
        current.next = new_node    # Last node now points to the new node

    def search(self, target):
        """Find a value in the list. Returns True/False. O(n) time."""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next  # Follow the pointer to the next node
        return False

    def display(self):
        """Print the list in a readable format."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")

## Starting from the LinkedList class in the Guided Example, add these methods:


    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""

        # case 1: the list is empty
        if self.head is None:
            return False

        # case 2: the target is at the head
        if self.head.value == target:
            self.head = self.head.next
            return True

        # case 3: the target is somewhere after the head
        if self.head is not None:
            # loop through
            current = self.head
            while current.next is not None:
                if current.next.value == target:
                    current.next = current.next.next
                    return True
                current = current.next

    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        linked_py_list = []
        current = self.head
        while current is not None:
            linked_py_list.append(current.value)
            current = current.next
        return linked_py_list

print(f"\n---------- Part 1 Tests ----------")    

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

# added to help myself visualize the linked list in memory
print(id(ll.head))                # address of the first node
print(id(ll.head.next))           # address of the second node
print(id(ll.head.next.next))      # address of the third node

ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
print(ll.length())     # 5
ll.delete(30)
print(f"Length after deletion: {ll.length()}")
ll.display()           # 10 -> 20 -> 40 -> 50 -> None
print(ll.to_list())    # [10, 20, 40, 50]

## Part 2: Stack: Bracket Validator

def is_balanced(text):
    """Return True if all brackets in text are properly matched.
    Handles: (), [], {}
    """
    stack = []
    matching_char = {")": "(", "]": "[", "}": "{"}
    opening_char = set(matching_char.values())

    for char in text:
        if char in opening_char:
            stack.append(char)
        elif char in matching_char:
            if not stack or stack.pop() != matching_char[char]:
                return False
    return not stack

tests = [
    "",
    "()",
    "{[()]}",
    "()[]{}",
    "hello (world)",
    "f(a[0], {k: v})",
    "(",
    "((",
    ")",
    ")(",
    "(]",
    "{[}]",
    "hello (world",
    "hello world)",
]

print(f"\n---------- Part 2 Tests ----------")

for text in tests:
    print(f"{text!r:20} -> {is_balanced(text)}")

## Part 3: Queue: Task Processor

from collections import deque

class TaskProcessor:
    """Simple task processor class with methods for add_task and process_next."""

    def __init__(self):
        self.tasks = deque()

    def add_task(self, name):
        if name: # added to manage cases of empty strings
            self.tasks.append(name)
    
    def process_next(self):
        if not self.tasks:
            return None
        return self.tasks.popleft() #FIFO processing

tp = TaskProcessor()
tp.add_task("send email")
tp.add_task("")
tp.add_task("resize image")

print(f"\n---------- Part 3 Tests ----------")

print(tp.process_next())
print(tp.process_next())   
print(tp.process_next())    # last two operations should result in None, because it should have skipped the empty string
print(tp.process_next())