class Node:
    def __init__(self):
        self.cnt = 0
        self.child = [None] * 26


class TrieTree:
    def __init__(self):
        self.root = Node()

    def add(self, s: str):
        node = self.root
        for i in s:
            v = ord(i) - ord("a")
            if node.child[v] == None:
                node.child[v] = Node()
            node = node.child[v]
            # ここに何らかの処理
            node.cnt += 1
            #################

    def serch(self, s: str) -> int:
        result = 0
        node = self.root
        for i in s:
            v = ord(i) - ord("a")
            if node.child[v] == None:
                return result
            node = node.child[v]
            # ここに何らかの処理
            result += node.cnt
            ##################
        return result
