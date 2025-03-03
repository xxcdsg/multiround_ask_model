from urllib3.filepost import writer

import write_string
from _input_ import _input_
from ask_one import ask_one
from merge_all import merge_all
from multi_process import multi_process

if __name__ == '__main__':
    api_key, key_word, word_list = _input_()

    """
    for word in word_list:
        try:
            response_word = ask_one(api_key,key_word, word)
        except Exception as e:  # 捕获异常并记录错误信息
            response_word = "error"
            print(f"An error occurred while processing '{word}': {e}")
        print("Note:\n" , word , "\n" , response_word)
        response_word_list.append(response_word)
    """

    response_word_list = multi_process(api_key,key_word,word_list)
    final_string = merge_all(word_list, response_word_list)
    write_string.write_final_string_to_file(final_string)