import threading
import time

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

def main(n, m):
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

    # Вывод результата
    print(f"Final counter value: {counter}")

if __name__ == "__main__":
    # Ввод числа потоков для инкрементирования и декрементирования
    n = int(input("Enter the number of increment threads: "))
    m = int(input("Enter the number of decrement threads: "))

    start_time = time.time()
    main(n, m)
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} seconds")
