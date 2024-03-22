import os
import streamlit as st

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
            gif_files.append(file)  # Only include file name
    return gif_files

def load_gifs_from_folder(gif_folder):
    trie = Trie()
    gif_files = scan_folder_for_gifs(gif_folder)
    for gif_file in gif_files:
        trie.insert(gif_file)
    return trie, gif_files


def on_change(*args, **kwargs):
    print('On change', args, kwargs)


def main():
    # Specify the folder containing the GIFs
    gif_folder = "D:/github/Web_Utils/gifs"

    # Load GIFs and build trie
    trie, gif_files = load_gifs_from_folder(gif_folder)

    # Streamlit UI
    st.title("GIF Search")

    # Search box with autocomplete suggestions
    prefix = st.text_input("Search GIFs by Prefix", "", on_change=on_change)
    suggestions = trie.search_prefix(prefix)

    # Display GIFs based on prefix search
    if prefix:
        st.write("Search Results:")
        for gif_name in gif_files:
            if gif_name.startswith(prefix):
                gif_path = os.path.join(gif_folder, gif_name)
                st.image(gif_path, use_column_width=True, caption=gif_name)

if __name__ == "__main__":
    main()
