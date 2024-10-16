from rich.tree import Tree
from rich import print as rprint

class Trie:

    __slots__ = ("character", "children", "is_closing_character", "is_root")

    def __init__(self):
        self.character = None
        self.children: list[Trie] = [None for _ in range(0, 26)]
        self.is_closing_character = False
        self.is_root = True
        

    def insert(self, word: str) -> None:
        first_character = ord(word[0])
        if self.is_root:
            child = self.children[first_character-97]
            if child is None:
                next_char = Trie()
                next_char.is_root = False
                self.children[first_character-97] = next_char
                next_char.insert(word)
            else:
                child.insert(word)
            return
        if self.character is None:
            self.character = first_character
        if len(word) == 1:
            self.is_closing_character = True
        else:
            rest = word[1:]
            first_char_of_rest = ord(rest[0])
            child = self.children[first_char_of_rest-97]
            if child is None:
                first_char_of_rest = ord(rest[0])
                next_char = Trie()
                next_char.is_root = False
                self.children[first_char_of_rest-97] = next_char
                next_char.insert(rest)
            else:
                child.insert(rest)
            
        

    def search(self, word: str) -> bool:
        first_character = ord(word[0])
        if self.is_root:
            child = self.children[first_character-97]
            if not child:
                return False
            return child.search(word)
        if len(word) == 1:
            return self.is_closing_character
        rest = word[1:]
        first_char_of_rest = ord(rest[0])
        child = self.children[first_char_of_rest-97]
        if not child:
            return False
        return child.search(rest)
        
        

    def startsWith(self, prefix: str) -> bool:
        first_character = ord(prefix[0])
        if self.is_root:
            child = self.children[first_character-97]
            if not child:
                return False
            return child.startsWith(prefix)
        if len(prefix) == 1:
            return True
        rest = prefix[1:]
        first_char_of_rest = ord(rest[0])
        child = self.children[first_char_of_rest-97]
        if not child:
            return False
        return child.startsWith(rest)
        
def print_trie(trie: Trie):
    def leaf_label(trie: Trie):
        char = chr(trie.character) if trie.character is not None else "."
        return char if not trie.is_closing_character else f"{char}*"
    tree = Tree(leaf_label(trie))
    def build_leaf(trie: Trie, leaf: Tree):
        for child in trie.children:
            if child is None:
                continue
            child_tree = leaf.add(leaf_label(child))
            build_leaf(child, child_tree)
    build_leaf(trie, tree)
    rprint(tree)


# Your Trie object will be instantiated and called as such:
trie =  Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))