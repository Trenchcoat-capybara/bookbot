def text_to_list(text):
    text_list = text.split()
    return text_list

def char_count(text):
    char_dict = {}
    unique = set()
    for word in text:
        low_word = word.lower()
        for ch in low_word:
            if ch in unique:
                temp = char_dict[ch] + 1
                char_dict[ch] = temp
            else:
                unique.add(ch)
                char_dict[ch] = 1
    return char_dict

def sorting_dict(diction):
    dict_list = []
    for name in diction:
        entry = {}
        entry["chara"] = name
        entry["count"] = diction[name]
        dict_list.append(entry)
    return dict_list

def sort_on(items):
    return items["count"]
    

