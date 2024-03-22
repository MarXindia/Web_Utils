import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt, pyqtSlot

# Example trie implementation supporting prefix search
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
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._collect_words(child_node, prefix + char))
        return words

def scan_folder_for_gifs(folder_path):
    gif_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".gif"):
            gif_files.append(os.path.join(folder_path, file))  # Include full file path
    return gif_files

class SearchWidget(QWidget):
    def __init__(self, gif_folder):
        super().__init__()
        self.trie = Trie()
        self.gif_folder = gif_folder
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.textChanged.connect(self.update_image_grid)
        self.layout.addWidget(self.search_box)
        self.image_grid = QGridLayout()
        self.layout.addLayout(self.image_grid)
        self.setLayout(self.layout)
        self.load_gifs_from_folder()

    def load_gifs_from_folder(self):
        gif_files = scan_folder_for_gifs(self.gif_folder)
        for gif_file in gif_files:
            gif_name = os.path.basename(gif_file)  # Extract the file name
            self.trie.insert(gif_name)

    def update_image_grid(self):
        # Clear the existing grid
        for i in reversed(range(self.image_grid.count())):
            self.image_grid.itemAt(i).widget().setParent(None)

        # Get the prefix from the search box
        prefix = self.search_box.text().strip()  # Remove leading and trailing whitespace

        # Display all GIFs in the folder if search box is empty
        if not prefix:
            return

        # Search for GIFs with the given prefix
        gif_names = self.trie.search_prefix(prefix)

        # Display the GIF images in the grid layout
        row, col = 0, 0
        for gif_name in gif_names:
            gif_path = os.path.join(self.gif_folder, gif_name)
            movie = QMovie(gif_path)
            label = QLabel()
            label.setMovie(movie)
            movie.start()
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid white;")  # Add border
            label.mousePressEvent = lambda event, path=gif_path: self.tile_clicked(path)  # Connect custom slot to mouse press event with gif path as parameter
            self.image_grid.addWidget(label, row, col)
            col += 1
            if col == 4:
                row += 1
                col = 0

    def tile_clicked(self, gif_path):
        print("GIF path:", gif_path)

if __name__ == "__main__":
    # Specify the folder containing the GIFs
    gif_folder = "D:/github/Web_Utils/gifs"

    app = QApplication(sys.argv)

    # Set dark theme stylesheet
    app.setStyleSheet("QWidget { background-color: #333; color: white; }"
                      "QLineEdit { background-color: #222; color: white; border: 1px solid white; }"
                      "QLabel { background-color: #222; color: white; }")

    widget = SearchWidget(gif_folder)
    widget.show()
    sys.exit(app.exec_())
