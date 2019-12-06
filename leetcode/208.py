class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end_of_word = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            not_found = True
            for child in node.children:
                if child.char == char:
                    not_found = False
                    node = child

            if not_found:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        node = self.root
        if len(node.children) == 0:
            return False

        for char in word:
            not_found = True
            for child in node.children:
                if child.char == char:
                    not_found = False
                    node = child
                    break

            if not_found:
                return False
        return node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        if len(node.children) == 0:
            return False

        for char in prefix:
            not_found = True
            for child in node.children:
                if child.char == char:
                    not_found = False
                    node = child
                    break

            if not_found:
                return False

        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)


# Faster:
class Trie(object):
    def __init__(self):
        self.trie = {}


    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t["-"] = True


    def search(self, word):
        t = self.trie
        for c in word:
            if c not in t: return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t: return False
            t = t[c]
        return True