def main():
    book_path = "books/text.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f'{num_words} found in the text')
    freqMap = count_letters(text)
    sorted_freqMap = sort_count_map(freqMap)
    for item in sorted_freqMap:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    
def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_letters(text):
    freqMap = {}
    for c in text:
        ch = c.lower()
        if ch in freqMap:
            freqMap[ch] += 1
        else:
            freqMap[ch] = 1
    return freqMap

def sort_on(d):
    return d["num"]
        
def sort_count_map(freqMap):
    sorted_list = []
    for ch in freqMap:
        sorted_list.append({"char" : ch, "num" : freqMap[ch]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list    
main()