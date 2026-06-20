# singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        return self.find_length()

    def print_list(self):
        temp = self.head
        print("H->", end="")
        while temp is not None:
            print(temp.value, end="->")
            temp = temp.next
        print()

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
        length = self.find_length()
        if index < 0 or index > length:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == length:
            self.append(value)
            return
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
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
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        value = temp.next.value
        temp.next = None
        return value

    def pop_first(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def remove(self, index):
        if index < 0 or index >= self.find_length():
            raise IndexError("Index out of range")
        if index == 0:
            return self.pop_first()
        if index == self.find_length() - 1:
            return self.pop()
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        value = temp.next.value
        temp.next = temp.next.next
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

    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def find_middle(self):
        length = self.find_length()
        if length == 0:
            return None
        mid_index = length // 2
        if length % 2 == 0:
            low = mid_index - 1
            curr = self.head
            for _ in range(low):
                curr = curr.next
            return curr.value, curr.next.value if curr.next is not None else None
        else:
            curr = self.head
            for _ in range(mid_index):
                curr = curr.next
            return curr.value

    def get(self, index):
        if index < 0 or index >= self.find_length():
            raise IndexError("Index out of range")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set(self, index, value):
        if index < 0 or index >= self.find_length():
            raise IndexError("Index out of range")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def clear(self):
        self.head = None


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\n")
        print("1. Print")
        print("2. Append")
        print("3. Insert")
        print("4. Pop")
        print("5. Length")
        print("6. Delete")
        print("7. Pop first element")
        print("8. Reverse")
        print("9. Find Middle")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                linked_list.print_list()
            elif choice == 2:
                value = int(input("Enter value: "))
                linked_list.append(value)
            elif choice == 3:
                index = int(input("Enter index: "))
                value = int(input("Enter value: "))
                linked_list.insert(index, value)
            elif choice == 4:
                print(linked_list.pop())
            elif choice == 5:
                print(len(linked_list))
            elif choice == 6:
                value = int(input("Enter value to delete: "))
                print(linked_list.delete(value))
            elif choice == 7:
                print(linked_list.pop_first())
            elif choice == 8:
                linked_list.reverse()
            elif choice == 9:
                print(linked_list.find_middle())
            elif choice == 10:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")
        except IndexError as e:
            print(e)

    print("Goodbye!")
