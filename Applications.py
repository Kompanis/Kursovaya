# Потоки (threading). Смотреть рис. 1
'''
import threading
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for i in range(65, 75):
        print(chr(i))
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
'''


# Процессы (multiprocessing). Смотреть рис. 2
'''
from multiprocessing import Process
import time

def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)

def print_letters():
    for i in range(65, 75):
        print(chr(i))
        time.sleep(1)


p1 = threading.Thread(target=print_numbers)
p2 = threading.Thread(target=print_letters)

p1.start()
p2.start()

p1.join()
p2.join()
'''


# Пример создания и запуска потока. Смотреть рис. 3
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
'''


# Пример использования метода join(). Смотреть рис. 4
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

print("All threads are done")
'''


# Пример использования блокировки (Lock) при работе с глобальной переменной. Смотреть рис. 5
'''
import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    with lock:
        for i in range(10000):
            counter += 1

threads = [threading.Thread(target=increment_counter) for i in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
'''


# В приведенном рис. 6 object_name является объектом класса Semaphore. 
'''
objeect_name = Semaphore(count)
'''


# Функция Acquire() и Функция release(). Пример использования смотреть рис. 7.
'''
import threading
import time

def show(name):
    for i in range(6):
        print(f"Javatpoint, {name}")
        time.sleep(1)

my_obj = threading.Semaphore(4)

threads = [threading.Thread(target=show, args=(f"Thread {i}",)) for i in range(6)]

for thread in threads:
    my_obj.acquire()
    thread.start()

for thread in threads:
    thread.join()
'''


# Пример использования условия смотреть рис. 8. 
'''
import  threading

cond_var = threading.Condition(lock=None)
'''


# Смотреть рис. 9, следующий код представляет ситуацию производитель/потребитель. 
'''
import threading
cond_var = threading.Condition(Lock=None)

# Потребитель порции данных
with cond_var:
    while not an_item_is_available():
        cond_var.wait()
    get_an_available_item()

# Производитель порции данных
with cond_var:
    make_an_item_available()
    cond_var.notify()
'''

# Метод .wait_for(). Смотреть рис. 10.
'''
import treading
cond_var = treading.Condition(lock=None)

# Потребитель порции данных
with cond_var:
    cond_var.wait_for(an_item_is_available)
    get_an_available_item()
'''


# Пример использования мьютексов смотреть рис. 11.
'''
import threading

mutex = threading.Lock()
shared_resource = 0

def access_resource():
    global shared_resource
    print(f'{threading.current_thread().name} ожидает доступ к ресурсy')
    mutex.acquire()
    print(f'{threading.current_thread().name} получил доступ к ресурсу')
    shared_resource += 1
    mutex.release()
    print(f'{threading.current_thread().name} освободил ресурс')

threads = []
for i in range(5):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Значение shared_resource: {shared_resource}')
'''


#Пример процесса смотреть рис. 12.
'''
import multiprocessing import Process

def my_function():
    print("Hello from all process!")

if __name__ == "__main__":
    my_process = Process(target=my_function)
    my_process.start()
    my_process.join()
'''


# Обмен данными между процессами Смотреть рис. 13.
'''
from multiprocessing import Process, Queue

def worker(queue):
    data = queue.get()
    print(f"Worker received: {data}")

if __name__ == "__main__":
    my_queue = Queue()
    my_process = Process(target=worker, args=(my_queue,))
    my_process.start()

    my_queue.put("Hello from the main process!")
    my_process.join()
'''


# Пул процессов. Смотреть рис. 14.
'''
from multiprocessing import Pool

def square(x):
    return x * x

if __name__  ==  "__main__":
    with Pool() as pool:
        result = pool.map(square, [1, 2, 3, 4, 5])
        print(result)
'''


# Использование Manager. Смотреть рис. 15.
'''
from multiprocessing import Process, Manager

def worker(shared_list):
    shared_list.append("Hello from worker!")

if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()
        my_process = Process(target=worker, args=(shared_list,))
        my_process.start()
        my_process.join()
        print(shared_list)
'''


# Создание подпроцессов. Смотреть рис. 16.
'''
from multiprocessing import Process

def worker():
    print("Hello from a subprocess!")

if __name__ == "__main__":
    my_process = Process(target=worker)
    my_process.start()
    my_process.join()
'''


# Модуль multiprocessing. Смотреть рис. 17.
'''
from multiprocessing import Process, Value, Array

def modify_shared_data(shared_value, shared_array):
    with shared_value.get_lock():
        shared_value.value += 1
    for i in range(len(shared_array)):
        shared_array[i] *= 2

if __name__ == "__main__":
    shared_value = Value("i", 0)
    shared_array = Array("i", [1, 2, 3, 4, 5])

    my_process = Process(target=modify_shared_data, args=(shared_value, shared_array))
    my_process.start()
    my_process.join()

    print(f"Shared value: {shared_value.value}")
    print(f"Shared array: {list(shared_array)}")
'''
