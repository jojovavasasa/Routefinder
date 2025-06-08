from collections import deque

def load_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = set(word.strip().lower() for word in f if len(word.strip()) > 0)
    return words

def one_letter_diff(w1, w2):
    return sum(a != b for a, b in zip(w1, w2)) == 1

def find_path(start, end, words):
    if start == end:
        return [start]
    visited = set()
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        last = path[-1]
        for word in words:
            if word not in visited and one_letter_diff(last, word):
                new_path = path + [word]
                if word == end:
                    return new_path
                queue.append(new_path)
                visited.add(word)
    return None

# MAIN
wordlist_file = input("Wordlist: ")
words = load_words("wordlists/" + wordlist_file + ".txt")

word1 = input("Word 1: ").lower()
word2 = input("Word 2: ").lower()

if len(word1) != len(word2):
    print("Woorden moeten even lang zijn.")
    exit()

words = {w for w in words if len(w) == len(word1)}

path = find_path(word1, word2, words)

if path:
    for word in path:
        print(word)
else:
    print("Geen pad gevonden.")
