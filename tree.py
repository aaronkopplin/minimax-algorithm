from __future__ import annotations

class Node:
    def __init__(self, letter: str, val: int or None, children: list or None):
        self.letter = letter
        self.val = val
        self.children = None
        if children is not None:
            self.children = children

    def print_self(self):
        if self.children is None:
            print("{}, {}".format(self.letter, self.val))
        else:
            print("{}, {}, children: ".format(self.letter, self.val))
            for child in self.children:
                child: Node
                child.print_self()


tree = Node("A", None, [
    Node("B", None, [
        Node("E", None, [
            Node("K", 2, None),
            Node("L", 1, None),
            Node("M", 3, None),
        ]),
        Node("F", None, [
            Node("N", 5, None),
            Node("O", 4, None)
        ])
    ]),
    Node("C", None, [
        Node("G", None, [
            Node("P", 7, None)
        ]),
        Node("H", None, [
            Node("Q", 6, None),
            Node("R", 8, None)
        ])
    ]),
    Node("D", None, [
        Node("I", None, [
            Node("S", 9, None),
            Node("T", 10, None)
        ]),
        Node("J", None, [
            Node("U", 12, None),
            Node("V", 11, None)
        ])
    ])
])

print(tree.print_self())


