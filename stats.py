def count_words(book_text):
    split_text = book_text.split()
    word_count = len(split_text)
    return word_count

def count_characters(book_text):
    clean_text = book_text.lower()
    chars_to_check = ("a","æ","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")",".",",","?","/","\\","|","-","_","+","=","[","]","{","}","<",">",":",";","'",'"'," ")
    char_count = {}
    for char in chars_to_check:
        count = clean_text.count(char)
        char_count[char] = count
    return char_count

def sort_char_count(book_text):
    char_count = count_characters(book_text)
    list_of_dicts = []
    for char, num in char_count.items():
        current_dict = {}
        current_dict["char"] = char
        current_dict["num"] = num
        list_of_dicts.append(current_dict)
    sorted_char_count = sorted(list_of_dicts, reverse=True, key=lambda items: items["num"])
    return sorted_char_count
