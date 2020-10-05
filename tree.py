from __future__ import annotations
from enum import Enum


class Player(Enum):
    min = "min"
    max = "max"


class Node:
    def __init__(self, letter: str, val: int or None, children: list or None, turn: Player):
        self.letter = letter
        self.val = val
        self.children = children
        self.turn = turn

    def get_val(self):
        child: Node

        if self.val is not None:
            return self.val

        if self.turn == Player.max:
            self.val = max([child.get_val() for child in self.children])
            return self.val
        else:
            self.val = min([child.get_val() for child in self.children])
            return self.val

    def print_self(self):
        if self.children is None:
            print("{}\t\t{}\t\t{}\t\t".format(self.turn.name, self.letter, self.val))
        else:
            print("{}\t\t{}\t\t{}\t\t{}".format(self.turn.name, self.letter, self.val, " ".join([child.letter for child in self.children])))
            for child in self.children:
                child: Node
                child.print_self()


tree = Node("A", None, [
    Node("B", None, [
        Node("E", None, [
            Node("K", 2, None, Player.min),
            Node("L", 1, None, Player.min),
            Node("M", 3, None, Player.min),
        ], Player.max),
        Node("F", None, [
            Node("N", 5, None, Player.min),
            Node("O", 4, None, Player.min)
        ], Player.max)
    ], Player.min),
    Node("C", None, [
        Node("G", None, [
            Node("P", 7, None, Player.min)
        ], Player.max),
        Node("H", None, [
            Node("Q", 6, None, Player.min),
            Node("R", 8, None, Player.min)
        ], Player.max)
    ], Player.min),
    Node("D", None, [
        Node("I", None, [
            Node("S", 9, None, Player.min),
            Node("T", 10, None, Player.min)
        ], Player.max),
        Node("J", None, [
            Node("U", 12, None, Player.min),
            Node("V", 11, None, Player.min)
        ], Player.max)
    ], Player.min)
], Player.max)

tree.get_val()
print("Turn\tNode\tValue\tChildren")
print("________________________________________")
tree.print_self()

