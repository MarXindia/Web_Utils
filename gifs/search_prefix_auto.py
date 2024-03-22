import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

# Example trie implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_files(node, prefix)

    def _collect_files(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child_node in node.children.items():
            results.extend(self._collect_files(child_node, prefix + char))
        return results

class SearchWidget(QWidget):
    def __init__(self, trie, gif_mapping):
        super().__init__()
        self.trie = trie
        self.gif_mapping = gif_mapping
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.textChanged.connect(self.search)
        self.layout.addWidget(self.search_box)
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)

    def search(self):
        query = self.search_box.text()
        results = self.trie.search_prefix(query)
        if results:
            file_paths = [self.gif_mapping.get(result) for result in results]
            pixmap = QPixmap('\n'.join(file_paths))
            self.result_label.setPixmap(pixmap)
            self.result_label.setScaledContents(True)
        else:
            self.result_label.clear()

if __name__ == "__main__":
    # Example data
    gif_mapping = {"cat": "D:/github/Web_Utils/gifs/cat/", "dog": "D:/github/Web_Utils/gifs/dog.gif"}  # Mapping of tags/names to GIF paths
    trie = Trie()
    for tag in gif_mapping:
        trie.insert(tag)

    app = QApplication(sys.argv)
    widget = SearchWidget(trie, gif_mapping)
    widget.show()
    sys.exit(app.exec_())
