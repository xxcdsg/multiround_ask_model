import os


def write_final_string_to_file(final_string, original_file_path = __file__):
    # 获取原文件所在的目录
    directory = os.path.dirname(original_file_path)
    # 定义新的文本文件的路径
    output_file_path = os.path.join(directory, 'output.txt')

    # 将 final_string 写入到新的文本文件中
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(final_string)

    print(f"Final string has been written to {output_file_path}")