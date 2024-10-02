from threading import Thread
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for line in range(word_count):
            file.write(f"Какое-то слово № {line + 1}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
res_time = end_time - start_time
print(f"Время выполнения {res_time}")

start_time = datetime.now()
first_ = Thread(target=write_words, args=(10, 'example1.txt'))
second_ = Thread(target=write_words, args=(30, 'example2.txt'))
third_ = Thread(target=write_words, args=(200, 'example3.txt'))
four_ = Thread(target=write_words, args=(100, 'example4.txt'))

first_.start()
second_.start()
third_.start()
four_.start()

first_.join()
second_.join()
third_.join()
four_.join()
end_time = datetime.now()
res_time = end_time - start_time
print(f"Время выполнения {res_time}")