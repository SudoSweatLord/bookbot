def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_char_counts(char_counts):
    """Return a sorted list of character counts as dictionaries."""
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha(): 
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
