# Потоки (threading). Смотреть рис. 1 <--- здесь кратко написано о коде, номер рисунка ссылается на тему в курсовой, там подробней можно прочитать. 
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
# Этот код использует модуль threading для создания двух потоков, 
# каждый из которых выполняет свою функцию: print_numbers() и print_letters(). 
# Функция print_numbers() выводит числа от 0 до 9 с интервалом в 1 секунду между выводами, 
# а функция print_letters() выводит буквы от 'A' до 'J' с тем же интервалом.

# Когда код выполняется, два потока (t1 и t2) создаются 
# и запускаются параллельно с использованием метода start(). 
# Затем метод join() вызывается для каждого потока, чтобы гарантировать, 
# что основной поток (главный поток) будет ждать завершения выполнения 
# обоих потоков перед завершением программы. Это делается для того, 
# чтобы основной поток не завершился до тех пор, пока оба потока не завершат свою работу.





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

if __name__ == "__main__":
    p1 = Process(target=print_numbers)
    p2 = Process(target=print_letters)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
'''
# Этот код использует модуль multiprocessing для создания двух отдельных процессов, 
# каждый из которых выполняет свою функцию. Код создает два процесса p1 и p2 для выполнения 
# функций print_numbers и print_letters соответственно.

#  print_numbers(): Функция выводит числа от 0 до 9 с интервалом в 1 секунду между выводами.
#  print_letters(): Функция выводит буквы от 'A' до 'J' с тем же интервалом  между выводами.

# В основном блоке (if __name__ == "__main__":), создаются два процесса p1 и p2 с указанием 
# соответствующих функций для выполнения. Затем оба процесса запускаются методом start(), 
# что позволяет им выполняться параллельно. Затем методы join() вызываются для p1 и p2, 
# чтобы главный процесс (основной поток) ожидал завершения выполнения обоих процессов перед завершением.






# Пример создания и запуска потока. Смотреть рис. 3
'''
import threading

def print_numbers():
    for i in range(10):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
'''
# Этот код создает поток и выводит числа от 0 до 9 в этом потоке.





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

# Этот код создает поток, который выводит числа от 0 до 9, 
# ждет завершения потока, затем выводит "All threads are done".





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

# Этот код использует 10 потоков для инкрементации общего счетчика (counter) на 100 000. 
# Используется блокировка (lock) для обеспечения безопасности при обращении к общему ресурсу из нескольких потоков.






# В приведенном рис. 6 object_name является объектом класса Semaphore. 
'''
object_name = Semaphore(count)
'''

# Функция Acquire() и Функция release(). Пример использования смотреть рис. 7.
'''
import threading
import time

def show(name):
    for i in range(2):
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
# В коде используется семафор для ограничения доступа к ресурсу. Создаются 6 потоков, каждый выводит сообщение. 
# Семафор (с начальным значением 4) ограничивает одновременное выполнение не более 4 потоков.





# Пример использования условия смотреть рис. 8. 
'''
import  threading

cond_var = threading.Condition(lock=None)
'''
# Этот код создает объект условия (Condition) для многозадачного программирования в Python. 
# Condition предоставляет средства для синхронизации потоков при работе с общими ресурсами. 
# Параметр lock=None указывает, что будет использован объект блокировки по умолчанию.





# Смотреть рис. 9, следующий код представляет ситуацию производитель/потребитель. 
'''
import threading

cond_var = threading.Condition()

# Потребитель порции данных
with cond_var:
    cond_var.wait_for(an_item_is_available)
    get_an_available_item()

# Производитель порции данных
with cond_var:
    make_an_item_available()
    cond_var.notify()
'''
# Этот краткий код предполагает наличие функций an_item_is_available(), get_an_available_item(), 
# и make_an_item_available() для работы с общим ресурсом, например, общим списком.
 




# Метод .wait_for(). Смотреть рис. 10.
'''
import treading
cond_var = treading.Condition(lock=None)

# Потребитель порции данных
with cond_var:
    cond_var.wait_for(an_item_is_available)
    get_an_available_item()
'''

# Создается объект условия (Condition) без явно указанной блокировки, что означает использование блокировки по умолчанию.
# В блоке потребителя поток ожидает, пока не станет доступен элемент с помощью cond_var.wait_for(an_item_is_available).
# Затем вызывается функция get_an_available_item(), предполагается, что она извлекает доступный элемент из общего ресурса.






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
for i in range(2):
    thread = threading.Thread(target=access_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Значение shared_resource: {shared_resource}')
'''

# Этот код использует блокировку (Lock) для безопасного доступа к общему 
# ресурсу (shared_resource) из нескольких потоков. 

#     Создается объект блокировки mutex.
#     Функция access_resource увеличивает shared_resource с использованием блокировки.
#     Создаются и запускаются 5 потоков, каждый вызывает access_resource.
#     Ожидается завершение всех потоков.
#     Выводится окончательное значение shared_resource.





#Пример процесса смотреть рис. 12.
'''
import multiprocessing
from multiprocessing import Process

def my_function():
    print("Hello from all process!")

if __name__ == "__main__":
    my_process = Process(target=my_function)
    my_process.start()
    my_process.join()
'''

# Код создает процесс с использованием модуля multiprocessing, который выполняет функцию my_function. 
# В данном случае, функция просто выводит сообщение "Hello from all processes!". 
# Код использует многозадачность для выполнения этой функции в отдельном процессе.





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
# В этом кратком коде создается процесс, который выполняет функцию worker, принимая данные из очереди 
# и выводя их. Главный процесс помещает сообщение в очередь, и процесс-рабочий выводит это сообщение.




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
# Этот код использует многозадачность (multiprocessing) для параллельного 
# вычисления квадрата чисел с использованием пула процессов (Pool). 
# Каждое число из списка подается на вход функции square, и результаты выводятся с помощью pool.map.



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
# Код использует многозадачность (multiprocessing) и менеджер (Manager) для создания процесса, 
# в котором функция worker добавляет элемент в общий список. 
# После выполнения процесса, содержимое общего списка выводится.




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
# Код создает и запускает процесс с использованием многозадачности (multiprocessing). 
# Процесс выполняет функцию worker, выводящую сообщение "Hello from a subprocess!".

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
# Этот код использует многозадачность (multiprocessing) для создания процесса, 
# который изменяет общие данные: shared_value (Value) и shared_array (Array). 
# После выполнения процесса выводятся измененные значения общих данных.