class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class Linked_List:

    def __init__(self, nodes):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))

            self.head = node

            for i in nodes:
                node.next = Node(data=i)
                node = node.next

    def __iter__(self):

        node = self.head

        while node is not None:
            yield node.data
            node = node.next

    def insert_front(self, node):
        node.next = self.head
        self.head = node

    def insert_end(self, node):

        if self.head is None:
            self.head = node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append("None")

        return " -> ".join(nodes)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    mylist = Linked_List(nodes=data)

    mylist.insert_end(Node(80))

    print(mylist)
