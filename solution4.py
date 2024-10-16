from rich.tree import Tree
from rich import print as rprint


class Trie:

    def __init__(self):
        self.children: dict[str, dict[dict, bool]] = {}
        

    def insert(self, word: str) -> None:
        children = self.children
        for idx, character in enumerate(word):
            if character not in children:
                children[character] = {"children": {}, "closing": False}
            if idx == (len(word)-1):
                children[character]["closing"] = True
            children = children[character]["children"]

    def search(self, word: str) -> bool:
        children = self.children
        for idx, character in enumerate(word):
            if character not in children:
                return False
            if idx == (len(word)-1):
                return children[character]["closing"]
            children = children[character]["children"]
        
        

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for idx, character in enumerate(prefix):
            if character not in children:
                return False
            if idx == (len(prefix)-1):
                return True
            children = children[character]["children"]
        

def print_trie(trie: Trie):
    tree = Tree(".")
    def traverse_build_tree(tree: Tree, children: dict[str, list[dict, bool]]):
        for char, child in children.items():
            child_branch = tree.add(char if not child["closing"] else f"{char}*")
            if child["children"]:
                traverse_build_tree(child_branch, child["children"])
    traverse_build_tree(tree, trie.children)
    rprint(tree)


# Your Trie object will be instantiated and called as such:
trie =  Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))
# breakpoint()
print_trie(trie)