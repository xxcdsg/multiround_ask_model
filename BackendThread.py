

import write_string
from ask_one import ask_one
from merge_all import merge_all

from threading import Thread
from queue import Queue
from PyQt5 import QtCore, QtGui, QtWidgets

class BackendThread(QtCore.QThread):
    update_data = QtCore.pyqtSignal(str)

    def __init__(self,api_key,key_word,words,thread_num,selected_model):
        super(BackendThread,self).__init__()
        self.selected_model = selected_model
        self.api_key = api_key
        self.key_word = key_word
        self.words = words
        self.ask_queue = Queue()
        self.ans = ['error'] * len(self.words)
        self.len = len(self.words)
        self.ok_num = 0
        self.thread_num = thread_num

    def run(self):
        try:
            index = 0
            for word in self.words:
                self.ask_queue.put((word,index)) # 将所有询问加入
                index += 1
            self.return_msg("开始询问")
            self.return_msg("----------------------------------------------------------------------------")
            threads = []
            for i in range(self.thread_num):
                t = Thread(target=self.ask, args=())
                t.setDaemon(True)
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

            self.return_msg("询问完成，生成文档中")

            final_string = merge_all(self.words,self.ans)
            write_string.write_final_string_to_file(final_string)

            self.return_msg("询问完成，已输出文件在output.txt中")
        except Exception as e:
            self.return_msg(f"发生错误{str(e)}")

    def ask(self):
        while not self.ask_queue.empty():
            (word, index) = self.ask_queue.get()
            try:
                self.return_msg(f"正在询问{word}")
                self.ans[index] = ask_one(self.api_key,self.key_word,word,self.selected_model)
                self.return_msg(f"询问{word}完成")
                self.ok_num += 1
                self.present_percent()
            except Exception as e:
                self.return_msg(f"发生错误{str(e)}")
                self.return_msg(f"重新加入任务{word}")
                self.ask_queue.put((word,index))

    def present_percent(self):
        progress_message = f"进度：{self.ok_num}/{self.len}"
        self.return_msg(progress_message)

    def return_msg(self,text):
        self.update_data.emit(text)