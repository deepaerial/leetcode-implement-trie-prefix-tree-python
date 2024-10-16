from rich.tree import Tree
from rich import print as rprint


class Trie:

    def __init__(self):
        self.leaf: dict[str, dict] = {}
        

    def insert(self, word: str) -> None:
        leaf = self.leaf
        for character in word:
            if character not in leaf:
                leaf[character] = {}
            leaf = leaf[character]
        leaf["closing"] = True

    def search(self, word: str) -> bool:
        leaf = self.leaf
        for character in word:
            if character not in leaf:
                return False
            leaf = leaf[character]
        return "closing" in leaf
        
        

    def startsWith(self, prefix: str) -> bool:
        leaf = self.leaf
        for character in prefix:
            if character not in leaf:
                return False
            leaf = leaf[character]
        return True
        

def print_trie(trie: Trie):
    tree = Tree(".")
    def traverse_build_tree(tree: Tree, leaf: dict[str, dict]):
        for char, child in leaf.items():
            if char == "closing":
                continue
            child_branch = tree.add(char if "closing" not in child else f"{char}*")
            if child:
                traverse_build_tree(child_branch, child)
    traverse_build_tree(tree, trie.leaf)
    rprint(tree)


# Your Trie object will be instantiated and called as such:
trie =  Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
print_trie(trie)