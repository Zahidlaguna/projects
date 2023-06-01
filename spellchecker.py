import re
import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.corpus import words

nltk.download("words")


class SpellingChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = scrolledtext.ScrolledText(self.root, font=("Times New Roman", 12))
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.old_content = ""

        self.load_word_corpus()

        self.root.mainloop()

    def load_word_corpus(self):
        nltk_words = set(words.words())
        self.word_corpus = set([word.lower() for word in nltk_words])

    def check(self, event):
        content = self.text.get("1.0", tk.END)
        new_content = content.replace(self.old_content, "")
        self.old_content = content

        words_to_check = re.findall(r"\b\w+\b", new_content)

        for word in words_to_check:
            if word.lower() not in self.word_corpus:
                start_pos = self.text.search(word, "1.0", tk.END)
                end_pos = f"{start_pos}+{len(word)}c"
                self.text.tag_add("misspelled", start_pos, end_pos)
                self.text.tag_config("misspelled", foreground="red")


SpellingChecker()
