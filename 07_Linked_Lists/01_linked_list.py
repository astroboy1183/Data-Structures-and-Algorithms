# singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        print("H->", end="")
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        if index == self.find_length():
            self.append(value)
            return
        if index < 0 or index > self.find_length():
            return "Invalid index"
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            if temp is None:
                return
        new_node.next = temp.next
        temp.next = new_node

    def find_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        value = temp.value
        temp = None
        return value

    def pop_first(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def delete(self, value):
        if self.head is None:
            return "List is empty"
        if self.head.value == value:
            self.head = self.head.next
            return "Deleted value at position 0"
        position = 0
        temp = self.head
        while temp.next is not None:
            position += 1
            if temp.next.value == value:
                temp.next = temp.next.next
                return f"Deleted value at position {position}"
            temp = temp.next
        return "Value not found"


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\n")
        print("1. Print")
        print("2. Append")
        print("3. Pop")
        print("4. Length")
        print("5. Delete")
        print("6. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            linked_list.print_list()
        elif choice == 2:
            value = int(input("Enter value: "))
            linked_list.append(value)
        elif choice == 3:
            print(linked_list.pop())
        elif choice == 4:
            print(linked_list.find_length())
        elif choice == 5:
            value = int(input("Enter value to delete: "))
            print(linked_list.delete(value))
        elif choice == 6:
            print(linked_list.pop_first())
        elif choice == 7:
            break
        else:
            print("Invalid choice")

    print("Goodbye!")
