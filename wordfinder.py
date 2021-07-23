"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Class for finding random words from a text file"""

    def __init__(self, file_path):
        """constructor"""
        self.word_list = self.build_list_from_file(file_path)
        print(f"{len(self.word_list)} words read")

    
    def __repr__(self):
        return f"<Word Finder with list of {len(self.word_list)} words>"
    
    def build_list_from_file(self,file_path):
        wList = []
        with open(file_path, 'r') as file:
            for line in file:
                text = line.strip()
                wList.append(text)
        return wList

    def random(self):
        return choice(self.word_list)

class NewWordFinder(WordFinder):
    """New and Improved Word Finder, omits comments (#) and empty lines in source file
    >>> new_finder = NewWordFinder("new.txt")
    4 words read

    >>> new_finder.random() in ["kale", "parsnips", "mango", "apple"]
    True
    
    """

    def build_list_from_file(self, file_path):
        wList = []
        with open(file_path, 'r') as file:
            for line in file:
                if line and line[0] != '#' and not line.isspace():
                    text = line.strip()
                    wList.append(text)
        return wList

