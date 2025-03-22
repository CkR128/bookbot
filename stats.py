def get_num_words(bookData):
    words = bookData.split()
    return len(words)

def get_char_stats(bookData):
    charData = {}
    bookData = bookData.lower()
    for char in bookData:
        if char not in charData:
            charData[char] = 0
        charData[char] += 1
    return charData

def sort_on(dict):
    return dict["count"]

def sort_chars(charDict):
    items = []
    for key, value in charDict.items():
        items.append({"char": key,
                      "count": value})
    items.sort(reverse=True, key=sort_on)
    return items
