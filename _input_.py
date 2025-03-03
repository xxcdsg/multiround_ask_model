
#sk-49601e55aef94eb191cb0340a2689ba1

def _input_():
    api_key = input("输入api_key\n")
    key_word = input("输入提示词\n")
    word_list_input = input("请输入 Word 列表（用逗号分隔）: \n")
    word_list = [word.strip() for word in word_list_input.split(',')]
    return api_key, key_word, word_list
