def merge_all(word_list,response_word_list):
    res = ""
    n = len(word_list)
    for i in range(n):
        res = res + word_list[i] + ":\n" + response_word_list[i] + "\n"
    return res;