import threading
import time
import os
import platform

# Инициализация счетчика и ReentrantLock
counter = 0
counter_lock = threading.RLock()

# Функция инкрементирования счетчика с использованием ReentrantLock
def increment_counter():
    global counter
    for _ in range(100000):
        with counter_lock:  # Защита счетчика с помощью ReentrantLock
            local_counter = counter
            local_counter += 1
            counter = local_counter

# Функция декрементирования счетчика с использованием ReentrantLock
def decrement_counter():
    global counter
    for _ in range(100000):
        with counter_lock:  # Защита счетчика с помощью ReentrantLock
            local_counter = counter
            local_counter -= 1
            counter = local_counter

def get_system_info():
    """Получаем информацию о системе."""
    if platform.system() == "Windows":
        return os.popen("systeminfo").read()
    elif platform.system() == "Linux":
        return os.popen("cat /proc/cpuinfo").read()
    else:
        return "System info not available"

def run_test(n, m):
    """Запускаем тест с n потоками инкрементирования и m потоками декрементирования."""
    global counter
    counter = 0

    # Список для хранения потоков
    threads = []

    # Запуск потоков инкрементирования
    for _ in range(n):
        t = threading.Thread(target=increment_counter)
        threads.append(t)
        t.start()

    # Запуск потоков декрементирования
    for _ in range(m):
        t = threading.Thread(target=decrement_counter)
        threads.append(t)
        t.start()

    # Ожидание завершения всех потоков
    for t in threads:
        t.join()

def main():
    # Открываем файл для записи результатов
    with open("Lab8.txt", "w") as file:
        file.write("Lab8 ReentrantLock Results\n")
        file.write("System Info:\n")
        file.write(get_system_info())
        file.write("\n")

        # Запускаем тесты с различными наборами потоков
        for num_threads in [1, 2, 4, 8]:
            n = num_threads  # Потоки инкрементирования
            m = num_threads  # Потоки декрементирования
            start_time = time.time()
            run_test(n, m)
            end_time = time.time()
            execution_time = end_time - start_time

            # Записываем результаты в файл
            file.write(f"Threads: {n} increment, {m} decrement\n")
            file.write(f"Final counter value: {counter}\n")
            file.write(f"Execution time: {execution_time} seconds\n\n")

if __name__ == "__main__":
    main()
