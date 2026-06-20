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
            raise IndexError("pop from empty list")
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
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        return value

    def remove(self, index):
        length = self.find_length()
        if index < 0 or index >= length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.pop_first()
        if index == length - 1:
            return self.pop()
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        value = temp.next.value
        temp.next = temp.next.next
        return value

    def delete(self, value):
        if self.head is None:
            return -1
        if self.head.value == value:
            self.head = self.head.next
            return 0
        position = 0
        temp = self.head
        while temp.next is not None:
            position += 1
            if temp.next.value == value:
                temp.next = temp.next.next
                return position
            temp = temp.next
        return -1

    def remove_all(self, value):
        while self.head is not None and self.head.value == value:
            self.head = self.head.next
        temp = self.head
        while temp is not None and temp.next is not None:
            if temp.next.value == value:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def remove_duplicates(self):
        seen = set()
        prev = None
        temp = self.head
        while temp is not None:
            if temp.value in seen:
                prev.next = temp.next
            else:
                seen.add(temp.value)
                prev = temp
            temp = temp.next

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
        pos = 0
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return pos
            pos += 1
            temp = temp.next
        return -1

    def count(self, value):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.value == value:
                count += 1
            temp = temp.next
        return count

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def is_palindrome(self):
        lst = []
        temp = self.head
        while temp is not None:
            lst.append(temp.value)
            temp = temp.next
        return lst == lst[::-1]

    def rotate_clockwise(self, k):
        if self.find_length() == 0:
            return
        i = k % self.find_length()
        temp = self.head
        prev = None
        while i != 0:
            while temp.next is not None:
                prev = temp
                temp = temp.next
            temp.next = self.head
            prev.next = None
            self.head = temp
            i -= 1

    def rotate_anticlockwise(self, k):
        if self.find_length() == 0:
            return
        i = k % self.find_length()
        temp = self.head
        while i != 0:
            p = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = p
            self.head = p.next
            p.next = None
            i -= 1


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\n")
        print("1. Print")
        print("2. Append")
        print("3. Prepend")
        print("4. Insert (by index)")
        print("5. Get (by index)")
        print("6. Set (by index)")
        print("7. Pop (last)")
        print("8. Pop first")
        print("9. Remove (by index)")
        print("10. Delete (by value)")
        print("11. Remove all (by value)")
        print("12. Remove duplicates")
        print("13. Search (position of value)")
        print("14. Count (occurrences)")
        print("15. Length")
        print("16. Reverse")
        print("17. Find middle")
        print("18. Is empty")
        print("19. Clear")
        print("20. Is palindrome")
        print("21. Rotate clockwise")
        print("22. Rotate anticlockwise")
        print("23. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                linked_list.print_list()
            elif choice == 2:
                value = int(input("Enter value: "))
                linked_list.append(value)
            elif choice == 3:
                value = int(input("Enter value: "))
                linked_list.prepend(value)
            elif choice == 4:
                index = int(input("Enter index: "))
                value = int(input("Enter value: "))
                linked_list.insert(index, value)
            elif choice == 5:
                index = int(input("Enter index: "))
                print(linked_list.get(index))
            elif choice == 6:
                index = int(input("Enter index: "))
                value = int(input("Enter value: "))
                linked_list.set(index, value)
            elif choice == 7:
                print(linked_list.pop())
            elif choice == 8:
                print(linked_list.pop_first())
            elif choice == 9:
                index = int(input("Enter index: "))
                print(linked_list.remove(index))
            elif choice == 10:
                value = int(input("Enter value to delete: "))
                pos = linked_list.delete(value)
                print(f"Deleted at position {pos}" if pos != -1 else "Value not found")
            elif choice == 11:
                value = int(input("Enter value to remove: "))
                linked_list.remove_all(value)
            elif choice == 12:
                linked_list.remove_duplicates()
            elif choice == 13:
                value = int(input("Enter value to search: "))
                print(linked_list.search(value))
            elif choice == 14:
                value = int(input("Enter value to count: "))
                print(linked_list.count(value))
            elif choice == 15:
                print(len(linked_list))
            elif choice == 16:
                linked_list.reverse()
            elif choice == 17:
                print(linked_list.find_middle())
            elif choice == 18:
                print(linked_list.is_empty())
            elif choice == 19:
                linked_list.clear()
            elif choice == 20:
                print(linked_list.is_palindrome())
            elif choice == 21:
                k = int(input("Enter rotations (k): "))
                linked_list.rotate_clockwise(k)
            elif choice == 22:
                k = int(input("Enter rotations (k): "))
                linked_list.rotate_anticlockwise(k)
            elif choice == 23:
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")
        except IndexError as e:
            print(e)

    print("Goodbye!")
