import multiprocessing as mp
import time
import random


def reader_proc(id, shared_data, read_count, mutex, wrt):
    time.sleep(random.uniform(0.1, 0.5))

    mutex.acquire()
    read_count.value += 1
    if read_count.value == 1:
        wrt.acquire()
    mutex.release()

    print(f"Reader {id} reads: {shared_data.value.decode()}")
    time.sleep(0.5)

    mutex.acquire()
    read_count.value -= 1
    if read_count.value == 0:
        wrt.release()
    mutex.release()


def writer_proc(id, shared_data, wrt):
    time.sleep(random.uniform(0.1, 0.5))

    wrt.acquire()
    msg = f"W{id}"
    shared_data.value = msg.encode()
    print(f"Writer {id} writes: {msg}")
    wrt.release()


if __name__ == "__main__":
    # 使用Manager统一管理共享对象
    manager = mp.Manager()
    shared_data = manager.Value('c', b' ' * 100)  # 字符值
    read_count = manager.Value('i', 0)
    mutex = manager.Semaphore(1)
    wrt = manager.Semaphore(1)

    processes = []
    # 创建进程时显式传递共享对象
    for i in range(3):
        p = mp.Process(target=writer_proc, args=(i, shared_data, wrt))
        processes.append(p)
    for i in range(5):
        p = mp.Process(target=reader_proc, args=(i, shared_data, read_count, mutex, wrt))
        processes.append(p)

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final data:", shared_data.value.decode())