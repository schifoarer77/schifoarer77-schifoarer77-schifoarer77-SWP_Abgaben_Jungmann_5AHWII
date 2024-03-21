import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return " -> ".join(map(str, elements))

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(10):  # Fügt 10 Zufallszahlen hinzu
        ll.append(random.randint(1, 100))

    print("Elemente der Liste:")
    for element in ll:
        print(element)

    print("Gesamtlänge der Liste:", ll.length())
    print("Liste:", ll)
