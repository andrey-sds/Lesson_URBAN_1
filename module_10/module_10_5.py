import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            content = file.readline()
            if not content:
                break
            else:
                all_data.append(content)
                # print(all_data)


filenames = [f'Files/file {number}.txt' for number in range(1, 5)]
# start_time = datetime.datetime.now()
# for i in filenames:
#     read_info(i)
# end_time = datetime.datetime.now()
# print(end_time - start_time)

# многопроцессность
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.datetime.now()
    print(end_time - start_time)


