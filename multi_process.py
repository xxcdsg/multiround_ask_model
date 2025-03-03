from concurrent.futures import ThreadPoolExecutor, as_completed
from ask_one import ask_one

def process_word(api_key,key_word,word):
    try:
        response_word = ask_one(api_key, key_word, word)
    except Exception as e:
        response_word = "error"
        print(f"An error occurred while processing '{word}': {e}")
    return word, response_word

def multi_process(api_key, key_word, word_list):
    response_word_list = []
    with ThreadPoolExecutor(max_workers=10) as executor:  # 你可以根据需要调整 max_workers 的数量
        # 提交所有任务
        futures = {executor.submit(process_word, api_key,key_word,word): word for word in word_list}

        # 收集结果
        for future in as_completed(futures):
            word, response_word = future.result()
            print("Note:\n", word, "\n", response_word)
            response_word_list.append(response_word)
    return response_word_list